"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
<<<<<<< HEAD
down_revision: Union[str, None] = ${repr(down_revision)}
=======
down_revision: Union[str, Sequence[str], None] = ${repr(down_revision)}
>>>>>>> 916b82829813a56b53efc07a2fbca561446ec169
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
<<<<<<< HEAD
=======
    """Upgrade schema."""
>>>>>>> 916b82829813a56b53efc07a2fbca561446ec169
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
<<<<<<< HEAD
=======
    """Downgrade schema."""
>>>>>>> 916b82829813a56b53efc07a2fbca561446ec169
    ${downgrades if downgrades else "pass"}
