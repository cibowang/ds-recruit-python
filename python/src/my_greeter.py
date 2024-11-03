import datetime

class MyGreeter:  

    def greeting(self):
        current_time = datetime.datetime.now().hour
        if 6 <= current_time < 12:
            return 'Good morning'
        elif 12 <= current_time < 18:
            return 'Good afternoon'
        else:
            return 'Good evening'

_my_beta_greeter = MyGreeter()
print(_my_beta_greeter.greeting())