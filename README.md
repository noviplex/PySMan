# PySMan

Lightweight Service Manager for Python projects

## Installation

To install PySMan, use the following command:

```bash
pip install PySMan 
```

## Usage

To register a service with PySMan, use the following code snippet:

```python
from pysman import ServiceManager
service_manager = ServiceManager()
service_manager.register_service(service_class)
```

Do not forget to load all dependencies. Class dependencies will be automatically resolved as you register your service.
