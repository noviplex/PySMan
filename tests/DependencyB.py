from tests.DependencyC import DependencyC


class DependencyB:
    def __init__(self, dependency_c: DependencyC):
        self.dependency_c = dependency_c
