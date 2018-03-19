from math import sqrt
import sys

FILENAME = "B-small-practice"
# FILENAME = "B-large-practice"

sys.setrecursionlimit(15000)


class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
            return self.memo[args]


@Memoize
def solve_rec(x):
    max_pancakes = x[-1]
    min_split = int(sqrt(max_pancakes))
    max_split = int(max_pancakes / 2)
    best_sol = x[-1]
    for i in range(min_split, max_split + 1):
        if not i:
            continue
        l = list(x)
        l[-1] -= i
        l.append(i)
        sol = solve_rec(tuple(sorted(l)))
        if sol + 1 < best_sol:
            best_sol = sol + 1
    return best_sol


def solve(x):
    x = tuple(sorted(x))
    return str(solve_rec(x))


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + ".out", 'w')
    all_lines = [l.replace("\n", '') for l in input_file]
    for i in range(len(all_lines))[1:]:
        if not i % 2:
            x = [int(e) for e in all_lines[i].split(' ')]
        else:
            continue
        print('\ninput :', x)
        s = solve(x)
        print('output:', s)
        j = int(i/2)
        output_file.write('Case #' + str(j) + ': ' + s + "\n")


def test():
    cases = [i for i in [(3,), (1, 2, 1, 2), (4,), ]]
    for x in cases:
        print('\ninput :', x)
        s = solve(x)
        print('output:', s)


if __name__ == '__main__':
    main()
    # test()
