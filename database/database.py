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
db_query(query2_11)