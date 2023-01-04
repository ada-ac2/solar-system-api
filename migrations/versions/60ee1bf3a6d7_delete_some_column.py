"""delete some column

Revision ID: 60ee1bf3a6d7
Revises: 927e0daedb50
Create Date: 2023-01-03 12:32:11.382959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60ee1bf3a6d7'
down_revision = '927e0daedb50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planet', 'namesake')
    op.drop_column('planet', 'diameter')
    op.drop_column('planet', 'livable')
    op.drop_column('planet', 'number_of_moons')
    op.drop_column('planet', 'atmosphere')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('atmosphere', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('planet', sa.Column('number_of_moons', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('planet', sa.Column('livable', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('planet', sa.Column('diameter', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('planet', sa.Column('namesake', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###