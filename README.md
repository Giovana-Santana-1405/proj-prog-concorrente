# Relatório da análise de dados de acidentes automotivos no tráfego dos EUA 
## Disciplina: Programação concorrente e distribuída 
## Alunos: Bruno Alves da Silva e Giovana Santana Costa Ferrari de Abreu 
## Professor: Rafael Marconi

# 1. Descrição do Projeto – Paralelização Concorrente com Base de Dados de Acidentes nos EUA
O objetivo inicial é analisar os dados do Data Set, utilizando as colunas de horário e quantidade de acidentes, para definir em qual período do dia ocorrem a maior parte dos acidentes de trânsito. A ideia central é descobrir o horário onde ocorrem os picos de acidente. A base de dados contém aproximadamente 7 milhões de registro, e, por conta da grande quantidade de dados existentes, um programa serial leva um tempo relativamente longo para percorrer todas as linhas. O foco do projeto é aplicar o paralelismo utlizando várias Threads, aplicar os cálculos de eficiência e SpeedUp para descobrir a melhor forma de processamento de dados, onde não ocorra perca significativa de eficiência e ainda assim acelere o tempo de leitura da base de dados. 

## Estatísticas de acidentes de carros em paralelos
A utilização de paralelismo permite reduzir significativamente o tempo de execução das análises, melhorar o aproveitamento dos recursos computacionais e aumentar a escalabilidade do sistema. Dessa forma, o projeto demonstra na prática como técnicas de programação paralela podem ser aplicadas em cenários reais de Big Data e análise de dados urbanos.<br>
Além do aspecto computacional, o projeto também possui relevância social, pois a análise dos acidentes pode auxiliar estudos sobre segurança no trânsito, impactos climáticos nas rodovias e identificação de áreas críticas para prevenção de acidentes.

## Link para a base de dados 
https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents?utm_source=chatgpt.com

## 2. Ambiente experimental 

Informar as características do hardware e software utilizados na execução dos testes.

| Item                        | Descrição |
| --------------------------- | --------- |
| Processador                 |  12th Gen Intel(R) Core(TM) i7-12700       |
| Número de núcleos           |      12   |
| Memória RAM                 |      8GB    |
| Sistema Operacional         |     Window 11     |
| Linguagem utilizada         |     Python      |
| Biblioteca de paralelização |      concurrent.future    |
| Compilador / Versão         |      Python 3.14     |

---

# 3. Metodologia de Testes

Inicialmente, o teste do tempo Serial foi realizado com um código funcional, porém falho para o objetivo do trabalho. O código lia diversas linhas de uma vez só e o código se encerrava muito rápido. Após analises e alterações, o código passou a ler 100000 linhas por vez, trazendo um tempo serial que pode ser utilizado. <br>
Após isso, foram realizados testes, já aplicando o paralelismo <br>

Teste 1 - <br>
Tempo serial: 814,21 segundos (13.57 minutos) <br>
Aplicações extras abertas: Spotify, Google Chrome (2 guias)  <br>
<br>
Teste 2 - <br>
Tempo paralelo (2 Threads): 172.85 segundos (2.88 minutos)  <br>
Aplicações extras abertas: Spotify, Google Chrome (2 guias)  <br>
<br>
Teste 3 - <br>
Tempo paralelo(4 threads): 165.54 segundos (2.76 minutos) <br>
Aplicações extras abertas: Spotify, Google Chrome (2 guias)  <br>
<br>
 Teste 4 - <br>
Tempo paralelo(8 threads): 161.50 segundos (2.69 minutos)  <br>
Aplicações extras abertas: Spotify, Google Chrome (2 guias)  <br>
<br>

Teste 5 - <br>
Tempo paralelo(12 threads): 200.88 segundos (3.35 minutos) <br>
Aplicações extras abertas: Spotify, Google Chrome (2 guias)  <br>
<br>

Notou-se que o tempo paralelo de 12 threads foi pior que o resto dos tempos paralelos, pois a máquina onde foram realizadas os testes tinham apenas 10 núcleos no processador. Por isso, ocorreu overhead, onde o sistema tenta gerenciar 12 threads, tendo apenas 10 disponíveis. 

Cada execução foi realizada uma vez, considerando inicialmente o tempo único, porém por conta da potência inferior da máquina em relação ao objetivo do projeto, foram realizadas novas levas de testes, em um máquina mais potente. Os primeiros testes realizados foram descartados, pois, por conta de alguns gargalos o código não estava alcançando o redução de tempo ideal. Houveram adaptações no código e finalmente chegamos no resultado final: <br>

Teste serial:  273.841 segundos (4.56 minutos)<br>
Teste 2 Threads: 118.60 segundos (1.98 minuto) <br>
Teste 4 Threads: 58.11 segundos <br>
Teste 8 Threads: 34.81 segundos <br> 
Teste 12 Threads: 29.85 segundos (1.53 minutos) <br> 




## Orientações


| Nº Threads/Processos | Tempo de Execução (s) |
| -------------------- | --------------------- |
| 1                    |           273.841          |
| 2                    |           118.60           |
| 4                    |              58.11         |
| 8                    |            34.81            |
| 12                   |           29.85            |

---

# 5. Cálculo de Speedup e Eficiência

## Fórmulas Utilizadas

### Speedup

```
Speedup(p) = T(1) / T(p)
```

Onde:

* **T(1)** = tempo da execução serial
* **T(p)** = tempo com p threads/processos

  Speedup utilizando 2 threads: 2,30<br>
  Speedup utilizando 4 threads: 4,71<br>
  Speedup utilizando 8 threads: 7,86<br>
  Speedup utilizando 12 threads:9,17<br>

### Eficiência

```
Eficiência(p) = Speedup(p) / p
```

Onde:

* **p** = número de threads ou processos

---

# 6. Tabela de Resultados

Preencha a tabela abaixo utilizando os tempos medidos.

| Threads/Processos | Tempo (s) | Speedup | Eficiência |
| ----------------- | --------- | ------- | ---------- |
| 1                 |     814.21     | 1.0     | 1.0        |
| 2                 |       172.85     |     2,30    |   115%         |
| 4                 |       165.54     |     4.71    |     117%       |
| 8                 |       161.50     |   7,86    |    98%        |
| 12                |      200.88      |     9,17    |      76%      |

---

# 7. Gráfico de Tempo de Execução

## A inserir


# 8. Gráfico de Speedup

## A inserir

# 9. Gráfico de Eficiência

## A inserir

# 10. Análise dos Resultados

## A inserir 

# 11. Conclusão

## A inserir 
