def draw_rectangle(width, height):
    # Vérification des dimensions minimales
    if width < 2 or height < 2:
        return "Dimensions insuffisantes pour dessiner un rectangle."
    
    # Ligne du haut
    top_line = "-" * width
    
    # Lignes du milieu (côtés)
    middle_lines = []
    for _ in range(height - 2):
        middle_line = "|" + " " * (width - 2) + "|"
        middle_lines.append(middle_line)
    
    # Ligne du bas
    bottom_line = "-" * width
    
    # Assembler le rectangle
    rectangle = [top_line] + middle_lines + [bottom_line]
    return "\n".join(rectangle)

print(draw_rectangle(20,6))