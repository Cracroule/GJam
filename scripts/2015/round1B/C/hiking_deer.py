# FILENAME = "C-small-practice-1"
# FILENAME = "C-small-practice-2"
FILENAME = "C-large-practice"
# FILENAME = "C-test-input"


def solve(hikers_descr):
    hikers = list()
    for pos, group_size, freq in hikers_descr:
        for i in range(group_size):
            # pos, freq, arrived_in_t
            hikers.append([pos, freq + i, (360 - pos) * (freq + i) / 360])

    nb_hikers = len(hikers)
    hikers = sorted(hikers, key=lambda x: x[2])

    best_solution = nb_hikers
    stop = False
    for i, hiker in enumerate(hikers):
        if stop:
            break
        if i > 0 and not i % 10000:
            print(i)
        h_pos, h_freq, h_t = hiker
        nb_crossed = nb_hikers - (i+1)

        # count slower humans
        for j in range(i+1, nb_hikers):
            if hikers[j][2] == h_t:
                nb_crossed -= 1 # already counted
            else:
                break

        # count faster humans
        for j in range(i):
            _, h_prec_freq, h_prec_t = hikers[j]
            nb_crossed += int((h_t - h_prec_t) / h_prec_freq)
            if nb_crossed > nb_hikers:
                stop = True
                break

        best_solution = min(best_solution, nb_crossed)

    return str(best_solution)


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + ".out", 'w')
    all_lines = [l.replace("\n", '') for l in input_file]
    nb_cases = int(all_lines[0])
    cur_line = 1
    for i in range(nb_cases):
        nb_hikers = int(all_lines[cur_line])
        hikers_descr = [[int(e) for e in all_lines[cur_line + j].split(' ')] for j in range(1, nb_hikers+1)]
        print('\ninput :', hikers_descr)
        s = solve(hikers_descr)
        print('output:', s)
        output_file.write('Case #' + str(i+1) + ': ' + s + "\n")
        cur_line += nb_hikers + 1


# def test():
#     cases = [[15, 1, 15], [3, 5, 14], [3, 5, 13], [3, 5, 12], [3, 5, 11], [3, 5, 10]]
#     for r, c, n in cases:
#         print('\ninput :', r, c, n)
#         s = solve(r, c, n)
#         print('output:', s)


if __name__ == '__main__':
    main()
    # test()
