from pyramid.httpexceptions import (
	HTTPFound,
	HTTPForbidden,
	)
from pyramid.view import (
	view_config,
	forbidden_view_config,
	)
from pyramid.security import (
	remember,
	forget,
	authenticated_userid,
	)

from ..models.services.user_type_record import UserTypeRecordService
from ..models.services.ratee_record import RateeRecordService
from ..models.services.user_rating_record import UserRatingRecordService
from ..models import UserRating

import json

@view_config(route_name='home', renderer='approvalratingsapp:templates/home.pt')
def home(request):
	if not authenticated_userid(request):
		return HTTPFound(location=request.route_url('login'))
	ratees = RateeRecordService.all()
	user_id = int(authenticated_userid(request))
	# user_ratings = UserRatingRecordService.by_user_id(authenticated_userid(request))
	ratings_tuple_list = []
	for ratee in ratees:
		user_rating = UserRatingRecordService.by_user_id_and_ratee_id(user_id, ratee.id)
		cumulative_rating = UserRatingRecordService.cumulative_ratee_rating(ratee.id)
		ratings_tuple_list.append((ratee, user_rating, cumulative_rating))
	return dict(
		ratings_tuple_list=ratings_tuple_list,
		logged_in=request.authenticated_userid,
		)

@view_config(route_name='post_rating', renderer='string')
def homepost(request):
	if request.method == 'POST':
		data = json.loads(json.dumps(request.json))
		ratee_id = int(data['ratee_id'])
		rating = int(data['rating'])
		user_id = int(authenticated_userid(request))
		user_rating = UserRatingRecordService.by_user_id_and_ratee_id(user_id, ratee_id)
		if user_rating:
			user_rating.rating = rating
		else:
			user_rating = UserRating(user_id, ratee_id, rating)
		UserRatingRecordService.commit(user_rating)
		return UserRatingRecordService.cumulative_ratee_rating(ratee_id)
	return 'OK'