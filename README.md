# Projeto de Análise de Tabelas Hash

Este projeto implementa e avalia diferentes funções de hash aplicadas a tabelas hash de variados tamanhos. O objetivo é analisar o desempenho das operações de inserção e busca, medindo o tempo de execução e a quantidade de colisões/comparações.

## Estrutura do Projeto

### 1. `tabelasHash.java`
Este código em Java realiza as operações de inserção e busca em tabelas hash usando três funções de hash distintas:
- **Função Módulo**: calcula o índice da tabela usando o operador de módulo.
- **Função Multiplicação**: utiliza um valor de multiplicação específico para dispersar os valores de forma uniforme.
- **Função Dobra**: utiliza uma técnica de "folding" para calcular o índice, dividindo o valor em partes e combinando-as.

Para cada função de hash, o código executa operações em diferentes configurações:
- **Tamanhos do Conjunto de Dados**: 1.000.000, 5.000.000 e 20.000.000 elementos.
- **Tamanhos da Tabela**: 10.000.000, 50.000.000 e 100.000.000 posições.

Cada configuração gera dados sobre o tempo de inserção, o número de colisões durante a inserção, o tempo de busca e o número de comparações na busca. Os resultados são armazenados em um arquivo `.csv` .

### 2. `tabelahash.py`
Este script em Python controla a execução automatizada do código Java em diferentes configurações, usando o módulo `subprocess`:
- **Compilação e Execução**: compila o `tabelasHash.java` e executa o programa com diferentes combinações de funções de hash, tamanhos de conjuntos e tamanhos de tabela.
- **Incremento de Seed**: modifica a seed em cada execução para aumentar a variabilidade nos testes e garantir que os dados gerados cubram uma ampla gama de cenários.
- **Gestão de Erros**: verifica se a compilação foi bem-sucedida e exibe erros, caso ocorram, permitindo fácil depuração.

Esse script facilita a coleta de dados em larga escala, economizando tempo e reduzindo o esforço manual.

### 3. `graficos.py`
Este script em Python realiza a análise e visualização dos dados coletados no arquivo `.csv` utilizando as bibliotecas `pandas`, `seaborn` e `matplotlib`. Ele gera gráficos que auxiliam na interpretação do desempenho das tabelas hash:
- **Média do Tempo de Inserção**: gráfico de barras que mostra o tempo médio de inserção para cada função de hash e tamanho do conjunto.
- **Média de Colisões na Inserção**: exibe o número médio de colisões durante as operações de inserção, destacando a eficácia de cada função de hash.
- **Média do Tempo de Busca**: ilustra o tempo médio necessário para buscas, permitindo avaliar a rapidez de cada abordagem de hash.
- **Média de Comparações na Busca**: exibe o número médio de comparações necessárias durante as buscas, indicando a eficiência de cada função hash para minimizar conflitos.

Cada gráfico utiliza uma escala logarítmica para facilitar a leitura de valores amplamente variáveis e inclui anotações que indicam os valores médios.

### 4. `dadosHash.csv`
Este arquivo armazena os dados brutos das operações de inserção e busca realizadas no `tabelasHash.java`. Ele contém as seguintes colunas:
- **FuncaoHash**: nome da função de hash utilizada (modulo, multiplicacao, dobra).
- **TamanhoConjunto**: quantidade de elementos inseridos na tabela.
- **TamanhoTabela**: número de posições na tabela hash.
- **TempoInsercao**: tempo médio de inserção, em milissegundos.
- **ColisoesInsercao**: número médio de colisões ocorridas durante a inserção.
- **TempoBusca**: tempo médio para realizar uma busca, em milissegundos.
- **ComparacoesBusca**: número médio de comparações necessárias durante a busca.

Esses dados são utilizados pelo `graficos.py` para gerar insights visuais sobre o desempenho das funções de hash.