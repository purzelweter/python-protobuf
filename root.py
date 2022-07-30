import root_pb2 as r
import a.a_pb2 as a
import b.b_pb2 as b

if __name__ == "__main__":
    m = r.MessageRoot()
    m.Name = "This is the Name field in the root message"
    m.MA.Name = "This is the Name field from the imported message A"
    m.MA.MB.Name = "This is the Name field from the imported message B which is imported in Message A"
    m.MB.Name = "This is the Name field from the imported message B"
    
    # This causes "AttributeError: 'MessageRoot' object has no attribute 'InProtoNotDefinedField'"
    # m.InProtoNotDefinedField = "in proto not defined field"
    
    print(m)