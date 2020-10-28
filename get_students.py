def get_students(path="./"):
    """
    Returns the a list of strings containing the students from 'students.txt'

    Args:
        path (string) path for 'students.txt' file
    Returns:
        students (list)

    """

    students = []
    with open(path + "students.txt") as textfile:
        for line in textfile:
            if line[0] != '#':
                # replace whitespaces with "_" and delete "\n" and
                students.append(line.replace(" ", "_")[:-1])
    return students
