class Car(object):
    def __init__(self,model,color,company,speed):
        self.model = model
        self.color = color
        self.company = company
        self.speed = speed
    
car1 = Car("supra","grey","toyta",200)
car2 = Car("outback","light blue","Subaru",165)

print(car1.speed)
print(car2.model)  