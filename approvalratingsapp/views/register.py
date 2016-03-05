from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from ..models.meta import DBSession
from ..models.user import User
from ..models.services.user_type_record import UserTypeRecordService
from ..models.services.user_record import UserRecordService

@view_config(route_name='register', renderer='approvalratingsapp:templates/register.pt')
def register(request):
	register_url = request.route_url('register')
	referrer = request.url
	if referrer == register_url:
		referrer = '/'
		# We don't want to user the register form itself as came_from
	came_from = request.params.get('came_from', referrer)
	message = ''
	email = ''
	password = ''
	confirm_password = ''
	user_type_id = 0
	name = ''
	if 'form.submitted' in request.params:
		email = request.params['email']
		password = request.params['password']
		confirm_password = request.params['confirm_password']
		name = request.params['name']
		user_type_id = request.params['user_type'] # (UserTypeRecordService.by_user_type('rater')).id
		if email and password and name:
			if password == confirm_password:
				users = UserRecordService.by_email(email)
				if not users:
					user = User(name=name, email=email, user_type_id=user_type_id)
					user.enc_insert_password(password)
					try:
						DBSession.add(user)
						return HTTPFound(location='login')
					finally:
						message = 'There was an error processing your registration.'
				else:
					message = 'Email is already in use.'
			else:
				message = 'Passwords do not match.'
		else:
			message = 'At least one field is missing.'
	return dict(
		user_types=UserTypeRecordService.all(),
		message=message,
		url=request.application_url+'/register',
		came_from=came_from,
		user_type_id=user_type_id,
		name=name,
		email=email,
		password=password,
		confirm_password=confirm_password,
		logged_in=request.authenticated_userid,
		)