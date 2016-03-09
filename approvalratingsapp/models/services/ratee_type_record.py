import sqlalchemy as sa
from sqlalchemy.sql.expression import func
from ..meta import DBSession
from ..ratee_type import RateeType

class RateeTypeRecordService(object):

	@classmethod
	def all(cls):
		return DBSession.query(RateeType).order_by(sa.desc(RateeType.id))

	@classmethod
	def by_id(cls, id):
		return DBSession.query(RateeType).get(id)

	@classmethod
	def  by_ratee_type(cls, ratee_type):
		return DBSession.query(RateeType).filter_by(ratee_type=ratee_type).first()

	@classmethod
	def create(cls, ratee_type_obj):
		DBSession.add(ratee_type_obj)
		return DBSession.query(func.max(RateeType.id)).scalar()