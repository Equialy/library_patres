"""Added cascading delete on foreign key

Revision ID: e3595be60515
Revises: 5ddd97fabd6a
Create Date: 2025-01-16 00:53:50.007962

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3595be60515'
down_revision: Union[str, None] = '5ddd97fabd6a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('borrows_id_book_fkey', 'borrows', type_='foreignkey')
    op.create_foreign_key(None, 'borrows', 'books', ['id_book'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'borrows', type_='foreignkey')
    op.create_foreign_key('borrows_id_book_fkey', 'borrows', 'books', ['id_book'], ['id'])
    # ### end Alembic commands ###
