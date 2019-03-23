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

    def create_database(self):
        engine = create_engine('sqlite:///users.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        return Session()

    def time_now(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    def save_db(self, connect_database, followers, followings):
        """Written followers and followings user to database"""
        session = connect_database
        now = self.time_now()
        for (followings, followers) in itertools.zip_longest(followings, followers, fillvalue=''):
            text = InstagramUsers(followings=followings, followers=followers, status="new", time=str(now))
            session.add(text)
        session.commit()

    def database_followings(self, connect_database):
        """Getting all followings of the database"""
        session = connect_database
        database_followings = session.query(InstagramUsers.followings).all()
        return [y for x in database_followings for y in x]

    def database_follower(self, connect_database):
        """Getting all followers of the database"""
        session = connect_database
        database_follower = session.query(InstagramUsers.followers).all()
        return [y for x in database_follower for y in x]

    def subscribed(self, connect_database, new_followers, new_followings):
        """Check whether the current user is in the database.If not, then add(status- subscribed)"""
        session = connect_database
        now = self.time_now()
        for following in new_followings:  # write to database subscribed followings
            if following not in self.database_followings(connect_database):
                text = InstagramUsers(followings=following, followers='', status="subscribed", time=str(now))
                session.add(text)
            session.commit()
        for follower in new_followers:  # write to database subscribed followers
            if follower not in self.database_follower(connect_database):
                text = InstagramUsers(followings='', followers=follower, status="subscribed", time=str(now))
                session.add(text)
            session.commit()

    def unsubscribed(self, connect_database, new_followers, new_followings):
        """Check whether the current database user is in the current list.If not, then add(status-unsubscribed)"""
        session = connect_database
        now = self.time_now()

        for following_l in self.database_followings(connect_database):  # write to database unsubscribed followings
            if following_l in new_followings:
                text = InstagramUsers(followings=following_l, followers='', status="unsubscribed", time=str(now))
                session.add(text)
                session.commit()
        for follower_l in self.database_follower(connect_database):  # write to database unsubscribed followers
            if follower_l in new_followers:
                text = InstagramUsers(followings='', followers=follower_l, status="unsubscribed", time=str(now))
                session.add(text)
                session.commit()


if __name__ == '__main__':
    instagram_info = GetInstagramInfo(user_name, password)
    user_id = instagram_info.get_user_id('case_iphone_lviv2019')
    followers = instagram_info.get_followers(user_id)
    followings = instagram_info.get_followings(user_id)
    connect_db = instagram_info.create_database()  # connect to database
    try:
        session = [x for x in connect_db.query(InstagramUsers.status).first()]
        if session[0] == 'new':
            instagram_info.subscribed(connect_db, followers, followings)  # to uncomment when bd is created
            instagram_info.unsubscribed(connect_db, followings, followers)  # to uncomment when bd is created
        else:
            print(True)
            instagram_info.save_db(connect_db,followers,followings)  # run once and commented
    except TypeError:
        instagram_info.save_db(connect_db, followers, followings)  # run once and commented
