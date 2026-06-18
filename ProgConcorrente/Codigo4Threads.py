import csv
import time
from concurrent.futures import ProcessPoolExecutor

# ==========================================
# FUNÇÃO DE PROCESSAMENTO (O QUE CADA PROCESSO VAI FAZER)
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

            # Carga computacional extra mantida para o seu benchmark
            for i in range(100):
                texto = str(hora) * 100
                texto = texto.lower().upper()
                len(texto)

            total_linhas += 1

        except Exception:
            pass

    return horarios_local, manha, tarde, noite, madrugada, total_linhas


# ==========================================
# FUNÇÃO PRINCIPAL (LEITURA EM TEMPO REAL)
# ==========================================
def main():
    print("Iniciando o programa...\n")
    inicio = time.perf_counter()

    # Altere aqui para 2, 4, 8 e 12 nos seus testes
    qtd_threads = 4  

    horarios = {}
    total_manha = total_tarde = total_noite = total_madrugada = 0
    total_linhas_lidas = 0

    with open("US_Accidents_March23.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor)
        indice_hora = cabecalho.index("Start_Time")

        print(f"Lendo o arquivo e distribuindo para {qtd_threads} threads simultaneamente...\n")

        with ProcessPoolExecutor(max_workers=qtd_threads) as executor:
            futuros = []
            linhas_temporarias = []
            
            # Tamanho do lote menor (25k por thread = 100k total por envio)
            # Isso evita o engarrafamento de dados que tínhamos antes!
            TAMANHO_LOTE_POR_THREAD = 25000
            TAMANHO_LOTE_TOTAL = TAMANHO_LOTE_POR_THREAD * qtd_threads
            id_tarefa = 1

            for linha in leitor:
                linhas_temporarias.append(linha)
                total_linhas_lidas += 1

                # EXATAMENTE IGUAL AO SEU PRIMEIRO CÓDIGO:
                # Printa em tempo real na tela enquanto lê do HD
                if total_linhas_lidas % 100000 == 0:
                    print(f"📖 [Leitor] Já leu {total_linhas_lidas} linhas do arquivo CSV...")

                # Quando acumula o lote total, divide e envia imediatamente de forma assíncrona
                if len(linhas_temporarias) >= TAMANHO_LOTE_TOTAL:
                    for i in range(qtd_threads):
                        fatia = linhas_temporarias[i * TAMANHO_LOTE_POR_THREAD : (i + 1) * TAMANHO_LOTE_POR_THREAD]
                        futuros.append(executor.submit(processar_linhas, fatia, indice_hora, id_tarefa))
                        id_tarefa += 1
                    
                    linhas_temporarias = [] # Limpa a memória para as próximas linhas

            # Envia o que sobrou no final do arquivo (se houver)
            if lines_restantes := len(linhas_temporarias):
                tamanho_fatia = max(1, lines_restantes // qtd_threads)
                for i in range(qtd_threads):
                    fatia = linhas_temporarias[i * tamanho_fatia : (i + 1) * tamanho_fatia] if i < qtd_threads - 1 else linhas_temporarias[i * tamanho_fatia:]
                    if fatia:
                        futuros.append(executor.submit(processar_linhas, fatia, indice_hora, id_tarefa))

            print("\n⏳ Leitura concluída! Aguardando as threads terminarem de processar os últimos lotes...")

            # Recolhe e consolida os resultados conforme eles terminam
            for futuro in futuros:
                horarios_local, m, t, n, md, _ = futuro.result()
                
                total_manha += m
                total_tarde += t
                total_noite += n
                total_madrugada += md

                for hora, qtd in horarios_local.items():
                    horarios[hora] = horarios.get(hora, 0) + qtd

    # ==========================================
    # FIM DO TEMPO PARALELO E RESULTADOS
    # ==========================================
    fim = time.perf_counter()
    tempo_segundos = fim - inicio
    tempo_minutos = tempo_segundos / 60

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
    print(f"\nTotal de linhas analisadas: {total_linhas_lidas}")
    print(f"\nTempo total com {qtd_threads} threads: {tempo_segundos:.2f} segundos ({tempo_minutos:.2f} minutos)")


if __name__ == "__main__":
    main()