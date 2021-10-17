from collections import namedtuple
InfoVent = namedtuple("InfoVent","fecha, articulo, descripcion, cantidadpza, precioventa")
Ventas = {}
contador = True

while contador:
    print("--------Menu--------")
    print("1.Agregar venta")
    print("2.Consultar venta")
    print("3.Salir")
    opcion= int(input("Seleciona una opcion: "))
    
    if opcion == 1:
        while True:
            print("Opcion de Agregar venta")
            folio = int(input("Ingresa el folio: "))
            for entrada in Ventas:
                if folio == entrada:
                    print("El folio ingresado ya existe")
                    break
            else:
                fechaVenta = input("Ingrese la fecha de venta:")
                art = input("Ingrese el articulo en venta:")
                detalles = input ("Ingrese detalles del articulo en venta:")
                cantpza = int(input("Ingrese cantidad de piezas en venta:"))
                preventa = int(input("Ingrese precio de venta:"))
                totalpago = preventa*cantpza
                infovent_en_turno = InfoVent(fechaVenta, art , detalles , cantpza , preventa )
                Ventas[folio] = infovent_en_turno
                respuesta = int(input("\nDeseas continuar agregando? 1[si], 2[no]: "))
                if respuesta != 1:
                    print("Monto total de pago:",totalpago)
                    iva= totalpago*.16
                    pagoreal= totalpago+iva
                    print("Monto total a pagar con iva incluido:",pagoreal) 
                    break
                
    elif opcion == 2:
            print("Consulta de venta")
            folio_a_buscar = int(input("Ingresa el folio de la venta a buscar: "))               
            if folio_a_buscar  in Ventas.keys():
                print(f"El folio es: {folio_a_buscar}")
                print(f"La fecha es: { Ventas[folio_a_buscar].fecha}")
                print(f"El articulo es:{ Ventas[folio_a_buscar].articulo}")
                print(f"Los detalles son: { Ventas[folio_a_buscar].descripcion}")
                print(f"La cantidad de piezas son:{ Ventas[folio_a_buscar].cantidadpza}")
                print(f"El precio de venta es:{ Ventas[folio_a_buscar].precioventa}")
            else:
                print(f"El folio a buscar: {folio_a_buscar}, No esta registrado")             
    
    elif opcion >= 3:
        print()
        print("El programa a sido finalizado")
        contador = False                
   


