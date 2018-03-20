# FILENAME = "D-small-practice"
FILENAME = "D-large-practice"


def solve(x, r, c):
    if x >= 7:
        return 'RICHARD'

    total_n = r * c
    small_c = min(r, c)
    long_c = max(r, c)

    if total_n % x:
        return 'RICHARD'

    biggest_small_c = int((x - 1) / 2) + 1
    if biggest_small_c > small_c:
        return 'RICHARD'
    elif biggest_small_c < small_c:
        return 'GABRIEL'

    if long_c < x:
        return 'RICHARD'

    if small_c > x-2:
        return 'GABRIEL'

    # else, the question is; can richard forces the surrounding of a x-non-divisible area
    # we know we have biggest_small_c == small_c
    remaining_x = x - biggest_small_c
    if not remaining_x:
        return 'GABRIEL'
    for i in range(0, int(remaining_x/2)+1):
        long_x, small_x = remaining_x - i, i
        good_pos = True
        for bar_pos in range(small_x+1, long_c-long_x-1):
            remaining_space_top = small_c * bar_pos - small_x
            remaining_space_bot = small_c * (long_c - bar_pos - 1) - long_x
            if remaining_space_top % x == 0 and remaining_space_bot % x == 0:
                good_pos = False
                break
        if good_pos:
            return 'RICHARD'
    return 'GABRIEL'


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + ".out", 'w')
    all_lines = [l.replace("\n", '') for l in input_file]
    for i in range(len(all_lines))[1:]:
        x, r, c = [int(e) for e in all_lines[i].split(' ')]
        print('\ninput #' + str(i) + ':', x, r, c)
        s = solve(x, r, c)
        print('output:', s)
        output_file.write('Case #' + str(i) + ': ' + s + "\n")


def test():
    cases = [[19, 19, 10]]
    for x, r, c in cases:
        print('\ninput :', x, r, c)
        s = solve(x, r, c)
        print('output:', s)


if __name__ == '__main__':
    main()
    # test()
