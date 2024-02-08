# 7D Driverless Car System
Welcome to the 7D Driverless Car System! This is a system implementation of code designed to support the operation of a driverless car based on [this](link) system design proposal. During the development process, it has been decided that driverless car will be named **7D Driverless Car System**.

## Car Operations
7D can only start running if an authorised user starts it. That user also has the capability to stop the car. After an authorised user starts the driverless car, it can then function autonomously. 

The three main operations of 7D are: 

1.) Car Control- covers the main movement of the car. The car can steer, accelerate, and brake. 

2.) Environment Perception- uses GPS and Light Detection and Ranging (LiDAR) hardware to inform the car about its surroundings. 
The GPS updates the current location of the car, while LiDAR detects objects around the car aids in preventing 
collision accidents. 

## Data Structures
Data structures used in the code include queue, dictionary, and lists. Please see code comments for their usage. 

3.) Vehicle to Infrastructure Communication (V2I)- This has been improved from the design proposal. Instead of LiDAR, car cameras will be used to decipher traffic signs and traffic lights. Initially, V2I only relayed real time data, and traffic lights and signs were in environment perception. But a development in author's thought process shifted traffic light and traffic sign detection to V2I involves communication with infrastructures. 

## Purpose
This is the first and second Summative Assessment requirement for the Object-Oriented Programming module offered by University of Essex Online.

The first summative assessment was a Driverless Car Design Proposal was represented by UML models and incorporated usage of data structures. The system design can be found [here](link)

The second part of the assessment, which is [System Impelementation](link), requires code implementation of the design proposal. 

## Running the Program 
The code was written on PyCharm and runs on Python 3.11 in the Conda environment. 

### Executing the code
Each car operation, including login, are stored in separate python files for clarity and organisation. 
All of these files are stored in the 7D System Folder. Open the folder and access the files from there. 

For User Login: 
- Open the login.py file
- When you run the code, your login will only be authorised if your input is the administrator credentials. So far, only the administrator can run the code.
- Pressing 1 will start the car, pressing 2 will stop it. 

For Car Control: 
- Open the car_control.py file
- Steering: You can check which direction the car is steering towards, whether left or right, by placing a steering angle. In the system, the steering angle is measured by radians. You can only input 1-179 degrees. 1-89 indicates steering towards the right, while 90-179 means steering towards the left.
- Acceleration: A value of 120 km/h has been set as the maximum speed. Therefore, the car can accelerate if the speed is below that. The car will automatically brake if maximum speed has been reached.
- Braking: Car will halt until it reaches a speed of 0 km/h. 

For Environment Perception: 
- Open the perception.py file
- Mapping: The GPS will be used to update the current city and country where the car is running.
- Avoid object: The LiDAR sensor will detect objects, and warn the car to avoid it if it is less than 10 meters away. The objects will be appended once they are avoided.
- Lane marking: The LiDAR well detect whether the car is driving within lane markings on the road.

For V2I: 
- Open the vtoi.py file
- Decipher traffic signs: The camera will interpret traffic signs and tell the car what to do. Pre-stored signs are stored in a list.
- Decipher traffic lights: The camera will interpret traffic lights and tell the car what to do. Pre-stored lights are stored as a dictionary.
  
## Testing the Program
The code for each operation is separated, for better organisation. The codes are embedded with assert statements in order to aid in debugging during the development stage. 

A corresponding unittest for each car operation was also developed in order to test whether code is working as desired. Assert statements are embedded in them as well. All you have to do is open the test files. They are named with "(car operation)_test.py" accordingly. 

All tests ran successfully. You can check them by importing unittest in your IDE. 

## Credits
I was inspired by [this](link) to organise the file folders in Github. 
[cameron](link) from discuss.python.org was also helpful in developing my code. 


