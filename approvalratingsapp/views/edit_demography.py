from pyramid.httpexceptions import (
	HTTPFound,
	HTTPForbidden,
	)
from pyramid.view import view_config
from pyramid.security import authenticated_userid
from ..models.services.demography_record import DemographyRecordService
from ..models.services.demography_type_record import DemographyTypeRecordService

@view_config(route_name='edit_demography', renderer='approvalratingsapp:templates/edit_demography.pt')
def edit_demography(request):
	institution_type = DemographyTypeRecordService.by_demography_type('institution')
	year_type = DemographyTypeRecordService.by_demography_type('year')
	degree_type = DemographyTypeRecordService.by_demography_type('degree')
	class_type = DemographyTypeRecordService.by_demography_type('class')
	optsub_type = DemographyTypeRecordService.by_demography_type('optional subject')
	schools = DemographyRecordService.by_demography_type(institution_type.id)
	years = DemographyRecordService.by_demography_type(year_type.id)
	degrees = DemographyRecordService.by_demography_type(degree_type.id)
	classes = DemographyRecordService.by_demography_type(class_type.id)
	optionalsubjects = DemographyRecordService.by_demography_type(optsub_type.id)
	return dict(
		url=request.application_url+'/edit_demography',
		logged_in=request.authenticated_userid,
		user_name=request.session['username'],
		schools=schools,
		years=years,
		degrees=degrees,
		certificates=None,
		classes=classes,
		optionalsubjects=optionalsubjects,
		)