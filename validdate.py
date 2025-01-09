
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Calculo de fecha valida")

def es_fecha_valida(dia, mes, año):
    # Lista de días por mes (considerando febrero con 28 días)
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Verificar si el año es bisiesto
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        dias_por_mes[1] = 29  # Febrero tiene 29 días en año bisiesto

    # Validar mes
    if mes < 1 or mes > 12:
        return False

    # Validar día
    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return False

    return True

# Leer día, mes y año
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

# Comprobar si la fecha es válida
if es_fecha_valida(dia, mes, año):
    print("La fecha es válida.")
else:
    print("La fecha no es válida.")