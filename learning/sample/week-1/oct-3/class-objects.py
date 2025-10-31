class person:
    def __init__(this, name, age):
        this.name = name
        this.age = age

    def __str__(this):
        return f"hello {this.name} - {this.age}"

    def write(self):
        return "welcome"

p1 = person("lohieth", 20)
print(p1.write())


class dogs:
    def __init__(this, name):
        this.name = name
        this.eat = False
        this.sleep = False

    def __str__(this):
        return f"this is {this.name} dog. eat = {this.eat}. sleep = {this.sleep}"

    def message(this):
        return f"this is the message from the {this.name} dog. eat = {this.eat}"

    # def setter(this, eat):
    #     this.eat = eat
    #
    # def getter(this):
    #     return f"eat = {this.eat}"

d1 = dogs("lohieth")
print(d1)
print(d1.message())
# d1.setter(True)
# print(d1.getter())
# print(d1.message())
# print(d1.__str__())
d1.eat = False
d1.sleep = True
print(d1)
print(d1.message())
# del d1.eat
# print(d1.message())
# print(d1)


class dog1(dogs):
    pass
d2 = dog1("jonny")
print(d2)