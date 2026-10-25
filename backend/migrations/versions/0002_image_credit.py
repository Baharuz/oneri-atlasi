"""görsel kaynak/atıf alanları

Revision ID: 0002
Revises: 0001
"""
from alembic import op
import sqlalchemy as sa

revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None

def upgrade():
    op.add_column("contents", sa.Column("image_credit", sa.String(300), nullable=True))
    op.add_column("contents", sa.Column("image_source_url", sa.String(500), nullable=True))

def downgrade():
    op.drop_column("contents", "image_source_url")
    op.drop_column("contents", "image_credit")
