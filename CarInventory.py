from Car import *
from CarInventoryNode import *
class CarInventory:
    def __init__(self):
        self.root = None

    def addCar(self, car):
        if self.root is None:
            self.root = CarInventoryNode(car)
            return
        self._insert(self.root, car)

    def _insert(self, curNode, car):
        if curNode is None:
            parent = CarInventoryNode(car)
            return parent
        else:
            if curNode.getMake() == car.make:
                if curNode.getModel() == car.model:
                    curNode.cars.append(car)
                elif curNode.getModel() < car.model:
                    curNode.setRight(self._insert(curNode.getRight(), car))
                    curNode.getRight().setParent(curNode)
                else:
                    curNode.setLeft(self._insert(curNode.getLeft(), car))
                    curNode.getLeft().setParent(curNode)
            elif curNode.getMake() < car.make:
                curNode.setRight(self._insert(curNode.getRight(), car))
                curNode.getRight().setParent(curNode)
            else:
                curNode.setLeft(self._insert(curNode.getLeft(), car))
                curNode.getLeft().setParent(curNode)
            return curNode


    def preOrder(self):
        return self._preorder(self.root)

    def _preorder(self, curNode):
        ret = ""
        if curNode is not None:
            ret += str(curNode)
            ret += self._preorder(curNode.getLeft())
            ret += self._preorder(curNode.getRight())
        return ret

    def inOrder(self):
        return self._inorder(self.root)

    def _inorder(self, curNode):
        ret = ""
        if curNode is not None:
            ret += self._inorder(curNode.getLeft())
            ret += str(curNode)
            ret += self._inorder(curNode.getRight())
        return ret


    def postOrder(self):
        return self._postorder(self.root)

    def _postorder(self, curNode):
        ret = ""
        if curNode is not None:
            ret += self._postorder(curNode.getLeft())
            ret += self._postorder(curNode.getRight())
            ret += str(curNode)
        return ret

    def doesCarExist(self, car):
        curNode = self.findNode(self.root, car.make.upper(), car.model.upper())
        if curNode is None:
            return False
        for c in curNode.cars:
            if c == car:
                return True
        return False

    def getBestCar(self, make, model):
        curNode = self.findNode(self.root, make.upper(), model.upper())
        if curNode is None:
            return None
        return sorted(curNode.cars)[-1]

    def getWorstCar(self, make, model):
        curNode = self.findNode(self.root, make.upper(), model.upper())
        if curNode is None:
            return None
        return sorted(curNode.cars)[0]

    def findNode(self, curNode, make, model):
        if curNode is None:
            return None
        if curNode.getMake() == make:
            if curNode.getModel() == model:
                return curNode
            elif curNode.getModel() < model:
                return self.findNode(curNode.getRight(), make, model)
            else:
                return self.findNode(curNode.getLeft(), make, model)
        elif curNode.getMake() < make:
            return self.findNode(curNode.getRight(), make, model)
        else:
            return self.findNode(curNode.getLeft(), make, model)

    def getTotalInventoryPrice(self):
        return self.totalprice(self.root)

    def totalprice(self, curNode):
        price = 0
        if curNode is not None:
            for c in curNode.cars:
                price += c.price
            price += self.totalprice(curNode.getLeft())
            price += self.totalprice(curNode.getRight())
        return price
