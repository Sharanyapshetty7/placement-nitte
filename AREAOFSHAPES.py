def circle():
    r = int(input("Enter radius of a circle: "))
    print("Area of circle is", 3.14 * r * r)

def square(a):
    print("Area of square is", a * a)

def triangle():
    b = int(input("Enter base: "))
    h = int(input("Enter height: "))
    return 0.5 * b * h

def rect(a, b):
    return a * b

while True:
    print("\n1. CIRCLE")
    print("2. SQUARE")
    print("3. TRIANGLE")
    print("4. RECTANGLE")
    print("5. EXIT")
    
    ch = int(input("Enter your choice: "))
    
    match ch:
        case 1:
            circle()
        case 2:
            a = int(input("Enter side of the square: "))
            square(a)
        case 3:
            res = triangle()
            print("Area of triangle is", res)
        case 4:
            a = int(input("Enter length of rectangle: "))
            b = int(input("Enter breadth of rectangle: "))
            res = rect(a, b)
            print("Area of rectangle is", res)
        case 5:
            exit(0)
        case _:
            print("Invalid option")
