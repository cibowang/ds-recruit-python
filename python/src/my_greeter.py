import datetime  
 
class MyGreeter:  

    def greeting(self, current_time=None):  
        if current_time is None:  
            now = datetime.datetime.now()  
        else:  
            now = current_time  
         
        self.hour = now.hour  
 
        if 6 <= self.hour < 12:  
            return "Good morning"  
        elif 12 <= self.hour < 18:  
            return "Good afternoon"  
        else:  
            return "Good evening"  
#实例化        
myGreeting = MyGreeter()
print(myGreeting.greeting())