from direction import Direction


def dfs(robot, x=0, y=0, move_to=0, visited=set()):
    robot.clean()
    visited.add((x, y))

    # down
    movement = move_to
    coord_x, coord_y = Direction.COORDINATES[movement]
    _x = x + coord_x
    _y = y + coord_y

    if (_x, _y) not in visited and robot.move():
        dfs(robot, _x, _y, movement, visited)
        robot.turn_right()
    else:
        robot.turn_left()

    # right
    movement = (move_to + 1) % 4
    coord_x, coord_y = Direction.COORDINATES[movement]
    _x = x + coord_x
    _y = y + coord_y

    if (_x, _y) not in visited and robot.move():
        dfs(robot, _x, _y, movement, visited)
    else:
        robot.turn_left(2)

    # left
    movement = (move_to + 3) % 4
    coord_x, coord_y = Direction.COORDINATES[movement]
    _x = x + coord_x
    _y = y + coord_y

    if (_x, _y) not in visited and robot.move():
        dfs(robot, _x, _y, movement, visited)
        robot.turn_left()
    else:
        robot.turn_right()

    # up
    movement = (move_to + 2) % 4
    coord_x, coord_y = Direction.COORDINATES[movement]
    _x = x + coord_x
    _y = y + coord_y

    if (_x, _y) not in visited and robot.move():
        dfs(robot, _x, _y, movement, visited)
        robot.turn_right(2)

    # move robot when the recursion is back
    robot.move()
