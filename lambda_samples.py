# First example with lambda function, lambda function is most used on strings, lists, dictionaries and mapping values on these kind of structures.
class employee():
    def __init__(self, last_name, job_title, age):
        self.last_name = last_name
        self.job_title = job_title
        self.age = age

    def __repr__(self):
        return repr((self.last_name, self.job_title, self.age))


employees = [employee("Lozano", "DevOps Engineer", 22), employee(
    "Bell", "QA Engineer", 32), employee("Marquez", "Delivery Manager", 42)]
print(sorted(employees, key=lambda employee: employee.job_title))


# Second example: Calculate the circle's area regarding its radius.
def circle_area(r): return (r**2)*(3.1416)


print(circle_area(2))
