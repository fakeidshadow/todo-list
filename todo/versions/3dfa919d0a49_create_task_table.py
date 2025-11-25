"""create Task table

Revision ID: 3dfa919d0a49
Revises: 
Create Date: 2025-11-25 14:59:30.180361

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3dfa919d0a49'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "task",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(30), nullable=False),
        sa.Column("status", sa.Integer, default=0),
        sa.Column("description", sa.String(150)),
        sa.Column("deadline", sa.String(20), default="")
    )

def downgrade() -> None:
    op.drop_table("task")
