''' We're working with a list of flowers and some information about each one.
The create_file function writes this information to a CSV file.
The contents_of_file function reads this file into records and
returns the information in a nicely formatted block.
Fill in the gaps of the contents_of_file function to turn the data in the
CSV file into a dictionary using DictReader.'''

import csv

# Create a file with data in it


def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row


def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename, newline='') as flowers:
        # Read the rows of the file into a dictionary
        reader_csv = csv.DictReader(flowers)
        # Process each item of the dictionary
        for row in reader_csv:
            return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
    return return_string


# Call the function
print(contents_of_file("flowers.csv"))


''' Using the CSV file of flowers again, fill in the gaps of the
contents_of_file function to process the data without turning it
into a dictionary. How do you skip over the header record with
the field names? '''


def contents_of_file_2(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename, newline='') as flowers:
        # Read the rows of the file
        rows = csv.reader(flowers, delimiter=",")
        row_count = 0
        # Process each row
        for row in rows:
            if row_count == 0:
                row_count += 1
                continue
            # Format the return string for data rows only
            return_string += "a {} {} is {}\n".format(row[0], row[1], row[2])
    return return_string


# Call the function
print(contents_of_file_2("flowers2.csv"))


''' Other interesting excersise:


def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list


employee_list = read_employees('C:\Documents\student-01-0aa3fde1d800\data\employees.csv')


def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data


dictionary = process_data(employee_list)


def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()


write_report(dictionary, 'C:\Documents\student-01-0aa3fde1d800\data\employees.csv')

'''
