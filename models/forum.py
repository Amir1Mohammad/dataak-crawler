from models.base import Base
import sqlalchemy as sa
from sqlalchemy_utils import UUIDType
from datetime import datetime


class Forum(Base):
    __tablename__ = 'forums'

    id = sa.Column(UUIDType, primary_key=True, server_default=sa.func.uuid_generate_v4())
    title = sa.Column(sa.Text, nullable=True)
    description = sa.Column(sa.Text, nullable=True)
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow, nullable=False)
