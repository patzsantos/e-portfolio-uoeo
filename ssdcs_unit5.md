<!--layout: page
title: "SSDCS Unit 5 "
permalink: /ssdcs_unit5-->

# Unit 5: An Introduction to Testing
<br>

_**In this unit we shall:** <br>_

- Explore the range of questions to ask when developing a test plan.<br>
- Become familiar with two industry software testing standards.<br>
- Examine a range of testing techniques and appreciate the relevance of each in different testing scenarios.<br>
- Recognise the tools and frameworks which are available to support and automate the Python testing process.<br>

_**On completion of this unit you will be able to:** <br>_
- Describe the key terms which are associated with testing software for security.<br>
- Prepare a list of questions to ask when designing a test plan for secure software.<br>
- Design software tests through understanding the range of ways which the security of software can be breached.<br>
<br>

## Independent Work

<details><summary><h3>Equivalence Testing in Python </h3></summary><br>  
<br>
Run equivalence.py in your chosen Jupyter Notebook workspace - Testing with Python - which is an implementation of equivalence partitioning. This test partitions integers [-3,5] into equivalence classes based on lambda x, y: (x-y)%4 == 0.<br>
<br>
In the output, you should be able to see how a set of objects to be partitioned are considered, and a function evaluates if the two objects are equivalent before printing the result.<br>
<br>
test_equivalence_partition() produces the following output:<br>
<br>
set([1, -3]) set([2, -2]) set([3, -1]) set([0, 4]) 0 : set([0, 4]) 1 : set([1, -3]) 2 : set([2, -2]) 3 : set([3, -1]) 4 : set([0, 4]) -2 : set([2, -2]) -3 : set([1, -3]) -1 : set([3, -1])
<Br>
<img src="images/ssdcs_unit5_equivalence2.png?raw=true"/>
<img src="images/ssdcs_unit5_equivalence1.png?raw=true"/>
</details>

<details><summary><h3>Portfolio Component: Exploring the Cyclomatic Complexity’s Relevance Today </h3></summary><br>  
The Cyclomatic Complexity is commonly considered in modules on testing the validity of code design today. However, in your opinion, should it be? Does it remain relevant today? Specific to the focus of this module, is it relevant in our quest to develop secure software? Justify all opinions which support your argument and share your responses with your team.
<br>
<br>
<img src="images/ssdcs_unit5_portfolio_cyclomatic1.png?raw=true"/>
<img src="images/ssdcs_unit5_portfolio_cyclomatic2.png?raw=true"/>
</details><br>

## Collaboration
<details><summary><h3>Portfolio Component: 'Exploring the Cyclomatic Complexity’s Relevance Today' Teamwork Discussion</h3></summary>

<img src="images/ssdcs_unit5_discussion1.png?raw=true"/>
</details>

<details><summary><h3>Team Bulwark Meeting 4 Minutes</h3></summary>
<br>
<img src="images/ssdcs_unit5_minutes.png?raw=true"/>
</details><br>

## Reflection
The assigned reading for this unit mostly covered Cyclomatic Complexity testing. There seems to be a mixed view on it, with some authors citing that they are unnecessary, while some saying that they are still valid in designing code today. In the same way, for the team discussion about Cyclomatic Complexity, there was no consensus within the team as well. We had divided opinions about it. You can see my opinion, as well as that of my team members, in the Cyclomatic Complexity individual portfolio component and team discussion in the sections above. <Br>

The lecturecast for the week is about Testing. I learned about the reasons for testing, and what steps to take in order to implement it. It is important to test code early in the Software Development Life Cycle in order to avoid wasting time and resources. MITRE listed down software weaknesses to watch out for when developing software such as user session errors, bad coding principles, processing errors, amongst others. OWASP also provides developers testing principles and techniques to write better and more secure code.<br>

There are many testing methods and designs to follow. Therefore, it is important for developers to fully understand what and who their software is intended for, so that they can implement the correct testing methods throughout its creation. At the same time, I think that knowing what to ask when planning tests and familiarising myself with testing standards, testing techniques, testing tools, and automated testing in Python, will help me towards the coding exericises in the next units, as well as that of the individual project. <br>

**_[Return to Software Secure Development Module Page](https://patzsantos.github.io/e-portfolio-uoeo/ssdcs_landing)_**
