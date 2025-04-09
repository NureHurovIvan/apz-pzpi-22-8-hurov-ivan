from abc import ABC, abstractmethod 
 
# Реалізація 
class Device(ABC): 
    @abstractmethod 
    def turn_on(self): 
        pass 
 
    @abstractmethod 
    def turn_off(self): 
        pass 
 
class TV(Device): 
    def turn_on(self): 
        print("TV is now ON") 
 
    def turn_off(self): 
        print("TV is now OFF") 
 
class Radio(Device): 
    def turn_on(self): 
        print("Radio is now ON") 
 
    def turn_off(self): 
        print("Radio is now OFF") 
 
# Абстракція 
class RemoteControl: 
    def __init__(self, device: Device): 
        self.device = device 
def press_power(self): 
print("Power button pressed:") 
self.device.turn_on() 
# Тестування 
tv_remote = RemoteControl(TV()) 
radio_remote = RemoteControl(Radio()) 
tv_remote.press_power() 
radio_remote.press_power()
