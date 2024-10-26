import sys
import logging
from utils.terminal import get_char
from utils.socket_handler import SocketHandler
import locale

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    except locale.Error:
        logger.warning("Nenhum locale suportado encontrado. Usando o locale padrão.")
        
class Cliente:
    def __init__(self, host='localhost', port=5000):
        try:
            self.socket_handler = SocketHandler(host, port)
            self.socket_handler.connect()
            logger.info("Conectado ao servidor")
        except Exception as e:
            logger.error(f"Erro ao iniciar cliente: {str(e)}")
            sys.exit(1)

    def iniciar(self):
        try:
            print("Digite seu texto (Ctrl+C para sair):")
            print("Pressione Enter para nova linha")
            linha_atual = ""
            
            while True:
                try:
                    # Lê um caractere
                    char = get_char()
                    
                    # Verifica se é Enter
                    if char in ['\r', '\n']:
                        self.socket_handler.send('\n'.encode('utf-8'))
                        print('\n', end='', flush=True)
                        linha_atual = ""
                    else:
                        # Envia o caractere para o servidor
                        self.socket_handler.send(char.encode('utf-8'))
                        print(char, end='', flush=True)
                        linha_atual += char
                        
                except UnicodeDecodeError:
                    logger.warning("Caractere inválido detectado")
                    continue
                except BrokenPipeError:
                    logger.error("Conexão com servidor perdida")
                    break
                
        except KeyboardInterrupt:
            logger.info("Encerrando conexão...")
        except Exception as e:
            logger.error(f"Erro inesperado: {str(e)}")
        finally:
            self.socket_handler.close()

if __name__ == "__main__":
    cliente = Cliente()
    cliente.iniciar()