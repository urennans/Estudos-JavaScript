import io

class SocketStreamWrapper:
    """Wrapper para fazer socket se comportar como stream"""
    def __init__(self, socket):
        self.socket = socket
        self.buffer = b''
    
    def write(self, data):
        """Envia dados pelo socket"""
        self.socket.sendall(data)
    
    def read(self, size=-1):
        """Lê dados do socket"""
        if size == -1:
            # Lê tudo até o final
            data = b''
            while True:
                chunk = self.socket.recv(4096)
                if not chunk:
                    break
                data += chunk
            return data
        else:
            # Lê quantidade específica de bytes
            while len(self.buffer) < size:
                chunk = self.socket.recv(size - len(self.buffer))
                if not chunk:
                    break
                self.buffer += chunk
            
            data = self.buffer[:size]
            self.buffer = self.buffer[size:]
            return data
    
    def flush(self):
        """Método flush para compatibilidade"""
        pass
    
    def close(self):
        """Fecha o socket"""
        self.socket.close()