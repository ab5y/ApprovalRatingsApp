import sqlalchemy as sa
from sqlalchemy.sql.expression import func
from ..meta import DBSession
from ..ratee import Ratee

class  RateeRecordService(object):
	"""docstring for  RateeRecordService"""
	
	@classmethod
	def all(cls):
		return DBSession.query(Ratee).order_by(sa.desc(Ratee.id))

	@classmethod
	def by_id(cls, id):
		return DBSession.query(Ratee).get(id)

	@classmethod
	def by_user_type(cls, id):
		return DBSession.query(Ratee).filter_by(user_type_id=id).all()

	@classmethod
	def by_name(cls, name):
		return DBSession.query(Ratee).filter_by(name=name).all()

	@classmethod
	def create(cls, ratee_obj):
		DBSession.add(ratee_obj)
		return DBSession.query(func.max(Ratee.id)).scalar()