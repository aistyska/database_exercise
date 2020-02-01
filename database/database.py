import sqlite3

def open_connection():
    db_host = "exercise.db"
    connection = sqlite3.connect(db_host)
    cursor = connection.cursor()
    return connection, cursor

def close_connection(connection):
    connection.close()

def db_query(query, query_parameters = None):
    try:
        connection, cursor = open_connection()
        if query_parameters == None:
            rez = cursor.execute(query)
        else:
            rez = cursor.execute(query, query_parameters)
        connection.commit()
        if "SELECT" in query:
            for row in rez:
                print(row)
    except sqlite3.DataError as error:
        print(error)
    finally:
        close_connection(connection)

# First part
# Table: employees
# Table columns:
# employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary,
# commission_pct, manager_id, department_id

# 1. Write a query to display the names (first_name, last_name) and salary for all employees
# whose salary is not in the range $10,000 through $15,000.
def ex_1_1():
    query = """SELECT first_name, last_name, salary FROM employees 
    WHERE salary NOT BETWEEN 10000 AND 15000"""
    db_query(query)

# 2. Write a query to display the names (first_name, last_name) and department ID of all
# employees in departments 30 or 100 in ascending alphabetical order by department ID.
def ex_1_2():
    query = """SELECT first_name, last_name, department_id FROM employees 
    WHERE department_id = 30 OR department_id = 100 
    ORDER BY department_id"""
    db_query(query)

# 3. Write a query to display the names (first_name, last_name) and salary for all employees
# whose salary is not in the range $10,000 through $15,000 and are in department 30 or 100.
def ex_1_3():
    query = """SELECT first_name, last_name, salary FROM employees
    WHERE (salary NOT BETWEEN 10000 AND 15000) AND (department_id = 30 OR department_id = 100)"""
    db_query(query)

# 4. Write a query to display the first_name of all employees who have both an "b" and "c" in their
# first name.
def ex_1_4():
    query = """SELECT first_name FROM employees 
    WHERE first_name LIKE '%b%c%' OR '%c%b%' """
    db_query(query)

# 5. Write a query to display the last name, job, and salary for all employees whose job is that of a
# Programmer or a Shipping Clerk, and whose salary is not equal to $4,500, $10,000, or $15,000.
def ex_1_5():
    query = """SELECT last_name, job_id, salary FROM employees 
    WHERE job_id = 'IT_PROG' OR job_id = 'SH_CLERK' 
    AND salary != 4500 AND salary != 10000 AND salary != 15000"""
    db_query(query)

# 6. Write a query to display the last names of employees whose names have exactly 6 characters.
def ex_1_6():
    query = """SELECT last_name FROM employees
    WHERE last_name LIKE '______' """
    db_query(query)

# 7. Write a query to display the last names of employees having 'e' as the third character.
def ex_1_7():
    query = """SELECT last_name FROM employees
    WHERE last_name LIKE '__e%' """
    db_query(query)

#PART 2
# 1. Write a query to list the amount of jobs available in the employees table.
#kiek darbuotoju keikvienoj pozicijoj
def ex_2_1():
    query = """SELECT job_id, COUNT(job_id) FROM employees 
    GROUP BY job_id"""
    db_query(query)

#kiek darbu rusiu
def ex_2_1_1():
    query = """SELECT COUNT(DISTINCT job_id) FROM employees"""
    db_query(query)
ex_2_1()

# 2. Write a query to get the total of salaries to pay.
def ex_2_2():
    query = """SELECT SUM(salary) FROM employees"""
    db_query(query)

# 3. Write a query to get the minimum salary from employees table.
def ex_2_3():
    query = """SELECT MIN(salary) FROM employees"""
    db_query(query)

# 4. Write a query to get the highest salary of an employee.
def ex_2_4():
    query = """SELECT MAX(salary) FROM employees"""
    db_query(query)

