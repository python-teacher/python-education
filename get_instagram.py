from InstagramAPI import InstagramAPI
from key import *


def user():
	api = InstagramAPI(username=user_name, password=password)
	api.login()
	try:
		user_id = api.username_id
		followers = api.getTotalFollowers(user_id)
		followings = api.getTotalFollowings(user_id)
		print(f'Number of followers: {len(followers)} followings: {len(followings)}')
		for following in followings:
			print(f"{urlInstagram}{following['username']}")
	except Exception:
		print("Username doesn't exist")
		return False


if __name__ == '__main__':
	user()