# Inputs
# input1 = "ddddaabbbcccc"
# input2 = "sssttttbbaaaaeeee"
# input3 = "aaaqqqquuiiiiiioo"
from collections import Counter


def top_repeated_chars(s):
    count = Counter(s)
    top = sorted(count.most_common(3), key= lambda x : (-x[1] , x[0]))
    for char, freq in top:
        print(char, freq)
# Inputs
s1 = "ddddaaabbbcccc"
s2 = "sssttttbbaaaeeee"
s3 = "aaqquuiiiiiioo"

print("Output1:")
top_repeated_chars(s1)
print("Output2:")
top_repeated_chars(s2)
print("Output3:")
top_repeated_chars(s3)

import problems
problems.hello()
print(dir(problems))
print(problems.s)

