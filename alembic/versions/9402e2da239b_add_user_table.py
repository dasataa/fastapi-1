"""add user table

Revision ID: 9402e2da239b
Revises: 50b9deb78234
Create Date: 2022-10-13 21:38:10.263481

"""
from wsgiref.simple_server import server_version
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9402e2da239b'
down_revision = '50b9deb78234'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', 
        sa.Column('id', sa.Integer(), nullable=False), 
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
