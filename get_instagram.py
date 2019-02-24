from InstagramAPI import InstagramAPI
from key import *
import requests


def get_user_id(username):
	request = requests.get(userID + str(username)).json()
	userid = 0
	for i in request['users']:
		userid = int(i['user']['pk'])
	return userid


def user(user_id):
	api = InstagramAPI(username=user_name, password=password)
	api.login()
	followers = api.getTotalFollowers(user_id)
	followings = api.getTotalFollowings(user_id)

	print(f'Number of followers: {len(followers)}!')
	print(f'Number of followings: {len(followings)}!')

	for following in followings:
		print(f"{urlInstagram}{following['username']}")


if __name__ == '__main__':
	ID = get_user_id('case_iphone_lviv2019')
	user(ID)
