# Generate proto files

- `python -m grpc_tools.protoc -Iproto_gen=. --python_out=. --pyi_out=. --grpc_python_out=. ./*.proto`