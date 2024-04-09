# Alumno: Mariano Lopez 
Ingenieria Informatica
## Para saber su funcionamiento
    def is_prime(valor):  #Define una función llamada is_prime que toma un parámetro llamado valor. Esta función determina si el valor proporcionado es un número primo.
    
        divisor = valor - 1   #Esta variable se usará para verificar si valor es divisible por algún número entre (valor - 1) y 2 
    
        while divisor>1:      #Inicia un bucle while que se ejecutará mientras el valor de divisor sea mayor que 1.
       
            if valor%divisor==0:   #Dentro del bucle while, comprueba si valor es divisible por divisor usando el operador %, que devuelve el resto de la división. Si el resto es cero, significa que valor es divisible por divisor, lo que indica que valor no es un número primo.
            
                return False      #Si valor es divisible por divisor, la función retorna False, lo que indica que el número no es primo.
       
            divisor=divisor-1     #Si valor no es divisible por divisor, se disminuye el valor de divisor en 1 para pasar al siguiente número menor.
    
        return True       #Si el bucle while se ejecuta completamente sin encontrar ningún divisor que pueda dividir valor, entonces valor no es divisible por ningún número entre (valor - 1) y 2, lo que significa que valor es primo. En este caso, la función retorna True.

## Para comprobar si funciona
    -Realizar un git clone (link con el SSH del repo) en la carpeta donde quieras almacenar el archivo.
    -Una vez con los direcctorios en su computadora los busca en la terminal usando cd (nombre de la carpeta donde se encuentra el archivo)
    -Ya en la carpeta donde se encuentra el archivo ejecutamos python3 test_nprimos.py
    -Luego de esto y finalmente se ejecutaran los test para comprobar si el codigo funciona correctamete.