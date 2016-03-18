import sqlalchemy as sa
from ..meta import DBSession
from ..user import User

class UserRecordService(object):

	@classmethod
	def all(cls):
		return DBSession.query(User).order_by(sa.desc(User.id))

	@classmethod
	def by_id(cls, id):
		# return User.query.get(id)
		return DBSession.query(User).filter_by(id=id).first()

	@classmethod
	def by_user_type(cls, user_type_id):
		return DBSession.query(User).filter_by(user_type_id=user_type_id).all()

	@classmethod
	def by_email(cls, email):
		return DBSession.query(User).filter_by(email=email).first()

	@classmethod
	def by_name(cls, name):
		return DBSession.query(User).filter_by(name=name).first()

	@classmethod
	def commit(cls, user_obj):
		return DBSession.add(user_obj)
