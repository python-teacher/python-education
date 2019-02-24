from InstagramAPI import InstagramAPI
from key import *
import requests


def user(username):
	request = requests.get(userID + str(username)).json()
	user_id = 0
	for i in request['users']:
		user_id = int(i['user']['pk'])
	api = InstagramAPI(username=user_name, password=password)
	api.login()
	followers = api.getTotalFollowers(user_id)
	followings = api.getTotalFollowings(user_id)
	print(f'Number of followers: {len(followers)}!')
	print(f'Number of followings: {len(followings)}!')
	for following in followings:
		print(f"{urlInstagram}{following['username']}")


if __name__ == '__main__':
	user('sergiy.budz')
