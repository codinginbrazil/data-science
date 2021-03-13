# Análise de grupos

> áreas: estatística, bioinformática, medicina, computação, biologia, matemática, públicidade e outras  

 * Grupos naturais descrito por Carmichael que grupos são aqueles que satisfazem duas condições particulares: 
    1. Existência de regiões contínuas do espaço, relativamente densamente populadas por objetos;
    2. Tais regiões estão rodeadas por regiões relativamente vazias.

---

## Medidas de similaridade 

* Matriz de confusão (contingência) 

### Dados binários
* Distância Hamming

|           Medida             |                Fórmula                     |            
|------------------------------|--------------------------------------------|
| S1: Coeficiente de Matching  | $$ S_{ij} = \frac{a + d}{a + b + c + d} $$ | 
| S2: Coeficiente de Jaccard   | $$ S_{ij} = \frac{a}{a+b+c}             $$ |
| S3: Rogers & Tanimoto        | $$ S_{ij} = \frac{a+d}{a+2(b+c)+d}      $$ |
| S4: Sokal & Sneath           | $$ S_{ij} = \frac{a}{a+2(b+c)}          $$ |
| S5: Gower & Legendre         | $$ S_{ij} = \frac{a+d}{a+0.5(b+c)+d}    $$ |
| S6: Gower & Legendre 2       | $$ S_{ij} = \frac{a}{a+0.5(b+c)}        $$ |


