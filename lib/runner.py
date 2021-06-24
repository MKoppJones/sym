import abc

class Runner(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        raise NotImplementedError