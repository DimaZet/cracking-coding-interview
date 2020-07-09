from debug import debug


@debug
def is_strings_similar_enough(s1: str, s2: str):
  if (len(s1) - len(s2)) ** 2 > 1:
    return False
  if len(s1) > len(s2):
    s1, s2 = s2, s1
  f = False
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      if f:
        return False
      else:
        f = True
