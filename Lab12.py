CSI = '\x1b['
RESET = f'{CSI}0m'
COLOR = 4


def draw_pattern():
    print(f"  {CSI}48;5;4m   {RESET}   {CSI}48;5;4m   {RESET}")

    print(f" {CSI}48;5;4m     {RESET} {CSI}48;5;4m     {RESET}")
    print(f" {CSI}48;5;4m     {RESET} {CSI}48;5;4m     {RESET}")
    
    print(f"  {CSI}48;5;4m   {RESET}   {CSI}48;5;4m   {RESET}")

def draw_pattern_repeat(time):
    for i in range(time):
        draw_pattern()


if __name__ == '__main__':
    draw_pattern_repeat(10)