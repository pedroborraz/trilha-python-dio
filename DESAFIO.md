# Sistema Bancário - Documentação de Requisitos

## Visão Geral
Este sistema bancário deve implementar as seguintes funcionalidades:
- Operações bancárias básicas: depósito, saque e extrato
- Gerenciamento de usuários e contas correntes

## Requisitos das Funções Bancárias

### Função `saque`
- **Argumentos**: A função deve receber apenas keyword arguments
  - `saldo` (float): Saldo atual da conta
  - `valor` (float): Valor a ser sacado
  - `extrato` (str): Histórico de movimentações
  - `limite` (float): Limite máximo por saque
  - `numero_saques` (int): Número de saques já realizados
  - `limite_saques` (int): Limite máximo de saques permitidos

- **Retorno**: Tupla contendo os valores atualizados de `saldo` e `extrato`

- **Assinatura**:
```python
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
```

### Função `deposito`
- **Argumentos**: A função deve receber apenas positional arguments
  - `saldo` (float): Saldo atual da conta
  - `valor` (float): Valor a ser depositado
  - `extrato` (str): Histórico de movimentações

- **Retorno**: Tupla contendo os valores atualizados de `saldo` e `extrato`

- **Assinatura**:
```python
def deposito(saldo, valor, extrato):
```

### Função `exibir_extrato`
- **Argumentos**: 
  - Positional: `saldo` (float)
  - Keyword: `extrato` (str)

- **Assinatura**:
```python
def exibir_extrato(saldo, *, extrato):
```

## Requisitos do Sistema de Usuários

### Estrutura do Usuário
Cada usuário é representado por um dicionário com os seguintes campos:
- `nome` (str): Nome completo do usuário
- `data_nascimento` (str): Data de nascimento no formato "dd-mm-aaaa"
- `cpf` (str): Número do CPF (apenas dígitos)
- `endereco` (str): Endereço no formato "logradouro, nro - bairro - cidade/sigla estado"

### Regras de Negócio
- Os usuários são armazenados em uma lista
- Não é permitida a duplicação de CPF no sistema

## Requisitos do Sistema de Contas Correntes

### Estrutura da Conta
Cada conta corrente é representada por um dicionário com os seguintes campos:
- `agencia` (str): Número da agência (fixo "0001")
- `numero_conta` (int): Número sequencial, começando em 1
- `usuario` (dict): Usuário vinculado à conta

### Regras de Negócio
- As contas são armazenadas em uma lista
- Um usuário pode ter mais de uma conta corrente
- Cada conta corrente está vinculada a um único usuário
- O vínculo é feito filtrando a lista de usuários pelo CPF

## Funções Adicionais

### `criar_usuario`
- Gerencia a criação de novos usuários, garantindo a unicidade do CPF

### `criar_conta_corrente`
- Gerencia a criação de novas contas correntes, vinculando a um usuário existente via CPF

---

*Documento criado para especificar os requisitos do sistema bancário*