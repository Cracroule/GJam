# FILENAME = "D-small-practice"
FILENAME = "D-large-practice"


def solve(k, c, s):
    # if s == 0:
    #     return 'IMPOSSIBLE'
    #
    # # at each check, we eliminate 2 initials inputs:
    # # one thanks to relative position
    # # one thanks to category
    #
    # if c == 0 and s < k:
    #     return 'IMPOSSIBLE'
    # if 2 * s < k:  # 2 checks each time
    #     return 'IMPOSSIBLE'
    #
    # if s < k:
    #     if c==1: return "IMPOSSIBLE"
    #     sol = list()
    #     nb_double_solution = k - s
    #     for i in range(nb_double_solution):
    #         double_solution = i * k**(c-1) + k - i - 1
    #         if double_solution >= k ** c:
    #             return "IMPOSSIBLE"
    #         sol.append(double_solution)
    #     sol += range(nb_double_solution, s)  # add remaining easy solutions
    #     print(len(sol))
    # else:
    #     # small trivial solution
    #     sol = range(k)
    #     if len(sol) > s:
    #         return "IMPOSSIBLE"
    # return ''.join([str(s + 1) + ' ' for s in sol])[:-1]
    #

    if c * s < k:
        return "IMPOSSIBLE"  # returns an empty list for impossible cases
    tiles = []
    # the list for the last tile choice is filled with copies of k
    # i is the first value of the list of the current tile choice
    for i in range(1, k + 1, c):
        p = 1
        # j is the step in the current list [i, i+1, ..., i+C-1]
        for j in range(c):
            # the min fills the last tile choice's list with copies of k
            p = (p - 1) * k + min(i + j, k)
        tiles.append(p)
    return ''.join([str(e) + ' ' for e in tiles]) if len(tiles) else "IMPOSSIBLE"


    # sol = list()
    # for i in range(int(k/2)):
    #     sol.append(k**i + k - i - 1)  # we eliminate k and k - i
    # if sol and sol[-1] >= k ** c:  # not enough expension to actually check
    #     return 'IMPOSSIBLE'

    # sol = list()
    # do_even_check = True
    # for i in range(int(k/2)):
    #     double_check_res = k**i + k - i - 1
    #     if double_check_res >= k ** c:
    #         if not i:
    #             return "IMPOSSIBLE"
    #         simple_check_res = k**(i-1) + k - (i-1) # last actual check + 1
    #         end_simple_check_res = k**i
    #         all_remaining_sol = range(simple_check_res, end_simple_check_res)
    #         print(all_remaining_sol)
    #         if len(all_remaining_sol) + len(sol) > s:
    #             return "IMPOSSIBLE"
    #         sol += all_remaining_sol
    #         do_even_check = False
    #         break
    #     sol.append(k**i + k - i - 1)  # we eliminate k and k - i
    #
    # if do_even_check and k % 2:
    #     sol.append(int(k/2))
    #
    # return ''.join([str(s + 1) + ' ' for s in sol])[:-1]


def main():
    input_file = open(FILENAME + ".in", 'r')
    output_file = open(FILENAME + ".out", 'w')
    all_lines = [l.replace("\n", '') for l in input_file]
    for i in range(len(all_lines))[1:]:
        k, c, s = [int(e) for e in all_lines[i].split(' ')]
        print('\ninput :', k, c, s)
        res = solve(k, c, s)
        print('output:', res)
        output_file.write('Case #' + str(i) + ': ' + res + "\n")


def test():
    cases = [[4, 2, 2]]
    for x in cases:
        print('\ninput :', x)
        s = solve(*x)
        print('output:', s)


if __name__ == '__main__':
    main()
    #test()
