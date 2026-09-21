def point_location(point):
    match point:
        case (0,0):
            print("Origin")
        case (x , 0):
            print(f"on the X axis {x}")
        case (0,y):
            print(f"on the Y axis {y}")
        case (x,y):
            print(f"Point at {x},{y}")
        case _:
            print("Can't find location")

point_location((0,0))
point_location((0,5))
point_location((0,0,0))

def person_details(details):
    match details:
        case {"name": name, "age": age}:
            print(f"Name: {name}, Age: {age}")
        case {"name": name}:
            print(f"Name: {name}, Age not provided")
        case _:
            print("Unknown data format")

person_details({"name":"Ali","age":14})
person_details({"name":"Ali","age":18})
person_details({"name":"Ali"})