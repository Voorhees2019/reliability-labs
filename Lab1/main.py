import re


def main():
    try:
        with open('data.txt', 'r') as file:
            input_lst = ''
            while line := file.readline():
                line = line.strip()
                if not line: continue
                elif line.startswith('γ'): gamma = float(re.findall(r'[+-]?[0-9]*\.?[0-9]+', line)[0])
                elif line.startswith('t1'): t1 = float(re.findall(r'\s([0-9]+)', line)[0])
                elif line.startswith('t2'): t2 = float(re.findall(r'\s([0-9]+)', line)[0])
                elif line[0].isdigit(): input_lst += line
        input_lst = input_lst.replace(' ', '')
        input_lst = [float(i) for i in input_lst.split(',')]
    except:
        print('Something went wrong. Check your input data')
        exit(1)

    k = 10
    N = len(input_lst)
    f_lst = []
    boundaries = []

    input_lst.sort()
    Tcp = sum(input_lst) / N
    h = (input_lst[-1] - input_lst[0]) / 10
    z = 0
    for i in range(1, k + 1):
        c = 0
        while z < len(input_lst) and input_lst[z] <= h * i + input_lst[0]:
            z += 1
            c += 1
        f_lst.append(c / N / h)

    p_lst = [f_i * h for f_i in f_lst]  # [round(fi*h, 2)for fi in f_lst]
    p_lst.insert(0, 1)

    for i in range(len(p_lst) - 1):
        if p_lst[i + 1] < gamma < p_lst[i]:
            boundaries.append((p_lst[i], i))
            boundaries.append((p_lst[i + 1], i + 1))
    d = (boundaries[0][0] - gamma) / (boundaries[0][0] - boundaries[1][0])
    Tgamma = boundaries[0][1] + h * d

    def get_P(t):
        tmp, f_i = 0, 0
        for i in range(k):
            if t > h * (i + 1):
                tmp += f_lst[i] * h
            else:
                tmp += f_lst[i] * (t - h * i)
                f_i = f_lst[i]
                break
        p = 1 - tmp
        return p, f_i

    P = get_P(t1)[0]
    P2, f_i = get_P(t2)
    try:
        Lambda = f_i / P2
    except ZeroDivisionError:
        print('Something went wrong. Check your input data')
        exit(1)

    print(f'Середній наробіток до відмови Tср: {Tcp}')
    print(f'γ-відсотковий наробіток на відмову при γ = {gamma}. Tγ = {Tgamma=}')
    print(f'Ймовірність безвідмовної роботи на час {t1} годин = {P}')
    print(f'Інтенсивність відмов на час {t2} годин = {Lambda}')


if __name__ == '__main__':
    main()
