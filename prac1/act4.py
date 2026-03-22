import random

#Tabla de llegadas
tiempos_llegada = [5, 10, 15, 20, 25, 30, 35, 40]
prob_llegada_acum = [0.05, 0.10, 0.20, 0.30, 0.60, 0.80, 0.95, 1.00]

#Tabla de servicios
tiempos_servicios = [10, 20, 30, 40]
prob_servicios_acum = [0.15, 0.40, 0.80, 1.00]

#Funcion random que toma un valor aleatorio y devuelve un valor de la tabla
def obtener_valor(lista_valores, lista_acumulada):
    r = random.random() #Funcion que genera un numero entre 0 y 1
    for i in range(len(lista_acumulada)):
        if r <= lista_acumulada[i]:
            return lista_valores[i]
    return lista_valores[-1]

# Variables de estado y acumuladores
reloj = 0
tiempo_fin_lavado_anterior = 0
total_espera_cola = 0
total_tiempo_sistema = 0
tiempo_ocupado_maquina = 0
cantidad_clientes = 0

print(f"{'Cliente':<8} | {'Llegada':<8} | {'Servicio':<8} | {'Inicio':<8} | {'Espera':<8} | {'Fin':<8}")
print("-" * 60)

while reloj < 300:
    #Llega un cliente
    intervalo = obtener_valor(tiempos_llegada, prob_llegada_acum)
    reloj += intervalo

    if reloj > 300: break   #Si llega despues que la maquina termina, no se hace nadd

    cantidad_clientes += 1

    #Se define el servicio que quiere
    duracion_lavado = obtener_valor(tiempos_servicios, prob_servicios_acum)

    # El servicio empieza cuando llega el primer cliente
    inicio_servicio = max(reloj, tiempo_fin_lavado_anterior)
    espera_en_cola = inicio_servicio - reloj
    fin_servicio = inicio_servicio + duracion_lavado
    tiempo_en_sistema = fin_servicio - reloj

    # Acumulo los datos para las metricas
    total_espera_cola += espera_en_cola
    total_tiempo_sistema += tiempo_en_sistema
    tiempo_ocupado_maquina += duracion_lavado
    tiempo_fin_lavado_anterior = fin_servicio

    print(f"{cantidad_clientes:<8} | {reloj:<8} | {duracion_lavado:<8} | {inicio_servicio:<8} | {espera_en_cola:<8} | {fin_servicio:<8}")

if cantidad_clientes > 0:
    tasa_llegada = cantidad_clientes / 300 
    utilizacion_maquina_lavadora = tiempo_ocupado_maquina / 300
    tiempo_promedio_cliente_en_sistema = total_tiempo_sistema / cantidad_clientes
    tiempo_promedio_cliente_en_cola = total_espera_cola / cantidad_clientes
    numero_promedio_clientes_en_comercio = tasa_llegada * tiempo_promedio_cliente_en_sistema
    numero_promedio_clientes_en_cola = tasa_llegada * tiempo_promedio_cliente_en_cola

    print("\n" + "="*40)
    print("--- RESULTADOS FINALES ---")
    print("="*40)
    print(f"i.   Utilización de la máquina: {utilizacion_maquina_lavadora*100:.2f}%")
    print(f"ii.  Tiempo promedio en el comercio: {tiempo_promedio_cliente_en_sistema:.2f} min")
    print(f"iii. Tiempo promedio en cola: {tiempo_promedio_cliente_en_cola:.2f} min")
    print(f"iv.  Número promedio de clientes en el comercio: {numero_promedio_clientes_en_comercio:.2f}")
    print(f"v.   Número promedio de clientes en la cola: {numero_promedio_clientes_en_cola:.2f}")

