import os
import time


CSI = '\x1b['
ZERO = f'{CSI}1G'
ERASE = f'{CSI}2K'
RESET = f'{CSI}0m'
FLAG_WIDTH = 40
FLAG_HEIGHT = 11


def clear_console():
    os.system('cls')
    print(ZERO,
          end='',
          flush = True)
    
def flag(color1, color2):
    for y in range(FLAG_HEIGHT):
        line = ''
        for x in range(FLAG_WIDTH):
            vert = 10 <= x < 16
            horz = 4 <= y < 7
            if vert or horz:
                line += f'{CSI}48;5;{color2}m {RESET}'
            else:
                line += f'{CSI}48;5;{color1}m {RESET}'
        print(line)

def animation():
    clear_console()
    colors = range(1, 231)
    while True:
        for color1 in colors:
            flag(color1, 4)
            print(f"{CSI}{FLAG_HEIGHT}A{ZERO}",
            end='',
            flush = True)
            time.sleep(0.1)
            
if __name__ == '__main__':
    animation()