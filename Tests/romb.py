import time

CSI = '\x1b['
ZERO = f'{CSI}1G'
ERASE = f'{CSI}2K'
RESET = f"{CSI}0m"
SIZE = 7

def animation():
    colors = range(1, 231)
    while True:
        for color in colors:
            draw_romb(SIZE, color)
            print(f"{CSI}{SIZE}A{ZERO}",
                  end='',
                  flush = True)
            time.sleep(0.1)

def draw_line(offset, filled, color):
    offset_part = f"{' ' * offset}"
    filled_part = f'{CSI}48;5;{color}m{" " * filled}{RESET}'
    line = f"{offset_part}{filled_part}"
    print(line)

def draw_romb(size, color):
    center = size // 2
    offset = center
    filled = 1

    for line in range(size):
        draw_line(offset, filled, color)
        if line < center:
            offset -= 1
            filled += 2
        else:
            offset += 1
            filled -= 2

if __name__ == '__main__':
    animation()