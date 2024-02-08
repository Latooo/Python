import json
from operator import itemgetter

# Cargar datos desde el archivo JSON
with open('data.json') as f:
    data = json.load(f)

# 1. Listado de todos los pedidos ordenados por fecha
pedidosFecha = sorted(data['ventas']['pedidos'], key=itemgetter('fecha'), reverse=True)
print("1. Ordenar por fecha:")
print(pedidosFecha)

# 2. Datos de los dos pedidos de mayor valor
pedidosMayorValor = sorted(data['ventas']['pedidos'], key=itemgetter('total'), reverse=True)[:2]
print("\n2. Los dos pedidos con mayor valor")
print(pedidosMayorValor)

# 3. Identificadores de clientes que han realizado algún pedido
clientesPedidos = list(set(pedido['id_cliente'] for pedido in data['ventas']['pedidos']))
print("\n3. Clientes que han hecho pedidos:")
print(clientesPedidos)

# 4. Pedidos en 2017 con cantidad total superior a 500€
pedidos2017 = [pedido for pedido in data['ventas']['pedidos'] if
                         pedido['fecha'].startswith('2017') and pedido['total'] > 500]
print("\n4. Pedidos de 2017 con total mayor a 500:")
print(pedidos2017)

# 5. Comerciales con comisión entre 0.05 y 0.11


# 6. Valor de la comisión más alta


# 7. Clientes de Sevilla ordenados alfabéticamente
clientesSevilla = sorted([{'id': cliente['id'], 'nombre': cliente['nombre'], 'apellido1': cliente['apellido1']} for cliente in
     data['ventas']['clientes'] if cliente['ciudad'] == 'Sevilla'],
    key=itemgetter('apellido1', 'nombre'))
print("\n7. Clientes de sevilla ordenados:")
print(clientesSevilla)

# 8. Nombres de clientes que empiezan por A y terminan por N, y nombres que empiezan por P
nombresANP = sorted(
    [cliente['nombre'] for cliente in data['ventas']['clientes'] if
     (cliente['nombre'].startswith('A') and cliente['nombre'].endswith('n')) or
     cliente['nombre'].startswith('P')])
print("\n8. Nombres iniciados en A y terminados en N, y nombres iniciados en P:")
print(nombresANP)

# 9. Nombres de clientes que empiezan por A
nombresA = sorted([cliente['nombre'] for cliente in data['ventas']['clientes'] if cliente['nombre'].startswith('A')])
print("\n9. Clientes que empiezan por A:")
print(nombresA)

# 10. Nombres de comerciales que tienen como apellido "Ruiz" (sin duplicados)
ruiz = set([comercial['nombre'] for comercial in data['ventas']['comerciales'] if
                      'Ruiz' in comercial['apellido1']])
print("\n10. Comerciales con apellido Ruiz:")
print(ruiz)
