from pyramid.httpexceptions import (
	HTTPFound,
	HTTPForbidden,
	)
from pyramid.view import view_config
from pyramid.security import authenticated_userid
from ..models import UserDemography
from ..models.services.demography_record import DemographyRecordService
from ..models.services.demography_type_record import DemographyTypeRecordService
from ..models.services.demography_mapping_record import DemographyMappingRecordService
from ..models.services.user_demography_record import UserDemographyRecordService
import json

@view_config(route_name='edit_demography', renderer='approvalratingsapp:templates/edit_demography.pt')
def edit_demography(request):
	institution_type = DemographyTypeRecordService.by_demography_type('institution')
	schools = DemographyRecordService.by_demography_type(institution_type.id)
	return dict(
		url=request.application_url+'/edit_demography',
		logged_in=request.authenticated_userid,
		user_name=request.session['username'],
		schools=schools,
		)

@view_config(route_name='post_demo', renderer='string')
def post_demo(request):
	if request.method == 'POST':
		data = json.loads(json.dumps(request.json))
		selected_demo_id = int(data['selected_id'])
		# Get children of selected demo
		mappings = DemographyMappingRecordService.by_parent_demography_id(selected_demo_id)
		if len(mappings) == 0:
			return ''
		children_demos = []
		pairs = '{'
		for mapping in mappings:
			child_demo = DemographyRecordService.by_id(mapping.child_demography_id)
			pair = '"' + child_demo.demography_name + '"' + ':' + str(child_demo.id) + ','
			pairs += pair
		pairs = pairs[:-1] +  '}'
		print pairs
		return pairs

@view_config(route_name='submit_demo', renderer='string')
def submit_demo(request):
	if request.method == 'POST':
		data = json.loads(json.dumps(request.json))
		user_id = int(authenticated_userid(request))
		user_demos = UserDemographyRecordService.by_user_id(user_id)
		for key, value in data.items():
			demo = DemographyRecordService.by_id(int(value))
			demo_type = DemographyTypeRecordService.by_id(demo.demography_type_id)
			if demo_type.demography_type == "subject":
				pass
			else:
				existing_user_demo = None
				for user_demo in user_demos:
					if user_demo.type_id == demo.demography_type_id:
						existing_user_demo = user_demo
						break
				if existing_user_demo == None:
					existing_user_demo = UserDemography(user_id, demo_type.id, demo.id)
				else: 
					existing_user_demo.demography_type_id = demo_type.id
					existing_user_demo.demography_id = demo.id
				UserDemographyRecordService.commit(existing_user_demo)
		return request.application_url