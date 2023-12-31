"""Model Tool

Revision ID: 6217396a0794
Revises: c45cc8f7d561
Create Date: 2023-11-15 19:09:56.367251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6217396a0794'
down_revision = 'c45cc8f7d561'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tool',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=36), nullable=False),
    sa.Column('author', sa.String(length=50), nullable=False),
    sa.Column('alias', sa.String(length=50), nullable=True),
    sa.Column('custom_alias', sa.String(length=50), nullable=True),
    sa.Column('name_repo', sa.String(length=50), nullable=True),
    sa.Column('type_install', sa.String(length=50), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('dependencies', sa.String(length=50), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tool')
    # ### end Alembic commands ###
