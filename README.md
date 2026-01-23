# PySMan

Lightweight Service Manager for Python projects. Supports both autoloading and registering services

## Installation

To install PySMan, use the following command:

```bash
pip install pysman 
```

## Usage

To autoload your services with PySMan, use it as follows:

```python
from project import ServiceClassA, ServiceClassB
from pysman import ServiceManager

service_manager = ServiceManager()
service_manager.autoload_services([ServiceClassA, ServiceClassB])
```

To register a service with PySMan, use it as follows:

```python
from project import ServiceClassA
from pysman import ServiceManager

service_manager = ServiceManager()
my_configuration = "config"
service_class = ServiceClassA(my_configuration)
service_manager.register_services([service_class])
```

For more information, see how it is used in tests.
