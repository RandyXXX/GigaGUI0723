x = 5
print("x=", x, " ,x id=", hex(id(x)))
x = 6
print("x=", x, " ,x id=", hex(id(x)))
Ll = [5]
print("x=", Ll, " ,x id=", hex(id(Ll)))
print("Ll[0] id=", hex(id(Ll[0])))
Ll[0] = 6
print("x=", Ll, " ,x id=", hex(id(Ll)))
print("Ll[0] id=", hex(id(Ll[0])))
#is就是c#跟java的.equals
print(x == Ll[0], x is Ll[0])
