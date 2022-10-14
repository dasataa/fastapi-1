"""create posts table

Revision ID: 3405a3d2dbf7
Revises: 
Create Date: 2022-10-12 01:35:43.127096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3405a3d2dbf7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
