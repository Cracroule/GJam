FILENAME = "A-small-practice"
# FILENAME = "A-large-practice"


def solve(R, C, W):
    # 1. The move to find the correct row where the battleship is:
    #    (R - 1) * (C // W)
    #
    # 2. The move to find the whole battle ship in the last row:
    #    case (1) C % W == 0:
    #        C // W - 1 + W = (C - 1) // W + W
    #    case (2) C % W != 0:
    #        C // W + W = (C - 1) // W + W
    #    case (1) + (2) <=> (C - 1) // W + W
    return ((R - 1) * (C // W)) + ((C - 1) // W + W)


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + ".out", 'w')
    all_lines = [l.replace("\n", '') for l in input_file]
    for i in range(len(all_lines))[1:]:
        r, c, w = [int(e) for e in all_lines[i].split(' ')]
        print('\ninput :', r, c, w)
        s = str(solve(r, c, w))
        print('output:', s)
        output_file.write('Case #' + str(i) + ': ' + s + "\n")


def test():
    # cases = [[e for e in el] for el in ['1', '19', '23']]
    # cases = ['1', '19', '23']
    # cases = ['19']
    # cases = ['99']
    cases = [[1, 10, 5], [1, 8, 4]]
    # cases = [[1, 10, 5], [1, 9, 5], [1, 8, 5], [1, 7, 5], [1, 6, 5]]
    for r, c, w in cases:
        print('\ninput :', r, c, w)
        s = solve(r, c, w)
        print('output:', s)


if __name__ == '__main__':
    main()
    # test()