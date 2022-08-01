import root_pb2 as r
import root_pb2_grpc as r_grpc
import a.a_pb2 as a
import b.b_pb2 as b
import grpc
from concurrent import futures

def Greeting(self, request, context):
    print(context)
    return  root_pb2.GreetingResponse()

# copy + pasted from https://grpc.io/docs/languages/python/basics/#starting-the-server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    r_grpc.add_RootServiceServicer_to_server(r_grpc.RootService(), server)
    server.add_insecure_port('[::]:8080')
    print("Listen on :8080 ...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    m = r.GreetingRequest()
    m.Name = "This is the Name field in the root message"
    m.MA.Name = "This is the Name field from the imported message A"
    m.MA.MB.Name = "This is the Name field from the imported message B which is imported in Message A"
    m.MB.Name = "This is the Name field from the imported message B"
    
    # This causes "AttributeError: 'MessageRoot' object has no attribute 'InProtoNotDefinedField'"
    # m.InProtoNotDefinedField = "in proto not defined field"
    
    print(m)

    serve()