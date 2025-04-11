N = int(input())
move = str(input())
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
H, W, order = 0, 0, 0
up_down, left_right, route = [0], [0], []
for m in move:
    if m == 'L':
        order = (order + 1) % 4
    elif m == 'R':
        order = 3 if order-1 < 0 else order-1
    else:
        H, W = H + dxy[order][0], W + dxy[order][1]
        up_down.append(H)
        left_right.append(W)
        route.append((H, W))
ud_set, lr_set = sorted(set(up_down)), sorted(set(left_right))
height = len(ud_set)
width = len(lr_set)
sx, sy = ud_set.index(0), lr_set.index(0)
maze = [['#']*width for _ in range(height)]
maze[sx][sy] = '.'
for x, y in route:
    maze[sx + x][sy + y] = '.'
for m in maze:
    print(''.join(m))
