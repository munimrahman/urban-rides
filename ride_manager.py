class Ride_Manager:
    def __init__(self) -> None:
        print('Ride Manager Activated.')
        self.__income = 0
        self.__trip_history = []
        self.__available_cars = []
        self.__available_bikes = []
        self.__available_cng = []
    
    def add_a_vehicle(self, vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__available_cars.append(vehicle)
        elif vehicle_type == 'bike':
            self.__available_bikes.append(vehicle)
        else:
            self.__available_cng.append(vehicle)

    def get_available_cars(self):
        return self.__available_cars

    def total_income(self):
        return self.__income

    def get_trip_history(self):
        return self.__trip_history

    def find_a_vehicle(self, rider, vehicle_type, destination):
        if vehicle_type == 'car':
            if len(self.__available_cars) == 0:
                print('Sorry! No cars is available now.')
                return False
            for car in self.__available_cars:
                # print('potential', rider.location, car.driver.location)
                if abs(rider.location - car.driver.location) < 10:
                    distance = abs(destination - rider.location)
                    fare = distance * car.rate
                    if rider.balance < fare:
                        print('You do not have enough money for this trip.', fare, rider.balance)
                        return False
                    if car.status == 'available':
                        car.status = 'unavailable'
                        trip_info = f'Match for {rider.name} for fare: {fare} with {car.driver.name} started: {rider.location} to: {destination}'
                        # print(f'available cars: {len(self.__available_cars)}')
                        self.__available_cars.remove(car)
                        rider.start_a_trip(fare, trip_info)
                        car.driver.start_a_trip( rider.location, destination, fare*0.80, trip_info)
                        self.__income += fare*0.20
                        # print(f'available cars: {len(self.__available_cars)}')
                        self.__trip_history.append(trip_info)
                        print(trip_info)
                        return True

uber = Ride_Manager()