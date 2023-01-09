"""Redoing migrations to debug errors

Revision ID: 2e9f4c3f0c72
Revises: 
Create Date: 2023-01-06 12:22:34.301088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e9f4c3f0c72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('mass', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('moons',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('size', sa.Float(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('discovery_date', sa.DateTime(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moons')
    op.drop_table('planets')
    # ### end Alembic commands ###
