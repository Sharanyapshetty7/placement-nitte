def circle():
    r = int(input("Enter the radius of the circle: "))
    print("Area of circle is", 3.14 * r * r)

def square(s):
    print("Area of square is", s * s)

def triangle():
    b = int(input("Enter the base: "))
    h = int(input("Enter the height: "))
    return 0.5 * b * h

def rectangle(l, br):
    return l * br

while True:
    print("\n1 Circle\n2 Square\n3 Triangle\n4 Rectangle\n5 EXIT")
    a = int(input("Enter your choice: "))
    
    match a:
        case 1:
            circle()
        case 2:
            s = int(input("Enter the side: "))
            square(s)
        case 3:
            tri = triangle()
            print("Area of triangle is", tri)
        case 4:
            l = int(input("Enter length: "))
            br = int(input("Enter breadth: "))
            print("Area of rectangle is", rectangle(l, br))
        case 5:
            break