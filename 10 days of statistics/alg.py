def find_combinations(n, start=1, current_combination=[]):
    if n == 0:
        # Si la suma es igual a 0, se ha encontrado una combinación
        print(current_combination)
        

    # Empezamos desde el valor 'start' para evitar repeticiones
    for i in range(start, n + 1):
        if i <= n:
            # Incluimos el número i y buscamos combinaciones para el resto
            find_combinations(n - i, i, current_combination + [i])

# Llamar la función con 9
find_combinations(9)
