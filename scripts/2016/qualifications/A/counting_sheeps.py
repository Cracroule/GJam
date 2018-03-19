# FILENAME = "A-small-practice"
FILENAME = "A-large-practice"


def solve(x):
    if x == 0:
        return 'INSOMNIA'
    digits = {str(i) for i in range(10)}
    current_value = x
    for i in range(100)[1:]:
        cur_value_digits = {i for i in str(current_value)}
        digits -= cur_value_digits
        if not len(digits):
            return str(current_value)
        current_value += x
    return 'INSOMNIA'


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + ".out", 'w')
    all_lines = [l.replace("\n", '') for l in input_file]
    for i in range(len(all_lines))[1:]:
        x = int(all_lines[i])
        print('\ninput :', x)
        s = solve(x)
        print('output:', s)
        output_file.write('Case #' + str(i) + ': ' + s + "\n")


def test():
    cases = [i for i in [0, 1, 2, 11, 1692]]
    for x in cases:
        print('\ninput :', x)
        s = solve(x)
        print('output:', s)


if __name__ == '__main__':
    main()
    #test()
