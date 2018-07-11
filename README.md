## Estados y Comportamientos

Los estados son datos, variables, propiedades, atributos (ej. color, marca, etc.) o constantes. Los comportamientos o métodos de una clase se refieren a las acciones que son capaces de hacer los objetos (mover, subir, cantar, etc.). 


#### Método constructor

El método `__init__` es el método constructor de la clase. Este método es usado para inicializar datos, puede recibir parámetros que estarán relacionados al comportamiento o estados de la clase.

```python
class Car:
  #método constructor 
  def __init__(self):
    print("Este es el método constructor.")

```

El argumento para este método constructor es la palabra `self`, la cual es una referencia a objetos que están basados en esta clase. De esta manera, para referenciar instancias u objetos de la clase, `self` siempre será el primer parámetro.

#### Variables de instancia y métodos de instancia

Las variables de instancia son propiedad de instancias de la clase. Para cada objeto o instancia de una clase, las variables de instancia son diferentes.

Del ejemplo anterior vamos a crear dos objetos `Car` (`audi`, `minicooper`). Los dos pueden contener información diferente como `brand` y `color` .  

```python
class Car:
    def __init__(self, brand, color):
        pass


def main():
	#instancias de Car
	audi = Car("audi", "black")
	minicooper = Car("minicooper", "red")

if __name__ == "__main__":
    main()
```

Las `variables de instancia` sirven para darle seguimiento a `brand` y `color` y serán diferentes para cada instancia u objeto.

```python
class Car:
    def __init__(self, brand, color):
        #variable de instancia 1
        self.brand = brand
        #variable de instancia 2
        self.color = color


def main():
	#instancias de Car
	audi = Car("audi", "black")
	minicooper = Car("minicooper", "red")
	print(audi.brand)
	print(audi.color)
	print(minicooper.brand)
	print(minicooper.color)

if __name__ == "__main__":
    main()

```

A pesar de que estos objetos son diferentes a través de `brand` y `color` tienen comportamientos idénticos, podrán acelerar, frenar y desarrollar otros comportamientos de un `car`. 

```python
class Car:
    def __init__(self, brand, color):
        #variable de instancia 1
        self.brand = brand
        #variable de instancia 2
        self.color = color


	#comportamiento 1
	def acelerar(self):
	    "Acelerando"

	#comportamiento 2
	def frenar(self):
	    "Frenando"

	#otros comportamientos...


def main():
	#instancias de Car
	audi = Car("audi", "black")
	minicooper = Car("minicooper", "red")


if __name__ == "__main__":
    main()
 
```

Los comportamientos o métodos definidos en una clase se llaman `métodos de instancia`. Los métodos de instancia definidos en una clase pueden ser utilizados por objetos o instancias de esa clase.

```python
class Car:
    def __init__(self, brand, color):
        #variable de instancia 1
        self.brand = brand
        #variable de instancia 2
        self.color = color

    #comportamiento 1
    def acelerar(self):
    	return "Acelerando"

    #comportamiento 2
    def frenar(self):
    	return "Frenando"

    #otros comportamientos...


def main():
	#instancias de Car
	audi = Car("audi", "black")
	minicooper = Car("minicooper", "red")
	#método de instancia 'acelerar'
	print(audi.acelerar())
	print(minicooper.acelerar())
	#método de instancia 'frenar'
	print(audi.frenar())
	print(minicooper.frenar())

if __name__ == "__main__":
    main()
```

Las `variables de instancia` permiten hacer un seguimiento del estado y los `métodos de instancia` muestran el comportamiento de los objetos.

## Métodos de clase

Los métodos de clase son métodos que no están ligados a un objeto o instancia, sino a una clase.

Los métodos de clase son marcados con el decorador `@classmethod`. En vez de aceptar un parámetro `self`, estos métodos toman un parámetro `cls` que apunta a una clase y no a la instancia u objeto cuando el método es llamado.

```python
class Car:
    def __init__(self, brand, color):
        #variable de instancia 1
        self.brand = brand
        #variable de instancia 2
        self.color = color

    #método de clase
    @classmethod
    def incrementar_velocidad(cls):
        return "Incrementando velocidad"

```

