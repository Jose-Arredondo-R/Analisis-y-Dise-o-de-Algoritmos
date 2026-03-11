def analizar_big_o(codigo):

    ciclos_for = codigo.count("for")
    ciclos_while = codigo.count("while")
    ciclos = ciclos_for + ciclos_while

    if ciclos == 0:
        return "O(1)", "Tiempo constante"

    elif ciclos == 1:
        return "O(n)", "Lineal"

    elif ciclos == 2:
        return "O(n²)", "Cuadrático"

    elif "log" in codigo:
        return "O(log n)", "Logarítmico"

    elif "n log n" in codigo:
        return "O(n log n)", "Lineal logarítmico"

    elif "recursion" in codigo:
        return "O(2ⁿ)", "Exponencial"

    else:
        return "Desconocido", "No detectado"


print("Analizador de Complejidad Big-O")
print("Escribe tu código (escribe FIN para terminar):")

codigo = ""
while True:
    linea = input()
    if linea.upper() == "FIN":
        break
    codigo += linea + "\n"

big_o, nombre = analizar_big_o(codigo)

print("\nResultado del análisis:")
print("Complejidad:", big_o)
print("Nombre:", nombre)