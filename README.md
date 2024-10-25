# Sistema de Chat em Tempo Real

## Visão Geral Técnica
O sistema implementa uma comunicação cliente-servidor em tempo real usando sockets TCP/IP, com as seguintes características principais:

### Componentes Principais
1. **SocketHandler**: Classe abstrata que encapsula operações básicas de socket
   - Gerencia conexões TCP
   - Fornece interface para envio/recebimento de dados
   - Abstrai operações de bind, listen e accept

2. **Terminal Utils**: Módulo para manipulação do terminal
   - Implementa leitura raw de caracteres
   - Gerencia configurações do terminal

3. **Cliente**: Implementação do lado cliente
   - Captura entrada em tempo real
   - Gerencia conexão com servidor
   - Processa eventos de teclado

4. **Servidor**: Implementação do lado servidor
   - Aceita conexões de clientes
   - Processa mensagens em tempo real
   - Gerencia estado do chat

### Fluxo de Dados
1. Cliente captura caracteres individuais do teclado
2. Caracteres são enviados imediatamente ao servidor
3. Servidor processa e exibe em tempo real
4. Suporte a quebra de linha com Enter

## Instruções de Uso

### Requisitos
- Python 3.7+
- Sistema operacional compatível com POSIX (Linux/Unix/MacOS)
- Terminal com suporte a ANSI

### Instalação
```bash
# Clone o repositório
git clone <repository-url>

# Entre no diretório
cd chat-realtime

# Instale as dependências (se necessário)
pip install -r requirements.txt
```

### Execução
1. Inicie o servidor:
```bash
python servidor.py
```

2. Em outro terminal, inicie o cliente:
```bash
python cliente.py
```

### Uso
- Digite normalmente para enviar mensagens
- Pressione Enter para nova linha
- Ctrl+C para sair

## Considerações Técnicas
- Utiliza sockets TCP para comunicação confiável
- Implementa leitura raw do terminal para captura em tempo real
- Mantem estado do chat no servidor