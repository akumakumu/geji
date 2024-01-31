import grpc
import hello_pb2_grpc
import hello_pb2

from concurrent import futures

class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message=f"Hello, {request.name}")
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Listened on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()