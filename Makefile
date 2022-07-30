compile:
	$(info >>> $@)
	python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. root.proto
	python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. a/a.proto
	python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. b/b.proto