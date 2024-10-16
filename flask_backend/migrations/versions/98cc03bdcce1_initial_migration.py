"""initial migration

Revision ID: 98cc03bdcce1
Revises: 51bcdfadae95
Create Date: 2024-10-09 18:12:42.597284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98cc03bdcce1'
down_revision = '51bcdfadae95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
