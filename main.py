from InstagramAPI import InstagramAPI
import datetime
import itertools
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

    def save_db(self, followers, followings):
        engine = create_engine(f'sqlite:///users.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        for (followings, followers) in itertools.zip_longest(followings, followers, fillvalue=''):
            text = InstagramUsers(followings=followings, followers=followers, status="new", time=str(now))
            session.add(text)
            session.commit()

    def user(self):
        engine = create_engine(f'sqlite:///users.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

        database_followings = session.query(InstagramUsers.followings).all()
        database_follower = session.query(InstagramUsers.followers).all()

        followings_list = [y for x in database_followings for y in x]
        followers_list = [y for x in database_follower for y in x]

        for following in followings:  # це  в бд людей на яких я підписався недавно
            if following not in followings_list:
                if len(following) >= 1:
                    text = InstagramUsers(followings=following, followers='', status="subscribed", time=str(now))
                    session.add(text)
                    session.commit()

        for following_l in followings_list:  # це запис в бд людей від яких відписався я недавно
            if following_l not in followings:
                if len(following_l) >= 1:
                    text = InstagramUsers(followings=following_l, followers='', status="unsubscribed", time=str(now))
                    session.add(text)
                    session.commit()

        for follower in followers:  # це в бд людей які підписались на мене  недавно
            if follower not in followers_list:
                if len(follower) >= 1:
                    text = InstagramUsers(followings='', followers=follower, status="subscribed", time=str(now))
                    session.add(text)
                    session.commit()

        for follower_l in followers_list:  # це в бд людей які відписались від мене  недавно
            if follower_l not in followers:
                if len(follower_l) >= 1:
                    text = InstagramUsers(followings='', followers=follower_l, status="unsubscribed", time=str(now))
                    session.add(text)
                    session.commit()


if __name__ == '__main__':
    instagram_info = GetInstagramInfo(user_name, password)
    user_id = instagram_info.get_user_id('case_iphone_lviv2019')
    followers = instagram_info.get_followers(user_id)
    followings = instagram_info.get_followings(user_id)
    # instagram_info.save_db(followers, followings) # розкоментити для запуску,один раз записати і закоментити
    instagram_info.user() # розкоментити після того як бд створено

