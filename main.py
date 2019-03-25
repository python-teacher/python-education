import datetime
import itertools

from InstagramAPI import InstagramAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, InstagramUsers

user_name = 'case_iphone_lviv2019'
password = 'игвяеуіе123'


class GetInstagramInfo:
    def __init__(self, username, password):
        self.api = InstagramAPI(username=username, password=password)
        self.api.login()
        engine = create_engine('sqlite:///users.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

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

    def time_now(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    def object_instagram(self, followings, followers, status, time):
        text = InstagramUsers(followings=followings, followers=followers, status=status, time=time)
        self.session.add(text)
        self.session.commit()

    def save_db(self, followers, followings):
        """Written followers and followings user to database"""
        now = self.time_now()
        for (followings, followers) in itertools.zip_longest(followings, followers, fillvalue=''):
            self.object_instagram(followings, followers, 'new', str(now))

    def database_followings(self):
        """Getting all followings of the database"""
        database_followings = self.session.query(InstagramUsers.followings).all()
        return [y for x in database_followings for y in x]

    def database_follower(self):
        """Getting all followers of the database"""
        database_follower = self.session.query(InstagramUsers.followers).all()
        return [y for x in database_follower for y in x]

    def subscribed(self, new_followers, new_followings):
        """Check whether the current user is in the database.If not, then add(status- subscribed)"""
        now = self.time_now()
        for following in new_followings:  # write to database subscribed followings
            if following not in self.database_followings():
                self.object_instagram(followings=following, followers='', status="subscribed", time=str(now))
        for follower in new_followers:  # write to database subscribed followers
            if follower not in self.database_follower():
                self.object_instagram(followings='', followers=follower, status="subscribed", time=str(now))

    def unsubscribed(self, new_followers, new_followings):
        """Check whether the current database user is in the current list.If not, then add(status-unsubscribed)"""
        now = self.time_now()
        for following_l in self.database_followings():  # write to database unsubscribed followings
            if len(following_l) >= 1:
                if following_l not in new_followings:
                    self.object_instagram(followings=following_l, followers='', status="unsubscribed", time=str(now))
        for follower_l in self.database_follower():  # write to database unsubscribed followers
            if len(follower_l) >= 1:
                if follower_l not in new_followers:
                    self.object_instagram(followings='', followers=follower_l, status="unsubscribed", time=str(now))

    def main(self, followers, followings):
        try:
            session = [x for x in self.session.query(InstagramUsers.status).first()]
            if session[0] == 'new':
                self.subscribed(followers, followings)
                self.unsubscribed(followers, followings)
        except TypeError:
            self.save_db(followers, followings)


if __name__ == '__main__':
    instagram_info = GetInstagramInfo(user_name, password)
    # user_id = instagram_info.get_user_id('case_iphone_lviv2019')
    user_id = instagram_info.get_user_id('Sergiy')
    followers = instagram_info.get_followers(user_id)
    followings = instagram_info.get_followings(user_id)
    instagram_info.main(followers, followings)
