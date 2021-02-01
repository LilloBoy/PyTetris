import cv2
import numpy as np
from Tetris import Tetris
from pynput import keyboard
import time

screenW, screenH = 500, 1000
colors = (
    (0, 0, 0),
    (255, 0, 255),
    (255, 0, 0),
    (29, 255, 145),
    (0, 255, 255),
    (0, 0, 255),
    (255, 166, 45),
    (0, 255, 0)
)


def drawGrid():
    for v in range(screenW // 50):
        cv2.line(screen, (v * 50, 0), (v * 50, screenH), (255, 255, 255), 1)
    for h in range(screenH // 50):
        cv2.line(screen, (0, h * 50), (screenW, h * 50), (255, 255, 255), 1)
    return


def draw_cursor(src, x, y):
    cv2.line(src, (to_screen(x), to_screen(y)), (to_screen(x) + 50, to_screen(y)), colors[1])
    cv2.line(src, (to_screen(x), to_screen(y)), (to_screen(x), to_screen(y) + 50), colors[1])
    cv2.line(src, (to_screen(x), to_screen(y) + 50), (to_screen(x) + 50, to_screen(y) + 50), colors[1])
    cv2.line(src, (to_screen(x) + 50, to_screen(y) + 50), (to_screen(x), to_screen(y) + 50), colors[1])


def to_screen(i):
    return i * 50


def drawSquare(src, x, y, c=(255, 255, 255)):
    cv2.rectangle(src, (to_screen(x), to_screen(y)), (to_screen(x) + 50, to_screen(y) + 50), c, cv2.FILLED)
    return


def drawPiece(p, x, y, r, c):

    def p0(x, y, r, c):

        def r0():
            for a in range(4):
                drawSquare(screen, x, (y-1) + a, colors[c])
            return

        def r1():
            for a in range(4):
                drawSquare(screen, (x-2) + a, y, colors[c])
            return

        def r2():
            for a in range(4):
                drawSquare(screen, x, (y-2) + a, colors[c])
            return

        def r3():
            for a in range(4):
                drawSquare(screen, (x - 1) + a, y, colors[c])
            return

        sort_r = {
            0: r0,
            1: r1,
            2: r2,
            3: r3
        }

        sort_r[r]()

        return

    def p1(x, y, r, c):

        def r0():
            for a in range(2):
                drawSquare(screen, x-1, y- a, colors[c])
            for a in range(2):
                drawSquare(screen, x+a, y, colors[c])
            return

        def r1():
            for a in range(2):
                drawSquare(screen, x+a, y-1, colors[c])
            for a in range(2):
                drawSquare(screen, x, y+a, colors[c])
            return

        def r2():
            for a in range(2):
                drawSquare(screen, x-a, y, colors[c])
            for a in range(2):
                drawSquare(screen, x+1, y+a, colors[c])
            return

        def r3():
            for a in range(2):
                drawSquare(screen, x, y-a, colors[c])
            for a in range(2):
                drawSquare(screen, x-a, y+1, colors[c])
            return

        sort_r = {
            0: r0,
            1: r1,
            2: r2,
            3: r3
        }

        sort_r[r]()

        return

    def p2(x, y, r, c):

        def r0():
            for a in range(2):
                drawSquare(screen, x+1, (y-1) + a, colors[c])
            for a in range(2):
                drawSquare(screen, (x-1)+a, y, colors[c])
            return

        def r1():
            for a in range(2):
                drawSquare(screen, x, (y-1)+a, colors[c])
            for a in range(2):
                drawSquare(screen, x+a, y+1, colors[c])
            return

        def r2():
            for a in range(2):
                drawSquare(screen, x+a, y, colors[c])
            for a in range(2):
                drawSquare(screen, x-1, y+a, colors[c])
            return

        def r3():
            for a in range(2):
                drawSquare(screen, x, y+a, colors[c])
            for a in range(2):
                drawSquare(screen, x-a, y-1, colors[c])
            return

        sort_r = {
            0: r0,
            1: r1,
            2: r2,
            3: r3
        }

        sort_r[r]()

        return

    def p3(x, y, r, c):

        def r0():
            for a in range(2):
                drawSquare(screen, x - a, y, colors[c])
            for a in range(2):
                drawSquare(screen, x + a, y - 1, colors[c])
            return

        def r1():
            for a in range(2):
                drawSquare(screen, x, y - a, colors[c])
            for a in range(2):
                drawSquare(screen, x + 1, y + a, colors[c])
            return

        def r2():
            for a in range(2):
                drawSquare(screen, x + a, y, colors[c])
            for a in range(2):
                drawSquare(screen, x - a, y + 1, colors[c])
            return

        def r3():
            for a in range(2):
                drawSquare(screen, x, y + a, colors[c])
            for a in range(2):
                drawSquare(screen, x - 1, y - a, colors[c])
            return

        sort_r = {
            0: r0,
            1: r1,
            2: r2,
            3: r3
        }

        sort_r[r]()

        return

    def p4(x, y, r, c):

        def r0():
            for a in range(2):
                drawSquare(screen, x - a, y - 1, colors[c])
            for a in range(2):
                drawSquare(screen, x + a, y, colors[c])
            return

        def r1():
            for a in range(2):
                drawSquare(screen, x + 1, y - a, colors[c])
            for a in range(2):
                drawSquare(screen, x, y + a, colors[c])
            return

        def r2():
            for a in range(2):
                drawSquare(screen, x - a, y, colors[c])
            for a in range(2):
                drawSquare(screen, x + a, y + 1, colors[c])
            return

        def r3():
            for a in range(2):
                drawSquare(screen, x, y - a, colors[c])
            for a in range(2):
                drawSquare(screen, x - 1, y + a, colors[c])
            return

        sort_r = {
            0: r0,
            1: r1,
            2: r2,
            3: r3
        }

        sort_r[r]()

        return

    def p5(x, y, r, c):

        def r0():
            for a in range(3):
                drawSquare(screen, (x - 1) + a, y, colors[c])
            drawSquare(screen, x, y - 1, colors[c])
            return

        def r1():
            for a in range(3):
                drawSquare(screen, x, (y - 1) + a, colors[c])
            drawSquare(screen, x + 1, y, colors[c])
            return

        def r2():
            for a in range(3):
                drawSquare(screen, (x - 1) + a, y, colors[c])
            drawSquare(screen, x, y + 1, colors[c])
            return

        def r3():
            for a in range(3):
                drawSquare(screen, x, (y - 1) + a, colors[c])
            drawSquare(screen, x - 1, y, colors[c])
            return

        sort_r = {
            0: r0,
            1: r1,
            2: r2,
            3: r3
        }

        sort_r[r]()

        return

    def p6(x, y, r, c):
        for a in range(2):
            drawSquare(screen, x - a, y, colors[c])
        for a in range(2):
            drawSquare(screen, x - a, y - 1, colors[c])
        return

    draw = {
        0: p0,
        1: p1,
        2: p2,
        3: p3,
        4: p4,
        5: p5,
        6: p6
    }

    draw[p](x, y, r, c)

    return


def update_matrix(src):

    # print("y: " + str(len(tetris.matrix)))
    # print("x: " + str(len(tetris.matrix[0])))

    for y in range(len(tetris.matrix)):
        for x in range(len(tetris.matrix[0])):
            # print(tetris.fallingMatrix[y][x], end='')
            if tetris.matrix[y][x] != 0:
                drawSquare(src, x, y, colors[tetris.matrix[y][x]])
            if tetris.fallingMatrix[y][x] != 0:
                drawSquare(src, x, y, colors[tetris.fallingMatrix[y][x]])
        # print("")
    # print("")


class Input:

    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):

        if key == keyboard.Key.up:
            tetris.rotate()

        if key == keyboard.Key.left:
            tetris.move(0)

        if key == keyboard.Key.right:
            tetris.move(1)

    def on_release(self, key):
        # print('{0} released'.format(key))
        pass


tetris = Tetris()

t = 1.0

start = time.time()

input = Input()

while True:

    # tetris.clear_falling_matrix()
    screen = np.zeros((screenH, screenW, 3), np.uint8)

    drawGrid()

    # tetris.update_falling_matrix()
    update_matrix(screen)

    if t >= 1:
        stop = time.time()
        elapsed = stop-start
        # print("time: " + str(elapsed))
        x, y, r, c, p = tetris.game_cycle()
        t = 0.0
        start = time.time()
    else:
        t += 0.01

    draw_cursor(screen, x, y)

    cv2.imshow("Tetris", screen)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
