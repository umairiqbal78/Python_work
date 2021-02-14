# Matrix A
matrixA = []
rowsA = float(input("enter number of rows for matrix A: "))
columnsA = float(input("enter number of columns matrix A: "))

a = 0
while a < rowsA:
  b= 0
  rowA = []
  while b < columnsA:
    entry = int(input(f"row {a+1},value # {b+1}: "))
    rowA.append(entry)
    b += 1
  matrixA.append(rowA)
  print("\n")
  a += 1

print("It is  matrixA\n",matrixA)

#MatrixB

matrixB = []
rowsB = int(input("enter number of rows for matrix B: "))
columnsB = int(input("enter number of columns for matrix B: "))

a = 0
while a < rowsB:
  b= 0
  rowB = []
  while b < columnsB:
    entry = int(input(f"row {a+1},value # {b+1}: "))
    rowB.append(entry)
    b += 1
  matrixB.append(rowB)
  print("\n")
  a += 1

print("It is matrixB \n",matrixB)



ask = int(input("What do you want \n 1.Addition \n 2.Subtraction \n 3.Multiplication: "))

#Addition
if ask == 1 :
  if rowsA == rowsB and columnsA == columnsB:
    mat = []
    a = 0

    while a < rowsA:
      row = []
      b = 0
      while b < columnsA:
        add = matrixA[a][b] + matrixB[a][b]
        row.append(add)
        b += 1

      mat.append(row)
      a +=1
    print("\nAddition of matrices is \n",mat)
  else:
    print("Invalid matrices orders for Addition")

#Subtraction
elif ask == 2 :
  if rowsA == rowsB and columnsA == columnsB:
    mat = []
    a = 0

    while a < rowsA:
      row = []
      b = 0
      while b < columnsA:
        add = matrixA[a][b] - matrixB[a][b]
        row.append(add)
        b += 1

      mat.append(row)
      a +=1
    print("\nSubtraction of matrices is\n",mat)
  else:
    print("Invalid matrices orders for subtraction")
#Multiplication
elif ask == 3 :
  if columnsA == rowsB:
    matrix = []
    a = 0
    while a < rowsA:
      b = 0
      row = []
      while b < columnsB :
        c = 0
        s = 0
        while c < rowsB :
          mult = (matrixA[a][c]) * (matrixB[c][b])
          s += mult
          c += 1
          
        row.append(s)
        b += 1

      print(row)
      matrix.append(row)
      a += 1
    print("\nMultiplication of matrices is \n",matrix)
  else:
    print("Invalid matrices orders for multiplication")