# 5. Write a query to get average salary and number of employees working in department 90.
def ex_2_5():
    query = """SELECT AVG(salary), COUNT(employee_id) FROM employees 
    WHERE department_id = 90"""
    db_query(query)

# 6. Write a query to get the highest, lowest, sum and average salary of all employees.
def ex_2_6():
    query = """SELECT MAX(salary), MIN(salary), SUM(salary), AVG(salary) FROM employees"""
    db_query(query)

# 7. Write a query to get the number of employees with the same job.
def ex_2_7():
    query = """SELECT COUNT(employee_id), job_id FROM employees 
    GROUP BY job_id"""
    db_query(query)

# 8. Write a query to get the difference between the highest and lowest salaries.
def ex_2_8():
    query = """SELECT (MAX(salary) - MIN(salary)) FROM employees"""
    db_query(query)

# 9. Write a query to get the department ID and the total salary payable in each department.
def ex_2_9():
    query = """SELECT department_id, SUM(salary) FROM employees 
    GROUP BY department_id"""
    db_query(query)

# 10. Write a query to get the average salary for each job ID excluding programmers.
def ex_2_10():
    query = """SELECT AVG(salary), job_id FROM employees 
    WHERE NOT job_id = 'IT_PROG' 
    GROUP BY job_id"""
    db_query(query)

# 11. Write a query to find the manager ID and the salary of the lowest paid employee for that manager. (Optional)
def ex_2_11():
    query = """SELECT manager_id, salary FROM employees 
    ORDER BY salary
    LIMIT 1"""
    db_query(query)

#PART 3
# Tables:
# 1. Employees - Columns: employee_id, first_name, last_name, email, phone_number,
# hire_date, job_id, salary, commission_pct, manager_id, department_id
# 2. Departments - Columns: Department_ID , depart_name, Manager_ID, Location_ID
# 3. Locations - Columns: location_id ,street_address,postal_code, city,
# state_province, country_id .
# 4. Jobs - Columns: Job_ID, Job_Title,Min_Salary, Max_Salary

# 1. Write a query to find the names (first_name, last_name) and salaries of the
# employees who have a higher salary than the employee whose last_name='Bull'.
# Table : employees
def ex_3_1():
    query = """SELECT first_name, last_name, salary FROM employees
    WHERE salary > (SELECT salary FROM employees
    WHERE last_name = 'Bull')"""
    db_query(query)

# 2. Write a query to find the names (first_name, last_name) of the employees who are managers.
# Table : employees
def ex_3_2():
    query = """SELECT first_name, last_name FROM employees 
    WHERE job_id IN (SELECT Job_ID FROM jobs WHERE Job_Title LIKE '%Manager%')"""
    db_query(query)

# 3. Write a query to find the names (first_name, last_name), the salary of the
# employees whose salary is greater than the average salary
# Table : employees
def ex_3_3():
    query = """SELECT first_name, last_name, salary FROM employees
    WHERE salary > 
    (SELECT AVG(salary) FROM employees)"""
    db_query(query)

# 4. Write a query to find the names (first_name, last_name), the salary of the
# employees whose salary is equal to the minimum salary for their job grade.
# Tables : employees, jobs.
def ex_3_4join():
    query = """SELECT first_name, last_name, salary FROM employees
    JOIN jobs ON employees.job_id = jobs.Job_ID
    WHERE employees.salary = jobs.Min_Salary"""
    db_query(query)

def ex_3_4sub():
    query = """SELECT first_name, last_name, salary FROM employees
     WHERE employees.salary = 
    (SELECT Min_Salary FROM jobs WHERE employees.job_id = jobs.Job_ID)"""
    db_query(query)

# 5. Write a query to find the names (first_name, last_name), the salary of the
# employees who earn more than the average salary and who works in any of the IT departments.
# Tables : employees, departments
def ex_3_5():
    query = """SELECT first_name, last_name, salary FROM employees 
    WHERE salary > (SELECT AVG(salary) FROM employees)
    AND department_id IN (SELECT department_id FROM departments 
    WHERE depart_name LIKE 'IT%')"""
    db_query(query)

