from approvalratingsapp.models.meta import Base, relationship
from sqlalchemy import (
	Column,
	Integer,
	Text,
	ForeignKey,
	)

class Demography(Base):
	__tablename__ = 'demography'

	id = Column(Integer, primary_key=True)
	demography_type_id = Column(Integer, ForeignKey('demography_type.id'), nullable=False)
	demography_name = Column(Text, nullable=False, unique=True)
	demography_nic = Column(Text, unique=True)

	demography_type = relationship("DemographyType", back_populates="demography")
	user_demography = relationship("UserDemography", back_populates="demography")

	def __init__(self, demography_name, demography_type_id, demography_nic=None):
		self.demography_name = demography_name
		self.demography_type_id = demography_type_id
		self.demography_nic = demography_nic