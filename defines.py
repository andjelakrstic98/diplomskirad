import requests
import json

def getCreds() :
	

	creds = dict()
	creds['access_token'] = 'EAACAgO2o86wBADSyodXET5cg9hHVlZB9oqHqzkZB3OIeZBpLWrvtrb1KZCrINR3pDbMURAhnQMHeJ78S1XuHWLTJy7SXkbjfK54jPKXTCZBOhNg3x6TjXdk6IcIjeAbIHtuufb8AyC6lrGs6rn3P29U3DAQceNLGjoXP6pcQZCpJIyeU0V1ZAg3' 
	creds['client_id'] = '141291231441836' 
	creds['client_secret'] = '9a9590bb7f72ef9d16d26d79154784a6' 
	creds['graph_domain'] = 'https://graph.facebook.com/' 
	creds['graph_version'] = 'v11.0' 
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' 
	creds['debug'] = 'no' 
	creds['page_id'] = '101744444704094' 
	creds['instagram_account_id'] = '17841448714009295' 
	creds['ig_username'] = 'angel0tech' 

	return creds

def makeApiCall( url, endpointParams, debug = 'no' ) : 
	data = requests.get( url, endpointParams )

	response = dict()
	response['url'] = url
	response['endpoint_params'] = endpointParams
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4)
	response['json_data'] = json.loads( data.content )
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 )


	return response



