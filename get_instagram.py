import requests

BASE_URL = 'https://api.instagram.com/v1/'
APP_TOKEN = '11166443968.c11ca5e.3cbeb9018cd249a589cace56eaaff7e4'
def get_user():
	request_url = (f"{BASE_URL}users/self/?access_token={APP_TOKEN}")
	good_link = requests.get(request_url).json()
	return good_link['data']['counts']

def get_post():
	request_url = (f"{BASE_URL}users/self/media/recent/?access_token={APP_TOKEN}\n")
	print(f'Request data from {request_url}')
	recent_post = requests.get(request_url).json()
	for data in recent_post['data']:
		print(f"Like count post {data['likes']['count']} and comment post {data['comments']['count']}")
		print(f'Tags {data["caption"]["text"]}')
		print(data['images']['standard_resolution']['url'])
		print()

print(get_user())
get_post()
