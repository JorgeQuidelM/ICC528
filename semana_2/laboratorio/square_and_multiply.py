from semana_2.laboratorio.cambio_base import cambio_base_euclides


def fast_modular_exp(base, exp, mod):
    exp_bin = cambio_base_euclides(exp, 2)
    result = 1
    for bit in exp_bin:
        result **= 2
        if bit == '1':
            result *= base
        result %= mod
    return result


def test():
    base = 500
    exp = 13
    mod = 17
    print(f'{base}^{exp}(mod {mod}) = {fast_modular_exp(base, exp, mod)}')
    base = 23
    exp = 373
    mod = 747
    print(f'{base}^{exp}(mod {mod}) = {fast_modular_exp(base, exp, mod)}')
    base = 240
    exp = 262
    mod = 14
    print(f'{base}^{exp}(mod {mod}) = {fast_modular_exp(base, exp, mod)}')
    base = 7
    exp = 9999
    mod = 1000
    print(f'{base}^{exp}(mod {mod}) = {fast_modular_exp(base, exp, mod)}')


if __name__ == '__main__':
    test()
