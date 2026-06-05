def read_matrix():
    rows, cols = map(int, input().split())
    matrix = [list(map(float, input().split())) for _ in range(rows)]
    return matrix


def print_matrix(matrix):
    for row in matrix:
        result = []
        for x in row:
            if abs(x - int(x)) < 1e-9:
                result.append(str(int(x)))
            else:
                result.append(str(round(x, 2)))
        print(*result)


def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None

    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)

    return result


def multiply_by_constant(matrix, constant):
    result = []
    for row in matrix:
        result.append([x * constant for x in row])
    return result


def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        return None

    result = []

    for i in range(len(a)):
        row = []

        for j in range(len(b[0])):
            value = 0

            for k in range(len(b)):
                value += a[i][k] * b[k][j]

            row.append(value)

        result.append(row)

    return result


def transpose_main(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)

    return result


def transpose_side(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[rows - 1 - i][cols - 1 - j])
        result.append(row)

    return result


def transpose_vertical(matrix):
    return [row[::-1] for row in matrix]


def transpose_horizontal(matrix):
    return matrix[::-1]


def minor(matrix, row, col):
    result = []

    for i in range(len(matrix)):
        if i == row:
            continue

        temp = []

        for j in range(len(matrix)):
            if j == col:
                continue

            temp.append(matrix[i][j])

        result.append(temp)

    return result


def determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0

    for col in range(n):
        det += ((-1) ** col) * matrix[0][col] * determinant(
            minor(matrix, 0, col)
        )

    return det


def inverse_matrix(matrix):
    det = determinant(matrix)

    if abs(det) < 1e-9:
        return None

    n = len(matrix)

    if n == 1:
        return [[1 / det]]

    cofactors = []

    for i in range(n):
        row = []

        for j in range(n):
            value = ((-1) ** (i + j)) * determinant(
                minor(matrix, i, j)
            )
            row.append(value)

        cofactors.append(row)

    adjugate = transpose_main(cofactors)

    inverse = []

    for row in adjugate:
        inverse.append([x / det for x in row])

    return inverse


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")

    choice = input("Your choice: ")

    if choice == "0":
        break

    elif choice == "1":
        print("Enter size of first matrix:")
        a = read_matrix()

        print("Enter size of second matrix:")
        b = read_matrix()

        result = add_matrices(a, b)

        if result is None:
            print("The operation cannot be performed.")
        else:
            print("The result is:")
            print_matrix(result)

    elif choice == "2":
        print("Enter size of matrix:")
        matrix = read_matrix()

        constant = float(input("Enter constant: "))

        result = multiply_by_constant(matrix, constant)

        print("The result is:")
        print_matrix(result)

    elif choice == "3":
        print("Enter size of first matrix:")
        a = read_matrix()

        print("Enter size of second matrix:")
        b = read_matrix()

        result = multiply_matrices(a, b)

        if result is None:
            print("The operation cannot be performed.")
        else:
            print("The result is:")
            print_matrix(result)

    elif choice == "4":
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")

        transpose_type = input("Your choice: ")

        print("Enter matrix size:")
        matrix = read_matrix()

        if transpose_type == "1":
            result = transpose_main(matrix)

        elif transpose_type == "2":
            result = transpose_side(matrix)

        elif transpose_type == "3":
            result = transpose_vertical(matrix)

        else:
            result = transpose_horizontal(matrix)

        print("The result is:")
        print_matrix(result)

    elif choice == "5":
        print("Enter matrix size:")
        matrix = read_matrix()

        if len(matrix) != len(matrix[0]):
            print("The operation cannot be performed.")
        else:
            print("The result is:")
            print(determinant(matrix))

    elif choice == "6":
        print("Enter matrix size:")
        matrix = read_matrix()

        if len(matrix) != len(matrix[0]):
            print("This matrix doesn't have an inverse.")
            continue

        result = inverse_matrix(matrix)

        if result is None:
            print("This matrix doesn't have an inverse.")
        else:
            print("The result is:")
            print_matrix(result)