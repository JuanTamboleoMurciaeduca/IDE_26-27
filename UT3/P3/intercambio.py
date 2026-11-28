libros_por_turno = [4, 11, 8, 11]
numero_turnos = len(libros_por_turno)

total_libros = 0
for libros in libros_por_turno:
    total_libros += libros
media = total_libros / numero_turnos

print("Turnos registrados:", numero_turnos)
print("Media de libros por turno:", media)
