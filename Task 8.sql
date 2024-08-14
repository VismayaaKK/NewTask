create database school;
use school;
create table students 
(StudentID INT auto_increment PRIMARY KEY,
FirstName VARCHAR(50),
LastName VARCHAR(50),
DateofBirth DATE,
Gender ENUM('Male','Female'),
EnrollmentDate DATE);
select * from students;
select * from students
where EnrollmentDate > 2024-01-01;
delete from students
where StudentID=4;
create table courses(
CourseID INT AUTO_INCREMENT PRIMARY KEY,
CourseName varchar(100),
Credit INT);
select * from courses;
use school;
Create table enrollments(
EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,
StudentID INT,
CourseID INT,
FOREIGN KEY (StudentID) references students(StudentID),
FOREIGN KEY (CourseID) references courses(CourseID));
select * from enrollments;
select EnrollmentID,FirstName,LastName,Gender,CourseName,Credit 
from students s 
JOIN enrollments e
ON s.StudentID=e.StudentID
JOIN courses c
ON e.CourseID=c.CourseID ;
select Gender,count(StudentID) from students
group by Gender;
select CourseName,count(CourseName) from courses
group by CourseName;

 




