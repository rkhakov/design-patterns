from abc import ABCMeta, abstractmethod


class IEngine(metaclass=ABCMeta):
    @abstractmethod
    def create_engine(self):
        pass


class JapaneseEngine(IEngine):
    def create_engine(self):
        print("Japanese engine created")


class GermanEngine(IEngine):
    def create_engine(self):
        print("German engine created")


class ICar(metaclass=ABCMeta):
    @abstractmethod
    def release_car(self, engine: IEngine):
        pass


class JapaneseCar(ICar):
    def release_car(self, engine: IEngine):
        engine.create_engine()
        print("Japanese car released")
    

class GermanCar(ICar):
    def release_car(self, engine: IEngine):
        engine.create_engine()
        print("German car released")
    

class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_engine(self) -> IEngine:
        pass

    @abstractmethod
    def create_car(self) -> ICar:
        pass


class JapaneseFactory(IFactory):
    def create_engine(self) -> IEngine:
        return JapaneseEngine()
    
    def create_car(self) -> ICar:
        return JapaneseCar()

    
class GermanFactory(IFactory):
    def create_engine(self) -> IEngine:
        return GermanEngine()
    
    def create_car(self) -> ICar:
        return GermanCar()


def main():
    j_factory = JapaneseFactory()
    j_engine = j_factory.create_engine()
    j_car = j_factory.create_car()
    j_car.release_car(j_engine)

    g_factory = GermanFactory()
    g_car = g_factory.create_car()
    g_car.release_car(g_factory.create_engine())


if __name__ == "__main__":
    main()

