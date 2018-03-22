# FILENAME = "B-small-practice"
FILENAME = "B-large-practice"
# FILENAME = "B-test-input"


def solve(s, keyboard, target_word):
    k = len(keyboard)
    l = len(target_word)

    # word probability computation
    p = 1
    all_letters_appear = True
    for letter in target_word:
        letter_occurences = keyboard.count(letter)
        p *= letter_occurences / k
        if not letter_occurences:
            all_letters_appear = False

    # total prob
    # total_prob = 0
    # for i in range(l-1):
    #     total_prob += (1-p)**i * p
    # for i in range(2*(l-1), s):
    #     total_prob += (1-p)**(l-1) * p

    total_prob = max(s - l + 1, 0) * p

    overlap = 0
    for i in range(1, len(target_word)):
        if target_word[i:] == target_word[0:len(target_word) - i]:
            overlap = len(target_word) - i
            break

    max_success = 1.0 + int((s-l)/(l-overlap)) if all_letters_appear else 0

    return str(float(round(max_success - total_prob, 10)))


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + ".out", 'w')
    all_lines = [l.replace("\n", '') for l in input_file]
    nb_cases = int(all_lines[0])
    cur_line = 1
    for i in range(nb_cases):
        k, l, s = [int(e) for e in all_lines[cur_line].split(' ')]
        keyboard = all_lines[cur_line + 1]
        target_word = all_lines[cur_line + 2]
        print('\ninput #' + str(i+1), ':', k, l, s, keyboard, target_word)
        s = solve(s, keyboard, target_word)
        print('output:', s)
        output_file.write('Case #' + str(i+1) + ': ' + s + "\n")
        cur_line += 3


# def test():
#     cases = [[15, 1, 15], [3, 5, 14], [3, 5, 13], [3, 5, 12], [3, 5, 11], [3, 5, 10]]
#     for r, c, n in cases:
#         print('\ninput :', r, c, n)
#         s = solve(r, c, n)
#         print('output:', s)


if __name__ == '__main__':
    main()
    # test()
