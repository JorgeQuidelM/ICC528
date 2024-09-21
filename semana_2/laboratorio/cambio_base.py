def cambio_base(n, base=10, to=10):
    n_base10 = cambio_a_base10(n, base)
    n_nueva_base = cambio_base_euclides(n_base10, to)
    return n_nueva_base


def cambio_a_base10(n, base):
    n_str = str(n)
    n_base10 = 0

    # Convertir de la base dada a base 10
    for i, digit in enumerate(n_str):
        if '0' <= digit <= '9':
            value = ord(digit) - ord('0')  # Convertir carácter a entero
        elif 'A' <= digit <= 'Z':
            value = ord(digit) - ord('A') + 10  # Convertir A-Z a 10-35
        else:
            return None  # Retornar None si hay un dígito inválido

        if value >= base:
            return None

        n_base10 += value * (base ** (len(n_str) - i - 1))

    return n_base10


def cambio_base_euclides(n, base):
    ans = ''
    handle_digit = lambda i: str(i) if i < 10 else chr(i + 55)
    while n > 0:
        r = n % base
        ans += handle_digit(r)
        n //= base
    return ans[::-1]


def test():
    print(cambio_base_euclides(95, 2))
    print(cambio_base_euclides(95, 16))
    print(cambio_base_euclides(95, 8))

    print("-------------------------------------------")

    print(cambio_a_base10('FF', 16))
    print(cambio_a_base10('1100100', 2))
    print(cambio_a_base10('A', 36))

    print("-------------------------------------------")

    print(cambio_base(255, base=10, to=16))  # Salida: FF
    print(cambio_base('1A3', base=16, to=10))  # Salida: 419
    print(cambio_base(100, base=10, to=2))  # Salida: 1100100
    print(cambio_base(10, base=10, to=36))  # Salida: A


if __name__ == '__main__':
    test()

