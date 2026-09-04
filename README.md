# Python Port Scanner

Um scanner de portas leve e de alta performance construído em Python utilizando a biblioteca nativa `socket` e concorrência com `concurrent.futures`. Este projeto conecta conceitos teóricos da certificação CompTIA Network+ com engenharia de software e segurança prática.

## Objetivo e Aplicação

Este script foi desenvolvido para consolidar os fundamentos de redes aprendidos durantes meus estudos para o CompTIA Network+ focando especificamente na **Camada 4 (Camada de Transporte)** do Modelo OSI.

* **Modelo OSI - Camada 4:** O script inicia conexões TCP para verificar o estado das portas, simulando técnicas reais de reconhecimento e footprinting.
* **Protocolos de Rede:** Alvo em serviços estruturais core, incluindo DNS (53), HTTP (80), SSH (22) e SMB (445).
* **Programação com Sockets:** Manipulação de sockets de rede, timeout de conexões e tratamento de códigos de erro nativos do sistema operacional via `connect_ex()`.
* **Sistemas Concorrentes:** Implementação de `ThreadPoolExecutor` para gerenciar múltiplas threads de rede, otimizando o tempo de espera gerado pela latência I/O.

## Funcionalidades

- **Varredura Concorrente:** Capaz de testar múltiplas portas simultaneamente de forma assíncrona, reduzindo o tempo total de execução drasticamente.
- **Tratamento de Resultados Ordenados:** Utiliza ordenação via funções `lambda` para garantir que o output seja exibido de forma linear e limpa no terminal.

## Como Funciona

O script dispara requisições TCP para o IP alvo (`8.8.8.8` por padrão).
- Retorno igual a `0`: Indica um handshake TCP bem-sucedido (**PORTA ABERTA**).
- Retorno diferente de `0`: Indica que a conexão falhou ou estourou o timeout (**PORTA FECHADA/FILTRADA**).

## Como Executar

Certifique-se de ter o Python 3.8+ instalado. Clone o repositório e execute:

```bash
python port_scanner.py
```

### Exemplo de Output

```text
Starting Concurrent Port Scan at : 8.8.8.8

Port 464 (Kerberos-change): CLOSED
Port 465 (SMTPS      ): CLOSED
Port 514 (Syslog     ): CLOSED
Port 515 (LPD        ): CLOSED
Port 587 (SMTP-submission): CLOSED
Port 636 (LDAPS      ): CLOSED
Port 993 (IMAPS      ): CLOSED
Port 995 (POP3S      ): CLOSED

Port Scan done in 2.02 seconds

```

## Roadmap do Projeto

- [x] **Fase 1:** Scanner sequencial single-threaded com tratamento básico de erros.
- [x] **Fase 2:** Implementação de Multi-threading para aceleração de performance via rede.
- [ ] **Fase 3:** Implementação de Banner Grabbing para identificação de versões de serviços.
- [ ] **Fase 4:** Adição de parser de argumentos via CLI (ex: `python scanner.py --target 1.1.1.1`).
