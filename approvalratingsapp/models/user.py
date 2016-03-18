import datetime
from approvalratingsapp.models.meta import Base, user_pwd_context, relationship
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
from approvalratingsapp.models.services.user_type_record import UserTypeRecordService

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	user_type_id = Column(Integer, ForeignKey('user_type.id'), nullable=False)
	name = Column(Text, nullable=False)
	email = Column(String(64), unique=True, nullable=False)
	password = Column(String(300), nullable=False)
	last_logged = Column(DateTime)
	birthday = Column(DateTime)
	gender = Column(Text)
	
	user_type = relationship("UserType", back_populates="users")
	user_ratings = relationship("UserRating", back_populates="user")
	user_demography = relationship("UserDemography", back_populates="user")

	def __init__(self, name, email, user_type_id):
		self.name = name
		self.email = email
		self.user_type_id = user_type_id

	def set_last_logged(self, time):
		self.last_logged = time

	def validate_password(self, password):
		ok, new_hash = user_pwd_context.verify_and_update(password, self.password)
		if ok:
			if new_hash:
				enc_insert_password(password)
		return ok

	def enc_insert_password(self, password):
		self.password = user_pwd_context.encrypt(password)

	def __repr__(self):
		return "<User(nickname = '%s', password = '%s', email = '%s')>" % (self.nickname, self.password, self.email)

	@property
	def __acl__(self):
		usr_typ = UserTypeRecordService.by_id(self.user_type_id)
		print "USER __ACL__ ENTERED. RETURNED: ", self.id, "TYPE: ", usr_typ.user_type
		if str(usr_typ.user_type) == 'admin':
			return [(Allow, 'admin', str(usr_typ.user_type))]
		return [(Allow, self.id, str(usr_typ.user_type))]