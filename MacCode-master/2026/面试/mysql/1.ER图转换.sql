-- 1:1联系
-- 1. 教师表（一方）
CREATE TABLE Teacher (
    TeacherID INT PRIMARY KEY,-- 作为主键
    TeacherName VARCHAR(50)
);

-- 2. 班级表（另一方，持有外键）
CREATE TABLE Class (
    ClassID INT PRIMARY KEY,-- 作为主键
    ClassName VARCHAR(50),
    TeacherID INT UNIQUE, -- 外键，加UNIQUE保证一对一（一个教师只管理一个班）
    StartDate DATE, -- 联系的属性：任职日期

    -- 保证 TeacherID 的值必须在 Teacher 表中存在，维护数据的参照完整性
    FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID)
);
/**

TeacherID	TeacherName
101	        张老师
102	        李老师
ClassID	ClassName	TeacherID	StartDate
1	    计算机1班	    101	        2023-09-01
2	    计算机2班	    102	        2024-03-01

**/

-- 1：N 联系
-- 1. 班级表（1方）
CREATE TABLE Class (
    ClassID INT PRIMARY KEY,        -- 班级号
    ClassName VARCHAR(50)           -- 班级名称
);

-- 2. 学生表（N方，持有外键）
CREATE TABLE Student (
    StudentID INT PRIMARY KEY,       -- 学号，作为主键
    StudentName VARCHAR(50),         -- 姓名
    ClassID INT,                     -- 外键，引用班级表的班级号
    JoinDate DATE,                    -- 联系的属性：入班日期
    --FOREIGN将ClassID设置为外键，引用Class表的ClassID
    FOREIGN KEY (ClassID) REFERENCES Class(ClassID)
);
/*
Class 表（班级）：
ClassID	    ClassName
1	        计算机1班
2	        计算机2班

Student 表（学生）：
StudentID	StudentName	ClassID	JoinDate
101	        张三	        1	2023-09-01
102	        李四	        1	2023-09-01
103	        王五	        2	2024-03-01
104	        赵六	        2	2024-03-01

*/
-- M：N 联系
-- 1. 学生表
CREATE TABLE Student (
    StudentID INT PRIMARY KEY,      -- 学号
    StudentName VARCHAR(50)         -- 姓名
);

-- 2. 课程表
CREATE TABLE Course (
    CourseID INT PRIMARY KEY,       -- 课程号
    CourseName VARCHAR(50),         -- 课程名称
    Credit INT                      -- 学分（课程自身属性）
);

-- 3. 选修表（联系表）
CREATE TABLE Enroll (
    StudentID INT,                   -- 外键，引用学生表
    CourseID INT,                     -- 外键，引用课程表
    Grade DECIMAL(5,2),               -- 联系属性：成绩
    PRIMARY KEY (StudentID, CourseID), -- 联合主键，确保同一学生同一课程只一条记录
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);
/*
Student 表：
StudentID	StudentName
101	        张三
102	        李四
103	        王五

Course 表：
CourseID	CourseName	Credit
1	        数据库原理	    3
2	        数据结构	    4
3	        操作系统	    3

Enroll 表：
StudentID	CourseID	Grade
101         	1	    85.5
101	            2	    90.0
102	            1	    78.0
102	            3	    88.5
103	            2	    92.0
*/

--弱实体的转换规则
-- 1. 职工表（强实体）
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,          -- 职工号（主键）
    EmpName VARCHAR(50),            -- 职工姓名
    Dept VARCHAR(50)                -- 部门（其他属性）
);

-- 2. 家属表（弱实体）
/* ON DELETE CASCADE: 当职工被删除时，其家属自动删除*/
CREATE TABLE Dependent (
    EmpID INT,                      -- 外键，引用职工表的职工号
    DependentName VARCHAR(50),      -- 家属姓名（部分码/分辨符）
    Relationship VARCHAR(20),        -- 与职工的关系（如配偶、子女）
    PRIMARY KEY (EmpID, DependentName),  -- 联合主键：职工号 + 家属姓名
    FOREIGN KEY (EmpID) REFERENCES Employee(EmpID)
        ON DELETE CASCADE            -- 当职工被删除时，其家属自动删除
);