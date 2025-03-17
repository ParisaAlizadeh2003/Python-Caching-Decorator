def Caching(func):
    Cach = {}
    def wrapper(*args): # بسته بندی کننده
        tuple_args = tuple(*args)
        if tuple_args in Cach:
            return Cach[tuple_args]
        Cach[tuple_args] = func(*args)
        return Cach[tuple_args]
    return wrapper

@Caching
def Sum(*args):
    return sum(*args)

print(Sum([1,4]))
print(Sum([2,4]))
print(Sum([1,4]))
print(Sum([3,4]))
