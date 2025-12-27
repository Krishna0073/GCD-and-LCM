def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
def lcm(a,b):
    res = abs(a*b)//(gcd(a,b))
    return res
x = int(input())
y = int(input())
print(gcd(x,y))
print(lcm(x,y))


