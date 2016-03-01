import sqlalchemy as sa
from ..meta import DBSession
from ..ratee_type import RateeType

class RateeTypeRecordService(object):

	@classmethod
	def all(cls):
		return DBSession.query(RateeType).order_by(sa.desc(RateeType.id))

	@classmethod
	def by_id(cls, id):
		return RateeType.query.get(id)

	@classmethod
	def  by_ratee_type(cls, ratee_type):
		return DBSession.query(RateeType).filter_by(ratee_type=ratee_type).all()