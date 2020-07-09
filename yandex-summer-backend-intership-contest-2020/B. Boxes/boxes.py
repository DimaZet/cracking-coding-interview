import sys

sys.stdin.readline()
queue = []
for line in sys.stdin:
  placed = False
  box = [int(x) for x in line.split()]
  box.sort()
  for q in queue[:]:
    if q[0] < box[0] and q[1] < box[1]:
      queue.remove(q)
    elif q[0] > box[0] and q[1] > box[1]:
      placed = True
  if not placed:
    queue.append(box)
sys.stdout.write(str(len(queue)) + '\n')
