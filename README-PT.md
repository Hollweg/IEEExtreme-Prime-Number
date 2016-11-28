#IEEExtreme-Prime-Number
**Problema proposto no concurso de programação IEEExtreme 2016.**

Esse ano eu participei do concurso **IEEExtreme** para ver como funcionava a competição, e para minha surpresa, é **mais difícil** do que **eu pensei que seria.** :P

##A proposta

Esse problema foi o último lançado na competição (nº 25) e tinha uma proposta relativamente simples:

* O usuário deve entrar com uma entrada (um número inteiro) no range de 1 a 10^18.
* Os objetivos do algoritmo são os seguintes:
    * Verificar se o número é primo.
    * Se o número for primo, retornar o número como o resultado na soma de 3 números primos.
    * Ex.: Entrada: 37     Saída: 3 + 3 + 31 = 37.
    * Ex2: Entrada: 7283   Saída: 7 + 23 + 7253 = 7283.

Tendo em vista que eu poderia usar qualquer linguagem de programação para resolver o problema, escolhi Python para essa tarefa. </br>
Por que Python? Por que Python é incrível. :D

Estou trabalhando para **melhorar o algoritmo em termos de otimização**, mas o principal problema de identificar e **retonar o número proposto como uma soma de 3 outros números primos foi solucionada**.

##Como ele funciona?

A principal ideia é verificar se o número é **primo**, e se o resultado for positivo, o algoritmo procura o **último número primo** da entrada, usando o mesmo método de busca. Entretanto, é varrido o último número primo de trás para frente, por quesitos de otimização. 

No momento que se acha o último primo número da entrada, é **calculada a diferença entre as entradas** (se ele for um número primo) **e seu último número primo.**

Em quase todos os casos, a diferença me retorna um número curto, como exemplo:

Entrada: **3517** </br>
3517 é um número primo, portanto, se calcula o último número primo, o qual é 3511. </br>
Então, a diferença entre 3517 - 3511 = 6. </br>
Agora, trabalha-se apenas com o número 6. </br>
Verifica-se **todos os números primos entre 2 e 6**. Esses números são: _[2,3,5]_. </br>
Dessa forma, tenta-se a soma de 3 números com 3511 e todas combinações em difererentes listas. </br>
Nesse caso o algoritmo me retorna o seguinte resultado: **3 + 3 + 3511 = 3517.**
 
Aqui está o link para a implementação no ambiente Codeskulptor: </br>
http://www.codeskulptor.org/#user42_sAVxLToaP0_2.py

##Direitos

**A solução do problema pode ser reproduzida em outras mídias sem problema algum :)**. </br>
Entretanto, caso isso seja feito, somente peço para que sejam mantidos **créditos ao autor**. </br>
Além disso, em caso de ser compartilhado o link do Codeskultpr, por favor, creditar a **Rice University** pelo desenvolvimento da plataforma.


Enjoy!

**Hollweg**

