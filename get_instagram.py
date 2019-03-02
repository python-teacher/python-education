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
        followers_list = list()
        followers = self.api.getTotalFollowers(self.user_id)
        for follower in followers:
            followers_list.append(follower['username'])
        return followers_list

    def get_followings(self):
        followings_list = list()
        followings = self.api.getTotalFollowings(self.user_id)
        for following in followings:
            followings_list.append(following['username'])
        return followings_list


if __name__ == '__main__':
    instagram_info = GetInstagramInfo(user_name, password)
    print(instagram_info.get_followers())
    print(instagram_info.get_followings())
