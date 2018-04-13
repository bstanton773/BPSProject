"""empty message

Revision ID: 6d900f231c39
Revises: 591aa427b712
Create Date: 2018-04-13 12:48:26.183774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d900f231c39'
down_revision = '591aa427b712'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('checkout',
    sa.Column('checkout_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('Date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('checkout_id')
    )
    op.create_table('receipt',
    sa.Column('receipt_id', sa.Integer(), nullable=False),
    sa.Column('checkout_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['checkout_id'], ['checkout.checkout_id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.product_id'], ),
    sa.PrimaryKeyConstraint('receipt_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('receipt')
    op.drop_table('checkout')
    # ### end Alembic commands ###
