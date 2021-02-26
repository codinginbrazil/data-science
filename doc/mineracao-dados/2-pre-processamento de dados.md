# Pré-processamento de dados


## O processo de preparação da base de dados

### Limpeza de dados
Imputação de valores ausentes, remoção de ruídos e correção de inconsistências;

### Integração dos dados
Unir dados de múltiplas fontes em um único local, como um armazém de dados (data warehouse);

### Redução dos dados
Reduzir a dimensão da base de dados, por exemplo, 
agrupando ou eliminando atributos redundantes, 
ou para reduzir a quantidade de objetos da base, sumarizando os dados;

### Transformação dos dados
Padronizar e deixar os dados em
um formato passível de aplicação das diferentes
técnicas de mineração;

###  Discretização dos dados
Permitir que métodos que trabalham apenas com atributos nominais possam ser empregados a um conjunto maior de problemas.
Também faz com que a quantidade de valores para um dado atributo (contínuo) seja reduzida.

---

## Limpeza de dados 

A baixa qualidade dos dados é um problema que afeta a maior parte das bases de dados reais. 
Assim, as ferramentas para a limpeza de dados atuam no sentido de imputar valores ausentes, suavizar ruídos, identificar valores discrepantes (outliers) e corrigir inconsistências. 

### Métodos tradicionais de imputação de valores ausentes

* Avestruz: 
descarta o objeto que possui atributo ausente.

* Manual: 
escolher manual de forma empírica um valor a ser imputado para cada valor ausente.

* Constante: 
substitui todo valor ausente por uma constante.

* Hot-deck: 
substitui o valor ausente por um valor mais similar a ele.

* Last observation carried forward: 
considera que a representação é uma medida contínua, para isto ordena todos os atributos, substituindo os valores ausentes por seus antecessores.

* Medidas centrais: 
usar a média ou a moda para substituir valores ausentes.

* Medidas centrais para classe: 
usar a média ou a moda da classe para substituir valores ausentes da mesma.

* Modelo preditivos: 
utiliza modelo preditivos para imputar os valores ausentes.
Nesse caso, o atributo com valores ausentes é utilizado como atributo dependente, ao passo que os outros atributos são usados como independentes para se criar o modelo preditivo.
Portanto, o modelo preditivo é usado para estimar os valores ausentes.

---

### Métodos de Redução de dados 

* Redução de dimensionalidade: seleção de atributos

* Compressão de atributos: 
também efetua uma redução da dimensionalidade, mas empregando algoritmos de codificação ou transformação de dados (atributos), em vez de seleção.
Exemplo é a Análise de Componentes Principais (Principal Component Analysis – PCA), que é um procedimento estatístico que converte um conjunto de objetos com atributos possivelmente
correlacionados em um conjunto de objetos com atributos linearmente descorrelacionados, chamados de componentes principais. 
O número de componentes principais é menor ou igual ao número de atributos da base, e a transformação é definida de forma que o primeiro componente principal possua a maior variância (ou seja, represente a maior variabilidade dos dados), o segundo componente principal

* Redução de número de dados: 
realiza um corte temporal das instância, podendo ser combinada com a redução de dimensionalidade.

* Discretização: 
os valores de atributos são substituídos por intervalos ou níveis conceituais mais elevados, reduzindo a quantidade final de atributos.

---

## Transformação dos dados

* Padronização: 
escala e unidades em bases compatíveis

* Normalização 
    * Máximo pelo minímo:

        A normalização Max-Min realiza uma transformação linear nos dados originais. Assuma que max_a e min_a são,respectivamente, os valores máximo e mínimo de determinado atributo a. 
        A normalização max-min mapeia um valor a em um valor a’ no domínio [novo_min_a′, novo_max_a′], de acordo com a Equação abaixo. 
        A aplicação mais frequente dessa normalização é colocar todos os atributos de uma base de dados sob um mesmo intervalo de valores, por exemplo no intervalo [0, 1].

        > a' = (a - min_a) / (max_a - min_a) * ( novo_max_a - novo_min_a) + novo_min_a

    * Escore-Z:
        
        Útil quando se desconhece a amplitude dos dados ou há outliers.

        > a' = (a - ã) / \delta_a

    * Escalonamento decimal:

        Estabelecido pelo escalonamento decimal move a casa decimal dos valores do atributo a. O número de casas decimais movidas depende do valor máximo absoluto do atributo a. 
        A Equação abaixo, na qual j é o menor inteiro tal que max(|a’|) < 1, ilustra o cálculo do valor normalizado.

        > a´ = a / 10^j

    * Range interquatil:

    * Trivial:
    
        > a´ = a / max_a



