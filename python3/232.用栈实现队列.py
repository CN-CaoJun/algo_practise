#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)        

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]
    
    def empty(self) -> bool:
        return not self.stack1 and not self.stack2    


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end


if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())  # 预期输出: 1
    print(queue.pop())   # 预期输出: 1
    print(queue.empty()) # 预期输出: False
    queue.push(3)
    print(queue.pop())   # 预期输出: 2
    print(queue.pop())   # 预期输出: 3
    print(queue.empty()) # 预期输出: True