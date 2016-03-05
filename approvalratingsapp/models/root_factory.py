from pyramid.security import (
    Allow,
    Everyone,
    )
class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'rater'),
                (Allow, 'admin', 'admin') ]

    def __init__(self, request):
        pass

    def __getitem__(self, key):
		user = UserRecordService.by_id(key)
		user.__parent__ = self
		user.__name__ = key
		print "SECURITY GET ITEM ENTERED. RETURNED: ", user.name
		return user