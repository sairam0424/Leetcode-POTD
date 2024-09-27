class MyCalendarTwo:

    def __init__(self):

        self.overlaps  = []

        self.calender = []
        

    def book(self, start: int, end: int) -> bool:

        for s,e in self.overlaps:

            if end>s and start<e:

                return False

        for s,e in self.calender:

            if end>s and start<e:

                self.overlaps.append((max(start,s),min(end,e)))

        self.calender.append((start,end))

        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
