<!--layout: page
title: "SSDCS Unit 3 "
permalink: /ssdcs_unit3-->

# Unit 3: Programming Languages: History, Concepts & Design
<br>

_**In this unit we shall:** <br>_

- Review the history and concepts of programming languages.<br>
- Investigate language concepts using Python as an example.<br>
- Describe best practices and methods to overcome common security issues.<br>
<br>

_**On completion of this unit you will be able to:** <br>_
- Describe some key milestones in the development of programming languages.<br>
- Outline some of the key paradigms that define the different types of languages.<br>
- Explain the key concepts that determine the operation of programming languages.<br>
- Discuss key programming challenges and recommended best practices.<br>
- Explain what design patterns are and when to use them.<br>
<br>

## Independent Work

<details><summary><h3>Collaborative Discussion 1 Summary Post</h3></summary>

<img src="images/ssdcs_unit3_summary1.jpg?raw=true"/>
<img src="images/ssdcs_unit3_summary2.jpg?raw=true"/>
<img src="images/ssdcs_unit3_summary3.jpg?raw=true"/>
<img src="images/ssdcs_unit3_summary4.jpg?raw=true"/>
<img src="images/ssdcs_unit3_summary5.jpg?raw=true"/></details> <br>

<details><summary><h3>Activity: Exploring Python Tools and Features</h3></summary><br>  
In this example, you will compile and run a program in C using the Jupyter notebook workspace provided (Buffer Overflow in C). The program is already provided as bufoverflow.c - a simple program that creates a buffer and then asks you for a name, and prints it back out to the screen.
<br>
<img src="images/ssdcs_unit3_activity1.png?raw=true"/>
<img src="images/ssdcs_unit3_activity2.png?raw=true"/>
<br>
<br>
  
>What happens?<br>
- A warning is given on declaring the ‘gets’ function. 

>What does the output message mean?<br>
- It is suggesting to use ‘fgets’ instead. According to Sneh (2022), ‘fgets()’ is advocated because it lets users indicate the size of the buffer, while ‘gets()’ does not,  which may cause storage to be jammed. 

Reference:<br>
Sneh. (2022) fgets() and gets() in C Programming | DigitalOcean. Available from: https://www.digitalocean.com/community/tutorials/fgets-and-gets-in-c-programming#fgets-function-in-c [Accessed 1 April 2024]. </details><br>
<br>
## Collaboration

<details><summary><h3>Team Activity Discussion: What is a Secure Programming Language?</h3></summary>
<br>
Team Discussion: What is a Secure Programming Language?
You should read Chapter 2,6,7,8 of the course text (Pillai, 2017) and Cifuentes & Bierman (2019) and then answer the questions below, adding them as evidence to your e-portfolio.<br>
<br>
  
- What factors determine whether a programming language is secure or not?<br>
- Could Python be classed as a secure language? Justify your answer.<br>
- Python would be a better language to create operating systems than C. Discuss.<br>

<br>
Team component
You should discuss your answers within your team, and you can share your team responses with the tutor for formative feedback or discuss it in next week’s seminar.<br>
<br>
>Team members: Gareth Williams, Mario Butorac, Miguel Bezares, and Patricia Santos
<br>

<img src="images/ssdcs_unit3_teamactivity1.jpg?raw=true"/>
<img src="images/ssdcs_unit3_teamactivity2.jpg?raw=true"/>
<img src="images/ssdcs_unit3_teamactivity3.jpg?raw=true"/>
<img src="images/ssdcs_unit3_teamactivity4.jpg?raw=true"/>
<img src="images/ssdcs_unit3_teamactivity5.jpg?raw=true"/>
<img src="images/ssdcs_unit3_teamactivity6.jpg?raw=true"/>
<img src="images/ssdcs_unit3_teamactivity7.jpg?raw=true"/>
<img src="images/ssdcs_unit3_teamactivity8.jpg?raw=true"/>
</details><br>

## Criticality 
<br>

### Reflection

<br>
We wrapped up the first discussion forum from units 1-3 this week. To summarise my learning, I can say that it is especially helpful for future software developers like me to get acquainted with the OWASP Top 10 in order to have an idea of cyber threats and which protocols to are accepted to fight against them. The feedback from my tutor and peer helped me revise my UML activity diagram for the better.
<br>

Team Bulwark, the software development team I am a part of, also had our second meeting this week. We discussed the document outline, as well as the reading we have to do in order to make headway in our project. Lastly, we discussed about the e-portfolio team activity compotent, wherein we have to discuss what constitutes a secure programming language. Over the week, we worked on our Team Activity and Design Document. On the last day of the unit, we went over our Design Document together. We discussed how we can improve on it, and decided to consult with our tutor within the week so that she can give us feedback. <br>
<br>
I had a chance to work on the individual activity, where I learned that the function fgets() is more secure than just gets(), as it prevents overloading and gives the developer the freedom to select the buffer size. I wanted to work on the second part of the activity, but I am having trouble installing pylint. I am still figuring out how to do that for now. 
<br>

**_[Return to Software Secure Development Module Page](https://patzsantos.github.io/e-portfolio-uoeo/ssdcs_landing)_**
