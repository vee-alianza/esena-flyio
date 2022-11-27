"""add bio, occupation to users

Revision ID: 61c523ed6e95
Revises: cf14ea352fff
Create Date: 2022-05-25 13:00:47.663977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61c523ed6e95'
down_revision = 'cf14ea352fff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('occupation', sa.String(length=100), nullable=False))
    op.add_column('users', sa.Column('bio', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'bio')
    op.drop_column('users', 'occupation')
    # ### end Alembic commands ###
