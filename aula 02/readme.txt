Anotações - Estrutura de Dados - Aula 02

TUPLAS

As tuplas são um tipo de estrutura de dados em Python que
armazenam um conjunto ordenado de elementos. Elas são muito
semelhantes às listas, mas com a principal diferença de serem
imutáveis, ou seja, uma vez criadas, seus elementos não podem ser
modificados.

TUPLAS CONCLUSÃO

As tuplas são uma estrutura de dados poderosa em Python, usadas
principalmente quando precisamos garantir que os dados permaneçam
imutáveis. Elas são eficientes, rápidas e úteis em diversas situações, como:
➢ Armazenamento de configurações constantes
➢ Uso como chaves em dicionários
➢ Retorno de múltiplos valores em funções
➢ Estruturas de dados imutáveis para maior segurança

LISTAS

As listas são uma das estruturas de dados mais utilizadas em Python. Elas permitem
armazenar múltiplos valores, que podem ser de diferentes tipos, e são mutáveis, ou seja,
podem ser alteradas após a criação.

LISTAS CONCLUSÃO

As listas são uma das estruturas de dados mais flexíveis em
Python. Elas permitem:
➢ Armazenar dados heterogêneos
➢ Modificar os valores livremente
➢ Usar métodos poderosos para manipulação

Tuplas x Listas: Quando Usar?

As tuplas são mais eficientes em termos de uso de memória e velocidade, então são ideais
quando os dados não precisam ser modificados.


DICIONÁRIOS

Os dicionários são uma das estruturas de dados mais poderosas e versáteis do Python. Eles
armazenam pares chave-valor, permitindo acesso rápido e eficiente aos dados.

DICIONÁRIOS CONCLUSÃO

Os dicionários são uma ferramenta essencial para organizar dados
no formato chave-valor. Eles oferecem:
➢ Acesso rápido aos dados
➢ Flexibilidade e mutabilidade
➢ Aplicações poderosas em APIs, JSON, e estruturação de dados

CONJUNTOS (SET)

O set em Python é uma estrutura de dados que armazena valores únicos e desordenados. Ele é
muito útil para eliminar duplicatas e realizar operações matemáticas de conjuntos (união, interseção,
diferença, etc.). E é recomendado utilizar estrutura set com valores dicionários.

CONJUNTOS (SET) CONCLUSÃO

Estrutura eficiente que dependendo do cenário é a melhor saída de utilizar. Usar quando:
➢ Para remover valores duplicados rapidamente.
➢ Para verificar pertinência (in) de forma eficiente.
➢ Para operações matemáticas de união, interseção e diferença.
➢ Para melhorar performance em buscas e verificações.

MATRIZES

Em Python, podemos representar matrizes de diferentes formas, mas a maneira mais
eficiente é utilizando a biblioteca NumPy. Uma matriz é uma estrutura de dados
bidimensional (ou multidimensional) que armazena valores em linhas e colunas. Elas são
amplamente utilizadas em computação científica, machine learning, estatística e
processamento de imagens.

MATRIZES

A biblioteca NumPy resolve o problema de listas aninhadas não possuem funções
matemáticas otimizadas, ao fornecer o tipo de dado ndarray, que é muito mais eficiente.
Vantagens do NumPy sobre listas:
➢ Mais rápido
➢ Ocupa menos memória
➢ Possui operações matemáticas otimizadas

MATRIZ TRANSPOSTA

A matriz transposta é uma matriz obtida ao trocar suas linhas por colunas.
Se tivermos uma matriz A de dimensão m x n (m linhas e n colunas), sua transposta será uma
matriz Aᵀ de dimensão n x m (n linhas e m colunas).
