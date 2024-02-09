"""Welcome to the 7D Driverless Car System! """


# Front-end interaction where a user login is authenticated before starting and stopping the car
class Car:
    def __init__(self):
        self.on = False

    def start(self):  # car will start only after login is authenticated
        assert not self.on, "Car is currently running."  # asserts that the car system is not yet running
        self.on = True  # car system is on
        print("Car has started.")

    def stop(self):  # the user can stop the car
        assert self.on, "Car is idle."  # asserts that the car system is running
        self.on = False  # car system is off
        print("Car is stopped")


def login():  # an authenticated login is required in order to start the car
    username = input("Type in your username: ")
    password = input("Type in your password: ")
    authenticated = (username == "administrator" and password == "keylock")  # only the admin has login rights for now
    assert authenticated, "Login error"  # asserts that login was successful
    print("Login authenticated")  # login has been authorised
    return True


# try to run the code
if __name__ == "__main__" and login():  # console that enables users to start and stop the car from the front end
    car = Car()

    while True:
        command = input("Select 1 to start or 2 to stop the 7D Driverless car.")  # initialisation message
        if command == "1":  # pressing button '1' starts the car
            car.start()  # car system will start
        elif command == "2":  # pressing button '2' stops the car
            car.stop()  # car system will stop
            break
        else:
            print("Error.")  # system error
