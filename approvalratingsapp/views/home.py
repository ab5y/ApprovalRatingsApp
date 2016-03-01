from pyramid.view import (
	view_config,
	forbidden_view_config,
	)

from ..models.services.user_type_record import UserTypeRecordService

@view_config(route_name='home', renderer='approvalratingsapp:templates/home.pt')
def home(request):
	return dict(
		logged_in=request.authenticated_userid)