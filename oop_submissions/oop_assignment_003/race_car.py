import math
from car import Car

class RaceCar(Car):
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._nitro = 0
        
    @property
    def nitro(self):
        return self._nitro
        
    def sound_horn(self):
        if self._is_engine_started == True:
          print('Peep Peep\nBeep Beep')
        else:
          print('Start the engine to sound_horn')    
          
    def accelerate(self):
        if self._nitro !=0:
            self._current_speed += (math.ceil(self._acceleration * 0.3))
            self._nitro -=  10
        super().accelerate()
        
    def apply_brakes(self):
        if (self._current_speed >self._max_speed/2):
            self._nitro += 10
        super().apply_brakes()
            
# racecar=RaceCar('red','250','50','30')
# racecar.start_engine()
# racecar.accelerate()
# racecar.accelerate()
# racecar.accelerate()
# print(racecar._current_speed)
# racecar.apply_brakes()
# print(racecar._current_speed)
# print(racecar._nitro)
# racecar.accelerate()
# print(racecar._current_speed)
# print(racecar._nitro)
# racecar.sound_horn()