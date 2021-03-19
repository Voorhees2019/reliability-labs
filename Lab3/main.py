from Lab2 import main as lab2
from math import factorial, log


def main():
    k1, k2 = 1, 1
    t = 1000
    p_system = lab2.get_uptime_probability()
    q_system = 1 - p_system
    t_system = round(-t / log(p_system))
    print(f'Загальне навантажене резервування з кратністю {k1}')
    print(f'P_system({t}): {p_system}')
    print(f'Q_system({t}): {q_system}')
    print(f'T_system: {t_system}')
    q_reversed_system = 1/(factorial(k1 + 1)) * q_system
    p_reversed_system = 1 - q_reversed_system
    t_reversed_system = round(-t / log(p_reversed_system))
    print(f'Q_reversed_system({t}): {q_reversed_system}')
    print(f'P_reversed_system({t}): {p_reversed_system}')
    print(f'T_reversed_system({t}): {t_reversed_system}')
    g_q = round(q_reversed_system / q_system, 3)
    g_p = round(p_reversed_system / p_system, 3)
    g_t = round(t_reversed_system / t_system, 3)
    print(f'G_q({t}): {g_q}')
    print(f'P_q({t}): {g_p}')
    print(f'T_q({t}): {g_t}')
    print()

    print(f'Роздільне вантажене резервування з кратністю {k2}')
    p_list = lab2.p_list
    p_reversed_list = [1 - (1 - p_list[i]) ** (k2 + 1) for i in range(len(p_list))]
    q_reversed_list = [1 - i for i in p_reversed_list]
    print(f'P_reserved_list: {p_reversed_list}')
    print(f'Q_reserved_list: {q_reversed_list}')
    p_reversed_system2 = lab2.get_uptime_probability(p_reversed_list)
    q_reversed_system2 = 1 - p_reversed_system2
    t_reversed_system2 = round(-t / log(p_reversed_system2))
    print(f'Q_reversed_system2({t}): {q_reversed_system2}')
    print(f'P_reversed_system2({t}): {p_reversed_system2}')
    print(f'T_reversed_system2({t}): {t_reversed_system2}')
    g_q2 = round(q_reversed_system2 / q_system, 3)
    g_p2 = round(p_reversed_system2 / p_system, 3)
    g_t2 = round(t_reversed_system2 / t_system, 3)
    print(f'G_q2({t}): {g_q2}')
    print(f'P_q2({t}): {g_p2}')
    print(f'T_q2({t}): {g_t2}')


if __name__ == '__main__':
    main()
