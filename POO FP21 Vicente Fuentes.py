import math
class Triangulo:
    def __init__(self,lado1,lado2,lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
    def __str__(self):
        return f'triangulo de lados {self.lado1}, {self.lado2}, y {self.lado3}'
    
    def tipo_de_triangulo(self):
        if self.lado1==self.lado2==self.lado3:
            return f'es un triangulo de lado equilatero'
        else:
            if self.lado1==self.lado2!=self.lado3 or self.lado1==self.lado3!=self.lado2 or self.lado2==self.lado3!=self.lado1:
                return f'es un triangulo de tipo isósceles'
            else:
                return f'es un triangulo de tipo escaleno'
    
    def area(self):
        
        if self.lado1==self.lado2==self.lado3:
            return f'el area de dicho triangulo es de {self.lado1*(math.sqrt(3)/4)}'
        
        if self.lado1==self.lado2!=self.lado3 or self.lado2==self.lado3!=self.lado1:
            return f'el area de dicho triangulo es de {(self.lado1*self.lado3)/2}'
        if self.lado1==self.lado3!=self.lado2:
            return f'el area de dicho triangulo es de {(self.lado1*self.lado2)/2}'

        if self.lado1!=self.lado3!=self.lado2:
            semiperimetro=(self.lado1+self.lado2+self.lado3)/2
            return f'el area de dicho triangulo es de {math.sqrt(semiperimetro*(semiperimetro-self.lado1)*(semiperimetro-self.lado2)*(semiperimetro-self.lado3))}'
    
    def perimetro(self):
        return f'el perimetro de dicho triangulo es de {self.lado1+self.lado2+self.lado3}'

t1 = Triangulo(3, 4, 5)
t2 = Triangulo(1, 5, 3)
t3 = Triangulo(4, 4, 3)
t4 = Triangulo(5, 5, 5)
t5 = Triangulo(5, 1, 1)
