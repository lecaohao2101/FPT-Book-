"""add_author_table

Revision ID: 630b32228127
Revises: 9c4e67f6fde9
Create Date: 2023-04-05 13:34:28.406319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '630b32228127'
down_revision = '9c4e67f6fde9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Author',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Author')
    # ### end Alembic commands ###
