FILENAME = "B-small-practice"
# FILENAME = "B-large-practice"


def solve(m, n):
    # b, n = [int(e) for e in input().strip().split()]
    # m = [int(e) for e in input().strip().split()]
    # # print(b, n, m)

    b = len(m)

    # Count the number of coming guests at the time T.
    def guest_num(T):
        num = 0
        for i in range(b):
            num += (T + m[i] - 1) // m[i]
        return num

    # Time:  O(log(N * max(M)))
    # Find the most time when the number of guests is still less than n
    L = 0
    R = 10 ** 14
    while L <= R:
        M = L + R >> 1
        if guest_num(M) >= n:
            R = M - 1
        else:
            L = M + 1

    # Now guest_num(L-1) < n <= guest_num(L)
    # At the time L, the number of coming guest achieves n.
    time_to_available = [0] * b
    for i in range(b):
        cnt = (L - 1 + m[i] - 1) // m[i]
        time_to_available[i] = cnt * m[i]
        n -= cnt

    # Time:  O(BlogB)
    # Sort time_to_available by time and id,
    # assign the remaining guests to the available ones by id order at the time L.
    # Now 0 <= n <= b
    idxs = sorted(range(b), key=lambda i: (time_to_available[i], i))

    # (i+1)th barber.
    return str(idxs[n - 1] + 1)


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + "2.out", 'w')
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