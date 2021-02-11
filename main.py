import os
import os.path
import shutil
from get_students import get_students

# List all experiments
experiments = ["V2", "V8", "V14", "V30", "V39", "V4041", "V42", "V64"]

# Read out students.txt list
students = get_students()

# create directories and fill it with data
for experiment in experiments:
    nb_filename = "Auswertung{}.ipynb".format(experiment)
    data_gen_script = os.path.join(experiment, "generateData{}.py".format(experiment))
    pdf_gen_script = os.path.join(experiment, "generatepdf{}.py".format(experiment))

    for student in students:
        student_basedir = os.path.join(experiment, student)

        # create student dir
        os.makedirs(student_basedir, exist_ok=True)

        # create data
        os.system(" ".join(["python3", data_gen_script, student]))

        # copy ipynb
        shutil.copy2(
            os.path.join(experiment, nb_filename),
            os.path.join(student_basedir, nb_filename)
        )

    # No need to copy the interactive notebook, it is already in place.

    # create pdf
    os.system(" ".join(["python3", pdf_gen_script]))
