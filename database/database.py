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

query1 = """SELECT first_name, last_name, salary FROM employees 
WHERE salary NOT BETWEEN 10000 AND 15000"""

# 2. Write a query to display the names (first_name, last_name) and department ID of all
# employees in departments 30 or 100 in ascending alphabetical order by department ID.

query2 = """SELECT first_name, last_name, department_id FROM employees 
WHERE department_id = 30 OR department_id = 100 
ORDER BY department_id"""

# 3. Write a query to display the names (first_name, last_name) and salary for all employees
# whose salary is not in the range $10,000 through $15,000 and are in department 30 or 100.

query3 = """SELECT first_name, last_name, salary FROM employees
WHERE (salary NOT BETWEEN 10000 AND 15000) AND (department_id = 30 OR department_id = 100)"""

# 4. Write a query to display the first_name of all employees who have both an "b" and "c" in their
# first name.
query4 = """SELECT first_name FROM employees 
WHERE first_name LIKE '%b%c%' OR '%c%b%' """

# 5. Write a query to display the last name, job, and salary for all employees whose job is that of a
# Programmer or a Shipping Clerk, and whose salary is not equal to $4,500, $10,000, or $15,000.
query5 = """SELECT last_name, job_id, salary FROM employees 
WHERE job_id = 'IT_PROG' OR job_id = 'SH_CLERK' 
AND salary != 4500 AND salary != 10000 AND salary != 15000"""

# 6. Write a query to display the last names of employees whose names have exactly 6 characters.
query6 = """SELECT last_name FROM employees
WHERE last_name LIKE '______' """

# 7. Write a query to display the last names of employees having 'e' as the third character.
query7 = """SELECT last_name FROM employees
WHERE last_name LIKE '__e%' """

#PART 2
# 1. Write a query to list the amount of jobs available in the employees table.
query2_1 = """SELECT job_id, COUNT(job_id) FROM employees 
GROUP BY job_id"""
query2_1_1 = """SELECT COUNT(DISTINCT job_id) FROM employees"""

# 2. Write a query to get the total of salaries to pay.
query2_2 = """SELECT SUM(salary) FROM employees"""

# 3. Write a query to get the minimum salary from employees table.
query2_3 = """SELECT MIN(salary) FROM employees"""

# 4. Write a query to get the highest salary of an employee.
query2_4 = """SELECT MAX(salary) FROM employees"""

# 5. Write a query to get average salary and number of employees working in department 90.
query2_5 = """SELECT AVG(salary), COUNT(employee_id) FROM employees 
WHERE department_id = 90"""

# 6. Write a query to get the highest, lowest, sum and average salary of all employees.
query2_6 = """SELECT MAX(salary), MIN(salary), SUM(salary), AVG(salary) FROM employees"""

# 7. Write a query to get the number of employees with the same job.
query2_7 = """SELECT COUNT(employee_id), job_id FROM employees 
GROUP BY job_id"""

# 8. Write a query to get the difference between the highest and lowest salaries.
query2_8 = """SELECT (MAX(salary) - MIN(salary)) FROM employees"""

# 9. Write a query to get the department ID and the total salary payable in each department.
query2_9 = """SELECT department_id, SUM(salary) FROM employees 
GROUP BY department_id"""

# 10. Write a query to get the average salary for each job ID excluding programmers.
query2_10 = """SELECT AVG(salary), job_id FROM employees 
WHERE NOT job_id = 'IT_PROG' 
GROUP BY job_id"""

# 11. Write a query to find the manager ID and the salary of the lowest paid employee for that manager. (Optional)
query2_11 = """SELECT manager_id, salary FROM employees 
ORDER BY salary
LIMIT 1"""


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
query3_1 = """SELECT first_name, last_name, salary FROM employees
WHERE salary > (SELECT salary FROM employees
WHERE last_name = 'Bull')"""

# 2. Write a query to find the names (first_name, last_name) of the employees who are managers.
# Table : employees
query3_2 = """SELECT first_name, last_name FROM employees 
WHERE job_id IN ("SELECT Job_ID FROM jobs WHERE Job_Title LIKE '%Manager%')"""

# 3. Write a query to find the names (first_name, last_name), the salary of the
# employees whose salary is greater than the average salary
# Table : employees
query3_3 = """SELECT first_name, last_name, salary FROM employees
WHERE salary > 
(SELECT AVG(salary) FROM employees)"""

# 4. Write a query to find the names (first_name, last_name), the salary of the
# employees whose salary is equal to the minimum salary for their job grade.
# Tables : employees, jobs.
query3_4_1 = """SELECT first_name, last_name, salary FROM employees
JOIN jobs ON employees.job_id = jobs.Job_ID
WHERE employees.salary = jobs.Min_Salary
"""

# query3_4 = """SELECT first_name, last_name, salary FROM employees
# WHERE job_id IN
# (SELECT Job_ID FROM jobs) AND salary IN (SELECT Min_Salary FROM jobs)"""


# 5. Write a query to find the names (first_name, last_name), the salary of the
# employees who earn more than the average salary and who works in any of the IT departments.
# Tables : employees, departments
query3_5 = """SELECT first_name, last_name, salary FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees)
AND department_id IN (SELECT department_id FROM departments 
WHERE depart_name LIKE 'IT%')"""

# 6. Write a query to get 3 maximum salaries.
# Tables : employees
query3_6 = """SELECT DISTINCT salary FROM employees 
ORDER BY salary DESC
LIMIT 3"""

# 7. Write a query to find the names (first_name, last_name) of the employees who
# have a manager who works for a department based in the United States.
# Tables : employees, departments, locations
query3_7 = """SELECT first_name, last_name FROM employees
WHERE manager_id IN
(SELECT Manager_ID FROM departments WHERE Location_ID IN 
(SELECT location_id FROM locations 
WHERE country_id = 'US'))"""

