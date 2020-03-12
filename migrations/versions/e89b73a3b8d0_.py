"""empty message

Revision ID: e89b73a3b8d0
Revises: c99adb8ff573
Create Date: 2020-03-10 14:59:27.871732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e89b73a3b8d0'
down_revision = 'c99adb8ff573'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jobs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nurse', sa.String(length=150), nullable=True),
    sa.Column('patient', sa.String(length=150), nullable=True),
    sa.Column('time', sa.String(length=150), nullable=True),
    sa.Column('address', sa.String(length=150), nullable=True),
    sa.Column('meds', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jobs')
    # ### end Alembic commands ###