from InstagramAPI import InstagramAPI
from key import *


def user():
	api = InstagramAPI(username=user_name, password=password)
	api.login()
	user_id = 9755530901  # 
	followers = api.getTotalFollowers(user_id)
	followings = api.getTotalFollowings(user_id)

	print(f'Number of followers: {len(followers)}!')
	print(f'Number of followings: {len(followings)}!')

	for following in followings:
		print(f"{urlInstagram}{following['username']}")


if __name__ == '__main__':
	user()
