import sys


def my_hash(s: str):
  if len(s) <= 1:
    return "0"
  h = ""
  for i in range(len(s) - 1):
    if ord(s[i]) < ord(s[i + 1]):
      h += str(ord(s[i + 1]) - ord(s[i])) + ','
    else:
      h += str(26 - ord(s[i]) + ord(s[i + 1])) + ','
  return h


words = {}
for x in sys.stdin.readline().split():
  h = my_hash(x)
  words[h] = x
sys.stdin.readline()
for line in sys.stdin:
  line = line.strip()
  sys.stdout.write(words[my_hash(line)] + '\n')
