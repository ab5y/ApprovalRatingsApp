import sqlalchemy as sa
from sqlalchemy.sql.expression import func
from ..meta import DBSession
from ..demography import Demography

class DemographyRecordService(object):

	@classmethod
	def all(cls):
		return DBSession.query(Demography).order_by(sa.desc(Demography.id))

	@classmethod
	def by_id(cls, id):
		return DBSession.query(Demography).get(id)

	@classmethod
	def by_demography_type(cls, id):
		return DBSession.query(Demography).filter_by(demography_type_id=id).all()

	@classmethod
	def by_name(cls, name):
		return DBSession.query(Demography).filter_by(demography_name=name).first()

	@classmethod
	def get_id_by_name(cls, name):
		return DBSession.query(Demography).filter_by(demography_name=name).first().id

	@classmethod
	def get_type_id_by_id(cls, id):
		return cls.by_id(id).demography_type_id

	@classmethod
	def create(cls, demography_obj):
		return DBSession.add(demography_obj)