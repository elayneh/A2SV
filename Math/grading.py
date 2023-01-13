#usr/bin/python3

def grading(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            tempGrade = grades[i]
            while tempGrade % 5 != 0:
                tempGrade = tempGrade + 1
            if (tempGrade - grades[i]) < 3:
                    grades[i] = tempGrade
    return grades


if __name__ == "__main__":

    print(grading([73, 67, 38, 33]))
