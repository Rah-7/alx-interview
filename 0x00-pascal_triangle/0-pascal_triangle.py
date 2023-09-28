def pascal_triangle(n):
    """
    Prints the Pascal's triangle of n.
    """
    if n <= 0:
        return

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(i):
            row.append(triangle[i-1][j] + triangle[i-1][j-1] if j > 0 else 1)
        triangle.append(row)

    for row in triangle:
        print(row)
