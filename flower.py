#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Este script dibuja una simple flor en la terminal usando caracteres ASCII
y códigos de escape ANSI para los colores.
"""

# Códigos de color ANSI
YELLOW = '\033[93m'
GREEN = '\033[92m'
RESET = '\033[0m' # Restablecer al color por defecto

def draw_flower():
    """Imprime una flor amarilla con un tallo verde en la terminal."""
    
    flower_art = [
        "    _    ",
        "   (_)   ",
        "  (_o_)  ",
        "   (_)   ",
        "    |    ",
        r"   / \   "  # Corregido usando una cadena raw r"..."
    ]

    # Imprimir la flor con colores
    print(YELLOW + flower_art[0] + RESET)
    print(YELLOW + flower_art[1] + RESET)
    print(YELLOW + flower_art[2] + RESET)
    print(YELLOW + flower_art[3] + RESET)
    print(GREEN + flower_art[4] + RESET)
    print(GREEN + flower_art[5] + RESET)
    print() # Línea extra para un mejor espaciado

if __name__ == "__main__":
    draw_flower()