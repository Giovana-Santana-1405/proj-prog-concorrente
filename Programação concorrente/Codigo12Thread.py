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

    # CONFIGURAÇÃO ALTERADA PARA 12 THREADS
    qtd_threads = 12 

    horarios = {}
    total_manha = total_tarde = total_noite = total_madrugada = total_linhas_processadas = 0

    with open("US_Accidents_March23.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor)
        indice_hora = cabecalho.index("Start_Time")

        print(f"Lendo o arquivo e distribuindo para {qtd_threads} threads simultaneamente...\n")

        with ProcessPoolExecutor(max_workers=qtd_threads) as executor:
            
            linhas_temporarias = []
            lotes_enviados = 0
            futuros = []
            
            # Ajustamos o lote para que cada uma das 12 threads pegue 100 mil linhas por vez
            TAMANHO_LOTE = 1200000  

            for linha in leitor:
                linhas_temporarias.append(linha)
                total_linhas_processadas += 1

                if total_linhas_processadas % 100000 == 0:
                    print(f"📖 [Leitor] Já leu {total_linhas_processadas} lines do arquivo CSV...")

                # Quando o lote acumular linhas suficientes para as 12 threads
                if len(linhas_temporarias) >= TAMANHO_LOTE:
                    lotes_enviados += 1
                    
                    # Calcula o tamanho de cada fatia (1/12 do lote)
                    tamanho_fatia = len(linhas_temporarias) // qtd_threads
                    
                    print(f"🚀 [Pool] Enviando lote {lotes_enviados} de dados para as {qtd_threads} threads...")
                    
                    # Divide o lote em 12 partes e dispara as 12 threads
                    for i in range(qtd_threads):
                        fatia = linhas_temporarias[i * tamanho_fatia : (i + 1) * tamanho_fatia]
                        futuros.append(executor.submit(processar_linhas, fatia, indice_hora, id_thread=i+1))
                    
                    # Limpa a memória temporária para o próximo lote
                    linhas_temporarias = []

            # Envia o restante das linhas caso o fim do arquivo não seja divisão exata
            if linhas_temporarias:
                lotes_enviados += 1
                tamanho_fatia = len(linhas_temporarias) // qtd_threads
                for i in range(qtd_threads):
                    if i == qtd_threads - 1:
                        fatia = linhas_temporarias[i * tamanho_fatia:]
                    else:
                        fatia = linhas_temporarias[i * tamanho_fatia : (i + 1) * tamanho_fatia]
                    futuros.append(executor.submit(processar_linhas, fatia, indice_hora, id_thread=i+1))

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
    print(f"\nTempo total com {qtd_threads} threads: {tempo_segundos:.2f} segundos ({tempo_minutos:.2f} minutos)")


if __name__ == "__main__":
    main()