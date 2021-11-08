class Robot:
    """Docstring"""
    def __init__(self, initX=0, initY=0):
        self.x = initX
        self.y = initY
    
    def __str__(self):
        return f"current position: ({self.x}, {self.y})"

    def move(self, moves):
        for dir, value in moves:
            if dir == "UP": self.y+=value
            elif dir == "DOWN": self.y-=value
            elif dir == "LEFT": self.x+=value
            elif dir == "RIGHT": self.x-=value
            else: print("Direction or value not valid")

    def distance(self):
        return round(((self.x ** 2) + (self.y ** 2)) ** 0.5)

my_robot = Robot()

data = input().strip().split()
moves = [(data[i],int(data[i+1])) for i in range(0,len(data),2)]

my_robot.move(moves)
print(my_robot.distance())