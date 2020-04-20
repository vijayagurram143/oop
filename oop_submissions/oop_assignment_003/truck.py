from car import Car
class Truck(Car):
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        if int(max_cargo_weight) < 0:
            raise ValueError('Invalid value for max_cargo_weight')
        else:
            self._max_cargo_weight = int(max_cargo_weight)
        self._cargo_weight =0   
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    @property
    def cargo_weight(self):
        return self._cargo_weight
    def sound_horn(self):
        if self.is_engine_started == True:
            print('Honk Honk')
        else:
          print('Start the engine to sound_horn')
    def load(self,loading):
        #self._cargo_weight = int(loading)
        if loading < 0:
            raise ValueError("Invalid value for cargo_weight")
        elif self._current_speed == 0:
            if self._cargo_weight + loading <= self._max_cargo_weight:
              self._cargo_weight += loading
            else:
              print('Cannot load cargo more than max limit: {}'.format(self._max_cargo_weight))
        else:
            print('Cannot load cargo during motion')
    def unload(self,loading):
        self._loading = int(loading)
        if self._is_engine_started == False or self._current_speed == 0:
            if self._loading > self._max_cargo_weight:
                print('Cannot unload cargo more than max limit: {}'.format(self._max_cargo_weight))
            elif self._loading < 0:
                raise ValueError("Invalid value for cargo_weight")
            elif self._loading < self._max_cargo_weight and self._cargo_weight < self._max_cargo_weight:
                self._cargo_weight = self._cargo_weight - self._loading
        elif self._is_engine_started == True:
            print('Cannot unload cargo during motion')
            