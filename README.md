# 📚 **Desafio – Simulador de Caixa Eletrônico em Python (Versão com Array)**

## 🔸 **Descrição do Desafio**

O objetivo deste desafio é desenvolver, em Python, um sistema de **Caixa Eletrônico** simples, utilizando apenas **arrays (listas)** e estruturas básicas como `while`, `input` e `print`.

Este sistema permitirá que um usuário realize operações de **login**, **consulta de saldo** e **saque**, de acordo com regras pré-estabelecidas.

---

## 🔧 **Requisitos Funcionais**

* ✔️ O sistema deve solicitar a **conta** e a **senha** do usuário para acesso.
* ✔️ Após o login, o usuário deve visualizar um **menu com três opções**:

  * **1 – Consultar saldo**
  * **2 – Realizar saque**
  * **3 – Sair**
* ✔️ Na opção de saldo, o sistema deve exibir o saldo atual.
* ✔️ Na opção de saque, o sistema deve:

  * Permitir saques em valores **múltiplos de 10 reais**.
  * Verificar se o valor do saque é **menor ou igual ao saldo disponível**.
  * Limitar o saque a um máximo de **R\$ 1500,00 por operação**.
  * Exibir a quantidade de notas entregues nas denominações de **100, 50, 20 e 10 reais**.
  * Atualizar o saldo após o saque.
* ✔️ Na opção de sair, o sistema deve encerrar com uma mensagem de despedida.

---

## 📜 **Regras de Negócio**

* 🔸 O sistema só permite o acesso se a **conta e senha estiverem corretas**.
* 🔸 O saque:

  * **Não pode exceder o saldo disponível.**
  * **Não pode exceder o limite de R\$1500,00 por operação.**
  * **Deve ser obrigatoriamente múltiplo de 10.**
* 🔸 O saldo é atualizado após cada operação de saque.
* 🔸 O sistema permanece ativo até que o usuário selecione a opção de sair.

---

## 🧠 **Modelo de Dados**

O usuário será representado por uma **lista (array)** contendo as seguintes informações, na ordem:

```python
usuario = ["Alessandro", "12345-6", "123", 1000.49]
```

### 🔑 **Significado dos índices:**

| Índice | Descrição | Exemplo      |
| ------ | --------- | ------------ |
| `[0]`  | Nome      | "Alessandro" |
| `[1]`  | Conta     | "12345-6"    |
| `[2]`  | Senha     | "123"        |
| `[3]`  | Saldo     | 1000.49      |

---

## 🚀 **Regras de Implementação**

* Utilize apenas:

  * Arrays (`[]`)
  * Estruturas de repetição (`while`)
  * Condições (`if`, `else`)
  * Funções básicas como `input()` e `print()`
* Não utilizar dicionários, funções ou bibliotecas externas.

---

## ⚠️ **Observações Importantes**

* A organização do código será parte da avaliação.
* Comente seu código para facilitar a leitura e compreensão.
* O envio deve conter:

  * O arquivo `.py` com o código.
 
---

