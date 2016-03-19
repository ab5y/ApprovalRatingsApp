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
from ..models import RateeType, Ratee

import json
import time
from datetime import datetime, timedelta

@view_config(route_name='create_ratee', renderer='approvalratingsapp:templates/create_poll.pt')
def create_ratee(request):	
	ratee_types = RateeTypeRecordService.all()
	
	class Duration(object):
		"""docstring for Durations"""
		def __init__(self, time, text):
			super(Duration, self).__init__()
			self.time = time
			self.text = text
	
	durations = [Duration(datetime.now() + timedelta(hours=24), "1 Day"),
				Duration(datetime.now() + timedelta(hours=48), "2 Days"),
				Duration(datetime.now() + timedelta(hours=72), "3 Days"),
				Duration(datetime.now() + timedelta(hours=96), "4 Days"),
				Duration(datetime.now() + timedelta(hours=120), "5 Days"),
				Duration(datetime.now() + timedelta(hours=144), "6 Days"),
				Duration(datetime.now() + timedelta(hours=168), "7 Days"),]
	
	print "REQUEST.SESSION: ", request.session	
	return dict(
		url=request.application_url+'/create_ratee',
		logged_in=request.authenticated_userid,
		user_name=request.session['username'],
		ratee_types=ratee_types,
		durations=durations,
		)

@view_config(route_name='post_ratee', renderer='string')
def post_ratee(request):
	if request.method == 'POST':
		data = json.loads(json.dumps(request.json))
		title = data['title']
		ratee_type = data['type']
		duration = data['duration']
		ratee_type_object = RateeTypeRecordService.by_ratee_type(ratee_type)
		if not ratee_type_object:
			ratee_type_object = RateeType(ratee_type)
			RateeTypeRecordService.create(ratee_type_object)
			ratee_type_object = RateeTypeRecordService.by_ratee_type(ratee_type)
		ratee = Ratee(title, ratee_type_object.id)
		if duration:
			duration = datetime.strptime(duration, "%Y-%m-%d %H:%M:%S.%f")
			ratee.scheduled_close = duration
		result = RateeRecordService.create(ratee)
		ratee = RateeRecordService.by_id(result)
		print 'Title: ', ratee.name, \
				'\nType: ', ratee.ratee_type_id, \
				'\nDuration: ', ratee.scheduled_close, \
				'\nRatee ID: ', ratee.id, \
				'\nResult: ', result
		if result:
			print 'comes here'
			return request.application_url
	return 'OK'