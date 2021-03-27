from models.base import Base
import sqlalchemy as sa
from sqlalchemy_utils import UUIDType
from datetime import datetime


class Post(Base):
    __tablename__ = 'posts'

    id = sa.Column(UUIDType, primary_key=True, server_default=sa.func.uuid_generate_v4())
    user = sa.Column(UUIDType, sa.ForeignKey('users.id'), nullable=False)
    # user = sa.Column(sa.Text, nullable=True)
    forum = sa.Column(UUIDType, sa.ForeignKey('forums.id'), nullable=True)
    title = sa.Column(sa.Text, nullable=True)
    description = sa.Column(sa.Text, nullable=True)
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow, nullable=False)
