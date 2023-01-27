# section4-0
age = input("Enter your age:")
int_age = int(age)

if int_age <= 1:
    print("You're baby.")
elif int_age > 1 and int_age <= 3:
    print("You're toddler.")
elif int_age > 3 and int_age <= 5:
    print("You're preschool.")
elif int_age > 5 and int_age <= 12:
    print("You're gradeschooler.")
elif int_age > 12 and int_age <= 18:
    print("You're teen.")
elif int_age > 18 and int_age <= 21:
    print("You're young adult.")
elif int_age > 21 and int_age < 65:
    print("You're adult.")
elif int_age >= 65 and int_age < 75:
    print("You're early elderly.")
else:
    print("You're late elderly.")

#section4-1
def f():
    """
    Returns x * x.
    :return: int x squared.
    """
    x = input("Input number:")
    x = int(x)
    return x * x

print(f())


#section4-2
def printer():
    """
    Returns string.
    :return: string.
    """
    string = input("Input name:")
    return print(string)

printer()


#section4-3
def g(a, b, c, d=0, e=0):
    """
    Returns a + b + c + d + e.
    :param a: int.
    :param b: int.
    :param c: int.
    :param d: int.
    :param e: int.
    :return: int sum of a, b, c, d and e.
    """
    return a + b + c + d + e

print(g(1, 2, 3, 4, 5))
print(g(1, 2, 3))


section4-4
x = input("Input number:")
x = int(x)

def f(x):
    """
    Returns x / 2.
    :param x: int.
    :return: float dividing a by 2.
    """
    y = x / 2
    return y

def g(y):
    """
    Returns y * 4.
    :param y: float.
    :return: float multipling y by 4.
    """
    y = f(x)
    z = y * 4
    return z

print(g(f(x)))


section4-5
def float_changer():
    """
    Returns num.
    :param num: int.
    :return: float num.
    """
    try:
        num = input("Type a number:")
        num = float(num)
        print(num)
    except ValueError:
        print("Invalid input.")           
    return num

float_changer()    


