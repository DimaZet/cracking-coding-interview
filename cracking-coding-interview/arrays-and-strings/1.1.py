from debug import debug


@debug
def are_all_chars_unique1(s: str):
  chars = set()
  for c in s:
    if c in chars:
      return False
    chars.add(c)
  return True


@debug
def are_all_chars_unique2(s: str):
  n = range(len(s))
  for i in n:
    for j in n:
      if i == j:
        continue
      if s[i] == s[j]:
        return False
  return True


if __name__ == '__main__':
  are_all_chars_unique1('abcde')
  are_all_chars_unique2('abcde')
  are_all_chars_unique1('abcdee')
  are_all_chars_unique2('abcdee')
  are_all_chars_unique1('abcdefjhigklmnopqrstxyz')
  are_all_chars_unique2('abcdefjhigklmnopqrstxyz')
  are_all_chars_unique1('abcdefjhigklmnopqrstxyzz')
  are_all_chars_unique2('abcdefjhigklmnopqrstxyzz')
