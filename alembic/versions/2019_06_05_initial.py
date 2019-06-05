"""initial

Revision ID: 337530c085b4
Revises:
Create Date: 2019-06-05 07:07:55.633746

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '337530c085b4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('password_hash', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
    )
    op.create_index(op.f('ix_user_created'), 'user', ['created'], unique=False)
    op.create_table(
        'person',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('deleted', sa.DateTime(), nullable=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('balance', sa.DECIMAL(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id']),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id', 'name'),
    )
    op.create_index(
        op.f('ix_person_created'), 'person', ['created'], unique=False
    )
    op.create_index(
        op.f('ix_person_deleted'), 'person', ['deleted'], unique=False
    )
    op.create_index(op.f('ix_person_name'), 'person', ['name'], unique=False)
    op.create_table(
        'operation',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.Column('deleted', sa.DateTime(), nullable=True),
        sa.Column('value', sa.DECIMAL(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('person_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['person_id'], ['person.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index(
        op.f('ix_operation_created'), 'operation', ['created'], unique=False
    )
    op.create_index(
        op.f('ix_operation_deleted'), 'operation', ['deleted'], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_operation_deleted'), table_name='operation')
    op.drop_index(op.f('ix_operation_created'), table_name='operation')
    op.drop_table('operation')
    op.drop_index(op.f('ix_person_name'), table_name='person')
    op.drop_index(op.f('ix_person_deleted'), table_name='person')
    op.drop_index(op.f('ix_person_created'), table_name='person')
    op.drop_table('person')
    op.drop_index(op.f('ix_user_created'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###