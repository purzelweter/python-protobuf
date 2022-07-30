import root_pb2 as r
import a.a_pb2 as a
import b.b_pb2 as b

if __name__ == "__main__":
    print("Root: ", r.DESCRIPTOR)
    print("A   : ", a.DESCRIPTOR)
    print("B   : ", b.DESCRIPTOR)