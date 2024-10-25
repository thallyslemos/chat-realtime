from utils.terminal import get_char
from utils.socket_handler import SocketHandler

class Cliente:
    def __init__(self, host='localhost', port=5000):
        self.socket_handler = SocketHandler(host, port)
        self.socket_handler.connect()
        print("Conectado ao servidor")
        
    def iniciar(self):
        try:
            print("Digite seu texto (Ctrl+C para sair):")
            print("Pressione Enter para nova linha")
            linha_atual = ""
            
            while True:
                # Lê um caractere
                char = get_char()
                
                # Verifica se é Enter (retorno de carro ou nova linha)
                if char in ['\r', '\n']:
                    # Envia nova linha
                    self.socket_handler.send('\n'.encode())
                    print('\n', end='', flush=True)
                    linha_atual = ""
                else:
                    # Envia o caractere para o servidor
                    self.socket_handler.send(char.encode())
                    print(char, end='', flush=True)
                    linha_atual += char
                
        except KeyboardInterrupt:
            print("\nEncerrando conexão...")
        finally:
            self.socket_handler.close()

if __name__ == "__main__":
    cliente = Cliente()
    cliente.iniciar()