from approvalratingsapp.models.meta import Base, relationship
from sqlalchemy import (
	Column,
	String,
	ForeignKey,
	Integer,
	Text,
	DateTime,
	)

class UserRating(Base):
	__tablename__ = 'user_rating'

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
	user = relationship("User", back_populates="user_ratings")
	ratee_id = Column(Integer, ForeignKey('ratee.id'), nullable=False)
	ratee = relationship("Ratee", back_populates="user_ratings")
	rating_val = Column(Integer, nullable=False)

	def __init__(self, user_id, ratee_id, rating_val):
		self.user_id = user_id
		self.ratee_id = ratee_id
		self.rating_val = rating_val