class MyCalendar:
    #this is the basic approach similar to the interactive problem and check if the interval is overlapped or not
    def __init__(self):

        self.events = []
        

    def book(self, start: int, end: int) -> bool:

        for s,e in self.events:

            if not (end<=s or e<=start):
                
                return False
            
        self.events.append((start,end))
                
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)