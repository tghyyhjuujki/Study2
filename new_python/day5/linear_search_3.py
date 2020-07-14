from typing import Any

def linear_search(lst: list, value: Any) -> int:
  i = 0

  while lst[i] != value:
    i += 1
  
  lst.pop()

  if i == len(lst):
    return -1
  else:
    return 1


