import socket
class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]
    def clear(self):
        self._cache.clear()

    def hasHost(self,host):
        return self._cache[host]

    def hasHost2(self,host):
        return host in self._cache

    def with_iterator(self,*args):
        i = iter(args)
        v = next(i)
        for length in i:
            v *= length
        return v

k = Resolver()
print(k.with_iterator(2, 4))

num = [1,2,3,4,5]
dict1 = {'1':1,"2":2}


def deco(f):
    def wrap(*args,**kwargs):
        print('num before after')
        x = f(*args)
        print('num after')
        if type(x) == int:
            return x/2
        else:
            return x.split()[-1]
    return wrap

class CallCount:
    def __init__(self,f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        print('after')
        self.count += 1
        return self.f(*args,**kwargs)

@deco
def city_name():
    return "some city"

@deco
def add(num1,num2,num3):
    print('num before')
    return num1+num2+num3


@CallCount
def hello_world():
    print('before')


hello_world()
hello_world()
hello_world()
print(hello_world.count)
hello_world()
print(city_name())
print(add(1,2,3))