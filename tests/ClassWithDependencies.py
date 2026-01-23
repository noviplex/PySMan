from tests.DependencyA import DependencyA
from tests.DependencyB import DependencyB

class ClassWithDependencies:
    def __init__(self, dependency_a: DependencyA, dependency_b: DependencyB):
        self.dependency_a = dependency_a
        self.dependency_b = dependency_b
