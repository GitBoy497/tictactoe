from abc import ABC, abstractmethod

class BotInterface(ABC):
    """An interface for bots."""

    @abstractmethod
    def play(self):
        """Play a turn in a tic tac toe game."""
        pass