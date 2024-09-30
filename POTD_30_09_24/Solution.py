class CustomStack:

    def __init__(self, maxSize: int):

        self.stack  = []#stack which follows the last in fast out (LIFO)

        self.maxSize = maxSize#get the maxsize of stack we can have
        

    def push(self, x: int) -> None:

        if len(self.stack)<self.maxSize:#this checks if the stack has not reached the maxSize it need to 

            self.stack.append(x)


        

    def pop(self) -> int:

        if self.stack:#pop the top of the stack if the stack is not empty else is the stack is empty we will return -1 

            return self.stack.pop()

        return -1

    def increment(self, k: int, val: int) -> None:

        for index in range(min(k,len(self.stack))):#increments the bottom k elements of the stack with the val .if there are less than k elements in the stack  , increment all the elements in the stack  using just an basic for loop struc of looping over min(k,len(stack))

            self.stack[index]+=val




        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)