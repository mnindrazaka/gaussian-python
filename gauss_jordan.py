def getDiagonalIndex(isReverse):
    if (isReverse):
        return reversed(range(0, num))
    else:
        return range(0, num)


def getDiagonalValue(index):
    return problem[index][index]


def getRemainingRowIndex(currentRow, isReverse):
    if (isReverse):
        return reversed(range(0, currentRow))
    else:
        return range(currentRow + 1, num)


def getRemainingColIndex():
    return range(0, num + 1)


def getMultiplier(diagonalValue, nextValue):
    return (0 - nextValue) / diagonalValue


def printProblem():
    for row in problem:
        for cell in row:
            print(round(cell, 1), end=" ")
        print("\n")


def printAnswer():
    for row in problem:
        print(round(row[num], 1))


def gauss(isReverse):
    for i in getDiagonalIndex(isReverse):
        if (getDiagonalValue(i) != 1):
            divider = getDiagonalValue(i)
            for l in getRemainingColIndex():
                problem[i][l] /= divider

        for j in getRemainingRowIndex(i, isReverse):
            nextValue = problem[j][i]
            multiplier = getMultiplier(getDiagonalValue(i), nextValue)
            if nextValue != 0:
                for k in getRemainingColIndex():
                    problem[j][k] = problem[i][k] * multiplier + problem[j][k]


if __name__ == "__main__":
    num = int(input("Masukkan Jumlah Variabel : "))
    problem = []

    for i in range(0, num):
        problem.append([])
        print("Input Soal ke-" + str(i + 1) + " : ")
        for j in range(0, num + 1):
            problem[i].append(float(input("input ke-" + str(j + 1) + " : ")))

    printProblem()

    gauss(False)
    gauss(True)
    printAnswer()
