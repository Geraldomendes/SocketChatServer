# SocketChatServer

**SocketChatServer** é um projeto de chat em Python que utiliza sockets para comunicação entre clientes e um servidor. O servidor gerencia múltiplos clientes, permitindo que enviem mensagens, troquem apelidos e "cutuquem" outros usuários. O projeto segue um protocolo de comunicação específico para garantir a consistência das interações no chat.

## Funcionalidades

- **Envio de Mensagens:** Permite que um usuário envie mensagens para todos os outros usuários conectados ao chat.
- **Troca de Apelido:** Usuários podem alterar seus apelidos (nicknames) a qualquer momento.
- **Cutucada:** Usuários podem enviar uma notificação para cutucar outro usuário no chat.
- **Notificação de Desconexão:** Quando um usuário se desconecta, todos os outros usuários são notificados.
- **Lista de Usuários:** Quando um usuário se conecta, ele recebe uma lista de todos os usuários atualmente online.

## Estrutura do Projeto

- `server.py`: Código do servidor que gerencia a comunicação entre os clientes.
- `client.py`: Código do cliente que se conecta ao servidor e interage com ele.

## Instalação

Para usar este projeto, você precisa ter o Python 3 instalado. Clone o repositório e execute os seguintes comandos:

```bash
git clone https://github.com/Geraldomendes/SocketChatServer
```

## Execução

1. **Inicie o servidor:**

   No diretório do projeto, execute o seguinte comando:

   ```bash
   python server.py
   ```

   O servidor começará a escutar conexões na porta padrão `55555`.

2. **Inicie um ou mais clientes:**

   Em um novo terminal (ou diferentes terminais para múltiplos clientes), execute o cliente com:

   ```bash
   python client.py
   ```

   Ao conectar, você será solicitado a escolher um apelido. Depois disso, poderá enviar mensagens, trocar apelidos e cutucar outros usuários no chat.

## Protocolo de Comunicação

O chat utiliza um protocolo de comunicação simples para garantir que todas as mensagens sigam um formato consistente. Abaixo estão os comandos suportados:

- **Conectar com Apelido:**

  Cliente envia:
  ```
  !nick <nickname>
  ```

  Servidor responde com a lista de usuários conectados:
  ```
  !users <total> <nickname1> <nickname2> ...
  ```

- **Enviar Mensagem:**

  Cliente envia:
  ```
  !sendmsg <mensagem>
  ```

  Servidor envia a todos os clientes:
  ```
  !msg <nickname> <mensagem>
  ```

- **Trocar Apelido:**

  Cliente envia:
  ```
  !changenickname <novo_nickname>
  ```

  Servidor notifica todos os clientes:
  ```
  !changenickname <nickname_antigo> <novo_nickname>
  ```

- **Cutucar Outro Usuário:**

  Cliente envia:
  ```
  !poke <nickname>
  ```

  Servidor notifica todos os clientes:
  ```
  !poke <nickname_poker> <nickname_poked>
  ```

- **Notificação de Desconexão:**

  Quando um usuário se desconecta, o servidor notifica todos os clientes:
  ```
  !left <nickname>
  ```

## Considerações Finais

O **SocketChatServer** é uma implementação simples e didática de um chat utilizando sockets em Python. Ele serve como uma base para entender como a comunicação via sockets pode ser implementada, além de fornecer um exemplo de como seguir um protocolo de comunicação específico para garantir a integridade das mensagens trocadas no chat.