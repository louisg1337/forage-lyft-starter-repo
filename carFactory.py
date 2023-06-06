from car import Car

from battery.nubbinBattery import NubbinBattery
from battery.spindlerBattery import SpindlerBattery

from engine.capuletEngine import CapuletEngine
from engine.willoughbyEngine import WilloughbyEngine
from engine.sternmanEngine import SternmanEngine


class carFactory():
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        
        calliope = Car(engine, battery)
        
        return calliope
    
    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        
        glissade = Car(engine, battery)
        
        return glissade
    
    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        
        palindrome = Car(engine, battery)
        
        return palindrome
    
    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        
        rorschach = Car(engine, battery)
        
        return rorschach
    
    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        
        thovex = Car(engine, battery)
        
        return thovex