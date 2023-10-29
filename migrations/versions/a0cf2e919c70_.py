"""empty message

Revision ID: a0cf2e919c70
Revises: fcc39c31adce
Create Date: 2023-10-24 08:59:24.121809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0cf2e919c70'
down_revision = 'fcc39c31adce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vyrobek',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nazev', sa.String(length=64), nullable=True),
    sa.Column('seriove', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sklad',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vyrobek_id', sa.Integer(), nullable=False),
    sa.Column('datum', sa.Date(), nullable=True),
    sa.Column('pocet_kusu', sa.Integer(), nullable=True),
    sa.Column('stav', sa.Enum('Nakup', 'Prodej'), nullable=False),
    sa.ForeignKeyConstraint(['vyrobek_id'], ['vyrobek.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('dite')
    op.drop_table('rodic')
    op.drop_table('typ_vozidla')
    op.drop_table('vyrobce')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vyrobce',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('vyrobce_vozidla', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('typ_vozidla',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('vyrobce_vozidla', sa.VARCHAR(length=50), nullable=True),
    sa.Column('vyrobce_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['vyrobce_id'], ['vyrobce.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rodic',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('jmeno', sa.VARCHAR(length=50), nullable=True),
    sa.Column('prijmeni', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dite',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('jmeno', sa.VARCHAR(length=50), nullable=True),
    sa.Column('prijmeni', sa.VARCHAR(length=50), nullable=True),
    sa.Column('rodic_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['rodic_id'], ['rodic.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('sklad')
    op.drop_table('vyrobek')
    # ### end Alembic commands ###
