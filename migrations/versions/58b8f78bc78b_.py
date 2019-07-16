"""empty message

Revision ID: 58b8f78bc78b
Revises: 5e647ed78984
Create Date: 2019-05-17 17:27:34.679163

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '58b8f78bc78b'
down_revision = '5e647ed78984'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cases', sa.Column('description', sa.Text(), nullable=True))
    op.add_column('items', sa.Column('description', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('_password', sa.Text(), nullable=False))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', mysql.TEXT(), nullable=False))
    op.drop_column('users', '_password')
    op.drop_column('items', 'description')
    op.drop_column('cases', 'description')
    # ### end Alembic commands ###