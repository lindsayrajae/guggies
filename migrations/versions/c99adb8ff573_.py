"""empty message

Revision ID: c99adb8ff573
Revises: 54b0b711201d
Create Date: 2020-03-10 14:30:11.390822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c99adb8ff573'
down_revision = '54b0b711201d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accept_payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_on_the_account', sa.String(length=120), nullable=False),
    sa.Column('account_num', sa.String(length=120), nullable=False),
    sa.Column('routing_num', sa.String(length=150), nullable=False),
    sa.Column('amount', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('account_num'),
    sa.UniqueConstraint('amount'),
    sa.UniqueConstraint('name_on_the_account'),
    sa.UniqueConstraint('routing_num')
    )
    op.create_table('payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_on_card', sa.String(length=120), nullable=False),
    sa.Column('card_num', sa.String(length=120), nullable=False),
    sa.Column('card_cvv', sa.String(length=120), nullable=False),
    sa.Column('card_exp', sa.String(length=120), nullable=False),
    sa.Column('card_name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('card_cvv'),
    sa.UniqueConstraint('card_exp'),
    sa.UniqueConstraint('card_name'),
    sa.UniqueConstraint('card_num'),
    sa.UniqueConstraint('name_on_card')
    )
    op.create_table('userpatienprofile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('patient_name', sa.String(length=120), nullable=True),
    sa.Column('patient_age', sa.String(length=120), nullable=True),
    sa.Column('patient_condition', sa.String(length=120), nullable=True),
    sa.Column('patient_allergies', sa.String(length=120), nullable=True),
    sa.Column('patient_medications', sa.String(length=120), nullable=True),
    sa.Column('patient_gender', sa.String(length=120), nullable=True),
    sa.Column('patient_race', sa.String(length=120), nullable=True),
    sa.Column('home_address', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('fullname'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userpatienprofile')
    op.drop_table('payment')
    op.drop_table('accept_payment')
    # ### end Alembic commands ###
