class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part = real_part
        self.imaginary_part = imaginary_part
        if isinstance(self.real_part,str) and isinstance(self.imaginary_part,str):
            raise ValueError('Invalid value for real and imaginary part')
        if isinstance(self.real_part,str):
            raise ValueError('Invalid value for real part')
        
        if isinstance(self.imaginary_part,str):
            raise ValueError('Invalid value for imaginary part')
            
             
        '''if self.real_part == str(self.real_part) and self:
            raise ValueError('Invalid value for real and imaginary part')
            
        if self.real_part == str(self.real_part):
            raise ValueError('Invalid value for real part')
            
        if self.imaginary_part == str(self.imaginary_part):
            raise ValueError('Invalid value for imaginary part')
            
        self.real_part = int(real_part)
        self.imaginary_part = int(imaginary_part)
        
        '''
            
    def __add__(self,other):
      self.real_part = self.real_part + other.real_part
      self.imaginary_part = self.imaginary_part + other.imaginary_part
      return self     
    
    def __sub__(self,other):
      self.real_part = self.real_part - other.real_part
      self.imaginary_part = self.imaginary_part - other.imaginary_part
      return self     
    
    def __mul__(self,other):
      return ComplexNumber(self.real_part * other.real_part-self.imaginary_part * other.imaginary_part,self.real_part*other.imaginary_part+other.real_part*self.imaginary_part)
   
    def __truediv__(self,other):
        abs_value = other.real_part**2+other.imaginary_part**2
        return ComplexNumber((self.real_part * other.real_part+self.imaginary_part * other.imaginary_part)/abs_value,(self.imaginary_part * other.real_part - self.real_part * other.imaginary_part)/abs_value)
    
    def __str__(self):
      if self.imaginary_part >=0:
        return'{}+{}i'.format(self.real_part,self.imaginary_part)
      else:
        return'{}{}i'.format(self.real_part,self.imaginary_part)
        
    def conjugate(self):
        return ComplexNumber(self.real_part,-self.imaginary_part)
        
    def __abs__(self):
        self.real_part = ((self.real_part**2)+(self.imaginary_part**2))**0.5
        return (round(self.real_part,3))
        
    def __eq__(self,other):     
            if self.real_part == other.real_part and self.imaginary_part == other.imaginary_part:
                 return True
            else:
                 return False
                 
one_plus_two_i = ComplexNumber(1,2)
absolute_value = abs(one_plus_two_i)
print(absolute_value)                 