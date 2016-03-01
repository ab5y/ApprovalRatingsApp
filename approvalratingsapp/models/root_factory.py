from pyramid.security import (
    Allow,
    Everyone,
    )
class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, '', 'edit') ]

    def __init__(self, request):
        pass