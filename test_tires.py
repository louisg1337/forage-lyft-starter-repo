import unittest
from tires.carriganTires import CarriganTires
from tires.octoprimeTires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire = CarriganTires([1,0,0.2,0.1])
        
        self.assertTrue(tire.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        tire = CarriganTires([0.1,0.89,0.4,0.5])
        
        self.assertFalse(tire.needs_service())
        
    def test_tire_edge_case(self):
        tire = CarriganTires([1])
        
        self.assertFalse(tire.needs_service())

class TestOctoprimeTires(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire = OctoprimeTires([1,1,1,0.1])
        
        self.assertTrue(tire.needs_service())
        
    def test_tire_should_not_be_serviced(self):
        tire = OctoprimeTires([0.1,0.5,0.4,0.5])
        
        self.assertFalse(tire.needs_service())
        
    def test_tire_edge_case(self):
        tire = OctoprimeTires([1])
        
        self.assertFalse(tire.needs_service())



if __name__ == '__main__':
    unittest.main()

        