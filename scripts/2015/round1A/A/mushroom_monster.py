# FILENAME = "A-small-practice"
FILENAME = "A-large-practice"


def solve(x):
    s1 = 0
    max_diff = 0
    prec_el = x[0]
    for i in range(len(x))[1:]:
        el = x[i]
        if el < prec_el:
            diff = prec_el - el
            s1 += diff
            max_diff = max(max_diff, diff)
        prec_el = el

    s2 = 0
    for i in range(len(x))[:-1]:
        s2 += min(max_diff, x[i])

    return str(s1) + ' ' + str(s2)


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + ".out", 'w')
    all_lines = [l.replace("\n", '') for l in input_file]
    for i in range(len(all_lines))[1:]:
        if not i % 2:
            x = [int(e) for e in all_lines[i].split()]
        else:
            continue
        j = int(i / 2)
        print('\ninput #' + str(j) + ':', x)
        s = solve(x)
        print('output:', s)
        output_file.write('Case #' + str(j) + ': ' + s + "\n")


def test():
    cases = [[10, 5, 15, 5],]
    for x in cases:
        print('\ninput :', x)
        s = solve(x)
        print('output:', s)


if __name__ == '__main__':
    main()
    # test()
