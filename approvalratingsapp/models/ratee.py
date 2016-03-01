from datetime import datetime, timedelta
from approvalratingsapp.models.meta import Base, relationship
from pyramid.security import Allow
from sqlalchemy import (
	Column,
	String,
	ForeignKey,
	Integer,
	Text,
	Unicode,
	UnicodeText,
	DateTime,
	)

class Ratee(Base):
	__tablename__ = 'ratee'

	id = Column(Integer, primary_key=True)
	ratee_type_id = Column(Integer, ForeignKey('ratee_type.id'), nullable=False)
	name = Column(Text, nullable=False)
	created = Column(DateTime, default=datetime.utcnow)
	scheduled_close = Column(DateTime, default=datetime.now() + timedelta(hours=24))
	
	ratee_type = relationship("RateeType", back_populates="ratees")
	user_ratings = relationship("UserRating", back_populates="ratee")

	def __init__(self, name, ratee_type_id):
		self.name = name
		self.ratee_type_id = ratee_type_id