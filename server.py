import grpc
from concurrent import futures
import time
import exemplo_pb2
import exemplo_pb2_grpc

# Implementação do serviço
class MeuServicoServicer(exemplo_pb2_grpc.MeuServicoServicer):
    def EnviarMensagem(self, request, context):
        # Processa a mensagem recebida
        texto_recebido = request.texto
        print(f"Mensagem recebida: {texto_recebido}")
        
        # Retorna uma resposta
        return exemplo_pb2.MensagemResponse(
            resposta=f"Recebi sua mensagem: {texto_recebido}",
            sucesso=True
        )

def serve():
    # Cria o servidor gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Adiciona o serviço ao servidor
    exemplo_pb2_grpc.add_MeuServicoServicer_to_server(
        MeuServicoServicer(), server
    )
    
    # Configura a porta
    porta = "50051"
    server.add_insecure_port(f"[::]:{porta}")
    
    # Inicia o servidor
    server.start()
    print(f"Servidor iniciado na porta {porta}")
    
    try:
        # Mantém o servidor rodando
        while True:
            time.sleep(86400)  # 24 horas
    except KeyboardInterrupt:
        server.stop(0)
        print("Servidor encerrado")

if __name__ == "__main__":
    serve()