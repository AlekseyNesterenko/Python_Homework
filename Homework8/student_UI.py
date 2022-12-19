def get_score(student):
    return student.subjects


def print_score(student):
    for subject, score in get_score(student).items():
        print(f"{subject}: {score}")