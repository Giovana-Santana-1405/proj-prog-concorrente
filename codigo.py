import csv
import time

# =========================
# INÍCIO DO TEMPO SERIAL
# =========================

inicio = time.perf_counter()

# =========================
# CONTADOR DE HORÁRIOS
# =========================

horarios = {}

# =========================
# ABRIR O CSV
# =========================

with open("US_Accidents_March23.csv", "r", encoding="utf-8") as arquivo:

    leitor = csv.DictReader(arquivo)

    total_linhas = 0

    # processamento serial
    for linha in leitor:

        # pega o horário
        data_hora = linha["Start_Time"]

        # pega somente a hora
        hora = data_hora[11:13]

        # conta acidentes
        if hora in horarios:
            horarios[hora] += 1
        else:
            horarios[hora] = 1

        total_linhas += 1

        # limite para não travar
        if total_linhas == 100000:
            break

# =========================
# FIM DO TEMPO SERIAL
# =========================

fim = time.perf_counter()

tempo_total = fim - inicio

# =========================
# RESULTADO
# =========================

print("\nAcidentes por horário:\n")

for hora in sorted(horarios):
    print(f"{hora}h -> {horarios[hora]} acidentes")

print(f"\nTotal de linhas analisadas: {total_linhas}")

print(f"Tempo serial: {tempo_total:.4f} segundos")