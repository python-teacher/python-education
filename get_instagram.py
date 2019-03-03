from InstagramAPI import InstagramAPI
from key import user_name, password


class GetInstagramInfo:
    def __init__(self, username, password):
	self.api = InstagramAPI(username=user_name, password=password)
	self.api.login()
	
    def get_followers(self, user_id=None):
	"""Returns list of user's followers."""
	user_id = user_id or self.api.username_id
	followers = self.api.getTotalFollowers(user_id)
	return [follower['username'] for follower in followers]

    def get_followings(self, user_id=None):
    	"""Returns list of user's followings."""
	user_id = user_id or self.api.username_id
	followings = self.api.getTotalFollowings(user_id)
	return [following['username'] for following in followings]


if __name__ == '__main__':
    instagram_info = GetInstagramInfo(user_name, password)
    print(instagram_info.get_followers())
    print(instagram_info.get_followings())
