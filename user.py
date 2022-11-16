import hashlib
from brta import BRTA
from vehicles import Car, Bike, Cng
from ride_manager import uber
from random import random, randint

license_authority = BRTA()

class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('user.txt', 'a') as file:
            file.write(f'{self.email} {pwd_encrypted}\n')
        file.close()

    @staticmethod
    def log_in(email, password):
        stored_pwd = ''
        with open('user.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_pwd = line.split(' ')[1]
        file.close()
        input_pwd = hashlib.md5(password.encode()).hexdigest()
        if input_pwd == stored_pwd:
            print('Valid User')
            return True
        else:
            print('Wrong Password')
            return False

class Rider(User):
    def __init__(self, name, email, password, location, balance) -> None:
        self.location = location
        self.balance = balance
        super().__init__(name, email, password)
    def set_location(self, location):
        self.location = location
    def get_location(self):
        return self.location
    def request_trip(self, destination):
        pass
    def start_a_trip(self, fare):
        self.balance -= fare

class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0
    
    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            pass
        else:
            self.license = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            if vehicle_type == 'car':
                new_vehicle = Car(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            else:
                new_vehicle = Cng(vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
        else:
            print('You are not a valid Driver.')

    def start_a_trip(self, destination, fare):
        self.earning += fare
        self.location = destination



rider1 = Rider('rider1', 'rider1@gmail.com', 'rider1', randint(0, 100), 5000)
rider2 = Rider('rider2', 'rider2@gmail.com', 'rider2', randint(0, 100), 5000)
rider3 = Rider('rider3', 'rider3@gmail.com', 'rider3', randint(0, 100), 5000)

driver1 = Driver('driver1', 'driver1@gmail.com', 'driver1', randint(0, 100), 5654)
driver1.take_driving_test()
driver1.register_a_vehicle('car', 1245, 10)

driver2 = Driver('driver2', 'driver2@gmail.com', 'driver2', randint(0, 100), 5654)
driver2.take_driving_test()
driver2.register_a_vehicle('car', 2245, 10)

driver3 = Driver('driver3', 'driver3@gmail.com', 'driver3', randint(0, 100), 5654)
driver3.take_driving_test()
driver3.register_a_vehicle('car', 3245, 10)

driver4 = Driver('driver4', 'driver4@gmail.com', 'driver4', randint(0, 100), 5654)
driver4.take_driving_test()
driver4.register_a_vehicle('car', 4245, 10)

print(uber.get_available_cars())
uber.find_a_vehicle(rider1, 'car', 90)


# For test
""" munim = User('Munim', 'munim@gmail.com', 'hridoy2091')
User.log_in('munim@gmail.com', 'hridoy2091')

kuber = Driver('Kuber Majhi', 'kuber@gmail.com', 'pass0987', 54, 4556)

res = license_authority.validate_license(kuber.email, kuber.license)

print(res)
kuber.take_driving_test()
r = license_authority.validate_license(kuber.email, kuber.license)
print(r) """