from espy.entity import Entity
from espy.decorators import set_method


class User(Entity):

    @set_method
    def increase_badge(users, amount):
        print(users.operations)
        print(amount)


users = User.where(active=True).where(age=18)

print(users)

users.increase_badge(10)