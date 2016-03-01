from approvalratingsapp.models.meta import Base, relationship
from sqlalchemy import (
	Column,
	String,
	ForeignKey,
	Integer,
	Text,
	)

class RateeType(Base):
	__tablename__ = 'ratee_type'
	id = Column(Integer, primary_key=True)
	ratee_type = Column(Text, unique=True)
	ratees = relationship("Ratee", back_populates="ratee_type")