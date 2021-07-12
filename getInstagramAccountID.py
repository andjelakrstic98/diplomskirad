from defines import getCreds, makeApiCall

def getInstagramAccountID( params ) :


	endpointParams = dict() 
	endpointParams['access_token'] = params['access_token'] 
	endpointParams['fields'] = 'instagram_business_account' 

	url = params['endpoint_base'] + params['page_id'] 

	return makeApiCall( url, endpointParams, params['debug'] )

params = getCreds() 
params['debug'] = 'no' 
response = getInstagramAccountID( params ) 

print ("\n----- INFORMATION ABOUT OUR INSTAGRAM ACCOUNT ------ ")
print ("\nInstagram Account ID:")
print (response['json_data']['instagram_business_account']['id'])
