from debug import debug


@debug
def is_string_shuffled_palindrome(s: str):
  loners = set()
  s = s.lower()
  for c in s:
    if c == ' ':
      continue
    if c in loners:
      loners.remove(c)
    else:
      loners.add(c)
  return len(loners) <= 1


if __name__ == '__main__':
  is_string_shuffled_palindrome('Tact Coa')
  is_string_shuffled_palindrome('Tact Coap')
