##определяем функцию
def add (x, y):
    return x + y
#Вызываем функцию
print(add(1, 2))

add(1, 2)

print(add ("i a", "m tester"))

def arg(a, b, c=2, d=3):
    return a + b + c + d#


#print (arg(1, 1, 1, 1))#
#print (arg(2, 2))#
#print(arg(2, 2, 0.1, 1))#

def task_func(a= (1, 2, 3, 4)) :
    return a[1]


print (task_func())


def compute_surface(radius, pi=3.14159):
    return pi * radius * radius
print (compute_surface(2))

#задача#

def string_length(s: str = '') -> int:
    return len(s)



def min_list(a: list, b: list) -> int:
    return max(len(a), len(b))