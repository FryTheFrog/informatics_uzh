from abc import ABC, abstractmethod

class Car(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def get_remaining_range(self):
        pass

    @abstractmethod
    def drive(self, dist):
        pass