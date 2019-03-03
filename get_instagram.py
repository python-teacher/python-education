from InstagramAPI import InstagramAPI
from key import user_name, password


class GetInstagramInfo:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.api = InstagramAPI(username=user_name, password=password)
		self.api.login()
		self.user_id = self.api.username_id

	def get_followers(self, user_id=None):
		"""Returns list of user's followers."""
		self.user_id = user_id if user_id is not None else self.user_id
		followers = self.api.getTotalFollowers(self.user_id)
		return [follower['username'] for follower in followers]

	def get_followings(self, user_id=None):
		"""Returns list of user's followings."""
		self.user_id = user_id if user_id is not None else self.user_id
		followings = self.api.getTotalFollowings(self.user_id)
		return [following['username'] for following in followings]


if __name__ == '__main__':
	instagram_info = GetInstagramInfo(user_name, password)
	print(instagram_info.get_followers())
	print(instagram_info.get_followings())
