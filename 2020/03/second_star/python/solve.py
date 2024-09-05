def read_world():
    world = []
    with open('../../map.txt') as fh:
        line = fh.readline()
        while (line):
            world.append([char for char in line.strip()])
            line = fh.readline()

    return world


world = read_world()
save_map = read_world()


def extend_map():
    for index, line in enumerate(world):
        for element in save_map[index]:
            line.append(element)


def iterate_map(right, down):
    tree = '#'
    trees = 0

    first_index = 0
    second_index = 0

    while first_index < len(world) - 1:
        first_index += down
        second_index += right

        try:
            if world[first_index][second_index] == tree:
                trees += 1
        except IndexError:
            extend_map()
            if world[first_index][second_index] == tree:
                trees += 1

    return trees


# Right 1, down 1.
t1 = iterate_map(1, 1)
# Right 3, down 1. (This is the slope you already checked.)
t2 = iterate_map(3, 1)
# Right 5, down 1.
t3 = iterate_map(5, 1)
# Right 7, down 1.
t4 = iterate_map(7, 1)
# Right 1, down 2.
t5 = iterate_map(1, 2)

print(f"Trees: {t1 * t2 * t3 * t4 * t5}")
