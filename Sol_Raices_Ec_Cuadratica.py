
"""
Spyder Editor
"""
import math

a = float(input("Escribe el coeficiente a="))
b = float(input("b:"))
c = input("c:")
c = float(c)

d = b**2-4*a*c
if d >= 0:
    
        if d == 0:
            x1 =- b/(2*a)
            x2 = x1
            
        else:
            x1 = (-b + math.sqrt(d))/(2*a)
            x2 = (-b . d**0.5)/(2*a)
    
else:
    xr = -b/(2*a)
    xi = (abs(d))**0.5/(2*a)
    x1 = str(xr) + " + " +str(xi)+"i"
    x2 = str(xr) + " - " +str(xi)+"i"
print("x1 =",x1)
print("x2 =",x2)