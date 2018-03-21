# FILENAME = "A-small-practice"
FILENAME = "A-large-practice"


def solve(x):
    nb_digits = len(x)
    if nb_digits == 1:
        return x
    perfect_nb = '1' + '0' * (nb_digits - 2) + '1'
    count = 0
    if x != perfect_nb:
        reversed_start = x[0:int(nb_digits/2)][::-1]
        end = x[int(nb_digits/2):]
        if int(end):
            count_if_split = 0 if int(reversed_start) == 1 else 1
            count = int(reversed_start) - 1 + int(end) - 1 + count_if_split
        else:
            return str(1 + int(solve(str(int(x) - 1))))
    # now it's a perfect_nb (i.e. 1 0 0 0 ... 0 0 0 1 )
    return str(count + 2 + int(solve(str(int(perfect_nb) - 2))))


def solve2(a):  # not from me, used to get correct results to debug above code
    N = int(a)
    count = 1
    while N > 1:
        while N % 10 != 1:
            N -= 1
            count += 1
        if N == 1:
            continue
        if N == int(str(N)[::-1]):
            N -= 1
            count += 1
            continue
        s = str(N)
        l = len(s)
        if all(map(lambda x: x == '0', s[int(l / 2):-1])):
            N = int(str(N)[::-1])
            count += 1
        else:
            N -= 1
            count += 1
    return count


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + ".out", 'w')
    all_lines = [l.replace("\n", '') for l in input_file]
    for i in range(len(all_lines))[1:]:
        x = all_lines[i]
        print('\ninput :', x)
        s = str(solve(x))
        print('output:', s)
        output_file.write('Case #' + str(i) + ': ' + s + "\n")


def test():
    # cases = [[e for e in el] for el in ['1', '19', '23']]
    # cases = ['1', '19', '23']
    # cases = ['19']
    # cases = ['99']
    cases = ['10110']
    for x in cases:
        print('\ninput :', x)
        s = solve(x)
        print('output:', s)


if __name__ == '__main__':
    main()
    # test()