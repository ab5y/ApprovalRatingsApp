import sqlalchemy as sa
from sqlalchemy import func
from ..meta import DBSession
from ..demography_mapping import DemographyMapping

class DemographyMappingRecordService(object):

	@classmethod
	def all(cls):
		return DBSession.query(DemographyMapping).order_by(sa.desc(DemographyMapping.id))

	@classmethod
	def by_id(cls, id):
		return DBSession.query(DemographyMapping).get(id)

	@classmethod
	def by_parent_demography_id(cls, id):
		return DBSession.query(DemographyMapping).filter_by(parent_demography_id=id).all()
	
	@classmethod
	def by_child_demography_id(cls, id):
		return DBSession.query(DemographyMapping).filter_by(child_demography_id=id).all()