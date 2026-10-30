"""Add catalog pace and editorial audience labels.

Revision ID: 0004
Revises: 0003
"""
from alembic import op
import sqlalchemy as sa

revision = "0004"
down_revision = "0003"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("contents", sa.Column("pace", sa.String(20), nullable=True))
    op.add_column("contents", sa.Column("audience", sa.String(40), nullable=True))


def downgrade():
    op.drop_column("contents", "audience")
    op.drop_column("contents", "pace")
