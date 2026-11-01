CSI = '\x1b['
RESET = f'{CSI}0m'
FLAG_WIDTH = 40
FLAG_HEIGHT = 11
WHITE = 15
BLUE = 4


def flag():
    for y in range(FLAG_HEIGHT):
        line = ''
        for x in range(FLAG_WIDTH):
            vert = 10 <= x < 16
            horz = 4 <= y < 7
            if vert or horz:
                line += f'{CSI}48;5;{BLUE}m {RESET}'
            else:
                line += f'{CSI}48;5;{WHITE}m {RESET}'
        print(line)


if __name__ == '__main__':
    flag()