# FILENAME = "C-small-practice"
FILENAME = "C-large-practice"
# FILENAME = "C-test-input"


def solve(c, d, v, coins):
    nb_created_coins = 0
    created_coins = list()  # not needed

    if 1 not in coins:
        coins.append(1)
        coins = sorted(coins)
        nb_created_coins += 1
        created_coins.append(1)  # not needed

    initial_coins = coins

    current_max = c
    for coin in initial_coins[1:]:
        while coin > current_max + 1:
            new_coin = current_max + 1
            current_max += new_coin * c
            nb_created_coins += 1
            created_coins.append(new_coin)  # not needed
        current_max += c * coin

    while current_max < v:
        new_coin = current_max + 1
        current_max += new_coin * c
        nb_created_coins += 1
        created_coins.append(new_coin)  # not needed

    # print('created_coins', created_coins)
    return str(nb_created_coins)


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + ".out", 'w')
    all_lines = [l.replace("\n", '') for l in input_file]
    nb_cases = int(all_lines[0])
    cur_line = 1
    for i in range(nb_cases):
        c, d, v = [int(e) for e in all_lines[cur_line].split(' ')]
        coins = [int(e) for e in all_lines[cur_line+1].split(' ')]
        print('\ninput #' + str(i+1), ':', c, d, v, coins)
        s = solve(c, d, v, coins)
        print('output:', s)
        output_file.write('Case #' + str(i+1) + ': ' + s + "\n")
        cur_line += 2


# def test():
#     cases = [[15, 1, 15], [3, 5, 14], [3, 5, 13], [3, 5, 12], [3, 5, 11], [3, 5, 10]]
#     for r, c, n in cases:
#         print('\ninput :', r, c, n)
#         s = solve(r, c, n)
#         print('output:', s)


if __name__ == '__main__':
    main()
    # test()
