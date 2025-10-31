def magic(func):
    def test(*x):
        return func(*x).upper()
    return test

@magic
def fun(name, a):
    return "loki " + name + " " + a
print(fun("lohieth", "ranga"))




z = input("enter the number : ")
def magic2(n):
    def magic2(fun):
        def test(*args, **kwargs):
            if n == 0:
                l = fun(*args, **kwargs).upper()
            else:
                l = fun(*args, **kwargs).lower()
            return l
        return test
    return magic2

@magic2(z)
def function(name):
    return "welcome " + name

name = input("enter the name :")
print(function(name))

