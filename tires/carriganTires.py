from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_quality):
        self.tire_quality = tire_quality
        
    def needs_service(self):
        if len(self.tire_quality) != 4:
            return False
        
        for i in range(len(self.tire_quality)):
            if (self.tire_quality[i] >= 0.9):
                return True
        
        return False