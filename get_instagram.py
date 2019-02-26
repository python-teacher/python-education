from InstagramAPI import InstagramAPI
from key import *


def user(username):
	api = InstagramAPI(username=user_name, password=password)
	api.login()
	try:
		api.searchUsername(username)
		user_id = api.LastJson["user"]["pk"]
		print(user_id)
		followers = api.getTotalFollowers(user_id)
		followings = api.getTotalFollowings(user_id)
		print(f'Number of followers: {len(followers)}!')
		print(f'Number of followings: {len(followings)}!')
		for following in followings:
			print(f"{urlInstagram}{following['username']}")
	except Exception:
		print("Username doesn't exist")
		return False


if __name__ == '__main__':
	user('case_iphone_lviv2019')
