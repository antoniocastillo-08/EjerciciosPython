import random


def main():
    rows = 4
    columns = 5
    table = []

    for i in range(rows):
        row = []
        for j in range(columns):
            num = random.randint(100, 999)
            row.append(num)
        table.append(row)

    print("Tabla de números:")
    print()

    for row in table:
        for num in row:
            print(f"{num:>6}", end="")
        print()

    print()
    print("Tabla con sumas:")
    print()

    total_sum = 0

    for i in range(rows):
        row_sum = 0
        for j in range(columns):
            print(f"{table[i][j]:>6}", end="")
            row_sum += table[i][j]
        print(f"{row_sum:>8}")
        total_sum += row_sum

    for j in range(columns):
        column_sum = 0
        for i in range(rows):
            column_sum += table[i][j]
        print(f"{column_sum:>6}", end="")

    print(f"{total_sum:>8}")


if __name__ == "__main__":
    main()