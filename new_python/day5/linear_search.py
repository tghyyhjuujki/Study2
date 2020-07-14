import time
import linear_search_1
import linear_search_2
import linear_search_3
from typing import Callable, Any

def time_it(search: Callable[[list, Any], Any], L: list, v: Any) -> float:
  t1 = time.perf_counter()
  search(L, v)
  t2 = time.perf_counter()
  return (t2 - t1) * 1000.0

def print_times(v, L) -> None:
  t1 = time.perf_counter()
  L.index(v)
  t2 = time.perf_counter()
  index_time = (t2 - t1) * 1000.0

  while_time = time_it(linear_search_1.linear_search, L, v)
  for_time = time_it(linear_search_2.linear_search, L, v)
  sentinel_time = time_it(linear_search_3.linear_search, L, v)
  print("{0}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}".format(v, while_time, for_time, sentinel_time, index_time))

L = list(range(10000001))
print_times(10, L)

L = list(range(10000001))
print_times(5000000, L)

L = list(range(10000001))
print_times(10000000, L)