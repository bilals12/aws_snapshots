from time import time, sleep
import webbrowser
from boto3.session import Session
import os

def session_sso(_):

	session = Session()
	account_id = os.environ.get('AWS_ACCOUNT_ID') or input("enter aws account ID: ")
	start_url = os.environ.get('AWS_START_URL') or input("enter aws sso start url: ")
	region = os.environ.get('AWS_REGION') or input("enter aws region: ")

	sso_oidc = session.client('sso-oidc')
	client_creds = sso_oidc.register_client(
		clientName='myApp',
		clientType='public',
	)

	device_authorization = sso_oidc.start_device_authorization(
		clientId=client_creds['clientId'],
		clientSecret=client_creds['clientSecret'],
		startUrl=start_url,
	)

	url = device_authorization['verificationUriComplete']
	device_code = device_authorization['deviceCode']
	expires_in = device_authorization['expiresIn']
	interval = device_authorization['interval']
	webbrowser.open(url, autoraise=True)

	for n in range(1, expires_in // interval + 1):
		sleep(interval)
		try:
			token = sso_oids.create_token(
				grantType='urn:ietf:params:oauth:grant-type:device_code',
				deviceCode=device_code,
				clientId=client_creds['clientId'],
				clientSecret=client_creds['clientSecret'],
			)
			break
		except sso_oidc.exceptions.AuthorizationPendingException
			pass

	access_token = token['accessToken']

	sso = session.client('sso')
	account_roles = sso.list_account_roles(
		accessToken=access_token,
		accountId=account_id,
	)
	roles = account_roles['roleList']
	role = roles[0]
	role_creds = sso.get_role_credentials(
		roleName=role['roleName'],
		accountId=account_id,
		accessToken=access_token,
	)

	session = Session(
		region_name=region,
		aws_access_key_id=role_creds['roleCredentials']['accessKeyId'],
		aws_secret_access_key=role_creds['roleCredentials']['secretAccessKey'],
		aws_session_token=role_creds['roleCredentials']['sessionToken'])

	return session