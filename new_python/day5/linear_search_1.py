from typing import Any

def linear_search(lst: list, value: Any) -> int:
  i = 0
  while i != len(lst) and lst[i] != value:
    i += 1
  
  if i == len(lst):
    return -1
  else:
    return i