# 6. Write a query to get 3 maximum salaries.
# Tables : employees
def ex_3_6():
    query = """SELECT DISTINCT salary FROM employees 
    ORDER BY salary DESC
    LIMIT 3"""
    db_query(query)

# 7. Write a query to find the names (first_name, last_name) of the employees who
# have a manager who works for a department based in the United States.
# Tables : employees, departments, locations
def ex_3_7():
    query = """SELECT first_name, last_name FROM employees
    WHERE manager_id IN
    (SELECT Manager_ID FROM departments WHERE Location_ID IN 
    (SELECT location_id FROM locations 
    WHERE country_id = 'US'))"""
    db_query(query)

#PART4
# TABLES:
# 1.Employees - Columns: employee_id, first_name, last_name, email, phone_number,
# hire_date, job_id, salary, commission_pct, manager_id, department_id
# 2.Departments - Columns: Department_ID , depart_name, Manager_ID, Location_ID
# 3.Locations - Columns: location_id ,street_address,postal_code, city, state_province,
# country_id .
# 4.job_history - Columns: employee_id, start_date, end_date, job_id, department_id.
# 5.Jobs - Columns: Job_ID, Job_Title,Min_Salary, Max_Salary

# 1. Write a query to get the department name and number of employees in the
# department.
# Tables: employees, departments
def ex_4_1():
    query = """SELECT departments.depart_name, COUNT(employees.employee_id) FROM employees
    JOIN departments ON employees.department_id = departments.Department_ID
    GROUP BY depart_name"""
    db_query(query)


# 2. Write a query to display the department ID, department name, and managers first name.
# Tables: employees, departments
def ex_4_2():
    query = """SELECT departments.Department_ID, departments.depart_name, employees.Manager_ID, employees.first_name FROM departments 
    JOIN employees ON departments.Manager_ID = employees.employee_id"""
    db_query(query)


# 3. Write a query to display the department name, manager name, and city.
# Tables: employees, departments, locations
def ex_4_3():
    query = """SELECT departments.depart_name, employees.first_name, employees.last_name, locations.city FROM departments 
    JOIN locations ON departments.Location_ID = locations.location_id
    JOIN employees ON departments.Manager_ID = employees.employee_id"""
    db_query(query)


# 4. Write a query to display the job history that was done by any employee who is currently drawing more than 10000 of salary.
# Tables: job_history , employees
def ex_4_4():
    query = """SELECT job_history.* FROM job_history
    JOIN employees ON job_history.employee_id = employees.employee_id
    WHERE employees.salary > 10000"""
    db_query(query)


# 5. Write a query to display the job title and average salary of employees.
# Tables: employees, jobs
def ex_4_5():
    query = """SELECT jobs.Job_Title, AVG(employees.salary) FROM jobs
    JOIN employees ON jobs.Job_ID = employees.job_id
    GROUP BY employees.job_id"""
    db_query(query)


# 6. Write a query to find the employee ID, job title number of days between ending
# date and starting date for all jobs in department 90 from job history.
# Tables: job_history, jobs
def ex_4_6():
    query = """SELECT job_history.employee_id, jobs.Job_Title, (end_date - start_date) AS days FROM job_history
    JOIN jobs ON job_history.job_id = jobs.Job_ID
    WHERE department_id = 90"""
    db_query(query)


# 7. Write a query to find the names (first_name, last_name) and hire date of the
# employees who were hired after 'Jones'. Tables: employees
def ex_4_7subquery():
    query = """SELECT first_name, last_name, hire_date FROM employees
    WHERE hire_date > (SELECT hire_date FROM employees WHERE last_name = 'Jones')"""
    db_query(query)
    
def ex_4_7join():
    query = """SELECT a.first_name, a.last_name, a.hire_date FROM employees AS a
    JOIN employees AS b ON b.last_name = 'Jones'
    WHERE a.hire_date > b.hire_date"""
    db_query(query)

