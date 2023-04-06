def part1():
    with open("data.in", 'r') as f:
        forest = tuple([(int(tree), False) for tree in trees.strip()] for trees in f.readlines())

        visible_trees = 0

        for tree_row in forest:
            max_left_tree_height = -1
            max_right_tree_height = -1

            for i in range(len(tree_row)):
                left_tree, left_visited = tree_row[i]
                right_tree, right_visited = tree_row[-i - 1]

                if left_tree > max_left_tree_height:
                    max_left_tree_height = left_tree

                    if not left_visited:
                        visible_trees += 1
                        tree_row[i] = (left_tree, True)

                if right_tree > max_right_tree_height:
                    max_right_tree_height = right_tree

                    if not right_visited:
                        visible_trees += 1
                        tree_row[-i - 1] = (right_tree, True)

        for tree_col in ([tree_row[i] for tree_row in forest] for i in range(len(forest))):
            max_left_tree_height = -1
            max_right_tree_height = -1

            for i in range(len(tree_col)):
                left_tree, left_visited = tree_col[i]
                right_tree, right_visited = tree_col[-i - 1]

                if left_tree > max_left_tree_height:
                    max_left_tree_height = left_tree

                    if not left_visited:
                        visible_trees += 1
                        tree_col[i] = (left_tree, True)

                if right_tree > max_right_tree_height:
                    max_right_tree_height = right_tree

                    if not right_visited:
                        visible_trees += 1
                        tree_col[-i - 1] = (right_tree, True)

    return visible_trees


def part2():
    with open("data.in", 'r') as f:
        forest = tuple(trees.strip() for trees in f.readlines())

        result = 0

        for row in range(len(forest)):
            for col in range(len(forest[0])):
                tree = forest[row][col]

                view_up = view_down = view_right = view_left = 0
                blocked_up = blocked_down = blocked_right = blocked_left = False

                for up, down in map(lambda i: (row - i, row + i), range(1, max(row + 1, len(forest) - row))):
                    if blocked_up and blocked_down:
                        break

                    if not blocked_up and up >= 0:
                        if forest[up][col] >= tree:
                            blocked_up = True

                        view_up += 1

                    if not blocked_down and down < len(forest):
                        if forest[down][col] >= tree:
                            blocked_down = True

                        view_down += 1

                for left, right in map(lambda i: (col - i, col + i), range(1, max(col + 1, len(forest[0]) - col))):
                    if blocked_left and blocked_right:
                        break

                    if not blocked_left and left >= 0:
                        if forest[row][left] >= tree:
                            blocked_left = True

                        view_right += 1

                    if not blocked_right and right < len(forest[0]):
                        if forest[row][right] >= tree:
                            blocked_right = True

                        view_left += 1

                result = max(result, view_up * view_down * view_right * view_left)

    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
