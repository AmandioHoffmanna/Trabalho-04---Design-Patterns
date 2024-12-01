# User Management System

Este projeto implementa um sistema de gerenciamento de usuários utilizando os padrões de projeto **Singleton** e **Observer**.

---

## 🛠️ Padrão Singleton

### 📖 Explicação

**Singleton com Thread-Safety:**

- A classe `UserRegistry` utiliza o método `__new__` para garantir que apenas uma instância será criada durante a execução do programa.
- Um bloqueio (`threading.Lock`) é usado para garantir **thread-safety**, permitindo que o sistema funcione corretamente em ambientes multi-threaded.

### 🚀 Funcionalidades

- `register_user`: Adiciona um novo usuário ao registro.
- `get_user_email`: Retorna o e-mail de um usuário pelo nome.
- `list_users`: Lista todos os usuários registrados.

### ✅ Testes Implementados

- Verifica se apenas uma instância de `UserRegistry` é criada.
- Valida a adição de usuários ao sistema.
- Impede o registro de usuários duplicados.
- Testa o comportamento com múltiplas threads para garantir integridade em cenários concorrentes.

### 🔍 Escolha do Singleton

A implementação utiliza a abordagem **Thread-Safe Singleton com Lock**, conhecida por sua robustez e simplicidade. É ideal para sistemas com múltiplos acessos simultâneos.

---

## 🧵 O que é Thread?

Uma **thread** é a menor unidade de processamento gerenciada pelo sistema operacional. Threads permitem que um programa execute várias tarefas ao mesmo tempo, como:

- Processamento de dados.
- Atualização da interface do usuário.
- Manipulação de solicitações de rede.

---

## 🔒 O que é Thread-Safety?

**Thread-safety** refere-se à criação de código que funcione corretamente em ambientes onde várias threads possam acessar ou modificar os mesmos recursos simultaneamente.

Problemas comuns em sistemas não thread-safe incluem:

- **Condições de corrida (Race Conditions):** Resultados imprevisíveis quando threads acessam recursos simultaneamente.
- **Deadlocks:** Bloqueios mútuos entre threads, impedindo a execução do programa.
- **Corrupção de dados:** Dados inconsistentes devido a acessos concorrentes.

### 🛡️ Por que garantir Thread-Safety?

- Evitar erros difíceis de reproduzir.
- Produzir resultados previsíveis.
- Proteger a integridade dos dados compartilhados.

---

## 📢 Padrão Observer

### 📖 Explicação

O **Padrão Observer** foi implementado para criar um sistema de notificações, permitindo que diferentes partes do sistema sejam informadas de eventos importantes.

### 📋 Estrutura

- Criada uma classe base `Observer` que define o método `update`.
- A classe `NotificationSystem` gerencia os **observadores**, oferecendo métodos para:
  - Inscrição.
  - Remoção.
  - Notificação de eventos.

### 🔔 Funcionalidade de Notificação

- Quando um novo usuário é registrado, a classe `UserRegistry` notifica o sistema de notificações.
- O sistema de notificações, por sua vez, informa todos os observadores registrados.

### 🛠️ Observadores Implementados

1. **`EmailNotificationService`**:
   - Simula o envio de e-mails de boas-vindas aos novos usuários.

2. **`AuditLogService`**:
   - Registra logs de auditoria para cada novo registro.

### 🖥️ Interatividade

Adicionado um menu que permite:

- Registrar usuários.
- Listar usuários registrados.
- Sair do sistema.

---

## 🧪 Testes e Escalabilidade

### ✅ Testes Realizados

- **Inscrição de Observadores**:
  - Validado que novos serviços podem ser facilmente adicionados implementando a interface `Observer`.

- **Notificação**:
  - Todos os observadores recebem atualizações corretamente ao registrar novos usuários.

### 📈 Escalabilidade

- O sistema é projetado para escalar com eficiência.
- A lógica de notificação utiliza uma lista de chamadas síncronas, mantendo a performance estável mesmo com múltiplos observadores.

---

## 🏁 Conclusão

Este projeto combina os padrões **Singleton** e **Observer** para resolver problemas de gerenciamento de instância única e notificação de eventos. Ele é extensível, seguro para múltiplos threads e pronto para escalabilidade em aplicações modernas.

Alunos: Amandio Arnoldo Hoffmann e Vinícius Da Veiga
