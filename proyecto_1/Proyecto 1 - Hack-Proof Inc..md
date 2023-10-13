# Grupo III

## Hacking Ético - Ciberseguridad en las TI

*Raúl Ladrón de Guevara*
*Juan Manuel Cumbrera López*
*Christian Romero Oliva*

# Índice

- [Introducción](#Introducción)
- [Vulnerabilidades Investigadas](#vulnerabilidades-investigadas)
  - [1 CVE-2023-43660 - ¿Warpgate?](#1-cve-2023-43660---warpgate)
    - [Descripción](#descripción)
    - [Impacto](#impacto)
    - [Exploración y Explotación](#exploración-y-explotación)
    - [Contramedidas](#contramedidas)
    - [Referencias](#referencias)
  - [2 CVE-2023-44466 Desbordamiento de búfer](#2-cve-2023-44466-desbordamiento-de-búfer)
    - [Descripción](#descripción)
    - [Impacto](#impacto)
    - [Exploración y Explotación](#exploración-y-explotación)
    - [Contramedidas](#contramedidas)
  - [3 CVE-2023-39191 - Kernel de Linux eBPF](#3-cve-2023-39191---kernel-de-linux-ebpf)
    - [Descripción](#descripción)
    - [Impacto](#impacto)
    - [Exploración y Explotación](#exploración-y-explotación)
    - [Contramedidas](#contramedidas)
  - [4 CVE-2021-3156 - Sudo (Baron Samedit)](#4-cve-2021-3156---sudo-baron-samedit)
    - [Descripción](#descripción)
    - [Impacto](#impacto)
    - [Exploración y Explotación](#exploración-y-explotación)
    - [Contramedidas](#contramedidas)
  - [5 CVE-2023-26604 - systemd 246](#5-cve-2023-26604---systemd-246)
    - [Descripción](#descripción)
    - [Impacto](#impacto)
    - [Exploración y Explotación](#exploración-y-explotación)
    - [Contramedidas](#contramedidas)
  - [6 CVE-2016-2414 - Minikin Android](#6-cve-2016-2414---minikin-android)
    - [Descripción](#descripción)
    - [Impacto](#impacto)
    - [Exploración y Explotación](#exploración-y-explotación)
    - [Contramedidas](#contramedidas)
  - [7 CVE-2022-2586 - Linux Kernel UAF](#7-cve-2022-2586---linux-kernel-uaf)
    - [Descripción](#descripción)
    - [Impacto](#impacto)
    - [Exploración y Explotación](#exploración-y-explotación)
    - [Contramedidas](#contramedidas)
  - [8 CVE-2018-4087 - iOS Core Bluetooth](#8-cve-2018-4087---ios-core-bluetooth)
    - [Descripción](#descripción)
    - [Impacto](#impacto)
    - [Exploración y Explotación](#exploración-y-explotación)
    - [Contramedidas](#contramedidas)
  - [9 Dirty pipe (CVE-2022-0847)](#9-dirty-pipe-cve-2022-0847)
    - [Descripción](#descripción)
    - [Impacto](#impacto)
    - [Exploración y Explotación](#exploración-y-explotación)
    - [Contramedidas](#contramedidas)
    
- [Conclusiones](#conclusiones)
- [Recomendaciones](#recomendaciones)

## Introducción

En el vasto campo de la ciberseguridad, la identificación y comprensión de las vulnerabilidades es un elemento clave en el aprendizaje como profesional. EN las operaciones de Red Team o Pentesting, las vulnerabilidades son un gran punto principal que un profesional de la ciberseguridad va a intentar buscar, corregir o explotar 

En este proyecto se realiza un análisis e investigación de una serie de vulnerabilidades en relación a varios sistemas operativos como Android o Linux. 

Se ofrece una breve clasificación de las mismas con diferentes secciones para ofrecer una información amigable y comprensible de un contenido altamente técnico.
## Vulnerabilidades Investigadas

### 1 CVE-2023-43660 - ¿Warpgate?

#### Descripción

La vulnerabilidad CVE-2023-43660 se produce debido a una falta de validación de entrada en el código utilizado para verificar las firmas de clave SSH, lo que podría proporcionar una clave SSH sin firma que el software Warpgate aceptará y ejecutará a un posible atacante.

#### Impacto

La vulnerabilidad discutida tiene un impacto grave en los sistemas vulnerables. Como las anteriores, esta permite a un atacante que pueda explotarla tomar el control total del sistema, acceder a datos confidenciales o causar daños.

Además de esto último, esta vulnerabilidad tendría las consecuencias siguientes, teniendo en cuenta los términos de confidencialidad, integridad y disponibilidad:

- **Confidencialidad:** El atacante podría acceder a datos confidenciales, como contraseñas, información financiera o datos personales.
- **Integridad:** El atacante podría modificar o destruir datos.
- **Disponibilidad:** El atacante podría interrumpir los servicios o sistemas.

#### Exploración y Explotación

Para explotar y hacer uso de esta vulnerabilidad, primero se debe tener acceso al sistema a atacar. Una vez que se ha conseguido el subsiguiente acceso, se puede proporcionar una clave SSH sin firma al software Warpgate. Este software aceptará la susodicha clave sin firma y ejecutará el código que contenga, el cual podrá ser usado por el hipotético atacante para controlar el sistema, además de acceder a datos confidenciales y/o producir daños en el mismo.

#### Contramedidas

A fin de reducir el riesgo de explotación de esta vulnerabilidad, exponemos algunas maneras de mantenerse a salvo:

- **Actualizar los sistemas a la última versión de Warpgate.** Esta versión corrige la vulnerabilidad CVE-2023-43660.
- **Limitar el acceso al software Warpgate.** Solo los usuarios autorizados deben tener acceso a este software.
- **Monitorear los sistemas en busca de signos de explotación de esta vulnerabilidad.** Los administradores de sistemas deben estar atentos a los signos de actividad maliciosa, como intentos de conectarse al sistema vulnerable con una clave SSH sin firma.

#### Referencias

[1]: **eBPF** (_Extended Berkeley Packet Filter_) es una máquina virtual que se ejecuta dentro del kernel de Linux. Esta funciona como un marco de programación que nos permite ejecutar de forma segura programas en código máquina en el kernel de Linux sin cambiar el código del mismo.
[2]: **CAP_BPF** Consiste en la capacidad de cargar y modificar programas BPF en el kernel.

### 2 CVE-2023-44466 Desbordamiento de búfer

#### Descripción

La vulnerabilidad CVE-2023-44466 es una vulnerabilidad de desbordamiento de búfer en el subsistema de mensajería del kernel de Linux, la cual permite a un atacante ejecutar código en un sistema vulnerable con privilegios de usuario root.

Esta se produce debido a una falta de validación de entrada en el código que se utiliza para procesar los mensajes enviados al subsistema de mensajería del kernel de Linux. Esto significa que un atacante puede proporcionar un mensaje malicioso que el kernel procesará incorrectamente, provocando un desbordamiento de búfer.

#### Impacto

Esta vulnerabilidad tiene un impacto grave en los sistemas vulnerables, ya que explotarla puede garantizar la toma de control sobre el sistema, el acceso a datos confidenciales o la posibilidad de causar daños.

La vulnerabilidad en cuestión puede tener una serie de posibles consecuencias puestas en términos de confidencialidad, integridad y disponibilidad:

- **Confidencialidad:** El atacante podría acceder a datos confidenciales, como contraseñas, información financiera o datos personales.
- **Integridad:** El atacante podría modificar o destruir datos.
- **Disponibilidad:** El atacante podría interrumpir los servicios o sistemas.

#### Exploración y Explotación

Para explotar esta vulnerabilidad, un atacante debe tener acceso al sistema vulnerable. Una vez que este haya conseguido acceso al sistema, podrá enviar un mensaje malicioso al subsistema de mensajería del kernel de Linux, el cual lo procesará de forma incorrecta, produciendo así un desbordamiento del búfer. Éste podría permitir al atacante ejecutar código arbitrario en el contexto del kernel.

#### Contramedidas

A continuación resumimos algunas medidas que los usuarios deben tomar, con el objeto de evitar o limitar el riesgo de explotación de esta vulnerabilidad:

- **Actualizar los sistemas a la última versión del kernel de Linux.** Esta versión corrige la vulnerabilidad CVE-2023-44466.
- **Limitar el acceso al subsistema de mensajería del kernel de Linux.** Solo los usuarios autorizados deben tener acceso a este subsistema.
- **Monitorear los sistemas en busca de signos de explotación de esta vulnerabilidad.** Los administradores de sistemas deben estar atentos a los signos de actividad maliciosa, como intentos de enviar mensajes maliciosos al subsistema de mensajería del kernel de Linux.


### 3 CVE-2023-39191 - Kernel de Linux eBPF

#### Descripción

La vulnerabilidad CVE-2023-39191 es una vulnerabilidad de validación de entrada en el subsistema _eBPF_[^1] del kernel de Linux. Estos programas se pueden utilizar para una variedad de propósitos, como la supervisión del rendimiento, el filtrado de tráfico y la creación de reglas de firewall.

IntroducciónEsta vulnerabilidad se produce debido a una falta de validación de entrada en el subsistema eBPF. Esto significa que un atacante puede proporcionar datos maliciosos a un programa eBPF que el kernel ejecutará sin verificar.

#### Impacto

Esta vulnerabilidad tiene un impacto grave en los sistemas vulnerables, dado que un atacante que pueda explotarla puede ejecutar código en el contexto del kernel. Esto le permitiría al atacante tomar el control total del sistema, acceder a datos confidenciales o causar múltiples daños.

El impacto potencial de la vulnerabilidad en términos de confidencialidad, integridad y disponibilidad de los datos o sistemas afectados es el siguiente:

- **Confidencialidad:** El atacante podría acceder a datos confidenciales, como contraseñas, información financiera o datos personales.
- **Integridad:** El atacante podría modificar o destruir datos.
- **Disponibilidad:** El atacante podría interrumpir los servicios o sistemas.

#### Exploración y Explotación

Para explotar esta vulnerabilidad, un atacante debe tener privilegios _CAP_BPF_[^2]. Estos privilegios se pueden obtener mediante una variedad de métodos, como explotar otra vulnerabilidad o obtener acceso a un sistema comprometido.

Una vez que el atacante tenga dichos privilegios, podrá proporcionar datos maliciosos a un programa eBPF, los cuales serán ejecutados por el kernel. Este código malicioso se podrá utilizar para controlar el sistema, acceder a datos confidenciales o causar daños.

#### Contramedidas

Para mitigar el riesgo de explotación de esta vulnerabilidad, los usuarios deben tomar las siguientes medidas:

- **Actualizar los sistemas a la última versión del kernel de Linux.** Esta versión corrige la vulnerabilidad CVE-2023-39191.
- **Limitar el acceso a los privilegios CAP_BPF.** Solo los usuarios autorizados deben tener estos privilegios.
- **Implementar controles de acceso para proteger los programas eBPF.** Estos controles pueden ayudar a evitar que los atacantes proporcionen datos maliciosos a los programas eBPF.
- **Monitorear los sistemas en busca de signos de explotación de esta vulnerabilidad.** Los administradores de sistemas deben estar atentos a los signos de actividad maliciosa, como intentos de ejecutar código arbitrario en el contexto del kernel.



### 4 CVE-2021-3156 - Sudo (Baron Samedit)

#### Descripción

Las versiones del comando "sudo" en las versiones v1.8.2 - v1.9.5p1 contienen un error que puede provocar un desbordamiento de búfer, permitiendo que cualquier usuario sin privilegios obtenga privilegios de root en un host vulnerable utilizando una configuración sudo predeterminada. El problema ocurre al ejecutar el comando "sudoedit -s" con un argumento de línea de comandos que termina con un único carácter de barra invertida.

Ejemplo: `sudoedit -s '\' perl -e 'print "A" x 65536'`

Esta vulnerabilidad afecta a varios sistemas operativos como Ubuntu 20.04 (Sudo 1.8.31), Debian 10 (Sudo 1.8.27) y Fedora 33 (Sudo 1.9.2) y demás sistemas operativos que usen estas versiones de sudo.

#### Impacto

El impacto de la vulnerabilidad es crítico ya que afecta directamente la confidencialidad, integridad y disponibilidad de los datos al obtener privilegios de root:

- Confidencialidad: El atacante podría acceder a datos confidenciales.
- Integridad: El atacante podría modificar o eliminar archivos.
- Disponibilidad: El atacante podría cambiar configuraciones o permisos.

#### Exploración y Explotación

Podríamos detectar la vulnerabilidad viendo la versión de sudo que tenemos instalada usando el comando: "apt list sudo"

También la podríamos detectar y explotar a través de herramientas que escanean vulnerabilidades, como Metasploit. También existen scripts en GitHub, Openwall o Packet Storm Security que permiten automatizar la explotación.

[Script en Packet Storm Security](https://packetstormsecurity.com/files/161230/Sudo-Buffer-Overflow-Privilege-Escalation.html)

[Script en Openwall](https://www.openwall.com/lists/oss-security/2021/01/26/3)

#### Contramedidas

 La mayoría de las distribuciones ya han lanzado actualizaciones para corregir esto, por lo que la actualización del sistema o del paquete de sudo solucionará esta vulnerabilidad.

### 5 CVE-2023-26604 - systemd 246

#### Descripción

Systemd anterior a la versión 247 no bloquea adecuadamente la escalada de privilegios locales para algunas configuraciones de Sudo, por ejemplo, el archivo sudoers que necesita de autenticación se podría ejecutar mediante el comando "systemctl status". Específicamente, systemd no establece LESSSECURE en 1 y, por lo tanto, se pueden iniciar otros programas desde el programa less (Es un visualizador de archivos de texto). Esto presenta un riesgo de seguridad sustancial cuando se ejecuta systemctl desde Sudo, porque less se ejecuta como root cuando el tamaño del terminal es demasiado pequeño para mostrar la salida completa de systemctl.

Systemd es un conjunto de procesos de administración de sistema, bibliotecas y herramientas que interactuan con el núcleo del Sistema operativo.

#### Impacto

- **Disponibilidad:** Un atacante podría utilizar esta vulnerabilidad para detener o interrumpir los servicios críticos del sistema. Por ejemplo, podría ejecutar el comando "systemctl stop nginx" para detener el servidor web nginx.
- **Integridad:** Un atacante podría utilizar esta vulnerabilidad para modificar o eliminar archivos críticos del sistema. Por ejemplo, para ejecutar el comando "cp /etc/passwd /tmp/passwd" y copiar el archivo de contraseñas.
- **Confidencialidad:** Un atacante podría utilizar esta vulnerabilidad para recopilar información confidencial del sistema. Por ejemplo, para ejecutar el comando "cat /etc/shadow" y leer las contraseñas.

#### Exploración y Explotación

Para explotar esta vulnerabilidad no hace falta nada en especial, simplemente ejecutar comandos de systemd como por ejemplo systemctl o journalctl.

Aquí podemos ver un ejemplo con el que se accede fácilmente a root :
Primero se lista los permisos de sudo con "sudo -l" y nos muestra que binarios tienen permisos de root (En este caso cron.service), luego simplemente ejecuta el comando como sudo ya que tiene privilegios para hacerlo y por último, invoca una shell con el comando !sh (!sh -> lo que hace es llamar a la última vez que se ejecuto el comando sh, con el comando bash podríamos hacer lo mismo (!/bin/bash))  y como vemos ya puede ejecutar comandos como usuario root:

![Ejemplo de Exploración y Explotación](./systemd246.png)

#### Contramedidas

Una solución sería modificar la variable LESSSECURE en el archivo "/etc/profile.d/lesssecure.sh" que debemos crear si no está creado con las siguientes variables:

```bash
LESSSECURE=1
readonly LESSSECURE
export LESSSECURE //hace que la variable esté disponible en procesos de segundo plano
```

Cuando la variable de entorno LESSSECURE se establece en 1, 
se ejecuta en modo "seguro". Esto significa que estas funciones están deshabilitadas:
- ! el comando de shell
- | el comando de tubería (pipe)
- :e el comando de examen.
- v el comando de edición
- s -o archivos de registro
- -k uso de archivos lesskey
- -t uso de archivos de etiquetas
- Metacaracteres en nombres de archivos, como *
- Finalización del nombre de archivo (TAB, ^L)

También se puede compilar Less para que esté permanentemente en modo "seguro". Para ello tenemos que modificar el archivo sudoers y añadir la variable: 
env_keep=LESSSECURE

### 6 CVE-2016-2414 - Minikin Android
#### Descripción

Esta es una vulnerabilidad encontrada en *MInikin* una implementación de la interfaz de renderizado de fuentes en Android. Es un componente clave de android al ser una parte integral del sistema de gráficos, al estar encargado de renderizar las fuentes y el manejo de varios aspectos referidos al texto.

La vulnerabilidad existe debido a que *MInikin* contiene un error a la hora de parsear los archivos .TTF (archivos de fuentes de texto) correctamente. Esto podría permitir a un atacante establecer un bloqueo completo de un dispositivo Android mediante la carga de un archivo .TTF debidamente modificado para desencadenar un error que termina provocando continuos reinicios permanentes en el dispositivo y corrupción de memoria, por lo tanto un ataque de denegación de servicio (DoS).

#### Impacto

La explotación de esta vulnerabilidad puede conllevar a una pérdida de la integridad y denegación completa de la disponibilidad de los datos de un dispositivo que tenga instalado Android 5.0.x anteriores a la 5.0.2, 5.1.x anteriores a la 5.1.1 y 6.x anteriores al 1 de abril de 2016.

#### Exploración y Explotación

Esta vulnerabilidad podría explotarse mediante la instalación de un archivo .TTF debidamente preparado para la ocasión, por ejemplo mediante manipulación de bytes, una técnica en la cual se modifican los valores binarios de un archivo para que contenga la información necesaria para poder desencadenar el efecto malicioso en un objetivo aprovechando la vulnerabilidad.

#### Contramedidas

Para evitar vernos afectados por esta vulnerabilidad podríamos seguir las siguientes recomendaciones:

- **Utilizar siempre las versiones más actualizadas de los sistemas operativos**, en este caso Android, que por lo general contienen actualizaciones que arreglan este tipo de problemas. (En este caso Google corrigió la vulnerabilidad en las actualizaciones de seguridad de Abril de 2016)
- **Evitar descargar o instalar fuentes de terceros o de origen desconocido** para modificar nuestro sistema.
- **Evitar abrir archivos adjuntos de correos electrónicos** cuyo remitente sea **desconocido o sospechoso**.


###  7 CVE-2022-2586 - Linux Kernel UAF

#### Descripción

Esta vulnerabilidad es una **vulnerabilidad de uso después de la liberación (UAF)** que se encuentra en el kernel de Linux.

Esta vulnerabilidad permite a un atacante local, con privilegios, causar un problema de UAF en el momento de la eliminación de una tabla, lo que podría conducir a una escalada de privilegios local.

La vulnerabilidad se encuentra en el código del kernel de Linux que maneja las tablas de nf_tables. Estas tablas se utilizan para implementar reglas de cortafuegos y otros filtros de paquetes. El código vulnerable libera incorrectamente un objeto de tabla después de haberlo utilizado, lo que permite al atacante acceder a la memoria liberada y modificarla.

#### Impacto

La explotación de esta vulnerabilidad podría permitir al atacante ejecutar código arbitrario con privilegios del kernel. Esto podría permitir al atacante tomar el control total del sistema. 

Por lo que la confidencialidad, la integridad y la disponibilidad de los datos se ven afectados en su totalidad.

#### Exploración y Explotación

Hablamos de vulnerabilidad UAF (*Use-After-Free*) cuando en uno de los tantos procesos de manejo de memoria que ocurren en un sistema, un espacio concreto de memoria se libera por error. Mediante un exploit podríamos acceder a ese espacio de memoria que se ha liberado en un proceso concreto, en este caso la administración de unas tablas llamadas "*nf_tables*" del kernel de Linux que se utilizan para implementar reglas de cortafuegos y otros filtros de paquetes.

En ese espacio de memoria el atacante mediante su exploit podría escribir directamente a nivel de kernel, por lo que podría establecerse con privilegios de administrador para poder tomar total control del sistema.
#### Contramedidas

Para protegerse de esta vulnerabilidad, los usuarios de sistemas Linux deben:

* **Actualizar a la versión 5.18.11 o posterior del kernel de Linux.** Esta versión corrige la vulnerabilidad.
* **Evitar ejecutar código arbitrario de fuentes desconocidas.** Esto podría ayudar a prevenir la explotación de la vulnerabilidad por parte de un atacante.

### 8 CVE-2018-4087 - iOS Core Bluetooth

#### Descripción



#### Impacto



#### Exploración y Explotación


#### Contramedidas

### 9 Dirty pipe (CVE-2022-0847)
#### Descripción: 
Es una vulnerabilidad en el kernel de Linux desde la versión 5.8 en adelante que permite sobrescribir datos en archivos de solo lectura. Esto conduce a una escalada de privilegios porque los procesos sin privilegios pueden inyectar código en los procesos raíz.

La vulnerabilidad se encuentra exactamente en la función "copy_page_to_iter_pipe()" del kernel de Linux. (la función se utiliza para copiar datos de una página de memoria al búfer del pipe o tubería "|" ). 
El búfer del pipe se utiliza para almacenar los datos que se están transmitiendo a través del pipe.

El fallo se produce porque la función no inicializa correctamente la variable donde se almacena la flag del pipe, que es donde se almacenan los permisos y estado del pipe, entonces como no puede leer los permisos y el estado, un atacante podría utilizar la vulnerabilidad para escribir datos en el búfer del pipe, por ejemplo, contraseñas, malware, etc...

Una vez que el atacante ha escrito datos en el búfer del pipe, podría enviar los datos a un archivo de solo lectura, como "/etc/passwd". 

#### Impacto: 

Esta vulnerabilidad tiene graves impactos sobre la disponibilidad, integridad y confidencialidad de los datos:

- Disponibilidad: se podría utilizar para interrumpir servicios críticos, instalar malware o tomar el control del sistema.
- Integridad: Se podría utilizar para modificar archivos de solo lectura.
- Confidencialidad: Se podría utilizar para recopilar información confidencial como contraseñas, archivos personales, etc...


#### Exploración y explotación:

La vulnerabilidad se podría detectar con herramientas como Nmap, Metasploit, Burp Suite, OpenVAS, etc...

También existe la posibilidad de detectar esta vulnerabilidad con un script que se encuentra alojado en GitHub llamado "CVE-2022-0847-dirty-pipe-checker" (https://github.com/basharkey/CVE-2022-0847-dirty-pipe-checker#cve-2022-0847-dirty-pipe-checker) que se utiliza de la siguiente manera:

- Ejecutando: ./dpipe.sh (Es un script simple que lo que hace es hacer comprobaciones con las versiones de kernel y comprobar si esta es vulnerable)
- Una vez se ejecuta nos mostraría la versión del kernel en la que estamos y si es vulnerable o no.

Para realizar la explotación podríamos hacerlo mediante la ejecución de scripts como:
https://github.com/AlexisAhmed/CVE-2022-0847-DirtyPipe-Exploits
Este repositorio tiene dos exploits que con cualquiera de ellos podríamos explotar esta vulnerabilidad:
- El primero lo que hace es sobrescribir datos sobre el fichero /etc/passwd.
- El segundo lo que hace es elevar los privilegios mediante un binario que tenga permisos SUID. (Este permiso se utiliza para permitir a los usuarios del sistema ejecutar binarios con privilegios elevados temporalmente para realizar una tarea específica.).
Ej: 
- Detectamos los binarios que tienen permisos SUID con el comando:
	- `find / -perm -4000 2>/dev/null`
- Y ejecutamos el exploit2 indicandole el directorio de ese binario:
	- `./exploit-2 /usr/bin/sudo`

#### Contramedidas: 

- Deshabilitar el acceso remoto al kernel. Esto se puede hacer editando el archivo /etc/sysctl.conf y comentando la siguiente línea:
-kernel.unprivileged_userns_clone=1
- Utilizar un firewall para bloquear el acceso no autorizado a ciertos servicios como por ejemplo ssh (puerto 22)
- Implementar un sistema de detección de intrusiones (IDS) para que nos ayude a detectar el ataque.
- La vulnerabilidad se solucionó en Linux 5.16.11, 5.15.25 y 5.10.102 por lo que usar una de estas versiones nos solucionaría el problema.

## Conclusiones

Durante el proceso de este proyecto nos hemos adentrado en conceptos y definiciones claves en la ciberseguridad, como exploit, vulnerabilidad, UAF o EBPF. [[Proyecto 1 - Hack-Proof Inc.]]


Este proyecto nos ha ayudado a mejorar nuestra capacidad de identificar las distintas vulnerabilidades que existen en los distintos sistemas operativos, en realizar un análisis de las mismas para comprender su funcionamiento y el impacto que tienen sobre el sistema, a saber como detectarlas mediante el uso de comandos, software, scripts, etc..., a como se podrián explotar mediante el uso de herramientas como Nmap, Burpsuit, Metasploit, OpenVAS, etc... o bien con scripts ya creados por la comunidad de ciberseguridad y a saber que distintas medidas de seguridad y prevención debemos aplicar para poder evitarlas o detectarlas a tiempo. También nos a ayudado a tener un poco más de conciencia sobre la importacia que tiene la ciberseguridad.

## Recomendaciones

Podemos recomendar que tengamos siempre instalado en nuestro sistema un antivirus/antimalware, un escaner de vulnerabilidades como pueden ser Nessus o OpenVas, también un sistema IDS que nos ayude a detectar intrusiones en nuestro sistema, actualizar siempre tanto las aplicaciones como el sistema operativo a la última versión ya que suelen corregir muchas vulnerabilidades, aplicar restricciones mediante el uso de un firewall, cambiar los puertos por defecto de los servicios más comunes como por ejemplo el de ssh.
