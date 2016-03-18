from approvalratingsapp.models.meta import Base, relationship
from sqlalchemy import (
	Column,
	ForeignKey,
	Integer,
	Text,
	)

class DemographyType(Base):
	__tablename__ = 'demography_type'
	id = Column(Integer, primary_key=True)
	demography_type = Column(Text, unique=True)

	demography = relationship("Demography", back_populates="demography_type")
	user_demography_type = relationship("UserDemography", back_populates="demography_type")

	def __init__(self, demography_type):
		self.demography_type = demography_type