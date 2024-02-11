# 7D Driverless Car System
Welcome to the 7D Driverless Car! This is the system implementation of code designed to support the operation of a driverless car.

## Purpose
This is the first and second Summative Assessment requirement for the Object-Oriented Programming module in the PG Certificate in Computer Science Course offered by the University of Essex Online.

The first summative assessment is a [Driverless Car System Design Proposal](https://github.com/patzsantos/e-portfolio-uoeo/blob/module2/oop/Driverless%20Car%20Summative%20Assessment%201%20and%202/System%20Design%20Proposal/OOP%20Assignment%201_%20A%20Design%20Proposal%20of%20Software%20to%20Support%20Operation%20of%20a%20Driverless%20Car.pdf) represented by Unified Modeling Language (UML) models. The second part of the assessment is the [System Implementation](https://github.com/patzsantos/e-portfolio-uoeo/tree/module2/oop/Driverless%20Car%20Summative%20Assessment%201%20and%202), which requires code that executes and tests the autonomous car. 

## Car Operations
7D can only start running autonomously only if an authorised user starts it from the front end. That user also has the capability to stop the car. 

**_The three main operations of 7D are:_**

**1.) Car Control**- Enables the car to steer, accelerate, and brake. 

**2.) Environment Perception**- Uses GPS to update the current location of the car, while LiDAR is used to detect objects and road lane markings around the car to prevent collision accidents. 

**3.) Vehicle to Infrastructure Communication (V2I)**- This operation is updated from the design proposal where initially, V2I only relayed real time data, and deciphering traffic lights and signs were functions in Environment Perception. Now, cameras will be used to decipher traffic signs and traffic lights instead of LiDAR.

## Executing the code
The code was written on ***PyCharm*** and runs on ***Python 3.11*** in the ***Conda*** environment. 

Each car operation, together with their corresponding test files, are stored in and can be accessed from the [**Car Operations**] (https://github.com/patzsantos/e-portfolio-uoeo/tree/module2/oop/Driverless%20Car%20Summative%20Assessment%201%20and%202/Car%20Operations) folder.

***For User Login:*** _Open **login.py** file_
- When you run the code, your login will only be authorised if your input is the administrator credential as they are currently the only ones with access to the system.
- Pressing 1 will start the car, pressing 2 will stop it. 

***For Car Control:*** _Open **car_control.py**__
- ***Steering:*** The car can steer to the left or right direction. In the system, the steering angle is measured by radians. 1-89 degrees indicates steering towards the right, while 90-179 degrees means steering towards the left.
- ***Acceleration:*** A value of 120 km/h has been set as the maximum speed value. Therefore, the car can accelerate while the speed is below that. The car will automatically brake once the maximum speed has been reached.
- ***Braking:*** The car will halt until its velocity falls to 0 km/h. 

***For Environment Perception:*** _Open **perception.py**_
- ***Mapping:*** The GPS updates the city and country where the car is currently running.
- ***Avoid object:*** The LiDAR sensor detects objects, and warns the car to avoid it once it is less than 10 meters away. The objects will be listed in a _queue,_ and eventually appended once they are avoided.
- ***Lane marking:*** The LiDAR senses lane markings on the road and makes sure that the car is driving within the lanes. 

***For V2I:*** _Open **vtoi.py** file_
- ***Decipher traffic signs:*** The camera interprets traffic signs and tells the car what to do. Pre-stored signs are stored in a _list._
- ***Decipher traffic lights:*** The camera interprets traffic lights and tells the car what to do. Pre-stored lights are stored as a _dictionary._
  
## Testing the Program
The codes are embedded with **assert statements** in order to aid in debugging during the development stage. 

A corresponding **unittest** for each car operation was executed in order to test whether code is working as desired. They are named with **"(car operation name)_test.py"** accordingly. 

All tests ran successfully. Proofs can be found in the [unittest Screenshots](https://github.com/patzsantos/e-portfolio-uoeo/tree/module2/oop/Driverless%20Car%20Summative%20Assessment%201%20and%202/unittest%20Screenshots) folder. 

## Credits
A big thank you to [Cameron Simpson](https://discuss.python.org/u/cameron/summary) from [discuss.python.org](https://discuss.python.org/) who guided me through the development of the code. 

I was inspired by how [turbits](https://github.com/turbits/essex-m2a2/tree/main) organised the file folders in his Github. 
