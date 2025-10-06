¿Por que no utilizar el archivo de reporte.py de la carpeta AntiPatron?
La clase Reporte tiene varios motivos de cambio:

Fuente de datos:
Si mañana los datos vienen de una base de datos o API, hay que cambiar esta clase.

Procesamiento:
Si en lugar de promedio queremos suma o filtros, también hay que tocar la misma clase.

Formato de salida:
Si necesitamos HTML en vez de JSON, otra vez cambiamos la clase.

Entrega/almacenamiento:
Si en lugar de guardarlo en un archivo queremos enviarlo por email, también se toca la clase.

En conclusion, cualquier cambio brusco que necesitemos hacer hay que cambiar la misma clase, por ende pasa a 
tener por lo menos 4 motivos de cambios y eso pasa a no ser single responsibility principle. 

¿Cual es la manera correcta de aplicar el patron SPR?
La manera correcta es la de la carpeta Patron, porque l enfoque en el que esta planteado el proyecto reporte, en este caso, es la forma correcta de usar SRP, cada clase tiene solo una responsabilidad, de esta manera no se viola el patron de diseño. 


Se agregaron los patrones Open/Close Principle y Liskov Substitution Principle. 
El patron OCP dice que las clases deben estar abiertas para extensión, pero cerradas para modificación 
El patron LSP dice que una clase hija tienen que poder reemplazar los objetos de su clase padre sin alterar el comportamiento esperado. 