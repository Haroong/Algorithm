# get input
num1, num2 = map(int, input().split())


def getGCD(a, b):
    remains = a % b
    if remains != 0:
        getGCD(b, remains)
    else:
        gcd = b
        print(gcd)
        getLCM(num1, num2, gcd)


def getLCM(num1, num2, gcd):
    lcm = num1 * num2 // gcd
    print(lcm)


getGCD(num1, num2)
