from defines import getCreds, makeApiCall
import sys

def getHashtagInfo( params ) :
	""" Get info on a hashtag
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/ig_hashtag_search?user_id={user-id}&q={hashtag-name}&fields={fields}
	Returns:
		object: data from the endpoint
	"""

	endpointParams = dict()
	endpointParams['user_id'] = params['instagram_account_id']
	endpointParams['q'] = params['hashtag_name'] 
	endpointParams['fields'] = 'id,name'
	endpointParams['access_token'] = params['access_token'] 

	url = params['endpoint_base'] + 'ig_hashtag_search' 

	return makeApiCall( url, endpointParams, params['debug'] ) 

def getHashtagMedia( params ) :
	""" Get posts for a hashtag
	
	API Endpoints:
		https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/top_media?user_id={user-id}&fields={fields}
		https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/recent_media?user_id={user-id}&fields={fields}
	Returns:
		object: data from the endpoint
	"""

	endpointParams = dict() 
	endpointParams['user_id'] = params['instagram_account_id'] 
	endpointParams['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink' 
	endpointParams['access_token'] = params['access_token'] 

	url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type'] 

	return makeApiCall( url, endpointParams, params['debug'] )

def getHashtagMedia( params ) :
	""" Get posts for a hashtag
	
	API Endpoints:
		https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/top_media?user_id={user-id}&fields={fields}
		https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/recent_media?user_id={user-id}&fields={fields}
	Returns:
		object: data from the endpoint
	"""

	endpointParams = dict() 
	endpointParams['user_id'] = params['instagram_account_id'] 
	endpointParams['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink' 
	endpointParams['access_token'] = params['access_token'] 

	url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type'] 

	return makeApiCall( url, endpointParams, params['debug'] ) 


try : 
	hashtag = sys.argv[1] 
except : 
	hashtag = 'keyboard' 

params = getCreds()
params['hashtag_name'] = hashtag 
hashtagInfoResponse = getHashtagInfo( params ) 
params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id']; 

print ("---------- HASHTAG INFORMACIJE ----------") 
print ("\nHashtag: " + hashtag) 
print ("Hashtag ID: " + params['hashtag_id']) 

print ("\n---------- HASHTAG TOP OBJAVA ----------") 
params['type'] = 'top_media' 
hashtagTopMediaResponse = getHashtagMedia( params )

for post in hashtagTopMediaResponse['json_data']['data'] : 
	print ("\n---- OBJAVA ----") 
	print ("\nLink ka objavi:" )
	print (post['permalink']) 
	print ("\nOpis objave:" )
	print (post['caption'] )
	print ("\nVrsta medija:" )
	print (post['media_type']) 

