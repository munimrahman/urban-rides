import random

class BRTA:
    def __init__(self) -> None:
        self.__license = {}

    def take_driving_test(self, email):
        score = random.randint(0, 100)
        if score >= 33:
            # print(f'Congrats, You have passed!\nYour Score is {score}')
            license_number = random.randint(5000, 9999)
            self.__license[email] = license_number
            return license_number
        else:
            # print(f'Sorry, You Failed!\nYour Score is {score}')
            return False
    
    def validate_license(self, email, license):
        for key, value in self.__license.items():
            if key == email and value == license:
                return True
        return False