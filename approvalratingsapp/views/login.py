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

from ..models.services.user_record import UserRecordService

@view_config(route_name='login', renderer='approvalratingsapp:templates/login.pt')
@forbidden_view_config(renderer='approvalratingsapp:templates/login.pt')
def login(request):
	if authenticated_userid(request):
		return HTTPForbidden()
	login_url = request.route_url('login')
	register_url = request.route_url('register')
	referrer = request.url
	if referrer == login_url:
		referrer = '/'
		# never use the login form itself as came_from
	came_from = request.params.get('came_from', referrer)
	message = ''
	if referrer == register_url:
		message = 'Your registration was successful. Please login using your regd email and password.'
	login = ''
	password = ''
	if 'form.submitted' in request.params:
		login = request.params['login']
		password = request.params['password']
		user = UserRecordService.by_email(login)
		if user:
			if user.validate_password(password):
				headers = remember(request, user.id)
				return HTTPFound(location=came_from, headers=headers)
			message = 'Failed login. Incorrect password.'
		else: message = 'Failed login. Incorrect username or password.'
	return dict(
		message=message,
		url=request.application_url+'/login',
		came_from=came_from,
		login=login,
		password=password,
		logged_in=request.authenticated_userid,
		)

@view_config(route_name='logout')
def logout(request):
	headers = forget(request)
	return HTTPFound(location=request.route_url('home'), headers=headers)