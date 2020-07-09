from debug import debug


@debug
def are_strings_have_same_chars(s1: str, s2: str):
  def get_chars_in_dict(s: str):
    d = dict()
    for c in s:
      d[c] = d.get(c, 0) + 1
    return d

  return get_chars_in_dict(s1) == get_chars_in_dict(s2)


if __name__ == '__main__':
  are_strings_have_same_chars('aabc', 'acba')
  are_strings_have_same_chars('aabc', 'cba')
  are_strings_have_same_chars('abc', 'cba')
  are_strings_have_same_chars('abc', 'cb')
  are_strings_have_same_chars('c', 'a')
