import sqlalchemy as sa
from sqlalchemy import func
from ..meta import DBSession
from ..user_rating import UserRating

class UserRatingRecordService(object):

	@classmethod
	def all(cls):
		return DBSession.query(UserRating).order_by(sa.desc(UserRating.id))

	@classmethod
	def by_id(cls, id):
		return DBSession.query(UserRating).get(id)

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
	def cumulative_ratee_rating(cls, ratee_id):
		# return DBSession.query(UserRating).filter_by(ratee_id=id).with_entities(func.sum(UserRating.rating)).scalar()
		all_ratings_by_id = cls.by_ratee_id(ratee_id)
		aggr = 0
		for rating in all_ratings_by_id:
			aggr = aggr + rating.rating
		return aggr

	@classmethod
	def commit(cls, user_rating_obj):
		return DBSession.add(user_rating_obj)