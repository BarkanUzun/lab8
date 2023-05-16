from abc import ABC, abstractmethod
from collections import Counter


class AbstractCount(ABC):
    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(AbstractCount):
    def calculateFreqs(self):
        with open(self.address, 'r') as file:
            text = file.read()
            unique_letters = list(set(text))
            frequencies = [text.count(letter) for letter in unique_letters]
            result = [f"{letter} = {freq}" for letter, freq in zip(unique_letters, frequencies)]
            print(result)


class DictCount(AbstractCount):
    def calculateFreqs(self):
        with open(self.address, 'r') as file:
            text = file.read()
            frequencies = Counter(text)
            print(frequencies)


list_count = ListCount('weirdWords.txt')
list_count.calculateFreqs()

dict_count = DictCount('weirdWords.txt')
dict_count.calculateFreqs()
