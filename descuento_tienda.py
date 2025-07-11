
'''
*****Proceso****

INICIO
   |
   v
[Ingresar cantidad de productos]
   |
   v
[Ingresar si es cliente frecuente]
   |
   v
[Ingresar monto total de la compra]
   |
   v
[¿Es día de promoción especial?]
   |
   v
[Inicializar descuento_total = 0]
   |
   v
[¿Cantidad de productos > 10?] --Sí--> [Sumar 10% a descuento_total]
                          |
                          No
                          v
[¿Cliente frecuente? (compras_previas > 5)] --Sí--> [Sumar 5% a descuento_total]
                          |
                          No
                          v
[¿Monto > 500?] --Sí--> [Sumar 7% a descuento_total]
                          |
                          No
                          v
[¿Día de promoción especial?] --Sí--> [Sumar 15% a descuento_total]
                          |
                          No
                          v
[¿descuento_total > 30%?] --Sí--> [descuento_total = 30%]
                          |
                          No
                          v
[Mostrar descuento_total al usuario]
   |
   v
FIN


'''

def calcular_descuento(cantidad_productos, compras_previas, total_compra, es_dia_promocion):
    descuento_total = 0

    # Condiciones principales
    if cantidad_productos > 10:
        descuento_total += 10

    if compras_previas > 5:
        descuento_total += 5

    if total_compra > 500:
        descuento_total += 7

    if es_dia_promocion:
        descuento_total += 15

    # Limitar el descuento total a 30%
    if descuento_total > 30:
        descuento_total = 30

    return descuento_total

# Ejemplo de uso:
cantidad_productos = int(input("Cantidad de productos comprados: "))
compras_previas = int(input("Cantidad de compras previas: "))
total_compra = float(input("Monto total de la compra ($): "))
es_dia_promocion = input("¿Es día de promoción especial? (s/n): ").lower() == 's'

descuento = calcular_descuento(cantidad_productos, compras_previas, total_compra, es_dia_promocion)

print(f"Descuento aplicado: {descuento}%")
