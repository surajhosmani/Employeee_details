from emp import emp_details

def test_emp_details():
    expected_op = (
        "Employee name: Suraj\n"
        "Employee id: 900\n"
        "Department: MCA\n"
        "Salary: 20000"
    )

    assert emp_details("Suraj", 900, "MCA", 200000) == expected_op
