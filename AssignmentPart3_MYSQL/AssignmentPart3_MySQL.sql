mysql;
USE COMPANY1;

---

/* TASK 1: List all Employees whose salary is between 1,000 AND 2,000. 
Show the Employee Name, Department and Salary */


SELECT ENAME, DNAME, SAL 
FROM EMP JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO
WHERE SAL BETWEEN 1000 AND 2000; 


/*Code comments: 
-SELECT displays the employee name, department, and salary columns.
-FROM-JOIN-ON merges the department numbers from the EMP and DEPT table.
-WHERE-BETWEEN-AND limits the employees listed to those whose salaries 
are between 1,000 and 2,000.


References: 

Mazumdar, A. (2023) Advanced SQL [Seminar]. LCS_PCOM7E AUGUST 2023.
Launching into Computer Science August 2023. University of Essex Online. 

MariaDB. (2018) JOIN Syntax. Available from: https://mariadb.com/kb/en/join-syntax/
[Accessed 18 October 2023]. 

TechOnTheNet. (N.D.b) MariaDB: Joins. Available from: https://www.techonthenet.com/mariadb/joins.php
[Accessed 18 October 2023].*/

---

/* TASK 2: Count the number of people in department 30 who receive a salary 
and the number of people who receive a commission */


SELECT COUNT(DEPTNO) AS "NUM_OF_PEOPLE_WITH_SAL" FROM EMP
WHERE DEPTNO = 30 AND SAL > 0;

SELECT COUNT(DEPTNO) AS "NUM_OF_PEOPLE_WITH_COMM" FROM EMP
WHERE DEPTNO = 30 AND COMM > 0;


/*Code comments: 
-At first, IS NOT NULL was used as the condition for the SAL and COMM 
to filter those receiving salares and commissions. However, the employee
with a commission written as "0" is still counted in MySQL. 
I learned from MariaDB(2019) that 0 is not considered as a null, 
therefore, I used the comparison operator > based on TechOnTheNet (N.D.a)
to identify the employees receiving positive salaries and commissions. 
- SELECT COUNT counts the number of people receiving salaries
and commissions. 
-They are filtered using the operators WHERE, by department number 30, 
and AND SAL/COMM > 0 for those receiving salaries and commissions.


References:

MariaDB. (2019) NULL Values. Available from: 
https://mariadb.com/kb/en/null-values/ [Accessed 21 October 2023].

TechOnTheNet. (N.D.a) MariaDB: Comparison Operators. 
Available from: https://www.techonthenet.com/mariadb/comparison_operators.php
[Accessed 21 October 2023].*/

---

/*TASK 3: Find the name and salary of employees in Dallas*/


SELECT ENAME, SAL
FROM EMP JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO
WHERE LOC = "DALLAS";


/*Code comments: 
-SELECT displays the name and salary of employees columns. 
-FROM-JOIN-ON merges the department numbers from the EMP and DEPT table.
-WHERE filters the location to "Dallas" only. 


Reference:

Mazumdar, A. (2023) Advanced SQL [Seminar]. LCS_PCOM7E AUGUST 2023.
Launching into Computer Science August 2023. University of Essex Online.*/

---

/*TASK 4: List all departments that do not have any employees*/


SELECT DEPTNO, DNAME FROM DEPT
WHERE DEPTNO NOT IN(SELECT DISTINCT DEPTNO FROM EMP);


/* Code comments:
-The DEPT table was selected, since it holds both DEPTNO and DNAME
columns and encompasses the main query, which asks for the departments. 
-NOT IN(SELECT DISTINCT--) retrieves the department number without employees
from the EMP table. 


Reference:

Mazumdar, A. (2023) Advanced SQL [Seminar]. LCS_PCOM7E AUGUST 2023.
Launching into Computer Science August 2023. University of Essex Online. */

---

/*TASK 5: List the department number and average salary of each department*/


SELECT DEPT.DEPTNO AS "DEPT_NUM", AVG(SAL) AS "AVG_SAL"
FROM EMP JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO
GROUP BY DEPT.DEPTNO; 

/*Code comments: 
-A new field titled "DEPT_NUM" that lists the department number and a 
new field titled "AVG_SAL" that lists the average salary were created.
-FROM-JOIN-ON merges the department numbers from the EMP and DEPT table.
-GROUP classifies the average salary by department.
-This task worked because I was able to identify that DEPT and DEPTNO, combined
into DEPT.DEPTNO, should be the columns used for the SELECT and GROUP functions 
based on the code of bgraham89(2022) for Query 5.


References:

bgraham89. (2022) queries.sql. Available from:
https://github.com/bgraham89/uoeo-eportfolio/blob/main/assets/artefacts/lics/Task%203/queries.sql
[Accessed 18 October 2023].

TechOnTheNet. (N.D.c) MySQL: AVG Function. 
Available from: https://www.techonthenet.com/mysql/functions/avg.php
[Accessed 19 October 2023].*/

----
/*Submitted by Patricia Annette C. Santos.*/