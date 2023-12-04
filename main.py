#черга через бібіліотеку колекції
from collections import deque
q = deque()

q.append("a")
q.append("b")
q.append("c")
q.append("d")
print(q)
q.rotate(2)
print(q)

