"""empty message

Revision ID: d8f097cd300a
Revises: 34cdcd853944
Create Date: 2020-12-18 09:56:58.080418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8f097cd300a'
down_revision = '34cdcd853944'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('SURVEY', sa.Column('education', sa.String(length=500), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('SURVEY', 'education')
    # ### end Alembic commands ###
