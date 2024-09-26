from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):

        self.calender = SortedList()
        

    def book(self, start: int, end: int) -> bool:

        event1 = SortedList.bisect_right(self.calender,start)

        event2 = SortedList.bisect_left(self.calender,end)

        if event1 == event2  and event1%2==0:

            self.calender.add(start)

            self.calender.add(end)

            return True

        return False

            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)