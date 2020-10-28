# This script removes all students data
from shutil import rmtree
from os import remove
from os.path import exists


# List all experiments
experiments = ["V2", "V8", "V14", "V30", "V39", "V4041", "V42", "V64"]

# Read out students.txt list
students = []
with open("students.txt") as textfile:
    for line in textfile:
        if line[0] != '#':
            # replace whitespaces with "_" and delete "\n" and
            students.append(line.replace(" ", "_")[:-1])

# create directories and fill it with data
for experiment in experiments:
    for student in students:
        rmtree(experiment + "/" + student, ignore_errors=True)
    PdfPath = experiment + "/Data" + experiment + ".pdf"
    if exists(PdfPath):
        remove(PdfPath)

print("Cleared all data.")
