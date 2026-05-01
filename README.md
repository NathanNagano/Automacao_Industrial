# Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento

Sistema desenvolvido em Python para automatizar o controle de qualidade de peças produzidas em uma linha de montagem industrial.

## Funcionalidades

* Cadastro de novas peças
* Validação automática de qualidade
* Aprovação ou reprovação com motivo registrado
* Armazenamento automático de peças aprovadas em caixas (10 peças por caixa)
* Fechamento automático de caixas ao atingir a capacidade máxima
* Remoção de peças cadastradas
* Listagem de peças aprovadas e reprovadas
* Relatório final consolidado da produção

## Critérios de Aprovação

A peça será **aprovada** somente se atender aos seguintes requisitos:

* **Peso:** entre 95g e 105g
* **Cor:** azul ou verde
* **Comprimento:** entre 10cm e 20cm

Caso algum critério não seja atendido, a peça será reprovada e o motivo será registrado no sistema.

## Tecnologias Utilizadas

* Python 3
* Estruturas condicionais (`if`, `elif`, `else`)
* Estruturas de repetição (`while`, `for`)
* Funções
* Listas e dicionários

## Como Executar

1. Instale o Python 3 em seu computador.
2. Clone este repositório:

```bash
git clone https://github.com/NathanNagano/Automacao_Industrial.git
```

3. Entre na pasta do projeto:

```bash
cd Automacao_Industrial
```

4. Execute o programa:

```bash
Automacao_Gestao_Pecas.py
```

## Menu do Sistema

```text
1 - Cadastrar nova peça
2 - Listar peças aprovadas/reprovadas
3 - Remover peça cadastrada
4 - Listar caixas fechadas
5 - Gerar relatório final
0 - Sair
```

## Exemplo de Uso

### Entrada

```text
ID: 001
Peso: 100
Cor: azul
Comprimento: 15
```

### Saída

```text
Peça APROVADA
```

### Entrada

```text
ID: 002
Peso: 110
Cor: vermelho
Comprimento: 25
```

### Saída

```text
Peça REPROVADA
Motivos:
- Peso fora do padrão
- Cor inválida
- Comprimento fora do padrão
```

## Objetivo Acadêmico

Projeto desenvolvido para aplicar conceitos de:

* Algoritmos
* Lógica de Programação
* Estrutura de Dados
* Organização de código com funções
* Simulação de automação industrial


