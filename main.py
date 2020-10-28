import os
import shutil
from get_students import get_students

# List all experiments
experiments = ["V2", "V8", "V14", "V30", "V39", "V4041", "V42", "V64"]

# Read out students.txt list
students = get_students()

# create directories and fill it with data
for experiment in experiments:
    for student in students:
        os.makedirs(experiment + "/" + student,
                    exist_ok=True)               # create student dir
        os.system("python3 " + experiment + "/" + "generateData" +           # create data
                  experiment + ".py" + " " + student)
        shutil.copy2(experiment + "/Auswertung" + experiment + ".ipynb",
                     experiment + "/" + student + "/Auswertung" + experiment + ".ipynb")  # copy ipynb
    os.system("python3 " + experiment + "/" + "generatepdf" +            # create pdf
              experiment + ".py")
