CREATE TABLE dept(
    code varchar(20) not null,
    name varchar(100) not null,
    description varchar(200),
    primary key (code)
)engine = InnoDB;

Insert into dept values('MARKT', 'Marketing', 'Marketing department'), ('DEVLP', 'Development', 'Development department'),
('ACC', 'Accounting', 'Accounting department'), ('HR', 'Human Resource', 'HR department')

CREATE TABLE employee (
    id INT AUTO_INCREMENT NOT NULL,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    mobile CHAR(10) NOT NULL,
    city VARCHAR(50),
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    dept_code varchar(20) NOT NULL,
    hire_date DATE,
    permanent_employee ENUM('yes', 'no') NOT NULL,
    primary key(id),
    foreign key(dept_code) references dept(code)
);