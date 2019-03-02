from InstagramAPI import InstagramAPI
from key import user_name, password


class GetInstagramInfo:
    def __init__(self, username, password):
	self.username = username
	self.password = password
	self.api = InstagramAPI(username=user_name, password=password)
	self.api.login()
	self.user_id = self.api.username_id

    def get_followers(self):
	"""Demonstrate followers of the profile"""
	followers = self.api.getTotalFollowers(self.user_id)
	return [follower['username'] for follower in followers]

    def get_followings(self):
	"""Demonstrate the following profile"""
	followings = self.api.getTotalFollowings(self.user_id)
	return [following['username'] for following in followings]


if __name__ == '__main__':
    instagram_info = GetInstagramInfo(user_name, password)
    print(instagram_info.get_followers())
    print(instagram_info.get_followings())
