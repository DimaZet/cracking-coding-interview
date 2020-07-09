from debug import debug


@debug
def replace_spaces_by_delimiter(s: str):
  s = list(s)
  spaces = 0
  for c in s:
    if c == ' ':
      spaces += 1
  n = len(s)
  s.extend([None] * (spaces * 2 - 1))
  c = 0
  N = len(s)
  for i in reversed(range(n-1)):
    if s[i] != ' ':
      s[N - 1 - c] = s[i]
      c += 1
    else:
      s[N - 1 - c - 2: N - 1 - c + 1] = list('%20')
      c += 3
  return ''.join(s)


if __name__ == '__main__':
  replace_spaces_by_delimiter('Mr J ohn Smith')
  replace_spaces_by_delimiter(' Mr  John  Smith')
