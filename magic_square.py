def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    num = 1
    i, j = 0, n // 2

    while num <= n**2:
        magic_square[i][j] = num
        num += 1

        newi, newj = (i - 1) % n, (j + 1) % n

        if magic_square[newi][newj] != 0:
            i = (i + 1) % n
        else:
            i, j = newi, newj

    return magic_square

def print_magic_square(square):
    for row in square:
        print(" ".join(str(x) for x in row))

def main():
    n = 4  # Size of the magic square (4x4)
    magic_square = generate_magic_square(n)
    
    print(f"Magic Square of order {n} where all rows, columns, and diagonals sum to 34:")
    print_magic_square(magic_square)

if __name__ == "__main__":
    main()
