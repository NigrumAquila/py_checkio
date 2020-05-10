class Friend:
    def __init__(self, name):
        self.name = name
        self.message = 'No party...'

    def invite(self, message):
        self.message = message

    def show_invite(self):
        return self.message


class Party:
    def __init__(self, place):
        self.place = place
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)
    
    def del_friend(self, friend):
        self.friends.remove(friend)

    def send_invites(self, date):
        for friend in self.friends:
            friend.invite(f'{self.place}: {date}')