"""add content column to posts table

Revision ID: 50b9deb78234
Revises: 3405a3d2dbf7
Create Date: 2022-10-12 02:37:40.276508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50b9deb78234'
down_revision = '3405a3d2dbf7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
