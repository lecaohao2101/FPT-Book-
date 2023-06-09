"""add_store_table

Revision ID: 941c5ed0a8d2
Revises: 2a50c68ede69
Create Date: 2023-04-05 13:39:48.822543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '941c5ed0a8d2'
down_revision = '2a50c68ede69'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Store',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Store')
    # ### end Alembic commands ###
