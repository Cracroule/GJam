FILENAME = "B-small-practice"
# FILENAME = "B-large-practice"


def safe_advance_t(m, remaining_t, advance_t):
    nb_haircuts = 0
    for i in range(len(m)):
        advance_t_i = advance_t
        if remaining_t[i] and remaining_t[i] <= advance_t:
            advance_t_i = advance_t - remaining_t[i]
            remaining_t[i] = 0
            nb_haircuts += 1
        elif remaining_t[i] > advance_t:
            remaining_t[i] -= advance_t
            continue

        nb_haircuts_i = int(advance_t_i/m[i])
        advance_t_i = advance_t_i % m[i]
        if advance_t_i:
            nb_haircuts_i += 1
            remaining_t[i] = m[i] - advance_t_i
        nb_haircuts += nb_haircuts_i
    return nb_haircuts, remaining_t


def solve(m, p):
    remaining_t = [0] * len(m)
    cur_pos = p
    shortest_t = min(m)
    nb_b = len(m)
    while True:
        min_wait = max(int(round(cur_pos / nb_b) - 1) * shortest_t, 0)
        if min_wait > shortest_t:
            nb_haircuts_made, remaining_t = safe_advance_t(m, remaining_t, min_wait)
            cur_pos -= nb_haircuts_made
        try:
            available_i = remaining_t.index(0)
            if cur_pos == 1:
                return str(available_i+1)
            else:
                remaining_t[available_i] = m[available_i]
                cur_pos -= 1
        except ValueError:
            remaining_t_min = min(remaining_t)
            remaining_t = [t - remaining_t_min for t in remaining_t]


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + ".out", 'w')
    all_lines = [l.replace("\n", '') for l in input_file]
    for i in range(len(all_lines))[1:]:
        if not i % 2:
            x = [int(e) for e in all_lines[i].split()]
        else:
            n, p = [int(e) for e in all_lines[i].split()]
            continue
        j = int(i / 2)
        print('\ninput #' + str(j) + ':', x, p)
        s = solve(x, p)
        print('output:', s)
        output_file.write('Case #' + str(j) + ': ' + s + "\n")


def test():
    # cases = [[4, [10, 5]], [12, [7, 7, 7]], [8, [4, 2, 1]]]
    # cases = [[10, [2, 2,]], ]
    # cases = [[1000000000, [25, 25, 25, 25, 25]], ]
    # cases = [[1000, [25, 25, 25, 25, ]], ]
    cases = [[8, [4, 2, 1]], ]
    for p, x in cases:
        print('\ninput :', p, x)
        s = solve(x, p)
        print('output:', s)


if __name__ == '__main__':
    main()
    # test()
