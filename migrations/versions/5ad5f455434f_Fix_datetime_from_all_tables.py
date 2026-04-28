"""Fix datetime defaults for all tables

Revision ID: 5ad5f455434f
Revises: a0ff4767f8bc
Create Date: 2025-11-28 14:35:41.229091
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = '5ad5f455434f'
down_revision = 'a0ff4767f8bc'
branch_labels = None
depends_on = None


def upgrade():
    tables = ["users", "products", "producers", "categories"]

    for table in tables:
        with op.batch_alter_table(table) as batch_op:

            # Fix created_at
            batch_op.alter_column(
                'created_at',
                existing_type=sa.DateTime(),
                server_default=text("CURRENT_TIMESTAMP"),
                existing_nullable=False
            )

            # Fix updated_at
            batch_op.alter_column(
                'updated_at',
                existing_type=sa.DateTime(),
                server_default=text("CURRENT_TIMESTAMP"),
                server_onupdate=text("CURRENT_TIMESTAMP"),
                existing_nullable=False
            )


def downgrade():
    tables = ["users", "products", "producers", "categories"]

    for table in tables:
        with op.batch_alter_table(table) as batch_op:
            batch_op.alter_column(
                'created_at',
                existing_type=sa.DateTime(),
                server_default=None,
                existing_nullable=False
            )

            batch_op.alter_column(
                'updated_at',
                existing_type=sa.DateTime(),
                server_default=None,
                server_onupdate=None,
                existing_nullable=False
            )
