from django.shortcuts import render
from InstagramAPI import InstagramAPI
from search_username.settings import password, user_name
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import SaveDataBase, Base
import datetime
import itertools

engine = create_engine('sqlite:///users.db')


class GetInstagramInfo:
    def __init__(self, username, password):
        self.api = InstagramAPI(username=username, password=password)
        self.api.login()

    def get_user_id(self, name):
        """Returns id user."""
        self.api.searchUsername(name)
        return self.api.LastJson["user"]["pk"]

    def get_followers(self, user_id):
        """Returns list of user's followers."""
        followers = self.api.getTotalFollowers(user_id)
        return [follower['username'] for follower in followers]

    def get_followings(self, user_id):
        """Returns list of user's followings."""
        followings = self.api.getTotalFollowings(user_id)
        return [following['username'] for following in followings]


instagram_info = GetInstagramInfo(user_name, password)
user = None


def index(request):
    if request.method == "GET":
        name = request.GET.get('name', '')
        if name:
            user_id = instagram_info.get_user_id(name)
            followers = instagram_info.get_followers(user_id)
            followings = instagram_info.get_followings(user_id)
            global user
            user = dict(
                list_of_followers=followers,
                list_of_followings=followings,
                name=name)
        if request.GET.get('save') == '':
            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            for (followings, followers) in itertools.zip_longest(
                    user['list_of_followings'],
                    user['list_of_followers'],
                    fillvalue=' '):
                text = SaveDataBase(followings=followings,
                                    followers=followers,
                                    time=str(now))
                session.add(text)
            session.commit()
            return render(request, "index.html")
        return render(request, "index.html", context=user)
    else:
        return render(request, "index.html")
