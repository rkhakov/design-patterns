from abc import ABCMeta, abstractmethod


class IScale(metaclass=ABCMeta):
    @abstractmethod
    def get_weight(self) -> float:
        pass


class RussianScales(IScale):
    def __init__(self, weight: float):
        self._weight = weight

    def get_weight(self) -> float:
        return self._weight


class BritishScales(IScale):
    def __init__(self, weight: float):
        self._weight = weight
    
    def get_weight(self) -> float:
        return self._weight
    

class AdapterFromBritishToRussianScales(IScale):
    def __init__(self, british_scales: BritishScales):
        self._british_scales = british_scales
    
    def get_weight(self) -> float:
        return self._british_scales.get_weight() * 0.453


def main():
    kg: float = 55.
    lb: float = 55.

    r_scales = RussianScales(kg)
    b_scales = AdapterFromBritishToRussianScales(BritishScales(lb))

    print(r_scales.get_weight())
    print(b_scales.get_weight())


if __name__ == "__main__":
    main()