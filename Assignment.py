 calculate_area(length, breadth):
    return length * breadth

 calculate_perimeter(length, breadth):
    return 2 * (length + breadth)

    shape == 'rectangle':
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    
    area = calculate_area(length, breadth)
    perimeter = calculate_perimeter(length, breadth)
    
    print("The area of the rectangle is:", area)
    print("The perimeter of the rectangle is:", perimeter)
