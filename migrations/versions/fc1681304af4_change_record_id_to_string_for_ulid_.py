"""Change record_id to String for ULID support

Revision ID: fc1681304af4
Revises: fe0a64bb9849
Create Date: 2025-11-27
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


revision = 'fc1681304af4'
down_revision = 'fe0a64bb9849'
branch_labels = None
depends_on = None


def upgrade():
    # 1. REMOVER foreign keys antes de alterar tipos
    op.drop_constraint('products_ibfk_1', 'products', type_='foreignkey')  # categories_id
    op.drop_constraint('products_ibfk_2', 'products', type_='foreignkey')  # producer_id

    # 2. ALTERAR IDs DAS TABELAS PAI
    with op.batch_alter_table('categories') as batch_op:
        batch_op.alter_column(
            'id',
            existing_type=mysql.INTEGER(),
            type_=sa.String(26),
            nullable=False
        )

    with op.batch_alter_table('producers') as batch_op:
        batch_op.alter_column(
            'id',
            existing_type=mysql.INTEGER(),
            type_=sa.String(26),
            nullable=False
        )

    # 3. ALTERAR TABELA FILHA PRODUCTS
    with op.batch_alter_table('products') as batch_op:
        batch_op.alter_column(
            'id',
            existing_type=mysql.INTEGER(),
            type_=sa.String(26),
            nullable=False
        )
        batch_op.alter_column(
            'categories_id',
            existing_type=mysql.INTEGER(),
            type_=sa.String(26),
            nullable=False
        )
        batch_op.alter_column(
            'producer_id',
            existing_type=mysql.INTEGER(),
            type_=sa.String(26),
            nullable=False
        )

    # 4. RECRIAR foreign keys
    op.create_foreign_key(
        'products_ibfk_1',
        'products',
        'categories',
        ['categories_id'],
        ['id'],
        ondelete='CASCADE',
    )

    op.create_foreign_key(
        'products_ibfk_2',
        'products',
        'producers',
        ['producer_id'],
        ['id'],
        ondelete='CASCADE',
    )


def downgrade():
    # Remover novas foreign keys
    op.drop_constraint('products_ibfk_1', 'products', type_='foreignkey')
    op.drop_constraint('products_ibfk_2', 'products', type_='foreignkey')

    # Restaurar tipos antigos
    with op.batch_alter_table('products') as batch_op:
        batch_op.alter_column(
            'producer_id',
            existing_type=sa.String(26),
            type_=mysql.INTEGER(),
            nullable=False
        )
        batch_op.alter_column(
            'categories_id',
            existing_type=sa.String(26),
            type_=mysql.INTEGER(),
            nullable=False
        )
        batch_op.alter_column(
            'id',
            existing_type=sa.String(26),
            type_=mysql.INTEGER(),
            nullable=False
        )

    with op.batch_alter_table('producers') as batch_op:
        batch_op.alter_column(
            'id',
            existing_type=sa.String(26),
            type_=mysql.INTEGER(),
            nullable=False
        )

    with op.batch_alter_table('categories') as batch_op:
        batch_op.alter_column(
            'id',
            existing_type=sa.String(26),
            type_=mysql.INTEGER(),
            nullable=False
        )

    # Recriar foreign keys antigas
    op.create_foreign_key(
        'products_ibfk_1',
        'products',
        'categories',
        ['categories_id'],
        ['id'],
    )

    op.create_foreign_key(
        'products_ibfk_2',
        'products',
        'producers',
        ['producer_id'],
        ['id'],
    )
