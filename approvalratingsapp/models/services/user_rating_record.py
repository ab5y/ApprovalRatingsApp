import sqlalchemy as sa
from ..meta import DBSession
from ..user_rating import UserRating

class UserRatingRecordService(object):

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
	def by_user_id_and_ratee_id(cls, user_id, ratee_id):
		return DBSession.query(UserRating).filter(UserRating.user_id==user_id). \
											filter(UserRating.ratee_id==ratee_id).first()

	@classmethod
	def by_rating(cls, val):
		return DBSession.query(UserRating).filter_by(rating=val).all()

	@classmethod
	def commit(cls, user_rating_obj):
		DBSession.add(user_rating_obj)