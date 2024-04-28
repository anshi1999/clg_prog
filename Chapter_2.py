def airthmatic():  # these are (+,-,*,/,**,//)
    a = 190
    b = 120
    c = 8
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    mod = a % b  # reminder
    sqr = (8 ** 2)  # exponent
    cube = (8 ** 3)
    float = (a / c)
    no_float = (a // c)  # floor division

    print(add, sub, mul, div, mod, sqr, cube, float, no_float)  # will give you output in a singal line


airthmatic()


def assignment():  # assignment operator used for assigning the value
    x = 8  # these are  = , += , -= , *= , /= , **= , %=
    x += 4  # 8+4=12
    x -= 5  # 12-5=7
    x *= 2  # 7*2=14
    x /= 7  # 14 /7=2
    x **= 3  # 2*2*2=8 cube of 2
    x %= 3  # reminder after dividing by 3
    print(x)


assignment()


def comparison():  # these are ==, !=, <=, >=, <=
    x = 10
    y = 20
    x_ = x == y  # when both x and y are equal
    y_ = x != y  # not equal
    g_ = x > y  # greater than
    l_ = x < y  # less than
    g_e = x >= y  # greater than equals to y
    l_e = x <= y  # less than equals to y

    return x, y, x_, y_, g_, l_, g_e, l_e


print(comparison())


def logical():
    x = 13
    y = 17
    A = x == 13 and x < y  # and gives result when all given conditions are true
    B = x < 15 or y > 15  # or is used when any one of the given condition is true
    C = not x > y  # reverse the result
    return A, B, C


print(logical())


def membership():
    string = 'anshika'
    l1 = [10, 20, 15, 16, 10]  # to check the value in any list or string
    t = 's' in string
    n = 15 not in l1
    return t, n


print(membership())


def identify():
    x = 12
    y = 14
    t = x is y  # x=y
    f = x is not y  # x!=(not equal) to y
    return (t, f)


print(identify())


def bitwise():  # Examples of Bitwise operators
    a = 10
    b = 4
    print(a & b)  # Print bitwise AND operation
    print(a | b)  # Print bitwise OR operation
    print(~a)  # Print bitwise NOT operation
    print(a ^ b)  # print bitwise XOR operation
    print(a >> 2)  # print bitwise right shift operation
    print(a << 2)  # print bitwise left shift operation

    print('''Operator	Description	Syntax
&	Bitwise AND	x & y
|	Bitwise OR	x | y
~	Bitwise NOT	~x
^	Bitwise XOR	x ^ y
>>	Bitwise right shift	x>>
<<	Bitwise left shift	x<<
''')
bitwise()
