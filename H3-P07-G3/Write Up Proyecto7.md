
# kali - PC-1
### Escaneo de red

Primero de todo vamos a escanear la red para comprobar cual es la dirección IP de PC-1.
![](./img/Pasted%20image%2020240424190849.png)

### Escaneo de puertos

Ahora que sabemos la dirección IP de la máquina que vamos a vulnerar, hacemos un escaneo de los puertos con nmap.
![](./img/Pasted%20image%2020240424194525.png)
Como podemos comprobar, la máquina tiene un puerto 3389 abierto. Vamos a intentar comprobar si es vulnerable a ms12-020 para ello usaremos metasploit.
Creamos un workspace para el pentesting que estamos haciendo.
![](./img/Pasted%20image%2020240424194733.png)

### Obtener acceso

Una vez creado, buscamos por ms12-020 con search. Usamos el 0 y añadiendo de manera global el RHOSTS con setg, ejecutamos el scanner para comprobar que es vulnerable.
![](./img/Pasted%20image%2020240424194834.png)
Pero a mi esto no me interesa ya que lo que realmente me interesa es conseguir una shell meterpreter de manera fácil. 
Así que vamos a usar bluekeep para ver si podemos conseguirlo. Primero escaneamos para comprobar que es vulnerable a dicha vulnerabilidad usando el 0.
![](./img/Pasted%20image%2020240424195058.png)
Como podemos comprobar, la máquina es 100% vulnerable.
![](./img/Pasted%20image%2020240424195141.png)
Así que ahora vamos a intentar conseguir una shell de meterpreter en esta máquina. Volvemos a buscar bluekeep y usamos esta vez el tercero. Comprobamos las opciones y seteamos el LHOST con nuestra IP y el target lo ponemos en 2.
![](Pasted%20image%2020240424200507.png)
Lo ejecutamos para obtener la shell y como vemos somos SYSTEM.
![](Pasted%20image%2020240424200950.png)
Estas vulnerabilidades han sido encontradas buscando en google como explotar el puerto 3389.
### Crear túnel con chisel

Ahora que estamos dentro, nos interesa crear un túnel con chisel pero primero vamos a ejecutar el módulo autoroute para obtener las rutas de la sesión que se ha generado.
![](./img/Pasted%20image%2020240424201330.png)
Ya tenemos las rutas, vamos a cambar a /Temp para subir con upload chisel.exe que se encuentra en nuestro kali.
![](./img/Pasted%20image%2020240424201643.png)
En nuestro kali ejecutamos el servidor de chisel.
![](./img/Pasted%20image%2020240424201740.png)
Y en el PC-1 ejecutamos el comando para ser cliente y crear el túnel pero primero tenemos que generar la shell con el comando del mismo nombre de meterpreter. Para ello colocamos nuestra dirección IP con R: seguido del puerto que está configurado en proxychains4.conf.
![](./img/Pasted%20image%2020240424201949.png)

# PC-1 - PC-2

### Escaneo de puertos

Siguiendo nuestro esquema, la dirección IP del PC-2 sería 10.10.10.129. Para ello añadiremos proxychains4 antes del comando de nmap. Esta vez buscaremos los puertos 21, 22, 80 y 445 por ahora ya que suelen ser de los puertos más típicos.  Tras el intento no me cogía nada entonces probé con la .130 y ahí si me los pilló como filtered.
![](./img/Pasted%20image%2020240424210445.png)

## Comprobación de servicios

Como aparecen en filtered al estar detrás de un firewall, vamos a intentar conectarnos en anónimo a ese ftp por ejemplo.
![](./img/Pasted%20image%2020240424211047.png)
No nos ha conectado, eso significa que posiblemente el puerto no esté abierto o no haya un usuario anónimo.  Vamos a probar lo mismo pero con cmb.
![](./img/Pasted%20image%2020240424211146.png)
¡Tenemos acceso anónimo! Ahora vamos a ver que contiene este usuario anónimo con ls. Vamos a descargar el fichero y comprobamos su contenido con cat. Tenemos 3 posibles contraseñas pero no los usuarios.
![](./img/Pasted%20image%2020240424211414.png)
Vamos a ver que shares contiene smbclient con smblienct -L, la dirección IP y la contraseña de nuestro kali. Tenemos un helios que podría ser un usuario al igual que anonymous.
![](./img/Pasted%20image%2020240424211909.png)
Probando una de las 3 contraseñas funcionó con qwerty.
![](./img/Pasted%20image%2020240424212116.png)
Nos descargamos los dos ficheros que contiene el usuario.
![](./img/Pasted%20image%2020240424212501.png)
Comprobamos el contenido de ambos ficheros. Leyendo el fichero research no he encontrado nada que sea interesante pero en todo.txt veo una posible ruta a una ¿Web?
![](./img/Pasted%20image%2020240424212720.png)
Primero vamos a comprobar que existe una página web con proxychains y firefox. 
![](./img/Pasted%20image%2020240424213101.png)
Como podemos ver si existe una página web.
![](./img/Pasted%20image%2020240424212805.png)
Vamos a probar ahora con la ruta.
![](./img/Pasted%20image%2020240424213039.png)
La ruta existe y encima podemos ver que es un wordpress.
![](./img/Pasted%20image%2020240424213020.png)
Si buscamos en google como vulnerar wordpress nos aparece un video de youtube con una herramienta.
![](./img/Pasted%20image%2020240424213424.png)
Si seguimos investigando un poco encontramos que tenemos que registrarnos para buscar con un token que nos genera los cve en su base de datos. La web usada es [Malcare](https://www.malcare.com/blog/how-to-use-wpscan/)
![](./img/Pasted%20image%2020240424214224.png)
Así que vamos a hacer exactamente lo mismo. Nos registramos y con nuestro token investigamos en la url. Como no ha funcionado no podemos seguir avanzando ya que las herramientas que hemos usado para escanear el wordpress, nos las bloqueaba el firewall.
![](./img/Pasted%20image%2020240424214955.png)


### Obtener acceso 

## PC-1 - PC-4

### Escaneo de puertos

Después de varios intentos sin exito las direcciones IP han cambiado. Siendo ahora la PC-2 la 10.10.10.129 y PC-1 la 10.10.10.130, escaneamos los puertos "más" comunes del PC-4. Pero nos aparecen todos los puertos cerrados sin motivo aparente.
