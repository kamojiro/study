import time
import datetime
from datetime import datetime as dt


class Vehicle:
    def __init__(self, size) -> None:
        self.vehicle_size = size
        self.parking_spot = None
        self.parking_start_time = None
        self.parking_end_time = None
    
    def get_size(self):
        return self.vehicle_size
    
    def start_parking(self, parking_spot):
        self.parking_spot = parking_spot
        self.parking_spot.is_parked = True
        self.parking_start_time = dt.now()
    
    def end_parking(self):
        if self.parking_spot:
            self.parking_spot.is_parked = False
            self.parking_spot = None
            self.parking_end_time = dt.now()
    
    def parked_time(self):
        if self.parking_start_time and self.parking_end_time:
            return self.parking_end_time - self.parking_start_time
        if self.parking_start_time:
            raise ValueError("not end")
        raise Exception("not parking")

BIKE_SIZE = 1
CAR_SIZE = 4
BUS_SIZE = 5

class Bike(Vehicle):
    def __init__(self) -> None:
        super().__init__(BIKE_SIZE)

class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__(CAR_SIZE)

class Bus(Vehicle):
    def __init__(self) -> None:
        super().__init__(BUS_SIZE)

class ParkingSpot:
    def __init__(self, size) -> None:
        self.spot_size = size
        self.parked = False
    def get_size(self):
        return self.spot_size
    def is_parked(self):
        return self.parked

class ParkingLot:
    def __init__(self, spot_size_level_list):
        self.spots_levels = [[ ParkingSpot(spot_size) for spot_size in spot_size_level] for spot_size_level in spot_size_level_list]

    def parking(self, vehicle: Vehicle):
        for spots in self.spots_levels:
            for spot in spots:
                if not spot.parked and vehicle.get_size() <= spot.get_size():
                    vehicle.start_parking(spot)
                    return True
        return False

def test():
    spot_size_level_list = [[1,1,1,4], [1,4,4,4]]
    park = ParkingLot(spot_size_level_list)
    vehicles = []
    for i in range(10):
        if i%3 == 0:
            vehicle = Car()
        elif i%3 == 1:
            vehicle = Bus()
        else:
            vehicle = Bike()
        vehicles.append(vehicle)
        print(f"{vehicle.__dict__}, {park.parking(vehicle)=}")
    time.sleep(3)
    for vehicle in vehicles:
        vehicle.end_parking()
        try:
            print(f"{vehicle.parked_time()=}")
        except:
            pass

if __name__=="__main__":
    test()



