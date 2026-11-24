"""Add source-backed creator metadata; year already exists."""
from alembic import op
import sqlalchemy as sa
revision = "0005"
down_revision = "0004"
branch_labels = None
depends_on = None

def upgrade():
    op.add_column("contents", sa.Column("creators", sa.JSON(), nullable=False, server_default=sa.text("'[]'")))
    op.add_column("contents", sa.Column("metadata_source_url", sa.String(1000), nullable=True))

def downgrade():
    op.drop_column("contents", "metadata_source_url")
    op.drop_column("contents", "creators")
