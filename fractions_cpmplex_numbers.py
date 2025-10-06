from fractions import Fraction
#from cmath import complex
try:
    f = Fraction(input("Enter a fraction: "))
except ZeroDivisionError:
    print("Invalid fraction")


