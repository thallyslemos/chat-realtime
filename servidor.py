from utils.socket_handler import SocketHandler

class Servidor:
    def __init__(self, host='localhost', port=5000):
        self.socket_handler = SocketHandler(host, port)
        self.socket_handler.bind_and_listen()
        print(f"Servidor iniciado em {host}:{port}")
        
    def iniciar(self):
        try:
            while True:
                # Aceita conexão do cliente
                client_socket, address = self.socket_handler.accept()
                print(f"Cliente conectado de {address}")
                
                # Buffer para armazenar a linha atual e todas as linhas
                linha_atual = ""
                todas_linhas = []
                
                while True:
                    # Recebe um caractere do cliente
                    caractere = client_socket.recv(1).decode()
                    
                    # Se não receber dados, o cliente desconectou
                    if not caractere:
                        print("Cliente desconectado")
                        break
                    
                    # Processa o caractere recebido
                    if caractere == '\n':  # Enter pressionado
                        # Adiciona a linha atual à lista de linhas
                        todas_linhas.append(linha_atual)
                        linha_atual = ""
                        
                        # Limpa a tela e mostra todas as linhas anteriores
                        print("\033[H\033[J", end='')  # Limpa a tela
                        for linha in todas_linhas:
                            print(linha)
                        print(linha_atual, end='', flush=True)
                        
                    else:
                        # Adiciona o caractere à linha atual
                        linha_atual += caractere
                        # Limpa a linha atual e mostra o texto atualizado
                        print(f"\r{linha_atual}", end='', flush=True)
                
                client_socket.close()
                
        except KeyboardInterrupt:
            print("\nServidor encerrado.")
        finally:
            self.socket_handler.close()

if __name__ == "__main__":
    servidor = Servidor()
    servidor.iniciar()