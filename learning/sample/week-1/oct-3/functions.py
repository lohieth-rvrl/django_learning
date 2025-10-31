def fun():
    print("hello")
    return "returned"
print(fun(), end="\n\n")

def fun(name, num):
    print(name + " " + str(num) , end="\n\n")
fun("loki", 10)

# arbitrary arguments
def fun(*names):
    print(names)
    print(names[len(names)-1], end="\n\n")
fun("loki", "lohi", "john", "funnybot")

# keyword arguments
def fun(num2, num1):
    print(f"{num1} - {num2}", end="\n\n")
fun(num1 = 20, num2 = 30)

# arbitrary keyword arguments
def fun(**names):
    print(names["name1"] + names["name2"], end="\n\n")
fun(name1 = "lohieth", name2 = "Rangasamy")

# default parameters
def function(name = "lohieth"):
    print("this is my name " + name, end="\n\n")
function("honey")

#positional argument -> don't allow keyword arguments
def check(x, /):
    return x+10
print(check(30))
# print(check(x=40)) -> error

# *, -> this allows only keyword arguments
def check2(*, x):
    return x*2
print(check2(x = 50))
# print(check2(50)) -> error

# Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)

# recursion
# def sum(x):
#     if(x>0):
#         sm = --x + sum(x-1)
#     else:
#         sm = 0
#     return sum
# sum(5)

def bot(name):
    print(name);
print(bot.__name__)
print(bot.__doc__)

print(list(range(10)))
print(list(range(0, -5, -1)))
print()

# lambda function
def x(b):
    return lambda a : a+b
fun = x(20)
print(fun(10))