from abc import ABCMeta, abstractmethod


class Phone:
    def __init__(self):
        self._data = []
    
    def append_data(self, data: str):
        self._data.append(data)
    
    def about_phone(self):
        return self._data


class IDeveloper(metaclass=ABCMeta):
    @abstractmethod
    def create_display(self):
        pass

    @abstractmethod
    def create_box(self):
        pass

    @abstractmethod
    def install_system(self):
        pass

    @abstractmethod
    def get_phone(self) -> Phone:
        pass


class AndroidDeveloper(IDeveloper):
    def __init__(self):
        self._phone = Phone()
    
    def create_display(self):
        self._phone.append_data("Display was produced")
    
    def create_box(self):
        self._phone.append_data("Phone body was produced")
    
    def install_system(self):
        self._phone.append_data("Android system was installed")
    
    def get_phone(self) -> Phone:
        return self._phone


class IPhoneDeveloper(IDeveloper):
    def __init__(self):
        self._phone = Phone()
    
    def create_display(self):
        self._phone.append_data("Display was produced")
    
    def create_box(self):
        self._phone.append_data("Phone body was produced")
    
    def install_system(self):
        self._phone.append_data("IOS system was installed")
    
    def get_phone(self) -> Phone:
        return self._phone


class Director:
    def __init__(self, developer: IDeveloper):
        self._developer = developer
    
    def set_developer(self, developer: IDeveloper):
        self._developer = developer
    
    def build_phone(self) -> Phone:
        self._developer.create_box()
        self._developer.create_display()
        return self._developer.get_phone()
    
    def build_phone_with_preinstalled_os(self):
        self._developer.create_box()
        self._developer.create_display()
        self._developer.install_system()
        return self._developer.get_phone()


def main():
    director = Director(AndroidDeveloper())
    phone = director.build_phone()
    print(phone.about_phone())

    director.set_developer(IPhoneDeveloper())
    iphone = director.build_phone_with_preinstalled_os()
    print(iphone.about_phone())


if __name__ == "__main__":
    main()
