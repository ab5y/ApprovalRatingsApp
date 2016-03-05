from pyramid.httpexceptions import (
	HTTPFound,
	HTTPForbidden,
	)
from pyramid.view import (
	view_config,
	forbidden_view_config,
	)
from pyramid.security import authenticated_userid

from ..models.services.user_type_record import UserTypeRecordService
from ..models.services.ratee_record import RateeRecordService
from ..models.services.ratee_type_record import RateeTypeRecordService
from ..models.services.user_rating_record import UserRatingRecordService
from ..models import UserRating

import json

@view_config(route_name='create_ratee', renderer='approvalratingsapp:templates/create_poll.pt')
def create_ratee(request):	
	ratee_types = RateeTypeRecordService.all()
	return dict(
		logged_in=request.authenticated_userid,
		ratee_types=ratee_types,
		)