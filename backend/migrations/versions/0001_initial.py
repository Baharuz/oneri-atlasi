"""Initial schema."""
from alembic import op
import sqlalchemy as sa

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table("users", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("email", sa.String(255), nullable=False), sa.Column("password_hash", sa.String(255), nullable=False), sa.Column("preferences", sa.JSON(), nullable=False), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False))
    op.create_index("ix_users_email", "users", ["email"], unique=True)
    op.create_table("contents", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("category", sa.String(20), nullable=False), sa.Column("title", sa.String(200), nullable=False), sa.Column("description", sa.Text(), nullable=False), sa.Column("genres", sa.JSON(), nullable=False), sa.Column("themes", sa.JSON(), nullable=False), sa.Column("moods", sa.JSON(), nullable=False), sa.Column("language", sa.String(20), nullable=False), sa.Column("year", sa.Integer(), nullable=True), sa.Column("image_url", sa.String(500), nullable=True), sa.Column("source", sa.String(30), nullable=False), sa.Column("source_id", sa.String(100), nullable=False), sa.UniqueConstraint("source", "source_id"))
    op.create_index("ix_contents_category", "contents", ["category"])
    op.create_index("ix_contents_title", "contents", ["title"])
    op.create_table("tags", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("kind", sa.String(20), nullable=False), sa.Column("name", sa.String(80), nullable=False), sa.UniqueConstraint("kind", "name"))
    op.create_table("content_tags", sa.Column("content_id", sa.Integer(), sa.ForeignKey("contents.id"), primary_key=True), sa.Column("tag_id", sa.Integer(), sa.ForeignKey("tags.id"), primary_key=True))
    op.create_table("interactions", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False), sa.Column("content_id", sa.Integer(), sa.ForeignKey("contents.id"), nullable=False), sa.Column("kind", sa.String(20), nullable=False), sa.UniqueConstraint("user_id", "content_id", "kind"))
    op.create_index("ix_interactions_user_id", "interactions", ["user_id"])
    op.create_table("recommendation_runs", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False), sa.Column("request_data", sa.JSON(), nullable=False), sa.Column("results", sa.JSON(), nullable=False), sa.Column("created_at", sa.DateTime(timezone=True), nullable=False))
    op.create_index("ix_recommendation_runs_user_id", "recommendation_runs", ["user_id"])

def downgrade():
    op.drop_table("recommendation_runs")
    op.drop_table("interactions")
    op.drop_table("content_tags")
    op.drop_table("tags")
    op.drop_table("contents")
    op.drop_table("users")
