# 7D Driverless Car System
Welcome to the 7D Driverless Car System! This is a system implementation of code designed to support the operation of a driverless car based on [this](link) system design proposal. During the development process, it has been decided that driverless car will be named **7D Driverless Car System**, or **7D**

## Car Operations
7D can only start running if an authorized user starts it. That user also has the capability to stop the car. After an authorized user starts the driverless car, it can then function autonomously. 

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

## Testing the Program
The code for each operation is separated, for better organization. The codes are embedded with assert statements in order to aid in debugging during the development stage. 

A corresponding unittest for each car operation was also developed in order to test whether code is working as desired. Assert statements are embedded in them as well. 

## Credits
I was inspired by [this](link) to organize the file folders in Github. 
[cameron](link) from discuss.python.org was also helpful in developing my code. 


