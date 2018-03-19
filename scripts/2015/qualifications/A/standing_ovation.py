# FILENAME = "A-small-practice"
FILENAME = "A-large-practice"


def solve(x):
    s = 0
    cur_sum = 0
    for i, n in enumerate(x):
        if cur_sum < i:
            s += i - cur_sum
            cur_sum = i
        cur_sum += n
    return str(s)


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + ".out", 'w')
    all_lines = [l.replace("\n", '') for l in input_file]
    for i in range(len(all_lines))[1:]:
        x = [int(e) for e in all_lines[i].split(' ')[-1]]
        print('\ninput :', x)
        s = solve(x)
        print('output:', s)
        output_file.write('Case #' + str(i) + ': ' + s + "\n")


def test():
    cases = [i for i in [(1, 1, 1, 1, 1), (0, 9), (1, 1, 0, 0, 1, 1), (1,)]]
    for x in cases:
        print('\ninput :', x)
        s = solve(x)
        print('output:', s)


if __name__ == '__main__':
    main()
    # test()
