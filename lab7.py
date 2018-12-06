def edit_distance(first,second):
    length_first = len(first)
    length_second = len(second)
    # making a matrix the depending on the size of the words
    matrix  =  [[0] * (length_second +1 ) for _ in range(length_first+1)]

    for i in range(length_first + 1):
        for j in range(length_second+1):
            if j == 0:  # checking if second word exists
                matrix[i][j] = i
            elif i == 0:  # checking if first word exists
                matrix[i][j] = j
            elif first[i-1] == second[j-1]: # checking if last values match
                matrix[i][j] = matrix[i-1][j-1]
            else :  # finding them minimum of operations
                matrix[i][j] = 1 + min(matrix[i][j - 1], matrix[i - 1][j - 1], matrix[i - 1][j])
    return matrix[length_first][length_second]


def main():
    first = input("Input first word")
    second = input("input second word")
    print(edit_distance(first,second))

main()