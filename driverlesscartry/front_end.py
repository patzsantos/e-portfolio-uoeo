# driverless car super class
class Car:
    Control = None  # first operation: car control
    Perception = None  # second operation: environment perception
    v2i = None  # third operation: vehicle to infrastructure communication


# front end where user interacts with the system
def login():  # in order to start the driverless car, there should be an authenticated login
    username = input("Type your username: ")
    password = input("Type your Password: ")
    authenticated = (username, password)
    if authenticated:
        print("Login authenticated.")  # login successful
        return True
    else:
        print("Login error. Try again.")
        return False  # login failed


# operation for starting and stopping the car after login
class Run:
    def __init__(self):
        self.car = car
        self.on = False

    def start(self):  # car can start only after user login
        if not self.on:
            self.on = True
            print("Car has started.") # display message when car starts
        else:
            self.on = False
            print("Car is stopped")  # display message when car is stopped

    def stop(self):
        if self.on:
            self.on = False
            print("Car is stopped.")  # display message when car is stopped
        else:
            self.on = True
            print("Car has started.")  # display message when car starts


if __name__ == "__main__":
    if login():  # login was authenticated
        car = Car()
        car_control = Run()

        while True:
            command = input("Select 1 to start or 2 to stop car.")  # select a button to start or stpp
            if command == "1":  # car will start
                car_control.start()
            elif command == "2":  #car will stop
                car_control.stop()
                break
            else:
                print("Error.")
