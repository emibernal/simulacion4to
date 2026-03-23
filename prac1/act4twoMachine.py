#Este codigo itera secuencialmente cliente por cliente
import random
import math

#Distribucion continua exponencial
def generar_interarribos():
    r = random.random()
    return -(1/3) * math.log(1-r)       #Nuestro lambda es 3 pq la tasa media es de 3 clientes

def generar_tiempos_servicios():
    r = random.random()
    return -(1/4) * math.log(1-r)       #Nuestro mu es 4 pq la tasa media es de 4 clientes

# Variables de estado y acumuladores
reloj = 0
fin_maquina_1 = 0
fin_maquina_2 = 0
total_espera_cola = 0
total_tiempo_sistema = 0
tiempo_ocupado_maquina = 0
cantidad_clientes = 0

print(f"{'Cliente':<8} | {'Llegada':<8} | {'Servicio':<8} | {'Inicio':<8} | {'Espera':<8} | {'Fin':<8}")
print("-" * 60)

while reloj < 300:
    #Llega un cliente
    intervalo = generar_interarribos()
    reloj += intervalo

    if reloj > 300: break   #Si llega despues que la maquina termina, no se hace nadd

    cantidad_clientes += 1

    #Se define el servicio que quiere
    duracion_lavado = generar_tiempos_servicios()

    primer_maquina_libre = min(fin_maquina_1, fin_maquina_2)

    # El servicio empieza cuando llega el primer cliente
    inicio_servicio = max(reloj, primer_maquina_libre)
    espera_en_cola = inicio_servicio - reloj
    fin_servicio = inicio_servicio + duracion_lavado
    tiempo_en_sistema = fin_servicio - reloj

    #Check maquina que se utilizo
    if primer_maquina_libre == fin_maquina_1:
        fin_maquina_1 = fin_servicio
    else:
        fin_maquina_2 = fin_servicio

    # Acumulo los datos para las metricas
    total_espera_cola += espera_en_cola
    total_tiempo_sistema += tiempo_en_sistema
    tiempo_ocupado_maquina += duracion_lavado

if cantidad_clientes > 0:
    #La tasa de llegada se calcula sobre el tiempo real de reloj, osea, 300 minutos
    tasa_llegada = cantidad_clientes / 300       
    #Se chequea con 600 porque se calcula la capacidad total de las maquinas                           
    utilizacion_maquina_lavadora = tiempo_ocupado_maquina / 600             
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

