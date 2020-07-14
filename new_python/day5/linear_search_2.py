from typing import Any

def linear_search(lst: list, value: Any) -> int:
  i = 0
  while i != len(lst) and lst[i] != value:
    i += 1
  
  for i in range(len(lst)):
    if lst[i] == value:
      return i
  
  return -1

