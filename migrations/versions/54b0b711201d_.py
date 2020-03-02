"""empty message

Revision ID: 54b0b711201d
Revises: 
Create Date: 2020-02-25 14:59:48.369930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54b0b711201d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nurses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.Column('age', sa.String(length=120), nullable=True),
    sa.Column('work_exprience', sa.String(length=120), nullable=True),
    sa.Column('license', sa.String(length=120), nullable=True),
    sa.Column('years_working', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('fullname'),
    sa.UniqueConstraint('username')
    )
    op.create_table('userpatient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=120), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('age', sa.String(length=120), nullable=True),
    sa.Column('race', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.Column('patient_name', sa.String(length=120), nullable=True),
    sa.Column('patient_age', sa.String(length=120), nullable=True),
    sa.Column('patient_condition', sa.String(length=120), nullable=True),
    sa.Column('patient_allergies', sa.String(length=120), nullable=True),
    sa.Column('patient_medications', sa.String(length=120), nullable=True),
    sa.Column('patient_gender', sa.String(length=120), nullable=True),
    sa.Column('patient_race', sa.String(length=120), nullable=True),
    sa.Column('home_address', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('fullname'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userpatient')
    op.drop_table('nurses')
    # ### end Alembic commands ###