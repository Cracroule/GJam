
FILENAME = "C-small-practice"
# FILENAME = "C-large-practice"


t = {'1': 1, 'i': 2, 'j': 3, 'k': 4}
op_tab = [[1, 2, 3, 4], [2, -1, 4, -3], [3, -4, -1, 2], [4, 3, -2, -1]]
# 1 = 1
# 2 = i
# 3 = j
# 4 = k


def op(a, b):
    sign_a = -1 if a < 0 else 1
    sign_b = -1 if b < 0 else 1
    return sign_a * sign_b * op_tab[abs(a)-1][abs(b)-1]


def convert_seq(seq):
    if not len(seq):
        return 1
    if len(seq) == 1:
        return seq[0]
    cur_seq = seq[0]
    for i in range(len(seq))[1:]:
        cur_seq = op(cur_seq, seq[i])
    return cur_seq


def find_el(seq, el, reversed=False):
    if len(seq) == 1:
        return None, None
    cur_seq = seq[0]
    if cur_seq == el: return 0, 0
    for i in range(len(seq))[1:]:
        cur_seq = op(cur_seq, seq[i]) if not reversed else op(seq[i], cur_seq)
        if cur_seq == el: return i, 0
    for i in range(len(seq)):
        cur_seq = op(cur_seq, seq[i]) if not reversed else op(seq[i], cur_seq)
        if cur_seq == el: return i, 1
    return None, None


def solve(seq, x):
    len_seq = len(seq)
    i, x_i = find_el(seq, t['i'])
    k, x_k = find_el(seq[::-1], t['k'], reversed=True)
    if i is None or k is None: return 'NO'
    t_x = x_i + x_k + 2 if i + k + 2 >= len_seq else x_i + x_k + 1
    if t_x > x: return 'NO'

    if x == t_x:
        remaining_seq = convert_seq(seq[i+1: len_seq-k-1])
        return 'YES' if remaining_seq == t['j'] else 'NO'

    remaining_x = x - t_x

    remaining_seq_i = convert_seq(seq[i+1:])
    remaining_seq_k = convert_seq(seq[:len_seq - k - 1])
    seq_j = remaining_seq_i
    if remaining_x > 1:
        converted_seq = convert_seq(seq)
        seq_j = op(seq_j, converted_seq)
        for i in range(remaining_x-2 % 4):
            seq_j = op(seq_j, converted_seq)

        # seq_j = op(seq_j, converted_seq)
        # if remaining_x % 2:
        #     seq_j = op(seq_j, converted_seq)
    seq_j = op(seq_j, remaining_seq_k)
    return 'YES' if seq_j == t['j'] else 'NO'


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + ".out", 'w')
    all_lines = [l.replace("\n", '') for l in input_file]
    for i in range(len(all_lines))[1:]:
        if not i % 2:
            seq = [e for e in all_lines[i]]
            t_seq = [t[e] for e in all_lines[i]]
        else:
            l, x = [int(e) for e in all_lines[i].split(' ')]
            continue
        print('\ninput :', x, seq)
        s = solve(t_seq, x)
        print('output:', s)
        j = int(i/2)
        output_file.write('Case #' + str(j) + ': ' + s + "\n")


def test():
    # cases = [i for i in [[1, ['i', 'k']], [1, ['i', 'j', 'k']], [1, ['k', 'j', 'i']], [6, ['j', 'i']], [10000, ['i']]]]
    # cases = [[5, ['i', 'k', 'i', 'i', 'j']], [1, ['i', 'k', 'i', 'i', 'j']], [2, ['i', 'k', 'i', 'i', 'j']], [4, ['i', 'k', 'i', 'i', 'j']]]
    cases = [[3462, ['i', 'k']], [3461, ['i', 'k']], [3460, ['i', 'k']]]
    for x, seq in cases:
        tseq = [t[e] for e in seq]
        print('\ninput :', x, seq)
        s = solve(tseq, x)
        print('output:', s)


if __name__ == '__main__':
    # main()
    test()
