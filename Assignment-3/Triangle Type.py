a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))

if a == b:
    if b == c:
        print("Equilateral")
    else:
        print("Isosceles")
elif a == c:
    print("Isosceles")
elif b == c:
    print("Isosceles")
else:
    print("Scalene")