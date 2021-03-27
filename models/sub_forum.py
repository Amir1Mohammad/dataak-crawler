from base import Base
import sqlalchemy as sa


class SubForum(Base):
	__tablename__ = 'sub_forums'
	
	id = sa.Column(UUIDType, primary_key=True, server_default=sa.func.uuid_generate_v4())
	forum_id = sa.Column(UUIDType, sa.ForeignKey('forums.id'), nullable=False)
	user_id = sa.Column(UUIDType, sa.ForeignKey('users.id'), nullable=False)
	title = sa.Column(sa.Text, nullable=False)
	description = sa.Column(sa.Text, nullable=False)
	created_at = sa.Column(sa.DateTime, default=datetime.utcnow, nullable=False)
