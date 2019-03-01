from InstagramAPI import InstagramAPI
from key import user_name, password, urlInstagram

api = InstagramAPI(username=user_name, password=password)
api.login()
user_id = api.username_id


def get_followers():
	followers_list = list()
	followers = api.getTotalFollowers(user_id)
	for follower in followers:
		followers_list.append(f"{urlInstagram}{follower['username']}")
	return followers_list

def get_followings():
	followings_list = list()
	followings = api.getTotalFollowings(user_id)
	for following in followings:
		followings_list.append(f"{urlInstagram}{following['username']}")
	return followings_list


if __name__ == '__main__':
	print(get_followers())
	print(get_followings())
