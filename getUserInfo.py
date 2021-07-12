from defines import getCreds, makeApiCall

def getAccountInfo( params ) :

	endpointParams = dict()
	endpointParams['fields'] = 'business_discovery.username('+ params['ig_username'] +'){username,name,ig_id,id,biography,follows_count,followers_count,media_count,media }'
	endpointParams['access_token'] = params['access_token']

	url = params['endpoint_base'] + '/' + params['instagram_account_id']

	return makeApiCall( url, endpointParams, params['debug'] )

params = getCreds()
params['debug'] = 'no'
response = getAccountInfo( params )


print ("\n----- INFORMATION ABOUT USER'S ACCOUNT ------ \n")
print ("Username:")
print (response['json_data']['business_discovery']['username'])
print ("\nNumber of posts:")
print (response['json_data']['business_discovery']['media_count'])
print ("\nFollowers:")
print (response['json_data']['business_discovery']['followers_count'])
print ("\nFollowing:")
print (response['json_data']['business_discovery']['follows_count'])
print ("\nBiography:")
print (response['json_data']['business_discovery']['biography'])
