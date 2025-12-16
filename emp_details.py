def emp_details(name, emp_id, dept, salary):
    result = (
        f"Employee name: {name}\n"
        f"Employee id: {emp_id}\n"
        f"Department: {dept}\n"
        f"Salary: {salary}"
    )
    return result

if __name__ == "__main__":
    name = "Suraj"
    emp_id = 900
    dept = "MCA"
    salary = 20000
    
    print(emp_details(name, emp_id, dept, salary))
