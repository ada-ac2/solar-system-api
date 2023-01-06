"""adds Moon model

Revision ID: 2734fb2348a0
Revises: 224c8797ae08
Create Date: 2023-01-05 14:40:19.153903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2734fb2348a0'
down_revision = '224c8797ae08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('moon',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['moon.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moon')
    # ### end Alembic commands ###