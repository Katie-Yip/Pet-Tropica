"""
Things I need to do: 
-> check every hour whether or not 10 hours has passed by 
-> check 
"""
class gameClock:
    def __init__ (self, currHour):
        self.currHour = currHour
    
    def check(hour):
        if hour - currHour > 10: 
            currHour = 0 
            return True
        return False 