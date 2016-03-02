import sqlalchemy as sa
from ..meta import DBSession
from ..user_type import UserType

class UserTypeRecordService(object):

	@classmethod
	def all(cls):
		return DBSession.query(UserType).order_by(sa.desc(UserType.id))

	@classmethod
	def by_id(cls, id):
		# return User.query.get(id)
		return DBSession.query(UserType).filter_by(id=id).first()

	@classmethod
	def by_user_type(cls, user_type):
		return DBSession.query(UserType).filter_by(user_type=user_type).first()
