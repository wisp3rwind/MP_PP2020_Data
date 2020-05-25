import os
import shutil

# List all experiments
experiments = ["V2", "V8", "V30", "V39", "V4041", "V42", "V64"]

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
        os.makedirs(experiment + "/" + student,
                    exist_ok=True)               # create student dir
        os.makedirs(experiment + "/" + "PDFs",
                    exist_ok=True)               # create pdfs dir
        os.system("python3 " + experiment + "/" + "generateData" +           # create data
                  experiment + ".py" + " " + student)
        os.system("python3 " + experiment + "/" + "generatepdf" +            # create pdf
                  experiment + ".py" + " " + student)
        shutil.copy2(experiment + "/Auswertung" + experiment + ".ipynb",
                     experiment + "/" + student + "/Auswertung" + experiment + ".ipynb")  # copy ipynb
