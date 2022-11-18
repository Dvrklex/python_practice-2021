#Calcular el sueldo a cobrar teniendo en cuenta que  los empleados que no han faltado y 
#  cuya antigüedad es superior a 5 años, tienen un adicional del 30% sobre el sueldo básico ($47.000). 
# Pedir la cantidad de días no trabajados y año de ingreso en la empresa.

adicional_al_sueldo = 47000 * 1.30
sueldo_final = int(adicional_al_sueldo)
dias_no_trabajados = int(input("Ingrese la cantidad de dias no trabajados: \r\n"))
año_de_ingreso = int(input("Ingrese año de ingreso a la empresa: \r\n"))
fundacion_empresa = 2015
antiguedad = año_de_ingreso - 2015
if dias_no_trabajados == 0 and antiguedad > 5:
    print('Debido a su antiguedad, su sueldo ahora es de $',sueldo_final)
else:
    print('Para obtener un aumento, debe tener una antiguedad de 5 años minimo, y no haber faltado ningun dia')