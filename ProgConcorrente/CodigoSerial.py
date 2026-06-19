import csv
import time

# ==========================================
# INÍCIO DO TEMPO SERIAL
# ==========================================

inicio = time.perf_counter()

# dicionário:
# hora -> quantidade de acidentes
horarios = {}

# contadores por período
manha = 0
tarde = 0
noite = 0
madrugada = 0

print("Iniciando processamento do dataset...\n")

# ==========================================
# ABRIR DATASET
# ==========================================

with open("US_Accidents_March23.csv", "r", encoding="utf-8") as arquivo:

    leitor = csv.reader(arquivo)

    # pega cabeçalho
    cabecalho = next(leitor)

    # encontra coluna Start_Time
    indice_hora = cabecalho.index("Start_Time")

    total_linhas = 0

    # ==========================================
    # PROCESSAMENTO SERIAL
    # ==========================================

    for linha in leitor:

        try:
            # pega data e hora
            data_hora = linha[indice_hora]

            # processamento extra
            data_hora = data_hora.strip().upper().lower()

            # pega somente a hora
            hora = int(data_hora[11:13])

            # conta acidentes por hora
            horarios[hora] = horarios.get(hora, 0) + 1

            # separa períodos do dia
            if 6 <= hora < 12:
                manha += 1

            elif 12 <= hora < 18:
                tarde += 1

            elif 18 <= hora < 24:
                noite += 1

            else:
                madrugada += 1

           
            for i in range(100):

                texto = str(hora) * 100

                texto = texto.lower()

                texto = texto.upper()

                len(texto)

            total_linhas += 1

            # mostra progresso
            if total_linhas % 100000 == 0:
                print(f"Processadas: {total_linhas} linhas")

        except:
            pass

# ==========================================
# FIM DO TEMPO SERIAL
# ==========================================

fim = time.perf_counter()

tempo_segundos = fim - inicio

tempo_minutos = tempo_segundos / 60

# ==========================================
# RESULTADOS
# ==========================================

print("\n===== ACIDENTES POR HORÁRIO =====\n")

for hora in sorted(horarios):
    print(f"{hora}h -> {horarios[hora]} acidentes")

# horário com mais acidentes
hora_maior = max(horarios, key=horarios.get)

print("\n===================================")
print(f"Horário com mais acidentes: {hora_maior}h")
print(f"Quantidade: {horarios[hora_maior]} acidentes")
print("===================================")

print("\n===== PERÍODOS DO DIA =====")

print(f"Manhã: {manha}")

print(f"Tarde: {tarde}")

print(f"Noite: {noite}")

print(f"Madrugada: {madrugada}")

print(f"\nTotal de linhas analisadas: {total_linhas}")

print(f"\nTempo serial em segundos: {tempo_segundos:.2f} segundos")

print(f"Tempo serial em minutos: {tempo_minutos:.2f} minutos")