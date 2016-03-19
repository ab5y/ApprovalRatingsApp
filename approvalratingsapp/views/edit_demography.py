from pyramid.httpexceptions import (
	HTTPFound,
	HTTPForbidden,
	)
from pyramid.view import view_config
from pyramid.security import authenticated_userid
from ..models.services.demography_record import DemographyRecordService
from ..models.services.demography_type_record import DemographyTypeRecordService
from ..models.services.demography_mapping_record import DemographyMappingRecordService
import json

@view_config(route_name='edit_demography', renderer='approvalratingsapp:templates/edit_demography.pt')
def edit_demography(request):
	institution_type = DemographyTypeRecordService.by_demography_type('institution')
	class_type = DemographyTypeRecordService.by_demography_type('class')
	optsub_type = DemographyTypeRecordService.by_demography_type('optional subject')
	schools = DemographyRecordService.by_demography_type(institution_type.id)
	classes = DemographyRecordService.by_demography_type(class_type.id)
	for class1 in classes:
		print class1.id
	optionalsubjects = DemographyRecordService.by_demography_type(optsub_type.id)
	return dict(
		url=request.application_url+'/edit_demography',
		logged_in=request.authenticated_userid,
		user_name=request.session['username'],
		schools=schools,
		certificates=None,
		classes=classes,
		optionalsubjects=optionalsubjects,
		)

@view_config(route_name='post_demo', renderer='string')
def post_demo(request):
	if request.method == 'POST':
		data = json.loads(json.dumps(request.json))
		selected_demo_id = int(data['selected_id'])
		# Get children of selected demo
		mappings = DemographyMappingRecordService.by_parent_demography_id(selected_demo_id)
		children_demos = []
		pairs = '{'
		for mapping in mappings:
			child_demo = DemographyRecordService.by_id(mapping.child_demography_id)
			pair = '"' + child_demo.demography_name + '"' + ':' + str(child_demo.id) + ','
			pairs += pair
		if len(mappings) == 0:
			return ''
		pairs = pairs[:-1] +  '}'
		print pairs
		return pairs