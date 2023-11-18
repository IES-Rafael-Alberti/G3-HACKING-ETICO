# Blackbird

</br>

![portada](./herramientas/img/portadabb.png)

**Integrantes**

- Guerrero Merlo, Sergio
- Ladrón de Guevara García, Raúl
- Romero Oliva, Christian
- Cumbrera López, Juan Manuel

## Índice

1. [Introducción](#introducción)
2. [Usos posibles](#para-que-sirve)
3. [Instalación](#instalación)
4. [Funcionamiento](#funcionamiento)
5. [Conclusión](#conclusión)
6. [Bibliografía](#bibliografía)

## Introducción

En esta primera parte del proyecto se han investigado numerosas herramientas OSINT de varios tipos, ya sean aplicaciones web, aplicación instalable o línea de comandos (*CLI*). 

Al encontrar que muchas de ellas solicitaban trámites como registro previo o diretamente opciones de pago para poder usarlas, decidimos limitar la lista de nuestras herramientas seleccionadas a aquellas con una relación mayor de facilidad de uso frente a calidad de información. De la lista hemos descartado algunas que consideramos bastante buenas como ***Hunter.io***, ***Breachdirectory.org***, ***Intelligence_X*** o algunas más con un enfoque menos general como ***jasperan/WhatsappOSINT***.

Finalmente nos hemos decidido por BlackBird debido a que es una herramienta gratuita, instalable, sin trámites y que ofrece una información relativamente útil con sencillez.

## Para que sirve

Blackbird es una herramienta OSINT que podemos usar para buscar posibles cuentas en múltiples plataformas a través de un nombre de usuario en más de 500 sitios web. Cada vez que se genera una busqueda, ***Blackbird*** utiliza un *user-agent* aleatorio de una lista de más de 1000 para evitar ser bloqueada.

Esta herramienta nos permite además la posibilidad de obtener metadatos siempre que sea posible como por ejemplo: Nombre, Biografía, Ubicación y fotos de perfil.

Blackbird utiliza solicitudes HTTP de manera asíncrona, lo que permite una mayor velocidad en estas peticiones.

## Instalación

Para instalar esta herramienta tan solo debemos clonar el repositorio de github donde se encuentra ubicada y seguir los siguientes pasos:

```bash
sudo apt-get update
sudo apt upgrade

git clone https://github.com/p1ngul1n0/blackbird
```

Una vez que se ha clonado el repositorio nos movemos al mismo desde la terminal de Kali Linux.

```bash
cd blackbird
```

Blackbird funciona con python, por lo que necesitaremos instalar las dependencias con el siguiente comando:

```bash
pip install -r requeriments.txt
```

## Funcionamiento

Existen tres formas de utilizar esta herramienta. 

La primera de ellas es mediante la terminal (CLI), para usarla mediante esta vía entramos al directorio de la herramienta con:

```bash
cd blackbird
```

Y desde aquí ya podremos empezar a usar la herramienta. Con tan solo el siguiente comando podremos **buscar usuario y ver en que redes posee  una posible cuenta**:

```bash
python blackbird.py -u NombreUsuario
```

> Es posible que en lugar de `python` tengamos que usar `python3` en algunos casos

La herramienta nos mostrará solo las cuentas de usuario que ha encontrado. Sin embargo, es posible que existan cuentas que la herramienta sea incapaz de encontrar por diversos motivos, por lo que sería interesante ver todas las búsquedas que se han realizado durante la ejecución. Podríamos utilizar el siguiente comando para ver todos los resultados sean cuales sean:

```bash
python blackbird.py -u crash --show-all
```

También podemos exportar el resultado a un fichero con extensión .csv de la siguiente manera.

```bash
python blackbird.py -u crash --csv
```

Podemos también ver la **lista de sitios que son compatibles** con la herramienta:

```bash
python blackbird.py --list-sites
```

La **segunda forma** de utilizar esta herramienta es levantarla en un servidor web local. Normalmente se levanta en el puerto 9797 (http://127.0.0.1:9797). 

```bash
python blackbird.py --web
```

Al utilizar esta segunda posibilidad, nos seguirá guardando en la carpeta results del repositorio que hemos clonado, los ficheros con el nombre del usuario y acabado en .json.

Además, mediante la interfaz web tendremos una opción para exportar los resulados a un archivo pdf.

La tercera forma y última es utilizando la web que el propio desarrollador de la misma ha publicado https://blackbird-osint.herokuapp.com/.

## Conclusión

En general Blackbird nos va a permitir agilizar el proceso de búsqueda y amplicar nuestra superficie de ataque rápidamente.

Por supuesto, por sí sola su utilidad es algo reducida, pero en combinación con otras herramientas puede resultar de bastante ayuda. Usada en conjunto con buscadores de bases de datos filtradas o con información personal ya obtenida o conocida previamente podríamos fácilmente cruzar datos para descubrir posibles brechas de seguridad. 

Bien sabemos que no todo el mundo mantiene íntegra el cien por cien de la superficie digital de su perfil.


## Bibliografía

- [https://github.com/p1ngul1n0/blackbird](https://github.com/p1ngul1n0/blackbird)
- [https://derechodelared.com/blackbird-cuentas-nombre-usuario/](https://derechodelared.com/blackbird-cuentas-nombre-usuario/)

![logo](./herramientas/img/logobb.png)
