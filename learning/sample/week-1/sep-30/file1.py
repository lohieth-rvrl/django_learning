# sys module in python
import sys
print(f"arg : {sys.argv}")
print(f"arg : {sys.version}")
print(f"arg : {sys.platform}")

print("\nModule Search Path (first 3):")
for path in sys.path[:3]:
    print(f"- {path}")


# variables in python
n = "loki"
n = 10
print(f"\n{n}")


# type casting in python
n = 10
n = str(n); #float(), int(), str(),
print(f"n - {n} \ntype - {type(n)} ")

x = "loki"
list = list(x)
print(list)
tuple = tuple(list)
print(tuple)
print(dict([(1,1),(2,1)]))

str = "10.92"
str = float(str);
print(str)

