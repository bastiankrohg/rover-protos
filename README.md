# Mars Rover Protos
## Repository Structure
- mars_rover.proto: Contains protobuf message definitions and gRPC service specifications for rover operations.

### Prerequisites

Ensure the following tools are installed on your system:
- Protocol Buffers Compiler (protoc): Installation Guide
- gRPC Plugins for Code Generation:
    - For Python: grpcio-tools
    - For other languages, refer to the respective gRPC documentation.

### Generating Code from Protobuf Definitions

To generate code from the .proto files:
1.	Navigate to the directory containing mars_rover.proto:
```bash
cd path/to/rover_protos
````

2.	Generate Python code using grpcio-tools:
```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mars_rover.proto
```

This command generates mars_rover_pb2.py and mars_rover_pb2_grpc.py in the current directory.

For other programming languages, use the appropriate plugins and follow their specific instructions.

### Integration with Other Modules

The generated code serves as the communication interface between various modules:
- rover-coral: Interacts with the mapping module using the generated stubs.
- rover-pi: Utilizes the protobuf definitions to handle hardware control messages.

Ensure that all modules use the same version of the generated code to maintain compatibility.

### Updating Protobuf Definitions

When modifying mars_rover.proto:
1.	Edit mars_rover.proto with the necessary changes.
2.	Regenerate the code for all target languages as outlined above.
3.	Update the submodules for all dependent modules (rover-pi, rover-coral, smart_rover, ...) using:
```bash
git submodule update --remote --recursive
```

NB! When updating the protos, you may have to change the import statement inside mars_rover_pb2_grpc.py, going from a
```python
import mars_rover_pb2_grpc as mars__rover__pb2__grpc
# To instead be 
from . import mars_rover_pb2_grpc as mars__rover__pb2__grpc
```

This process ensures that all components remain synchronized with the latest communication protocols.

Additional Resources
	•	Protocol Buffers Documentation: https://developers.google.com/protocol-buffers
	•	gRPC Documentation: https://grpc.io/docs/
