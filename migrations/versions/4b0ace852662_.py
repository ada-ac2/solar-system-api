"""empty message

Revision ID: 4b0ace852662
Revises: 934749f17def
Create Date: 2022-12-21 10:24:56.300990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b0ace852662'
down_revision = '934749f17def'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planets', sa.Column('distance', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planets', 'distance')
    # ### end Alembic commands ###