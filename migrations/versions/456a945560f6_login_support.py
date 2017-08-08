"""login support
Revision ID: 456a945560f6
Revises: 38c4e85512a9
Create Date: 2013-12-29 00:18:35.795259
"""

# revision identifiers, used by Alembic.
revision = '456a945560f6'
down_revision = '38c4e85512a9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_email', 'users')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    ### end Alembic commands ###