CSI = '\x1b['
RESET = f"{CSI}0m"


def draw_line(filled, color):
    print(f'{CSI}48;5;{color}m{" " * filled}{RESET}')

f = open('sequence.txt')
data = f.read().split()
f.close()
numbers_prom = [float(i) for i in data]
numbers = [i for i in numbers_prom if (5 <= i <= 10) or (-10 <= i <= -5)]

pos_prom = sum(i for i in numbers if i > 0)
neg_prom = abs(sum(i for i in numbers if i < 0))
total = pos_prom + neg_prom

pos = (pos_prom / total) * 100
neg = (neg_prom / total) * 100

print(f"Положительные: {pos:.2f}%")
draw_line(int(pos), 2)

print(f"Отрицательные: {neg:.2f}%")
draw_line(int(neg), 1)