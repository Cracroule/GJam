# FILENAME = "B-small-practice"
FILENAME = "B-large-practice"


def count_cells_filling_diag(small_c, long_c, fill_upper_right=True):
    if small_c < 0 or long_c < 0:
        return 0
    if fill_upper_right:
        return int((small_c + 1) / 2) * int((long_c + 1) / 2) + int(small_c / 2) * int(long_c / 2)
    return int(small_c / 2) * int((long_c + 1) / 2) + int((small_c + 1) / 2) * int(long_c / 2)


def solve(r, c, n):
    small_c = min(r, c)
    long_c = max(r, c)

    cost_corner = 2 if small_c > 1 else 1
    cost_bound = 3 if small_c > 1 else 2

    placed_n_odd = count_cells_filling_diag(small_c, long_c, True)
    placed_n_even = count_cells_filling_diag(small_c, long_c, False)

    if n <= placed_n_even or n <= placed_n_odd:
        return '0'

    # ATTEMPT ONE: start filling by upper left
    cost_1 = 0
    remaining_n = n - placed_n_odd

    # count empty corners
    corners = 0
    if small_c % 2 == 0:
        corners = 2  # bottom left AND either top right or bottom right
    elif long_c % 2 == 0:
        corners = 2 if small_c > 1 else 1

    if remaining_n > corners:
        cost_1 += corners * cost_corner
        remaining_n -= corners
    else:
        cost_1 += remaining_n * cost_corner
        remaining_n = 0

    # count bounds
    bounds_spots = placed_n_even - count_cells_filling_diag(small_c - 2, long_c - 2, False) - corners
    if remaining_n > bounds_spots:
        cost_1 += bounds_spots * cost_bound
        remaining_n -= bounds_spots
    else:
        cost_1 += remaining_n * cost_bound
        remaining_n = 0

    cost_1 += remaining_n * 4

    # ATTEMPT TWO: don t fill upper left
    cost_2 = 0
    remaining_n = n - placed_n_even

    # count empty corners
    corners = 0
    if small_c % 2 == 1:
        corners += 2 if small_c > 1 else 1  # left side
        if long_c % 2 == 1:
            corners += 2 if small_c > 1 else 1
    else:
        corners += 1  # top left corner
        if long_c % 2 == 1:
            corners += 1  # top right
        elif small_c > 1:
            corners += 1  # bottom right

    if remaining_n > corners:
        cost_2 += corners * cost_corner
        remaining_n -= corners
    else:
        cost_2 += remaining_n * cost_corner
        remaining_n = 0

    # count bounds
    bounds_spots = placed_n_odd - count_cells_filling_diag(small_c - 2, long_c - 2, True) - corners
    if remaining_n > bounds_spots:
        cost_2 += bounds_spots * cost_bound
        remaining_n -= bounds_spots
    else:
        cost_2 += remaining_n * cost_bound
        remaining_n = 0

    cost_2 += remaining_n * 4

    return str(min(cost_1, cost_2))


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + ".out", 'w')
    all_lines = [l.replace("\n", '') for l in input_file]
    for i in range(len(all_lines))[1:]:
        r, c, n = [int(e) for e in all_lines[i].split(' ')]
        print('\ninput :', r, c, n)
        s = solve(r, c, n)
        print('output:', s)
        output_file.write('Case #' + str(i) + ': ' + s + "\n")


def test():
    cases = [[15, 1, 15], [3, 5, 14], [3, 5, 13], [3, 5, 12], [3, 5, 11], [3, 5, 10]]
    for r, c, n in cases:
        print('\ninput :', r, c, n)
        s = solve(r, c, n)
        print('output:', s)


if __name__ == '__main__':
    main()
    # test()
