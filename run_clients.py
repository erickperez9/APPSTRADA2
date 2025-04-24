import subprocess
import time

# Número de clientes a ejecutar
NUM_CLIENTS = 3

# Lista para guardar los procesos
processes = []

# Lanzar cada cliente en un proceso separado
for i in range(NUM_CLIENTS + 1):  # incluye el número 3
    print(f"Ejecutando cliente {i}...")
    process = subprocess.Popen(["python", "client.py", "--client_id", str(i)])
    processes.append(process)

# Esperar a que todos los procesos terminen
for process in processes:
    process.wait()

print("Todos los clientes han terminado.")
