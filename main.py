#черга через список
queue = []
queue.append("a")
queue.append("b")
queue.append("c")
print(queue)
print(queue.pop(0))
#queue.append(queue.pop(0)) #Кругова черга (Ring Buffer)
print(queue)