class Orders:
    def __init__(self,orderNum,customer,order,totalCost):
        self.orderNum = orderNum
        self.customer = customer
        self.order = order
        self.totalCost = totalCost

class FoodItems:
    def __init__(self,id,itemName,cost,category):
        self.id = id
        self.itemName = itemName
        self.cost = cost
        self.category = category        
        