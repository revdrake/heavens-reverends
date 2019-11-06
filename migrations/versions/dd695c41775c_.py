"""empty message

Revision ID: dd695c41775c
Revises: f371f854abd1
Create Date: 2019-11-06 01:44:54.572553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd695c41775c'
down_revision = 'f371f854abd1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('appointments', 'appointment_date',
               existing_type=sa.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('appointments', 'appointment_date',
               existing_type=sa.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###
