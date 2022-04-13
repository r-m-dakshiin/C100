class Cars():
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speedlimit = speed_limit
    
    def start(self):
        print("started")
    def stop(self):
        print("Stoped")
    def change_gear(self, gear_type):
        print("gear changed")


Audi = Cars("Q3", "Red", "Audi", 200)
print(Audi.color)
