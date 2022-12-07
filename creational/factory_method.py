from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    @abstractmethod
    def release(self):
        pass


class Car(IProduct):
    def release(self):
        return "Car released"


class Truck(IProduct):
    def release(self):
        return "Truck released"


class IWorkShop(metaclass=ABCMeta):
    @abstractmethod
    def create(self) -> IProduct:
        pass


class CarWorkShop(IWorkShop):
    def create(self) -> IProduct:
        return Car()


class TruckWorkShop(IWorkShop):
    def create(self) -> IProduct:
        return Truck()


def main():
    print(CarWorkShop().create())
    print(TruckWorkShop().create())


if __name__ == "__main__":
    main()