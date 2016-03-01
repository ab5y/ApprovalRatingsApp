import sqlalchemy as sa
from ..meta import DBSession
from ..user_rating import UserRating

class UserRatingRecord(object):

	@classmethod
	def all(cls):
		return DBSession.query(UserRating).order_by(sa.desc(UserRating.id))

	@classmethod
	def by_id(cls, id):
		return UserRating.query.get(id)

	@classmethod
	def by_user_id(cls, id):
		return DBSession.query(UserRating).filter_by(user_id=id).all()

	@classmethod
	def by_ratee_id(cls, id):
		return DBSession.query(UserRating).filter_by(ratee_id=id).all()

	@classmethod
	def by_rating_val(cls, val):
		return DBSession.query(UserRating).filter_by(rating_val=val).all()