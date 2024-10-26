import socket
import logging
from typing import Tuple

class SocketHandler:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.socket = None
        self.logger = logging.getLogger(__name__)

    def connect(self) -> None:
        """Estabelece conexão com o servidor"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.logger.info(f"Conectado ao servidor {self.host}:{self.port}")
        except ConnectionRefusedError:
            self.logger.error("Conexão recusada. Servidor está rodando?")
            raise
        except Exception as e:
            self.logger.error(f"Erro ao conectar: {str(e)}")
            raise

    def bind_and_listen(self, backlog: int = 1) -> None:
        """Configura o servidor para aceitar conexões"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.host, self.port))
            self.socket.listen(backlog)
            self.logger.info(f"Servidor iniciado em {self.host}:{self.port}")
        except Exception as e:
            self.logger.error(f"Erro ao iniciar servidor: {str(e)}")
            raise

    def accept(self) -> Tuple[socket.socket, Tuple[str, int]]:
        """Aceita uma nova conexão"""
        try:
            client_socket, address = self.socket.accept()
            self.logger.info(f"Nova conexão de {address}")
            return client_socket, address
        except Exception as e:
            self.logger.error(f"Erro ao aceitar conexão: {str(e)}")
            raise

    def send(self, data: bytes) -> None:
        """Envia dados para o socket"""
        try:
            if isinstance(data, str):
                data = data.encode('utf-8')
            self.socket.send(data)
        except BrokenPipeError:
            self.logger.error("Conexão perdida")
            raise
        except Exception as e:
            self.logger.error(f"Erro ao enviar dados: {str(e)}")
            raise

    def recv(self, bufsize: int = 1024) -> bytes:
        """Recebe dados do socket"""
        try:
            data = self.socket.recv(bufsize)
            if not data:
                raise ConnectionResetError("Conexão fechada pelo peer")
            return data
        except Exception as e:
            self.logger.error(f"Erro ao receber dados: {str(e)}")
            raise

    def close(self) -> None:
        """Fecha a conexão do socket"""
        try:
            if self.socket:
                self.socket.close()
                self.logger.info("Conexão fechada")
        except Exception as e:
            self.logger.error(f"Erro ao fechar conexão: {str(e)}")
            raise