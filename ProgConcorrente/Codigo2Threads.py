import csv
import time
from concurrent.futures import ProcessPoolExecutor

# ==========================================
# FUNÇÃO DE PROCESSAMENTO (O QUE CADA THREAD VAI FAZER)
# ==========================================
def processar_linhas(linhas_chunk, indice_hora, id_thread):
    horarios_local = {}
    manha = tarde = noite = madrugada = total_linhas = 0

    for linha in linhas_chunk:
        try:
            data_hora = linha[indice_hora]
            data_hora = data_hora.strip().upper().lower()
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

        except Exception:
            pass

    return horarios_local, manha, tarde, noite, madrugada, total_linhas


# ==========================================
# FUNÇÃO PRINCIPAL (GERENCIADORA)
# ==========================================
def main():
    print("Iniciando o programa...\n")
    inicio = time.perf_counter()

    # Configuramos 2 threads/processos como você pediu antes
    qtd_threads = 2 

    horarios = {}
    total_manha = total_tarde = total_noite = total_madrugada = total_linhas_processadas = 0

    # Abrimos o arquivo e vamos processar em lotes (chunks)
    with open("US_Accidents_March23.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor)
        indice_hora = cabecalho.index("Start_Time")

        print("Lendo o arquivo e distribuindo para as threads simultaneamente...\n")

        # Criamos o Pool de processos
        with ProcessPoolExecutor(max_workers=qtd_threads) as executor:
            
            linhas_temporarias = []
            lotes_enviados = 0
            futuros = []
            TAMANHO_LOTE = 200000  # Envia lotes de 200 mil linhas por vez para o pool

            for linha in leitor:
                linhas_temporarias.append(linha)
                total_linhas_processadas += 1

                # Feedback visual de leitura no terminal
                if total_linhas_processadas % 100000 == 0:
                    print(f"📖 [Leitor] Já leu {total_linhas_processadas} linhas do arquivo CSV...")

                # Quando acumular linhas suficientes para preencher o lote das 2 threads
                if len(linhas_temporarias) >= TAMANHO_LOTE:
                    lotes_enviados += 1
                    # Divide o lote no meio (uma parte para cada thread)
                    meio = len(linhas_temporarias) // 2
                    chunk1 = lines_chunk = linhas_temporarias[:meio]
                    chunk2 = linhas_temporarias[meio:]

                    print(f"🚀 [Pool] Enviando lote {lotes_enviados} de dados para processamento paralelo...")
                    
                    # Dispara as threads para processarem esse lote
                    futuros.append(executor.submit(processar_linhas, chunk1, indice_hora, 1))
                    futuros.append(executor.submit(processar_linhas, chunk2, indice_hora, 2))
                    
                    # Limpa a memória temporária para o próximo lote
                    linhas_temporarias = []

            # Envia o restante das linhas (caso o total não seja divisão exata de TAMANHO_LOTE)
            if linhas_temporarias:
                lotes_enviados += 1
                meio = len(linhas_temporarias) // 2
                futuros.append(executor.submit(processar_linhas, linhas_temporarias[:meio], indice_hora, 1))
                futuros.append(executor.submit(processar_linhas, linhas_temporarias[meio:], indice_hora, 2))

            print("\n⏳ Aguardando a finalização de todas as threads...")

            # Recolhe e consolida os resultados de todas as tarefas
            for futuro in futuros:
                horarios_local, m, t, n, md, _ = futuro.result()
                
                total_manha += m
                total_tarde += t
                total_noite += n
                total_madrugada += md

                for hora, qtd in horarios_local.items():
                    horarios[hora] = horarios.get(hora, 0) + qtd

    # ==========================================
    # FIM DO TEMPO PARALELO
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

    hora_maior = max(horarios, key=horarios.get)

    print("\n===================================")
    print(f"Horário com mais acidentes: {hora_maior}h")
    print(f"Quantidade: {horarios[hora_maior]} acidentes")
    print("===================================")

    print("\n===== PERÍODOS DO DIA =====")
    print(f"Manhã: {total_manha} | Tarde: {total_tarde} | Noite: {total_noite} | Madrugada: {total_madrugada}")
    print(f"\nTotal de linhas analisadas: {total_linhas_processadas}")
    print(f"\nTempo total em segundos: {tempo_segundos:.2f} segundos")
    print(f"Tempo total em minutos: {tempo_minutos:.2f} minutos")


if __name__ == "__main__":
    main()