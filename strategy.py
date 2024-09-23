from abc import abstractmethod, ABC


class Strategy(ABC):

    @abstractmethod
    def player_move(self, history):
        pass

    @abstractmethod
    def get_name(self):
        pass
