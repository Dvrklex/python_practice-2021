#Preguntar nombre, carrera en la que se inscribe y ciudad donde vive un ingresante al Instituto.
#Los estudiantes de la carrera de Electromecánica y que no viven en Río Cuarto tendrán un 15% de descuento
#en la cuota que es de $4500. Mostrar nombre, ciudad, carrera y monto final de la cuota.

Lugar_de_la_institucion = ('Rio Cuarto')
carreras = ['Desarrollo de software', 'Electromecanica', 'Turismo y Hoteleria']
nombre = input('Ingrese su nombre y apellido \r\n')
cuidad_donde_vive = input('Ingrese el lugar donde vide: \r\n')
carrera_inscripto = input('Ingrese a que carrera se inscribio: \r\n')
descuento = 4500 * 0.15
total_final = int(descuento) 
if cuidad_donde_vive != Lugar_de_la_institucion and carrera_inscripto == carreras[1]:
     print('Gracias por inscribirse a Electromecanica, usted tiene acceso de un 15% de descuento en la cuota mensual, su total es $',total_final)
elif carreras [0]:
    print('Gracias por inscribirse en nuestra carrera de Desarrollo de Software, su total por mes es $4500,SOMOS LOS MEJORES') 
else:
    print('Gracias por inscribirse a nuestra carrera de Turismo y Hoteleria, su total por es $4500')

