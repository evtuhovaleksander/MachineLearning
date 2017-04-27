from peewee import *


class FacebookUser(Model):
    id = PrimaryKeyField()
    url = CharField(default='')
    name = CharField(default='')
    job = CharField(default='')
    birthday = CharField(default='')


class Group(Model):
    id = PrimaryKeyField()
    name = CharField(default='')


class JoinFriends(Model):
    user = ForeignKeyField(FacebookUser, related_name='user1')
    user2 = ForeignKeyField(FacebookUser, related_name='user2')


class JoinGroups(Model):
    user = ForeignKeyField(FacebookUser)
    group = ForeignKeyField(Group)
