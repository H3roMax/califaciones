"""Tareas Modified

Revision ID: 0d3288d0cfab
Revises: 047272387864
Create Date: 2021-06-09 16:12:20.766754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d3288d0cfab'
down_revision = '047272387864'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tarea', sa.Column('titulo', sa.String(length=150), nullable=True))
    op.add_column('tarea', sa.Column('fecha_de_creacion', sa.DateTime(), nullable=True))
    op.add_column('tarea', sa.Column('fecha_de_entrega', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tarea', 'fecha_de_entrega')
    op.drop_column('tarea', 'fecha_de_creacion')
    op.drop_column('tarea', 'titulo')
    # ### end Alembic commands ###