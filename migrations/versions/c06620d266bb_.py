"""empty message

Revision ID: c06620d266bb
Revises: 349ea302b8f0
Create Date: 2019-05-18 18:38:18.543935

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c06620d266bb'
down_revision = '349ea302b8f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'expiration_period')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('expiration_period', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###