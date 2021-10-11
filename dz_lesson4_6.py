# 6-1

from itertools import count


def generate_numbers(begin, end):
    for el in count(begin, 1):
        if el < end:
            yield el
        else:
            break


for i in generate_numbers(5, 10):
    print(i)

# In[8]:


# 6-2
from itertools import cycle


def iterate_list(list_of_items, count_of_items):
    c = 0
    for el in cycle(list_of_items):
        if c < count_of_items:
            yield el
            c += 1
        else:
            break


for i in iterate_list(["A", "B", "C"], 10):
    print(i)

