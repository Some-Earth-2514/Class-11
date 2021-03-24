"""In a company an employee is paid as under:
If his basic salary is < Rs.1500, then HRA = 10% of his basic salary and DA = 90% of basic salary:
If his salary is >= Rs.1500, then HRA = Rs.500 and DA = 98% of basic salary.
If the employee's salary is input through the keyboard WAP to find his gross salary
"""
salary = int(input("Enter your salary "))
if salary < 1500:
    HRA = salary * 10 / 100
    DA = salary * 90 / 100
    gross_salary = salary + HRA + DA
    print("The total salary = ", gross_salary)
if salary >= 1500:
    HRA = 500
    DA = salary * 98 / 100
    gross_salary = salary + HRA + DA
    print("The total salary = ", gross_salary)
