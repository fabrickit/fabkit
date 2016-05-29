"""mod task

Revision ID: 913114c4f8a7
Revises: 541071568ae6
Create Date: 2016-05-21 19:14:48.877449

"""

# revision identifiers, used by Alembic.
revision = '913114c4f8a7'
down_revision = '541071568ae6'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('active', sa.Boolean(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'active')
    ### end Alembic commands ###