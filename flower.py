#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Este script dibuja uno o más girasoles en la terminal usando caracteres ASCII
y códigos de escape ANSI para los colores.
"""

# Códigos de color ANSI
YELLOW = '\033[93m'
GREEN = '\033[92m'
RESET = '\033[0m' # Restablecer al color por defecto

def get_colored_flower():
    """
    Crea el arte de un girasol con códigos de color.
    Devuelve una lista de cadenas, donde cada cadena es una línea de la flor.
    """
    # Pétalos: Amarillo, Centro (semillas): Color por defecto, Tallo/Hojas: Verde
    line1 = YELLOW + "  .'~'.  " + RESET
    line2 = YELLOW + " (" + RESET + " OOO " + YELLOW + ") " + RESET
    line3 = YELLOW + "(" + RESET + " OOOOO " + YELLOW + ")" + RESET
    line4 = YELLOW + " (" + RESET + " OOO " + YELLOW + ") " + RESET
    line5 = YELLOW + " '.___.'  " + RESET
    line6 = GREEN + "    ||    " + RESET
    # Usando cadenas raw (r"...") para evitar errores con la barra invertida
    line7 = GREEN + r"   /||\   " + RESET
    line8 = GREEN + r"  / || \  " + RESET

    return [line1, line2, line3, line4, line5, line6, line7, line8]

def draw_flowers(number_of_flowers=1):
    """
    Dibuja un número específico de flores en una sola fila.
    """
    if number_of_flowers <= 0:
        return

    single_flower = get_colored_flower()
    # Inicializa las líneas de salida. Hay tantas líneas como en una sola flor.
    output_lines = [""] * len(single_flower)
    
    # Para cada flor que queremos dibujar
    for _ in range(number_of_flowers):
        # Para cada línea en el arte de la flor
        for i, line_part in enumerate(single_flower):
            # Añade la parte de la línea de la flor actual a la línea de salida correspondiente
            output_lines[i] += line_part + "  " # Añade espacio entre flores

    # Imprime el resultado final
    for line in output_lines:
        print(line)
    
    print() # Línea extra para un mejor espaciado

if __name__ == "__main__":
    # Dibuja 1 flor por defecto.
    # Puedes cambiar el número en la siguiente línea.
    draw_flowers(1)
