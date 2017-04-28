from peewee import *

db = SqliteDatabase('peewee.db')

class FacebookUser(Model):
    id = PrimaryKeyField()
    url = CharField(default='')
    name = CharField(default='')
    job = CharField(default='')
    birthday = IntegerField(default=0)

    class Meta:
        # data is coming from schools.db
        database = db

class Group(Model):
    id = PrimaryKeyField()
    name = CharField(default='')

    class Meta:
        # data is coming from schools.db
        database = db

class JoinFriends(Model):
    user = ForeignKeyField(FacebookUser, related_name='user1')
    user2 = ForeignKeyField(FacebookUser, related_name='user2')

    class Meta:
        # data is coming from schools.db
        database = db

class JoinGroups(Model):
    user = ForeignKeyField(FacebookUser)
    group = ForeignKeyField(Group)

    class Meta:
        # data is coming from schools.db
        database = db