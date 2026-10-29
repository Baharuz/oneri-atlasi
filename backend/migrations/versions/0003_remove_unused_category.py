"""Remove retired catalog entries and their dependent records."""
from alembic import op
import sqlalchemy as sa

revision = "0003"
down_revision = "0002"
branch_labels = None
depends_on = None


def upgrade():
    connection = op.get_bind()
    retired_ids = set(connection.execute(sa.text("SELECT id FROM contents WHERE category = :category"), {"category": "müzik"}).scalars())
    if not retired_ids:
        return
    users = sa.table("users", sa.column("id"), sa.column("preferences", sa.JSON()))
    for user_id, preferences in connection.execute(sa.select(users.c.id, users.c.preferences)):
        if not isinstance(preferences, dict):
            continue
        updated = dict(preferences)
        updated["source_ids"] = [item for item in updated.get("source_ids", []) if item not in retired_ids]
        updated["categories"] = [category for category in updated.get("categories", []) if category != "müzik"]
        if updated != preferences:
            connection.execute(users.update().where(users.c.id == user_id).values(preferences=updated))
    runs = sa.table("recommendation_runs", sa.column("id"), sa.column("request_data", sa.JSON()), sa.column("results", sa.JSON()))
    for run_id, request_data, results in connection.execute(sa.select(runs.c.id, runs.c.request_data, runs.c.results)):
        updated_request = dict(request_data or {})
        updated_request["source_ids"] = [item for item in updated_request.get("source_ids", []) if item not in retired_ids]
        answers = dict(updated_request.get("answers") or {})
        if "categories" in answers:
            answers["categories"] = [category for category in answers["categories"] if category != "müzik"]
            updated_request["answers"] = answers
        updated_results = {category: [item for item in ids if item not in retired_ids] for category, ids in (results or {}).items() if category != "müzik"}
        if updated_request != request_data or updated_results != results:
            connection.execute(runs.update().where(runs.c.id == run_id).values(request_data=updated_request, results=updated_results))
    connection.execute(sa.text("DELETE FROM content_tags WHERE content_id IN (SELECT id FROM contents WHERE category = :category)"), {"category": "müzik"})
    connection.execute(sa.text("DELETE FROM interactions WHERE content_id IN (SELECT id FROM contents WHERE category = :category)"), {"category": "müzik"})
    connection.execute(sa.text("DELETE FROM contents WHERE category = :category"), {"category": "müzik"})


def downgrade():
    # Removed catalog records cannot be reconstructed from a schema downgrade.
    pass
