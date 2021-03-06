"""update task

Revision ID: 86ba2060c277
Revises: 4747e559aac0
Create Date: 2016-11-05 22:07:39.820888

"""

# revision identifiers, used by Alembic.
revision = '86ba2060c277'
down_revision = '4747e559aac0'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('msg', sa.String(length=255), nullable=False))
    op.drop_column('task', 'err_msg')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('err_msg', mysql.VARCHAR(length=255), nullable=False))
    op.drop_column('task', 'msg')
    ### end Alembic commands ###
