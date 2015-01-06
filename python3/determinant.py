def CheckForInvalidIndex(matrix):
	for row in matrix:
		for column in row:
			if type(column) != int:
				return False
	return True

def CheckIfSquare(matrix):
	for row in matrix:
		if len(row) != len(matrix):
			return False
	return True

def FindRowWithMostZeros(matrix):
	rowIndex = None
	count = None
	for row in range(len(matrix)):
		newCount = matrix[row].count(0)
		if rowIndex == None:
			rowIndex = row
			count = newCount
		elif count < newCount:
			count = newCount
			rowIndex = row
	return rowIndex

def GetSubMatrix(matrix, row, column):
	newMatrix = []
	for rowIndex in range(len(matrix)):
		if rowIndex == row:
			continue
		newMatrix.append([])
		for columnIndex in range(len(matrix[0])):
			if columnIndex == column:
				continue
			newMatrix[rowIndex - 1].append(matrix[rowIndex][columnIndex])
	return newMatrix

def Determinant(matrix):
	if not CheckIfSquare(matrix) or not CheckForInvalidIndex(matrix):
		return None
	elif len(matrix) == len(matrix[0]) == 2:
		return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
	else:
		detResults = []
		row = FindRowWithMostZeros(matrix)
		count = 0
		for columnIndex in range(len(matrix[row])):
			count += 1
			if matrix[row][columnIndex] == 0:
				continue
			else:
				sign = 1 if count % 2 == 1 else -1
				result = Determinant(GetSubMatrix(matrix, row, columnIndex))
				detResults.append(result * matrix[row][columnIndex] * sign)
		return sum(detResults)

x = [[9, 1, 3, 5], [4, 358, 31, 48], [7, 4784, 3, 78], [31, 89, 68, 53]]
y = Determinant(x)
print(y)
