import sqlalchemy as sa
from sqlalchemy import func
from ..meta import DBSession
from ..demography_type import DemographyType

class DemographyTypeRecordService(object):
	@classmethod
	def all(cls):
		return DBSession.query(DemographyType).order_by(sa.desc(DemographyType.id))

	@classmethod
	def by_id(cls, id):
		return DBSession.query(DemographyType).get(id)

	@classmethod
	def by_demography_type(cls, demography_type):
		return DBSession.query(DemographyType).filter_by(demography_type=demography_type).first()

	@classmethod
	def get_id_by_demography_type(cls, demography_type):
		return DBSession.query(DemographyType).filter_by(demography_type=demography_type).first().id

	@classmethod
	def create(cls, demography_type_obj):
		return DBSession.add(demography_type_obj)