import datetime
from approvalratingsapp.models.meta import Base, relationship
from sqlalchemy import (
	Column,
	Integer,
	Text,
	ForeignKey,
	DateTime,
	)

class UserDemography(Base):
	__tablename__ = 'user_demography'

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
	demography_type_id = Column(Integer, ForeignKey('demography_type.id'), nullable=False)
	demography_id = Column(Integer, ForeignKey('demography.id'), nullable=False)
	created = Column(DateTime, default=datetime.datetime.utcnow)

	user = relationship("User", back_populates="user_demography")
	demography_type = relationship("DemographyType", back_populates="user_demography_type")
	demography = relationship("Demography", back_populates="user_demography")

	def __init__(self, user_id, demography_type_id, demography_id):
		self.user_id = user_id
		self.demography_type_id = demography_type_id
		self.demography_id = demography_id