"""client, conviction, charge models

Revision ID: 698f2f334f02
Revises: 73fa18b37f37
Create Date: 2019-04-07 17:02:38.841657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '698f2f334f02'
down_revision = '73fa18b37f37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=12), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('sex', sa.String(), nullable=True),
    sa.Column('race', sa.String(), nullable=True),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('address_line_1', sa.String(), nullable=True),
    sa.Column('address_line_2', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.VARCHAR(length=10), nullable=True),
    sa.Column('license_number', sa.String(), nullable=True),
    sa.Column('license_issuing_state', sa.VARCHAR(length=2), nullable=True),
    sa.Column('license_expiration_date', sa.Date(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('conviction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.Column('agency', sa.String(), nullable=True),
    sa.Column('court_name', sa.String(), nullable=True),
    sa.Column('court_city_county', sa.String(), nullable=True),
    sa.Column('judge', sa.String(), nullable=True),
    sa.Column('record_name', sa.String(), nullable=True),
    sa.Column('release_status', sa.String(), nullable=True),
    sa.Column('release_date', sa.Date(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('charge',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('conviction_id', sa.Integer(), nullable=True),
    sa.Column('charge', sa.String(), nullable=True),
    sa.Column('citation', sa.String(), nullable=True),
    sa.Column('sentence', sa.String(), nullable=True),
    sa.Column('class_type', sa.Enum('A', 'B', 'C', 'D', 'E', 'UNDEFINED', name='class'), nullable=True),
    sa.Column('charge_type', sa.Enum('FELONY', 'MISDEMEANOR', name='charge'), nullable=True),
    sa.Column('eligible', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['conviction_id'], ['conviction.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('user_type', sa.Enum('LAWYER', 'CLIENT', 'ADMIN', 'SUPER_ADMIN', name='user'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'user_type')
    op.drop_column('user', 'updated_at')
    op.drop_column('user', 'created_at')
    op.drop_table('charge')
    op.drop_table('conviction')
    op.drop_table('client')
    # ### end Alembic commands ###