Los `métodos de clase` solamente pueden ser llamados usando la clase donde fueron definidos.

```python
class Car:
    def __init__(self, brand, color):
        #variable de instancia 1
        self.brand = brand
        #variable de instancia 2
        self.color = color

    #método de clase
    @classmethod
    def incrementar_velocidad(cls):
        return "Incrementando velocidad"


def main():
	#instancias de Car
	audi = Car("audi", "black")
	minicooper = Car("minicooper", "red")
	#método de clase 'incrementar_velocidad'
	print(Car.incrementar_velocidad())


if __name__ == "__main__":
    main()

```

## Variables de clase

Las variables de clase son propiedad de la clase misma, son compartidas por todas las instancias de la clase.

Las variables de clase son variables cuyos valores son los mismos para la clase y para todas sus instancias. Por convención una variable de clase en Python es definida afuera de todos los métodos y colocada justo debajo del encabezado de la clase y antes del método constructor y otros métodos.

Un ejemplo de variable de clase y método de clase es el siguiente:

```python
"""Clase 'Car' con variable de clase y un método de clase"""


class Car:
  #variable de clase
  number_of_cars = 0
  
  #método constructor
  def __init__(self):
      Car.number_of_cars += 1

  #método de clase
  @classmethod
  def total_of_cars(cls):
      return cls.number_of_cars


def main():
    #obteniendo el número de carros a través del método de clase
    print(Car.total_of_cars())
    #>> 0
    #creando instancia 'car1'
    car1 = Car()
    #obteniendo el número de carros a través del método de clase
    print(Car.total_of_cars())
    #>> 1
    #creando instancia 'car2'
    car2 = Car()
    #creando instancia 'car3'
    car3 = Car()
    #creando instancia 'car4'
    car4 = Car()
    #obteniendo el número de carros a través del método de clase
    print(Car.total_of_cars())
    #>> 4

if __name__ == "__main__":
    main()

```

## Método Estático

Los métodos estáticos son un caso especial de métodos, son marcados con el decorador `@staticmethod`. Estos métodos pertenecen a una clase, sin embargo no usan del todo el objeto en sí.


```python
from random import randint

class Car:
  #variable de clase
  number_of_cars = 0
  
  #método constructor
  def __init__(self, model):
  	  self.model = model
  	  Car.number_of_cars += 1

  def numero_de_serie(self):
  	  return self.mix_serie_and_model(self.model)
  
  #método estático
  @staticmethod
  def mix_serie_and_model(string):
  	  serie = ""
  	  for i in range(7):
  	      serie += str((randint(0,9)))
  	  return string.lower() + serie

  #método de clase
  @classmethod
  def total_of_cars(cls):
      return cls.number_of_cars


def main():
    #obteniendo el número de carros a través del método de clase
    minicooper = Car("Minicooper")
    print(minicooper.numero_de_serie())
    print(minicooper.mix_serie_and_model("Toyota"))
    print(Car.mix_serie_and_model("Audi"))


if __name__ == "__main__":
    main()
```

Una ventaja de este tipo de método es que permite evitar el uso de un argumento `self` o `cls` que no sería usado. Pueden ser llamados a través de la clase o a través de la instancia.


## Ejercicio - Clase Bird

Crea una clase `Bird` que permita crear objetos `Bird` con diferentes nombres y que le permita al pájaro realizar las siguientes acciones: `who_am_i`, `flying` y `jump`. También es posible conocer el nombre del pájaro.

Desarrolla el código basado en las pruebas `specs` correspondientes.

```python
"""Bird class"""

...

```

```python
"""Ejemplo de objeto y salida"""

bird_3 = Bird("Zulu")

print(bird_3.jump())
#>> "Saltando..."

print(bird_3.fly(20))
#>> "Volando 20 mts..."

print(bird_3.fly(10))
#>> "Volando 30 mts..."

print(Bird.who_am_i())
#>> "Soy un pájaro"
```

```python
#Test Driven Development - TDD
$ test_bird.py
```

