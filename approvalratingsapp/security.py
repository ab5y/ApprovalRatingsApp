from pyramid.security import Allow, Everyone, Authenticated, ALL_PERMISSIONS
from approvalratingsapp.models.services.user_record import UserRecordService

class UserFactory(object):
	__acl__ = [	(Allow, '%d', ALL_PERMISSIONS)	]

	def __init__(self, request):
		self.request = request

	def __getitem__(self, key):
		user = UserRecordService.by_id(key)
		user.__parent__ = self
		user.__name__ = key
		print "SECURITY GET ITEM ENTERED. RETURNED: ", user.name
		return user