from approvalratingsapp.models.meta import Base, relationship
from sqlalchemy import (
	Column,
	Integer,
	Text,
	ForeignKey,
	)

class DemographyMapping(Base):
	__tablename__ = 'demography_mapping'

	id = Column(Integer, primary_key=True)
	parent_demography_id = Column(Integer, ForeignKey('demography.id'), nullable=False)
	child_demography_id = Column(Integer, ForeignKey('demography.id'), nullable=False)

	def __init__(self, parent_demography_id, child_demography_id):
		self.parent_demography_id = parent_demography_id
		self.child_demography_id = child_demography_id