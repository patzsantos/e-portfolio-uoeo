<!--layout: page
title: "SSDCS Unit 8 "
permalink: /ssdcs_unit8-->

# Unit 8: Cryptography and Its Use in Operating Systems
<br>

_**In this unit we shall:** <br>_

- Look at what is meant by cryptography and examine a case study in how it can be applied to operating systems.<br>
- Explore some common cryptographic libraries.<br>
- Create a basic application that uses cryptographic libraries to encode sample data.<br>


_**On completion of this unit you will be able to:** <br>_
- Describe some of the issues encountered with cryptographic libraries.<br>
- Explain the pros and cons of using common cryptographic libraries.<br>
- Demonstrate the use of cryptographic libraries in a simple application.<br>
<br>

## Independent Work

<details><summary><h3>Unit 8 Seminar Activity: Cryptography Programming Exercise </h3></summary><br>  
Read the Cryptography with Python blog at tutorialspoint.com (link is in the reading list). Select one of the methods described/ examples given and create a python program that can take a short piece of text and encrypt it.

Create a python program (you can use the Jupyter Notebooks space) that can take a text file and output an encrypted version as a file in your folder on the system. Demonstrate your program operation in this week’s seminar session.

Answer the following questions in your e-portfolio:

Why did you select the algorithm you chose?
Would it meet the GDPR regulations? Justify your answer.
We will review your work from Unit 7 (Python Shell) in this week’s seminar, as well as this cryptography activity. There will also be an opportunity to review your team’s assignment progress during the seminar.
<br>
<img src="images/ssdcs_unit8_cryptography1.png?raw=true"/>
<img src="images/ssdcs_unit8_cryptography2.png?raw=true"/>
</details>

<!--<details><summary><h3>Activity 1: Exploring a Simple Python Shell</h3></summary><br>  
In this session, you will create a command shell in Python, and then run it and answer questions about it. You can use your chosen Jupyter Notebook space for your work.

Review the blogs at Praka (2018) and Szabo (n.d.) and then create a CLI/ shell that implements the following:

When you enter the command LIST it lists the contents of the current directory
The ADD command will add the following two numbers together and provide the result
The HELP command provides a list of commands available
The EXIT command exits the shell
Add suitable comments to your code and add the program to your e-portfolio. Be prepared to demonstrate it in the seminar session next week.

Run the shell you have created, try a few commands and then answer the questions below. Be prepared to discuss your answers in the seminar.

What are the two main security vulnerabilities with your shell?
What is one recommendation you would make to increase the security of the shell?
Add a section to your e-portfolio that provides a (pseudo)code example of changes you would make to the shell to improve its security.
Remember to also record your results, ideas and team discussions in your e-portfolio.
<br>
<br>
<img src="images/ssdcs_unit7_pythonshell1.png?raw=true"/>
<img src="images/ssdcs_unit7_pythonshell2.png?raw=true"/>
</details>

<details><summary><h3>Activity 2: Developing an API for a Distributed Environment</h3></summary><br>  
In this session, you will create a RESTful API which can be used to create and delete user records. Responses to the questions should be recorded in your e-portfolio.

You are advised to use these techniques to create an API for your team’s submission in Unit 11 and be prepared to demonstrate it during next week’s seminar (Unit 10). Remember that you can arrange a session with the tutor during office hours for more support, if required.

Using the Jupyter Notebook workspace, create a file named api.py and copy the following code into it (a copy is provided for upload to Codio/GitHub): You can install Jupyter Notebook on your local machine following these instructions or via the University of Essex Software Hub.

#source of code: Codeburst
<br>
<img src="images/ssdcs_unit7_pythonshell1.png?raw=true"/>
<img src="images/ssdcs_unit7_pythonshell2.png?raw=true"/>
</details><br>-->
<br>

## Collaboration
<details><summary><h3>Collaborative Discussion 2: Cryptography case study - TrueCrypt</h3></summary>
TrueCrypt was a popular and well-respected operating system add-on that could create encrypted volumes on a Windows and/or Linux system. In addition, it was also designed to create a complete, bootable volume that could encrypt the entire operating system and data for a Windows XP system. It was discontinued in 2014.
<br>
  
Case Study: Read the TrueCrypt cryptanalysis by Junestam & Guigo (2014) (link is in the reading list) and then answer the following questions:
<br>

The (anonymous) TrueCrypt authors have said “Using TrueCrypt is not secure as it may contain unfixed security issues” (TrueCrypt, 2014). Does the cryptanalysis provided above prove or disprove this assumption?
Would you be prepared to recommend TrueCrypt to a friend as a secure storage environment? What caveats (if any) would you add?
Remember to save this to your e-portfolio.
<br>

Present an ontology design which captures the weaknesses of TrueCrypt, and organise them according to their severity. Expand the ontology design by considering the factors which will cause each weakness to become an issue from a user's perspective. For example, if a user wishes to encrypt a disk storing bank details using TrueCrypt, which weakness of the software might cause this specific user goal to be negatively impacted? 
<img src="images/ssdcs_unit8_initial1.jpg?raw=true"/>
<img src="images/ssdcs_unit8_initial2.jpg?raw=true"/>
<img src="images/ssdcs_unit8_initial3.jpg?raw=true"/>
<img src="images/ssdcs_unit8_initial4.jpg?raw=true"/>
</details><br>

## Reflection


**_[Return to Software Secure Development Module Page](https://patzsantos.github.io/e-portfolio-uoeo/ssdcs_landing)_**
