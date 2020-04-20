class Car:
    
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self._color = color
        self._is_engine_started = False
        self._current_speed = 0
        
        if int(max_speed) < 0:
            raise ValueError('Invalid value for max_speed')
        else:
            self._max_speed = int(max_speed)
        
        if int(acceleration) < 0:
            raise ValueError('Invalid value for acceleration')
        else:
            self._acceleration = int(acceleration)
        
        if int(tyre_friction) < 0:
            raise ValueError('Invalid value for tyre_friction')
        else:
            self._tyre_friction = int(tyre_friction)
             
            

    @property
    def is_engine_started(self):
        return self._is_engine_started
    
    @property
    def max_speed(self):
        return self._max_speed
    
    @property
    def acceleration(self):
        return self._acceleration
    
    @property
    def tyre_friction(self):
        return self._tyre_friction
            
    @property
    def color(self):
        return self._color
    
    @property
    def current_speed(self):
        return self._current_speed 
    
    def start_engine(self):
        self._is_engine_started = True
    pass
    
    def apply_brakes(self):
        if self._current_speed > self._tyre_friction: 
           self._current_speed -= self._tyre_friction
        else:
          self._is_engine_started = False
          self._current_speed = 0
            
    pass

    def accelerate(self):
        if self._is_engine_started == True and self._current_speed <=self._max_speed:
          self._current_speed += self._acceleration
        elif self._is_engine_started == True and self._current_speed > self._max_speed:
          self._current_speed = self._max_speed    
        else:
            print('Start the engine to accelerate')
        pass 
    
    def sound_horn(self):
        if self._is_engine_started == True:
          print('Beep Beep')
        else:
          print('Start the engine to sound_horn')    
    pass
    
    def stop_engine(self):
       if self._is_engine_started == True:      
          self._is_engine_started = False
