import csv
import os
import time
from concurrent.futures import ProcessPoolExecutor

# ==========================================
# FUNÇÃO DE PROCESSAMENTO (RODA EM CADA PROCESSO)
# ==========================================
def processar_fatia_arquivo(nome_arquivo, inicio_byte, fim_byte, indice_hora):
    horarios_local = {}
    manha = tarde = noite = madrugada = total_linhas = 0
    pid = os.getpid()  # Pega o ID do processo atual para o print

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        if inicio_byte > 0:
            arquivo.seek(inicio_byte)
            arquivo.readline()

        while arquivo.tell() < fim_byte:
            linha_texto = arquivo.readline()
            if not linha_texto:
                break 

            leitor = csv.reader([linha_texto])
            try:
                linha = next(leitor)
                if not linha:
                    continue
                
                data_hora = linha[indice_hora]
                data_hora = data_hora.strip().lower()
                hora = int(data_hora[11:13])

                horarios_local[hora] = horarios_local.get(hora, 0) + 1

                if 6 <= hora < 12:
                    manha += 1
                elif 12 <= hora < 18:
                    tarde += 1
                elif 18 <= hora < 24:
                    noite += 1
                else:
                    madrugada += 1

                # Carga computacional extra
                for i in range(100):
                    texto = str(hora) * 100
                    texto = texto.lower().upper()
                    len(texto)

                total_linhas += 1

                # ADICIONADO: Print de progresso a cada 100.000 linhas neste processo
                if total_linhas % 100000 == 0:
                    print(f"[Processo {pid}] Linhas processadas: {total_linhas}")

            except Exception:
                pass

    # Print final de cada núcleo individualmente
    print(f"-> [Processo {pid}] Concluído! Total final deste núcleo: {total_linhas}")
    return horarios_local, manha, tarde, noite, madrugada, total_linhas


# ==========================================
# FUNÇÃO PRINCIPAL (GERENCIADORA)
# ==========================================
def main():
    print("Iniciando o experimento de escalabilidade...\n")
    inicio = time.perf_counter()

    qtd_processos = 12
    nome_arquivo = "US_Accidents_March23.csv"

    tamanho_total_bytes = os.path.getsize(nome_arquivo)
    tamanho_fatia = tamanho_total_bytes // qtd_processos

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        cabecalho = next(csv.reader(arquivo))
        indice_hora = cabecalho.index("Start_Time")

    horarios = {}
    total_manha = total_tarde = total_noite = total_madrugada = total_linhas_processadas = 0

    print(f"Executando com {qtd_processos} processos independentes...\n")

    with ProcessPoolExecutor(max_workers=qtd_processos) as executor:
        futuros = []

        for i in range(qtd_processos):
            inicio_byte = i * tamanho_fatia
            fim_byte = tamanho_total_bytes if i == qtd_processos - 1 else (i + 1) * tamanho_fatia
            futuros.append(executor.submit(processar_fatia_arquivo, nome_arquivo, inicio_byte, fim_byte, indice_hora))

        for futuro in futuros:
            horarios_local, m, t, n, md, linhas_proc = futuro.result()
            
            total_manha += m
            total_tarde += t
            total_noite += n
            total_madrugada += md
            total_linhas_processadas += linhas_proc

            for hora, qtd in horarios_local.items():
                horarios[hora] = horarios.get(hora, 0) + qtd

    fim = time.perf_counter()
    tempo_segundos = fim - inicio

    print("\n===== PERÍODOS DO DIA =====")
    print(f"Manhã: {total_manha} | Tarde: {total_tarde} | Noite: {total_noite} | Madrugada: {total_madrugada}")
    print(f"\nTotal global de linhas analisadas: {total_linhas_processadas}")
    print(f"Tempo total com {qtd_processos} processos: {tempo_segundos:.2f} segundos")


if __name__ == "__main__":
    main()