"""alter_notifications

Revision: 363fd32983f2
Revises: 7d8d1662e7bd
Created: 2015-02-12 10:22:24.552198
"""

revision = '363fd32983f2'
down_revision = '7d8d1662e7bd'

from alembic import op
from spire.schema.fields import *
from sqlalchemy import Column, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint, CheckConstraint
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.execute("alter table notification alter column created type timestamp with time zone")
    ### end Alembic commands ###
def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.execute("alter table notification alter column created type timestamp with time zone")
    ### end Alembic commands ###
