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

Teste serial:  273.841 segundos (4.56 minutos)<br> <br>
Teste 2 Threads: 118.60 segundos (1.98 minuto) <br> <br>
Teste 4 Threads: 58.11 segundos <br> <br>
Teste 8 Threads: 34.81 segundos <br> <br>
Teste 12 Threads: 29.85 segundos (1.53 minutos) <br> <br> 




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
  Speedup utilizando 12 threads: 9,17<br>

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
| 1                 |    273.84| 1.0     | 1.0        |
| 2                 |       118.60     |     2,30    |   1,15         |
| 4                 |       58.11     |     4.71    |     1,17      |
| 8                 |     34.81    |   7,86    |    0,98        |
| 12                |      29.85      |     9,17    |      0,76     |

---

# 7. Gráfico de Tempo de Execução

<img width="600" height="371" alt="Tempo de Execução" src="https://github.com/user-attachments/assets/bb242c36-bd11-43b2-aa86-6e42b2fe6dbc" />


# 8. Gráfico de Speedup

<img width="1600" height="870" alt="Speedup" src="https://github.com/user-attachments/assets/ab94fdf8-2614-47df-aee2-8952163f8bbe" />


# 9. Gráfico de Eficiência

<img width="438" height="276" alt="Eficiencia" src="https://github.com/user-attachments/assets/914592b2-a324-484a-a767-f4482b3dcb3b" />


# 10. Análise dos Resultados

Após a análise dos resultados, percebeu-se que o tempo de execução caiu consideravelmente. Passando de um tempo serial de 273,841 segundos para um tempo paralelizado utilizando 12 processos de 29,85 segundos. Inicialmente, o tempo de execução foi reduzido próximo ao esperado. Mas quando foi implementado o código com 12 processos, foi analizado que o tempo caiu aproximadamente 5 segundos, um tempo mais distante do ideal. Também foram analisados os gráficos de SpeedUp e eficiência.

Na análise do SpeedUp do sistema foi concluído que, até 8 processos, o ganho de SpeedUp ficou bem próximo do ideal, com 2 e 4 processos chegando a ultrapassar a taxa ideal, causando um SpeedUp superlinear, porém, quando aplicamos 12 processos simultâneos, pode-se perceber que ocorre uma queda drástica no SpeedUp, trazendo um resultado consideravelmente distante do ideal. 

Na análise de eficiência, foi constatado que, com 2 e 4 processos, ocorreu um ganho alto de eficiência, com os resultados em 115% e 117%, bem acima do esperado. Com 8 processos, a eficiência foi de 98%, um pouco abaixo, porém ainda dentro do ideal. Já com 12 processos, a eficiência cai para 76%, um numéro ainda dentro do padrão, porém não tão convincente quanto os outros. 

Depois de uma análise completa desses gráficos, foi constado que a melhor saída para o sistema é utilizar o paralelismo com 8 processos, pois, quando chegamos em 12 processos, a eficiência cai consideravelmente e não ocorre um ganho de tempo muito elevado, portanto, a utilização de 8 processos pode ser um pouco mais lenta, porém, mais eficiente, então, não vale a pena sacrificar tanta eficiência do projeto por 5 segundos de diferença no tempo de execução
