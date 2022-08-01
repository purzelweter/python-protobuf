compile:
	$(info >>> $@)
	python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. --go_out=$(CURDIR) --go_opt=paths=source_relative --go-grpc_out=$(CURDIR) --go-grpc_opt=paths=source_relative root.proto
	python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. --go_out=$(CURDIR) --go_opt=paths=source_relative --go-grpc_out=$(CURDIR) --go-grpc_opt=paths=source_relative a/a.proto
	python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. --go_out=$(CURDIR) --go_opt=paths=source_relative --go-grpc_out=$(CURDIR) --go-grpc_opt=paths=source_relative b/b.proto