import threading


class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, value: str):
        self._value = value

    @property
    def value(self):
        return self._value

def test_singleton(value: str):
    print(Singleton(value).value)


def main():
    threading.Thread(target=test_singleton, args=("FOO",)).start()
    threading.Thread(target=test_singleton, args=("BAR",)).start()


if __name__ == "__main__":
    main()
