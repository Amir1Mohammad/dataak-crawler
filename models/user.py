from models.base import Base
import sqlalchemy as sa
from sqlalchemy_utils import UUIDType
from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(UUIDType, primary_key=True, server_default=sa.func.uuid_generate_v4())
    name = sa.Column(sa.Text, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow, nullable=False)
