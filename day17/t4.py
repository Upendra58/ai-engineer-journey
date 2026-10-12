from collections import deque

queue = deque([10, 20, 30])
queue.append(40)
queue.appendleft(5)
queue.popleft()
print(queue)
