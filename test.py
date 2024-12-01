def count_cells(a, b, c, k):
    black_cells = a * a
    red_cells = 0
    current_side = a

    for i in range(1, k + 1):
        if i % 2 == 1:
            current_side += 2 * b
            new_red_cells = current_side * current_side - \
                (current_side - 2 * b) * (current_side - 2 * b)
            red_cells += new_red_cells
        else:
            current_side += 2 * c
            new_black_cells = current_side * current_side - \
                (current_side - 2 * c) * (current_side - 2 * c)
            black_cells += new_black_cells

    return black_cells, red_cells


a, b, c, k = map(int, input().strip().split())
black_cells, red_cells = count_cells(a, b, c, k)
print(black_cells, red_cells)
