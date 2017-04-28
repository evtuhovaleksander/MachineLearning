import models
import datetime

def drop_tables():
    models.FacebookUser.drop_table()
    models.Group.drop_table()
    models.JoinFriends.drop_table()
    models.JoinGroups.drop_table()


def create_tables():
    models.FacebookUser.create_table()
    models.Group.create_table()
    models.JoinFriends.create_table()
    models.JoinGroups.create_table()


def recreate_db():
    drop_tables()
    create_tables()


recreate_db()
#models.FacebookUser.drop_table()
#models.FacebookUser.create_table()

#f=models.FacebookUser().get_or_create(id=1, url='url', name='name', job='job', birthday=datetime.datetime.now())
