from tests.DependencyA import DependencyA
from tests.DependencyB import DependencyB


class ClassWithDependenciesAndVariables:
    def __init__(
            self,
            dependency_a: DependencyA,
            dependency_b: DependencyB,
            config_value: str = "default_config",
    ):
        self.dependency_a = dependency_a
        self.dependency_b = dependency_b
        self.config_value = config_value
