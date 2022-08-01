import root_pb2 as r
import root_pb2_grpc
import a.a_pb2 as a
import b.b_pb2 as b
import grpc
from concurrent import futures
import logging
from datetime import datetime, timezone, timedelta
import pprint


class RootServicer(root_pb2_grpc.RootServicer):

    def Greeting(self, request, context):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(request)
        pp.pprint(context)

        timezone_offset = +2.0  # Central European Summer Time (UTC+02:00)
        tzinfo = timezone(timedelta(hours=timezone_offset))
        return r.GreetingResponse(GreetedAt=str(datetime.now(tzinfo)))


# copy + pasted from https://grpc.io/docs/languages/python/basics/#starting-the-server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    root_pb2_grpc.add_RootServicer_to_server(RootServicer(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    print("Listen on 0.0.0.0:8080 ...")
    server.wait_for_termination()


if __name__ == "__main__":
    # m = r.GreetingRequest()
    # m.Name = "This is the Name field in the root message"
    # m.MA.Name = "This is the Name field from the imported message A"
    # m.MA.MB.Name = "This is the Name field from the imported message B which is imported in Message A"
    # m.MB.Name = "This is the Name field from the imported message B"
    
    # This causes "AttributeError: 'MessageRoot' object has no attribute 'InProtoNotDefinedField'"
    # m.InProtoNotDefinedField = "in proto not defined field"
    
    # print(m)

    logging.basicConfig()
    serve()