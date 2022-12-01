class CarInventoryNode:
    def __init__(self,car):
        self.make = car.make
        self.model = car.model
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None
    
    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model
    
    def getParent(self):
        return self.parent
    
    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setParent(self,parent):
        self.parent = parent

    def setLeft(self,left):
        self.left = left

    def setRight(self,right):
        self.right = right
    
    def __str__(self):
        list = []
        for car in self.cars:
            list.append(str(car))
            list.append('\n')
        return "".join(list)

