def airthmatic(): # these are (+,-,*,/,**,//)
    a = 190
    b = 120
    c = 8
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    mod = a % b   #reminder
    sqr = (8**2)   #exponent
    cube = (8 ** 3)
    float = (a / c)
    no_float = (a//c) # floor division

    return [add,sub,mul,div,mod,sqr,cube,float,no_float]
airthmatic()

def assignment():  #assignment operator used for assigning the value
    equal = " x= 8 "
    add = "x + = 2"
    subs = "x - = 1"
    return(equal, add ,subs)
assignment()

def comparison ():
    x = 10
    y = 20
    x_ = x==y # when both x and y are equal
    y_ = x!=y #not equal
    g_ = x>y #greater than
    l_ = x < y #less than
    g_e = x>=y #greater than equals to y
    l_e = x<=y #less than equals to y

    return(x,y,x_,y_,g_,l_,g_e,l_e)
print(comparison())

def logical():
    x = 13
    y= 17
    A = x==13 and x<y #and gives result when all given conditions are true
    B = x<15 or y>15 # or is used when any one of the given condition is true
    C =not x > y #reverse the result
    return(A, B ,C )
print (logical())

def membership():

    string = 'anshika'
    l1 = [10,20,15,16,10] #to check the value in any list or string
    t = 's' in string
    n = 15 not in l1
    return(t,n)
print (membership())
def identify():
    x = 12
    y= 14
    t = x is y   # x=y
    f = x is not y #x!=(not equal) to y
    return(t , f)
print(identify())
def bitwise():
    x = 2
    y = 3
    s= bin (x&y),x & y   #and
    k = bin (x|y) , x|y  # or
    h = bin (x^y),x^y   #xor
    return(s,k,h)
print(bitwise())

