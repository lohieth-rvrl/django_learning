# datatypes in python

# text type -> str
# numeric types -> int - float - complex
# sequence type  -> list - tuple - range
# mapping type -> dict
# set types -> set - frozenset
# boolean type -> bool
# binary type -> bytes - bytearray - memoryview
# none type -> None

# Random numbers
import random
from dataclasses import replace
from shlex import split

print(random.randrange(1,6))
print(random.randint(1,5))
print(random.randbytes(1))
print(random.random)
print(f"{random.getrandbits(2)}\n")

# Strings
s = "Apple "
for i in range(len(s)):
    # print(f"{s[i]}")
    print(s[i], end="")
print()
for i in s:
    print(i, end="")
print("\n" + str(len(s)))
print("".join(s))
print("a" not in s)
print(" " in s)
print(s.count("e"))
print(s.islower())
# methods in string
# lower(), upper(), strip(), replace(), split(), count(val), islower(), islower() etc...



string = "aabbcc"
for i in range(0,len(string),2):
    # print(i)
    print(string[i:i+2])


my_dict = {'b': 2, 'a': 1, 'c': 3}

# Get a sorted list of keys
sorted_keys = sorted(my_dict.values())
print(f"Sorted keys: {sorted_keys}")

# Create a new dictionary sorted by keys
sorted_dict_by_key = {key: my_dict[key] for key in sorted_keys}
print(f"Dictionary sorted by key: {sorted_dict_by_key}")
