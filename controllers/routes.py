from sqlalchemy import func
from models.base import session

from models.post import Post


def total_forum():
    total = session.query(func.count(Post.id))
    print(total)


def most_user_forum():
    user_obj = session.query(func.count(Post.user), Post.user).group_by(Post.user).all()
    user_obj.sort(key=lambda tup: tup[0], reverse=True)
    print(user_obj)


def active_forum_user():
    obj = session.query(
        Post.user, func.max(Post.created_at).label('last_user')).group_by(Post.user).subquery()
    print(obj)
