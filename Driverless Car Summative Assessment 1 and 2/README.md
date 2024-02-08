# 7D Driverless Car System
Welcome to the 7D Driverless Car! This is a system implementation of code designed to support the operation of a driverless car based on [this](link) system design proposal.

## Car Operations
7D can only start running if an authorised user starts it from the front end. That user also has the capability to stop the car. After an authorised login is enable, the car can then function autonomously. 

**_The three main operations of 7D are:_**

**1.) Car Control**- The main movements of the car. It can steer, accelerate, and brake. 

**2.) Environment Perception**- Uses GPS and Light Detection and Ranging (LiDAR) to inform the car about its surroundings. The GPS updates the current location of the car, while LiDAR detects objects around the car aids in preventing collision accidents. 

**3.) Vehicle to Infrastructure Communication (V2I)**- This varies from the design proposal. Instead of LiDAR, car cameras will be used to decipher traffic signs and traffic lights. Initially, V2I only relayed real time data, and traffic lights and signs were functions in environment perception. However, it has been decided to move them here since V2I involves communication between vehciles and infrastructures. 

## Data Structures
Data structures used in the code include queue, dictionary, and lists. Please see [Executing the Code section]([link)](https://github.com/patzsantos/e-portfolio-uoeo/edit/module2/oop/Driverless%20Car%20Summative%20Assessment%201%20and%202/README.md#car-operations) for their detailed use.

## Purpose
This is the first and second Summative Assessment requirement for the Object-Oriented Programming module offered by University of Essex Online.

The first summative assessment was a Driverless Car Design Proposal represented by Unified Modeling Language (UML) models. The system design can be found [here](link)

The second part of the assessment, which is [System Impelementation](link), requires code implementation and testing of the autonomous car. 

## Executing the code

The code was written on ***PyCharm*** and runs on ***Python 3.11*** in the ***Conda*** environment. 

Each car operation, including login, are stored in separate python files for clarity and organisation. 
All of these files, together with their corresponding test files (labeled with an additional "_test.py") after each operation name) are stored in and can be accessed from the **Car Operations** folder.

***User Login:***
- Open the login.py file
- When you run the code, your login will only be authorised if your input is the administrator credentials. So far, only the administrator can run the code.
- Pressing 1 will start the car, pressing 2 will stop it. 

***For Car Control:***
- Open the car_control.py file
- Steering: You can check which direction the car is steering towards, whether left or right, by placing a steering angle. In the system, the steering angle is measured by radians. You can only input 1-179 degrees. 1-89 indicates steering towards the right, while 90-179 means steering towards the left.
- Acceleration: A value of 120 km/h has been set as the maximum speed. Therefore, the car can accelerate if the speed is below that. The car will automatically brake if maximum speed has been reached.
- Braking: Car will halt until it reaches a speed of 0 km/h. 

***For Environment Perception:***
- Open the perception.py file
- Mapping: The GPS will be used to update the current city and country where the car is running.
- Avoid object: The LiDAR sensor will detect objects, and warn the car to avoid it if it is less than 10 meters away. The objects will be appended once they are avoided.
- Lane marking: The LiDAR well detect whether the car is driving within lane markings on the road.

***For V2I:***
- Open the vtoi.py file
- Decipher traffic signs: The camera will interpret traffic signs and tell the car what to do. Pre-stored signs are stored in a list.
- Decipher traffic lights: The camera will interpret traffic lights and tell the car what to do. Pre-stored lights are stored as a dictionary.
  
## Testing the Program
The code for each operation is separated, for better organisation. The codes are embedded with assert statements in order to aid in debugging during the development stage. 

A corresponding **unittest** for each car operation was executed in order to test whether code is working as desired. Assert statements are embedded both in the unittests and main codes. All you have to do is open the test files. They are named with "(car operation)_test.py" accordingly. 

All tests ran successfully.

## Credits
I was inspired by [this](link) to organise the file folders in Github. 
[cameron](link) from discuss.python.org was also helpful in developing my code. 


