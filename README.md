# Projeto de paralelismo e serialização 
Projeto desenvolvido para o trabalho final da matéria de programação concorrente e distribuída 
## Professor
Rafael Marconi 
## Integrantes 
Giovana Santana Costa Ferrari de Abreu <br> 
Bruno Alves da Silva 

# Descrição do Projeto – Paralelização Concorrente com Base de Dados de Acidentes nos EUA
Este projeto utiliza a base de dados Kaggle “US Accidents (2016–2023)”, desenvolvida por Sobhan Moosavi, com o objetivo de realizar processamento paralelo e concorrente de grandes volumes de dados relacionados a acidentes de trânsito nos Estados Unidos<br> 
O conjunto de dados contém aproximadamente 7,7 milhões de registros de acidentes ocorridos entre fevereiro de 2016 e março de 2023, cobrindo 49 estados norte-americanos. As informações foram coletadas por meio de APIs de tráfego em tempo real, integrando dados provenientes de departamentos de transporte, sensores viários, câmeras de trânsito e órgãos de segurança pública.<br>
A base apresenta características ideais para aplicações de computação concorrente e paralela devido ao seu grande volume de dados e diversidade de atributos. Entre as principais informações disponíveis estão:<br>
Localização geográfica dos acidentes (latitude e longitude);<br>
Data e horário da ocorrência;<br>
Condições climáticas;<br>
Severidade do acidente;<br>
Condições da via;<br>
Visibilidade, temperatura, umidade e velocidade do vento;<br>
Informações urbanas e ambientais próximas ao local do acidente.<br>

## Objetivo do projeto
O projeto tem como foco aplicar técnicas de paralelização para otimizar tarefas de processamento de dados, como:
leitura simultânea de grandes arquivos CSV;<br>
divisão de processamento por regiões ou períodos de tempo;<br>
análise concorrente de estatísticas;<br>
processamento distribuído de consultas;<br>
identificação de padrões e hotspots de acidentes;<br>
aceleração de etapas de limpeza e transformação dos dados.<br>

## Estatísticas de acidentes de carros em paralelos
A utilização de concorrência permite reduzir significativamente o tempo de execução das análises, melhorar o aproveitamento dos recursos computacionais e aumentar a escalabilidade do sistema. Dessa forma, o projeto demonstra na prática como técnicas de programação paralela podem ser aplicadas em cenários reais de Big Data e análise de dados urbanos.<br>
Além do aspecto computacional, o projeto também possui relevância social, pois a análise dos acidentes pode auxiliar estudos sobre segurança no trânsito, impactos climáticos nas rodovias e identificação de áreas críticas para prevenção de acidentes.



