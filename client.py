import grpc
import exemplo_pb2
import exemplo_pb2_grpc

def run():
    # Cria um canal para se conectar ao servidor
    with grpc.insecure_channel("localhost:50051") as channel:
        # Cria um stub (cliente)
        stub = exemplo_pb2_grpc.MeuServicoStub(channel)
        
        # Cria uma requisição
        mensagem = exemplo_pb2.MensagemRequest(texto="Olá, servidor gRPC!")
        
        # Envia a requisição e recebe a resposta
        resposta = stub.EnviarMensagem(mensagem)
        
        # Processa a resposta
        print(f"Resposta do servidor: {resposta.resposta}")
        print(f"Sucesso: {resposta.sucesso}")

if __name__ == "__main__":
    run()