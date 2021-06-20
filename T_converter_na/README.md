# Temperature Convert
 
This tool convert the temperatures beteween Celsius, Fahrenheit, Kelvin and Rankine.
 
## Instalation 
 
From testpypi
~~~
pip install -i https://test.pypi.org/simple/ t-converter-na==0.0.1
~~~
 
## How to use it
 
~~~
# Para invocar la libreria use
from t_converter_na import convertions as cvt

# Cree un objeto de alguna de las clases de Temperatura
fharenheit = cvt.Fahrenheit()
celcius = cvt.Celsius()

# Para transformar use los metodos que tiene la clase.
fharenheit.F_to_K(50)
~~~
