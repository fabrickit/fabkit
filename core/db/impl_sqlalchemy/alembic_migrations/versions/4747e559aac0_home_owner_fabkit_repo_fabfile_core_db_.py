"""/home/owner/fabkit-repo/fabfile/core/db/impl_sqlalchemy

Revision ID: 4747e559aac0
Revises: 3309b47f3848
Create Date: 2016-11-05 18:51:19.547728

"""

# revision identifiers, used by Alembic.
revision = '4747e559aac0'
down_revision = '3309b47f3848'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('owner', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'owner')
    ### end Alembic commands ###