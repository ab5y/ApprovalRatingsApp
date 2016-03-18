import sqlalchemy as sa
from sqlalchemy import func
from ..meta import DBSession
from ..user_demography import UserDemography

class UserDemographyRecordService(object):

	@classmethod
	def all(cls):
		return DBSession.query(UserDemography).order_by(sa.desc(UserDemography.id))

	@classmethod
	def by_id(cls, id):
		return DBSession.query(UserDemography).get(id)

	@classmethod
	def by_user_id(cls, id):
		return DBSession.query(UserDemography).filter_by(user_id=id).all()

	@classmethod
	def by_demography_id(cls, id):
		return DBSession.query(UserDemography).filter_by(demography_id=id).all()

	@classmethod
	def  by_demography_type_id(cls, id):
		return DBSession.query(UserDemography).filter_by(demography_type_id=id).all()

	@classmethod
	def by_user_id_and_demography_id(cls, user_id, demography_id):
		return DBSession.query(UserDemography).filter(UserDemography.user_id==user_id). \
											filter(UserDemography.demography_id==demography_id).first()

	@classmethod
	def commit(cls, user_demography_obj):
		return DBSession.add(user_demography_obj)