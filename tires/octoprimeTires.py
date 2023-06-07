from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_quality):
        self.tire_quality = tire_quality
        
    def needs_service(self):
        if len(self.tire_quality) != 4:
            return False
        
        return sum(self.tire_quality) >= 3