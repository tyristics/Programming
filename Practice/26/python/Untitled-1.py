 
int i, j, temp
int max = 0, maxX = 0, maxY = 0
for (i=0
     i < n
     i++)
for (j=0
     j < m
     j++)
if (a[i][j] > max) {
    max = a[i][j]
    maxX = i
    maxY = j
}
for (i=0
     i < n
     i++) {
    temp = a[i][0]
    a[i][0] = a[i][maxX]
    a[i][maxX] = temp
}
for (j=0
     j < m
     j++) {
    temp = a[0][j]
    a[0][j] = a[maxY][j]
    a[maxY][j] = temp
}
