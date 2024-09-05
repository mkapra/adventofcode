tree = '#'


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


trees = 0
walker = 0

first_index = 0
second_index = 0
while walker != len(world) - 1:
    first_index += 1
    second_index += 3

    try:
        if world[first_index][second_index] == tree:
            trees += 1
    except IndexError:
        extend_map()
        if world[first_index][second_index] == tree:
            trees += 1

    walker += 1

print(f'Encountered trees: {trees}')
