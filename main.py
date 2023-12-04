#черга через бібіліотеку queue
from queue import Queue
q = Queue(maxsize=3)
print(q.qsize())
q.put("a")
q.put("b")
q.put("c")
q.get("c")
q.put("d")
q.put_nowait("e")
print(q.queue)
print(q.qsize())
