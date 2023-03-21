def computeRoomArea(numberOfRooms):
    for i in range(int(numberOfRooms)):
        print("Room:",i+1)
        shape_of_room = int(input("Select the shape of the room: \n 1 -Rectangular \n 2 -Square \n 3 -Custom(more or less than 4 walls, all square or rectangles) \n"))
        shapes = {1:computeRectangleWallsArea, 2:computeSquareWallsArea, 3:computeCustomeWallsArea}
        paintArea = shapes[shape_of_room]() - computeWindowsDoorsArea() 
        print("For Room: " + str(i+1) +", the area to be painted is",f"{paintArea:.2f}" ,"square ft and will required " , f"{computeGallons(paintArea):.2f}"," gallons of pain. This will cost the customer $", f"{computePaintPrice(paintArea):.2f}" )


def computeRectangleWallsArea():
    length,width,height = float(input("Enter the length of the room in feet: \n")), float(input("Enter the width of the room in feet:\n")), float(input("Enter the height of the room in feet:\n"))
    result = (calculateRectangleArea(length, height) + calculateRectangleArea(width,height)) * 2
    # result = 2 * height * (length + width)
    return result 


def calculateRectangleArea(length,width):
    TotalArea = float(length) * float(width)
    return TotalArea


def computeSquareWallsArea():
    side = input("Enter the length of one side of the room: \n")
    return computeSquareArea(side) *4


def computeSquareArea(side):
    areaOfSquare = float(side) * float(side)
    return areaOfSquare


def computeWindowsDoorsArea():
    totalArea = 0.0
    for i in range( int(input("How many windows and doors does the room contain? \n"))):
        totalArea += float(input(f"Enter window/door length for window/door {i+1} in feet\n")) * float(input(f"Enter window/door width for window/door {i+1} in feet\n"))
    return totalArea


def computeCustomeWallsArea():
    totalArea = 0
    for i in range(int(input("How many walls are there in the room\n"))):
        totalArea += float(input(f"Enter the height of wall {i+1} in feet\n")) * float(input(f"Enter the length of wall {i+1} in feet\n"))
    return totalArea


def computeGallons(area):
    paintRequired =  float(area) / paint_coverage
    return paintRequired


def computePaintPrice(area):
    totalPrice =float(computeGallons(area)) * cost_of_each_gallon
    return totalPrice


paint_coverage = 350
cost_of_each_gallon = 42
print("Welcome to Shiny Paint Company for indoor painting!")
room_number = input("How many Rooms do you want to paint:\n")
print("Thank you!")
computeRoomArea(room_number)