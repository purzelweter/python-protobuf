compile:
	$(info >>> $@)
	python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. root.proto a/a.proto b/b.proto