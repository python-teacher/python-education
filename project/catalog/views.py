from django.shortcuts import render,redirect

from InstagramAPI import InstagramAPI

user_name = 'case_iphone_lviv2019'
password = 'игвяеуіе123'


class GetInstagramInfo:
	def __init__(self, username, password):
		self.api = InstagramAPI(username=username, password=password)
		self.api.login()

	def get_user_id(self, name):
		"""Returns id user."""
		self.api.searchUsername(name)
		return self.api.LastJson["user"]["pk"]

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


instagram_info = GetInstagramInfo(user_name, password)
def index(request):
	user = None
	if request.method == "GET":
		name = request.GET.get('name', '')
		if name:
			user_id = instagram_info.get_user_id(name)
			followers = instagram_info.get_followers(user_id)
			followings = instagram_info.get_followings(user_id)
			user = dict(get_followers=followers, get_followings=followings,
						name=name)
		return render(request, "../templates/index.html", context=user)

	else:
		return render(request, "../templates/index.html")
