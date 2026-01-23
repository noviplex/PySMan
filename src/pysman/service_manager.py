from inspect import signature


class ServiceManager:
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized'):
            return
        self.service_container = {}
        self.aliases = {}
        self._initialized = True

    def get_service(self, service_name):
        return self.service_container[service_name]

    def autoload_service(self, service):
        parameters = []

        try:
            dependencies = signature(service).parameters
        except ValueError:
            raise ValueError("Dependencies must be a class or a callable")

        if len(dependencies) == 0:
            instantiated = service()
            self.service_container[service.__name__] = instantiated
            return instantiated
        else:
            for dependency_name in dependencies:

                dependency = dependencies[dependency_name].annotation

                if dependency.__name__ in self.aliases:
                    dependency = self.aliases[dependency.__name__]

                if dependency.__name__ in self.service_container:
                    parameters.append(
                        self.service_container[dependency.__name__]
                    )
                else:
                    parameters.append(self.autoload_service(dependency))

            instantiated = service(*parameters)
            self.service_container[service.__name__] = instantiated
            return instantiated

    def autoload_services(self, services):
        for service in services:
            self.autoload_service(service)

    def register_service(self, service_instance):
        self.service_container[service_instance.__class__.__name__] = service_instance

    def register_services(self, service_instances: list):
        for service_instance in service_instances:
            self.service_container[service_instance.__class__.__name__] = service_instance

    def register_alias(self, alias_name, alias_class):
        self.aliases[alias_name] = alias_class

    def register_aliases(self, alias_services: dict):
        self.aliases = alias_services
