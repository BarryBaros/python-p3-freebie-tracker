from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '285cab923bba'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Create the 'freebies' table
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('item_name', sa.String(), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id'), nullable=False),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    # Drop the 'freebies' table
    op.drop_table('freebies')
