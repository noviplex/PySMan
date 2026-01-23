import unittest

from src.pysman.service_manager import ServiceManager
from tests.ClassWithDependencies import ClassWithDependencies
from tests.ClassWithDependenciesAndVariables import ClassWithDependenciesAndVariables
from tests.DependencyA import DependencyA
from tests.DependencyB import DependencyB


class TestInstantiation(unittest.TestCase):
    #  when_autoloading_services_with_only_dependencies_then_dependencies_passed_as_class_instances
    def test_autoloading_with_only_dependencies(self):
        service_manager: ServiceManager = ServiceManager()
        service_manager.autoload_services([
            ClassWithDependencies,
        ])
        instance = service_manager.get_service("ClassWithDependencies")

        self.assertIsInstance(instance.dependency_a, DependencyA)
        self.assertIsInstance(instance.dependency_b, DependencyB)

    # when_autoloading_services_with_non_class_dependencies_then_non_class_dependencies_passed_as_parameter
    def test_registering_with_dependencies_and_variables(self):
        service_manager: ServiceManager = ServiceManager()
        service_manager.autoload_services([
            DependencyA,
            DependencyB
        ])
        service_manager.register_service(
            ClassWithDependenciesAndVariables(
                service_manager.get_service("DependencyA"),
                service_manager.get_service("DependencyB"),
                config_value="my_config"
            )
        )
        instance = service_manager.get_service(
            "ClassWithDependenciesAndVariables"
        )

        self.assertIs(instance.config_value, "my_config")
        self.assertIsInstance(instance.dependency_a, DependencyA)
        self.assertIsInstance(instance.dependency_b, DependencyB)

    #  when_autoloading_services_with_dependencies_and_variables_then_raises_exception
    def test_autoloading_with_dependencies_and_variables_will_fail(self):
        service_manager: ServiceManager = ServiceManager()

        with self.assertRaises(ValueError):
            service_manager.autoload_services([
                ClassWithDependenciesAndVariables,
            ])
