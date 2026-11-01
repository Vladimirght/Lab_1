import time

CSI = '\x1b['
ZERO = f'{CSI}1G'
ERASE = f'{CSI}2K'


def draw_progress(width, num_tasks):
    for task in range(num_tasks):
        for filled in range(width + 1):
            bar = f'{'#' * filled}{'-' * (width - filled)}'
            print(f'{ZERO}{ERASE}{task}: {bar}',
                  end='',
                  flush = True)
            time.sleep(0.1)


if __name__ == '__main__':
    draw_progress(30, 3)