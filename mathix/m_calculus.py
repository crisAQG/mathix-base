def limit(f, x, dx=1e-6):
    return (f(x + dx) + f(x - dx)) / 2


def derivative(f, x, dx=1e-6):
    return (f(x + dx) - f(x - dx)) / (2 * dx)


def integral(f, a, b, n=1000):
    width = (b - a) / n
    total = 0
    for i in range(n):
        total += f(a + i * width + width / 2)
    return total * width


def symbolic_derivative(expr, var="x"):
    # Soporta derivadas simples de polinomios del tipo "ax^n"
    terms = expr.replace('-', '+-').split('+')
    result = []
    for term in terms:
        term = term.strip()
        if var not in term:
            continue
        coef, power = 1, 1
        if '^' in term:
            parts = term.split(var + '^')
            coef = float(parts[0].replace(var, '').strip()) if parts[0].strip() not in ('', '+', '-') else 1.0 if parts[
                                                                                                                      0] in (
                                                                                                                      '',
                                                                                                                      '+') else -1.0
            power = int(parts[1])
        elif var in term:
            coef = float(term.replace(var, '').strip()) if term.replace(var, '').strip() not in ('', '+',
                                                                                                 '-') else 1.0 if term.startswith(
                var) or term.startswith('+') else -1.0
            power = 1
        new_coef = coef * power
        new_power = power - 1
        if new_power == 0:
            result.append(f"{new_coef}")
        elif new_power == 1:
            result.append(f"{new_coef}{var}")
        else:
            result.append(f"{new_coef}{var}^{new_power}")
    return " + ".join(result) if result else "0"


def symbolic_integral(expr, var="x"):
    # Soporta integrales simples de polinomios del tipo "ax^n"
    terms = expr.replace('-', '+-').split('+')
    result = []
    for term in terms:
        term = term.strip()
        if var not in term:
            try:
                val = float(term)
                result.append(f"{val}{var}")
            except Exception as e:
                print(f"Se produjo una excepción en integrales por simbologia: {e}")
                continue
            continue
        coef, power = 1, 1
        if '^' in term:
            parts = term.split(var + '^')
            coef = float(parts[0].replace(var, '').strip()) if parts[0].strip() not in ('', '+', '-') else 1.0 if parts[
                                                                                                                      0] in (
                                                                                                                      '',
                                                                                                            '+') else -1.0
            power = int(parts[1])
        elif var in term:
            coef = float(term.replace(var, '').strip()) if term.replace(var, '').strip() not in ('', '+',
                                                                                                 '-') else 1.0 if term.startswith(
                var) or term.startswith('+') else -1.0
            power = 1
        new_power = power + 1
        new_coef = coef / new_power
        result.append(f"{new_coef}{var}^{new_power}")
    return " + ".join(result) + " + C"
