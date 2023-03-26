"""adds stocks table

Revision ID: ee04488f087e
Revises: 
Create Date: 2023-03-25 08:31:03.548945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee04488f087e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('symbol', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('volume', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stock_data_id'), 'stock_data', ['id'], unique=False)
    op.create_index(op.f('ix_stock_data_symbol'), 'stock_data', ['symbol'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stock_data_symbol'), table_name='stock_data')
    op.drop_index(op.f('ix_stock_data_id'), table_name='stock_data')
    op.drop_table('stock_data')
    # ### end Alembic commands ###