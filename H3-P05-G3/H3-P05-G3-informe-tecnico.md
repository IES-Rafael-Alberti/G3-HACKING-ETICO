# Índice

- [Resumen Ejecutivo](#resumen-ejecutivo)
- [Tabla de Riesgos](#tabla-de-riesgos)
- [Evaluación](#evaluacion)
    - [Breve Resumen](#breve-resumen)
    - [Tabla de Hallazgos](#tabla-de-hallazgos)
- [Metodologías](#metodologías)
  - [Herramientas utilizadas](#herramientas-utilizadas)
  - [Procedimiento](#procedimiento)
    - [Fase 1: Reconocimiento](#fase-1-reconocimiento)
    - [Fase 2: Explotación](#fase-2-explotación)
- [Conclusión](#conclusión)

# Resumen Ejecutivo

En el presente informe se detallan las vulnerabilidades explotadas en la auditoría realizada a la empresa La Descuidada S.A, con el objetivo de identificar y evaluar las vulnerabilidades en sus sistemas. La auditoría se centró en dos servidores acordados con la empresa, Windows Server 2008 R2 Standard y Windows Server Metasploitable 3.

Usando como base la extensa lista de vulnerabilidades encontradas en los análisis previos realizados, y tras llevar a cabo múltiples pruebas con la lista mencionada, logramos explotar algunas de las vulnerabilidades especificadas en los análisis. 

Se identificó una vulnerabilidad de nivel alto relacionada con el protocolo SMB, la cual fue exitosamente explotada durante la auditoría. A pesar de esta vulnerabilidad, se observó que este servidor presentaba un menor número de vulnerabilidades en comparación con el otro servidor evaluado.

En el segundo servidor, denominado Windows Server Metasploitable 3, logramos explotar múltiples vulnerabilidades de varios niveles, siendo algunas de estas de nivel crítico, siendo las demás de nivel alto y medio.  

# Tabla de Riesgos

La siguiente tabla explica de forma clara y concisa la puntuación de los riesgos de los sistemas en una escala del 1 al 10.

| Riesgo | CVSSv3 | Descripción |
|--------|--------|-------------|
| CRÍTICA | 10 | Se describe una vulnerabilidad que ha sido calificada como crítica y requiere resolución tan rápida como sea posible. |
| ALTA | 7 - 9.9 | Se describe una vulnerabilidad que ha sido calificada como alta y requiere resolución a corto plazo. |
| MEDIA | 4 - 6.9 | Se describe una vulnerabilidad que ha sido calificada como media y debe resolverse como parte del mantenimiento de seguridad de un sistema. |
| BAJA | 1 – 3.9 | Se describe una vulnerabilidad que ha sido calificada como baja y debe ser abordada como parte de las tareas de mantenimiento rutinario. |
| INFO | 0 – 0.9 | Se realizó un descubrimiento de carácter informal y debe ser abordado con el fin de cumplir con una buena práctica de seguridad. |

# Evaluación

## Breve Resumen

Se ha realizado un test de caja negra por cada sistema auditado y se han encontrado varias vulnerabilidades catalogadas teniendo en cuenta las dos tablas siguientes. Las vulnerabilidades críticas, altas y medias podrían suponer un peligro para los sistemas auditados.

**Windows Server 2008 R2 Standard**
![guillermonessus](./img/tablaguillermo.png)

**Windows Server Metasploitable 3**

![ME3Wnessus](./img/tablametasploitable3.png)

Además se ha encontrado una vulnerabilidad con el CVE: CVE-2018-15473 de SSH que no se encuentra entre los análisis realizados.

### Tabla de hallazgos

#### Vulnerabilidades Windows Server 2008 R2 Standard

| Descripción de la vulnerabilidad |El servidor SMBv1 en Microsoft Windows Vista SP2; Windows Server 2008 SP2 y R2 SP1; Windows 7 SP1; Windows 8.1; Windows Server 2012 Gold y R2; Windows RT 8.1 y Windows 10 Gold, 1511 y 1607 y Windows Server 2016 permite a atacantes remotos ejecutar código arbitrario a través de paquetes manipulados, vulnerabilidad también conocida como "Windows SMB Remote Code Execution Vulnerability"|
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |              [CVE-2017-0143](https://nvd.nist.gov/vuln/detail/cve-2017-0143)                                                |
| CVSS v3                          |                    [8.1](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2017-0143&vector=AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H&version=3.0&source=NIST)                                          |
| Severidad                        |                    Alta                                          |
| Impacto                          | Si un atacante consigue acceder a la máquina usando esta vulnerabilidad, puede obtener acceso de manera remota a la máquina y por lo tanto podría leer, modificar, crear o borrar información importante, escalar privilegios, hacer landing a otras máquinas de la red y obtener persistencia.   |
| Sistemas afectados               |                     Windows server 2008 R2 Standard                                   |
| Prueba de concepto (POC)        |        ![eternalguillermo](./img/eternalguillermo.png)                                                      |
| Remediación                      |   Actualizar el Sistema Operativo a una versión más reciente ya que se ha parcheado esta vulnerabilidad.                                                     |
| Link de referencia               |       [https://attack.mitre.org/techniques/T1210/](https://attack.mitre.org/techniques/T1210/)                                                       |

<br>
<br>

#### Vulnerabilidades Windows Server Metasploitable 3

| Descripción de la vulnerabilidad |El servidor SMBv1 en Microsoft Windows Vista SP2; Windows Server 2008 SP2 y R2 SP1; Windows 7 SP1; Windows 8.1; Windows Server 2012 Gold y R2; Windows RT 8.1 y Windows 10 Gold, 1511 y 1607 y Windows Server 2016 permite a atacantes remotos ejecutar código arbitrario a través de paquetes manipulados, vulnerabilidad también conocida como "Windows SMB Remote Code Execution Vulnerability"|
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |              [CVE-2017-0143](https://nvd.nist.gov/vuln/detail/cve-2017-0143)                                                |
| CVSS v3                          |                    [8.1](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2017-0143&vector=AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H&version=3.0&source=NIST)                                          |
| Severidad                        |                    Alta                                          |
| Impacto                          | Si un atacante consigue acceder a la máquina usando esta vulnerabilidad, puede obtener acceso de manera remota a la máquina y por lo tanto podría leer, modificar, crear o borrar información importante, escalar privilegios, hacer landing a otras máquinas de la red y obtener persistencia.   |
| Sistemas afectados               |                     Windows Server Metasploitable 3                                        |
| Prueba de concepto (POC)        |        ![eternalguillermo](./img/eternalblueme3w.png)                                                      |
| Remediación                      |   Actualizar el Sistema Operativo a una versión más reciente ya que se ha parcheado esta vulnerabilidad.                                                     |
| Link de referencia               |       [https://attack.mitre.org/techniques/T1210/](https://attack.mitre.org/techniques/T1210/) |

<br>
<br>

| Descripción de la vulnerabilidad |                                                El servicio de protocolo de escritorio remoto (RDP) en Microsoft Windows Server 2008 R2 Service Pack 1 y R2 y Windows 7 Gold y SP1 permite a atacantes remotos causar una denegación de servicio (la aplicación se bloquea) a través de una serie de paquetes modificados, también conocido como "Terminal Server Denial of Service Vulnerability."              |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |                                                    [CVE-2012-0152](https://nvd.nist.gov/vuln/detail/CVE-2012-0152)         |
| CVSS v3                          |                                            [7.5](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H&version=3.0)                  |
| Severidad                        |                                      Alta                        |
| Impacto                          |                                  Un atacante puede realizar un ataque de denegación de servicio y bloquear la máquina                           |
| Sistemas afectados               |                                           Windows Server Metasploitable 3                |
| Prueba de concepto (POC)        |                                                      ![ms12-020](./img/ms12-020.png)        |
| Remediación                      |                                  Instalar las actualizaciones de seguridad más recientes o desactivar el acceso remoto a la máquina a través de RDP.                            |
| Link de referencia               |                                              [https://attack.mitre.org/techniques/T1498/](https://attack.mitre.org/techniques/T1498/)                |

<br>
<br>

| Descripción de la vulnerabilidad |                                              Un atacante remoto no autenticado podría aprovechar esta vulnerabilidad para leer archivos de aplicaciones web desde un servidor vulnerable. En los casos en que el servidor vulnerable permite la carga de archivos, un atacante podría cargar código JavaServer Pages (JSP) malicioso dentro de una variedad de tipos de archivos y activar esta vulnerabilidad para obtener la ejecución remota de código.        |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |                                   [CVE-2020-1745](https://nvd.nist.gov/vuln/detail/CVE-2020-1745)     |
| CVSS v3                          |                                       [9.8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2020-1745&vector=AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H&version=3.1&source=NIST)                       |
| Severidad                        |                                  Alta                            |
| Impacto                          |                               Un atacante puede leer cualquier archivo de la aplicación web pudiendo acceder a información importante.                         |
| Sistemas afectados               |                                         Windows Server Metasploitable 3                    |
| Prueba de concepto (POC)        |                                                       ![ajptomcat](./img/ajptomcat.png)       |
| Remediación                      |                               Deshabilitar AJP y usar en su lugar HTTP o HTTPS                               |
| Link de referencia               |                                          [https://attack.mitre.org/techniques/T1659/](https://attack.mitre.org/techniques/T1659/)                    |

<br>
<br>

| Descripción de la vulnerabilidad |                                                 La lista de usuarios LanMan del host remoto se puede obtener mediante SNMP.|
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |                                      [CVE-1999-0499](https://nvd.nist.gov/vuln/detail/CVE-1999-0499)                        |
| CVSS v3                          |                                      [5.3](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator)                        |
| Severidad                        |                                   Medio                           |
| Impacto                          |                                      Un atacante podría tener acceso a una lista de usuarios dentro del protocolo SNMP.                        |
| Sistemas afectados               |                                           Windows Server Metasploitable 3                   |
| Prueba de concepto (POC)        |                                                     ![snmpuser](./img/snmpuser.png)         |
| Remediación                      |                                  Desactivar el protocolo si no se utiliza                            |
| Link de referencia               |                                           [https://attack.mitre.org/techniques/T1087/](https://attack.mitre.org/techniques/T1087/)                   |

<br>
<br>

| Descripción de la vulnerabilidad |                                                 La lista de servicios LanMan que se ejecutan en el host remoto se puede obtener mediante SNMP. |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |                                   [CVE-1999-0499](https://nvd.nist.gov/vuln/detail/CVE-1999-0499)                             |
| CVSS v3                          |                                     [5.3](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L&version=3.0)                         |
| Severidad                        |                                       Medio                       |
| Impacto                          |                                  Un atacante podría ver los servicios de red que se están usando en el sistema a través de SNMP para posible explotación de los mismos.                            |
| Sistemas afectados               |                                        Windows Server Metasploitable 3                      |
| Prueba de concepto (POC)        |                              Utilizando el modulo de metasploit snmp_enum podemos encontrar los servicios entre otra información importante del sistema a auditar. <br>                      ![networksnmp](./img/networksnmp.png)          |
| Remediación                      |                                   Desactivar el protocolo si no se utiliza  |
| Link de referencia               |                                        [https://attack.mitre.org/techniques/T1046/](https://attack.mitre.org/techniques/T1046/)                      |

<br>
<br>

| Descripción de la vulnerabilidad |                                                  OpenSSH hasta la versión 7.7 es propenso a una vulnerabilidad de enumeración de usuarios debido a que no retrasa el rescate de un usuario de autenticación no válido hasta que el paquete que contiene la petición haya sido analizado completamente. Esto está relacionado con auth2-gss.c, auth2-hostbased.c, y auth2-pubkey.c.            |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |                                     [CVE-2018-15473](https://nvd.nist.gov/vuln/detail/cve-2018-15473)                         |
| CVSS v3                          |                                     [5.3](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2018-15473&vector=AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N&version=3.1&source=NIST)                         |
| Severidad                        |                                      Medio                        |
| Impacto                          |                                Un atacante podría ver los usuarios que tiene el sistema para luego ejecutarle fuerza bruta.                              |
| Sistemas afectados               |                                           Windows Server Metasploitable 3                   |
| Prueba de concepto (POC)        |                ![sshuser](./img/sshuser.png)                                              |
| Remediación                      |                          Actualizar OpenSSH a una versión más moderna.                                    |
| Link de referencia               |       [https://attack.mitre.org/techniques/T1087/](https://attack.mitre.org/techniques/T1087/)|

<br>
<br>

| Descripción de la vulnerabilidad |  La vulnerabilidad se encuentra en la clase FileUploadServlet. Cuando se carga un archivo 7z, el parámetro ConnectionId, controlado por el usuario, no se valida adecuadamente. Esto permite a un atacante remoto inyectar un byte nulo al final del valor para crear un archivo malicioso con un tipo de archivo arbitrario. Posteriormente, este archivo malicioso puede ser colocado en un directorio que permita la ejecución de scripts del lado del servidor, lo que resulta en la ejecución remota de código bajo el contexto del usuario SYSTEM.   |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |                CVE-2015-8249                                 |
| CVSS v3                          |                9.8                                           |
| Severidad                        |                Crítica                                       |
| Impacto                          |   Un atacante puede cargar y ejecutar archivos de su elección a través del parámetro ConnectionId.    |
| Sistemas afectados               |           Windows Server Metasploitable 3                    |
| Prueba de concepto (POC)         |   ![POC-MED](./img/ManageEngine-Desktop-Central-Exploit.png)   |
| Remediación                      |      Actualizar a una build igual o posterior a la 91100     |
| Link de referencia               |      https://nvd.nist.gov/vuln/detail/CVE-2015-8249          |

<br>
<br>

| Descripción de la vulnerabilidad |  La configuración por defecto en ElasticSearch en versiones anteriores a la 1.2 permite el scrpting dinámico, lo que permite a los atacantes remotos ejecutar expresiones MVEL (MVEL es un lenguaje basado en la sintaxis de Java) y código en Java a través del parámetro fuente para _search.  |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |                CVE-2014-3120                                 |
| CVSS v3                          |                [6.8](https://www.cvedetails.com/cve/CVE-2014-3120/)  |
| Severidad                        |                Media                                       |
| Impacto                          |  Un atacante puede ejecutar código arbitrario de forma remota, permitiéndoles acceder al sistema.  |
| Sistemas afectados               |       Windows Server Metasploitable 3                        |
| Prueba de concepto (POC)         |   ![ElasticSearch](./img/ElasticSearch.png)                    |
| Remediación                      |      Actualizar a una versión igual o posterior a la 1.2     |
| Link de referencia               |      https://nvd.nist.gov/vuln/detail/CVE-2014-3120          |


| Descripción de la vulnerabilidad | CWE-200: Exposure of Sensitive Information to an Unauthorized Actor. Oracle Glassfish                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CVE/CWE                          | CWE-200                                                                                                                                                                                                                                                                                                                                                                                                                         |
| CVSS v3                          | 7.2                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Severidad                        | Alto                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Impacto                          | La exposición de información sensible puede tener un impacto significativo, dependiendo del tipo de información revelada. Esto puede variar desde la revelación de información personal privada, como mensajes personales, datos financieros, registros de salud, ubicación geográfica o detalles de contacto, hasta información sobre el estado y el entorno del sistema, como el sistema operativo y los paquetes instalados. |
| Sistemas afectados               | Metasploitable 3                                                                                                                                                                                                                                                                                                                                                                                                                |
| Prueba de concepto (POC)         | Acceder al puerto 8080 a través de un navegador<br><br>![](./img/Pasted%20image%2020240407002020.png)                                                                                                                                                                                                                                                                                                                                 |
| Remediación                      | Para mitigar este tipo de vulnerabilidades, se recomienda sanitizar la información (como los datos del usuario), así como implementar la compartimentación y establecer áreas seguras trazando límites de confianza para los datos. En el caso específico de Oracle Glassfish, asegúrate de que la configuración del servidor esté correctamente establecida para no exponer información sensible a través del puerto 8080.     |
| Link de referencia               | [CWE-200: Exposure of Sensitive Information to an Unauthorized Actor - MITRE](https://cwe.mitre.org/data/definitions/200.html)                                                                                                                                                                                                                                                                                                  |

| Descripción de la vulnerabilidad |                                                                                                                                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CVE/CWE                          | CWE-200: Exposure of Sensitive Information to an Unauthorized Actor. <br><br>Apache Tomcat                                                                          |
| CVSS v3                          | 7.2                                                                                                                                                                 |
| Severidad                        | Alto                                                                                                                                                                |
| Impacto                          | Esta página por defecto muestra información de que efectivamente este servidor posee un apache Tomcat además de mostrar su versión y desvelar el puerto donde está. |
| Sistemas afectados               | Metasploitable 3                                                                                                                                                    |
| Prueba de concepto (POC)         | Acceder al puerto 8282 a través de un navegador.<br><br>![](./img/Pasted%20image%2020240407002618.png)<br>                                                                |
| Remediación                      | Añadir configuración para no mostrar pantalla,                                                                                                                      |
| Link de referencia               | https://cwe.mitre.org/data/definitions/200.html                                                                                                                     |

| Descripción de la vulnerabilidad |                                                                                                                                                                                                                                                                                  |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CVE/CWE                          | CWE-521 (Weak Password Requirements)<br><br>Manage Engine                                                                                                                                                                                                                        |
| CVSS v3                          | 9.8                                                                                                                                                                                                                                                                              |
| Severidad                        | Crítica                                                                                                                                                                                                                                                                          |
| Impacto                          | La contraseña y usuario para entrar a este servicio es *admin:admin*, lo cual es un problema de seguridad crítico. Cualquier atacante que lo intente podría adquirir privilegios de administrador con tan solo hacer o bien una prueba manual básica o un ataque de fuerza bruta |
| Sistemas afectados               | Metasploitable 3                                                                                                                                                                                                                                                                 |
| Prueba de concepto (POC)         | Acceder al puerto 8020 o 8022 y realizar una prueba con varios conjuntos de credenciales básicas. Realizar un ataque de fuerza bruta con diccionarios básicos.<br><br>![](./img/Pasted%20image%2020240407181516.png)                                                                   |
| Link de referencia               | https://www.cvedetails.com/cwe-details/521/Weak-Password-Requirements.html                                                                                                                                                                                                       |

| Descripción de la vulnerabilidad |                                                                                                                                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CVE/CWE                          | CWE-200: Exposure of Sensitive Information to an Unauthorized Actor. <br><br>Apache WampServer                                                                      |
| CVSS v3                          | 7.2                                                                                                                                                                 |
| Severidad                        | Alto                                                                                                                                                                |
| Impacto                          | Esta página por defecto muestra información de que efectivamente este servidor posee un apache Tomcat además de mostrar su versión y desvelar el puerto donde está. |
| Sistemas afectados               | Metasploitable 3                                                                                                                                                    |
| Prueba de concepto (POC)         | Acceder al puerto 8585 a través de un navegador.<br><br>![](./img/Pasted%20image%2020240407010628.png)                                                                    |
| Remediación                      | Añadir configuración para no mostrar pantalla,                                                                                                                      |
| Link de referencia               | https://cwe.mitre.org/data/definitions/200.html                                                                                                                     |


<br>
<br>

| Descripción de la vulnerabilidad |                                                                                                                                                                                                                                                                                  |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CVE/CWE                          | CWE-521 (Weak Password Requirements)<br><br>Manage Engine                                                                                                                                                                                                                        |
| CVSS v3                          | 9.8                                                                                                                                                                                                                                                                              |
| Severidad                        | Crítica                                                                                                                                                                                                                                                                          |
| Impacto                          | La contraseña y usuario para entrar a este servicio es *admin:admin*, lo cual es un problema de seguridad crítico. Cualquier atacante que lo intente podría adquirir privilegios de administrador con tan solo hacer o bien una prueba manual básica o un ataque de fuerza bruta |
| Sistemas afectados               | Metasploitable 3                                                                                                                                                                                                                                                                 |
| Prueba de concepto (POC)         | Acceder al puerto 8020 o 8022 y realizar una prueba con varios conjuntos de credenciales básicas. Realizar un ataque de fuerza bruta con diccionarios básicos.<br><br>![](./img/Pasted%20image%2020240407181516.png)                                                                   |
| Link de referencia               | https://www.cvedetails.com/cwe-details/521/Weak-Password-Requirements.html                                                                                                                                                                                                       |

<br>
<br>

| Descripción de la vulnerabilidad |                                                                                                                                                                                                                                                                                                 |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CVE/CWE                          | CWE-521 (Weak Password Requirements)<br><br>MySQL                                                                                                                                                                                                                                               |
| CVSS v3                          | 9.8                                                                                                                                                                                                                                                                                             |
| Severidad                        | Crítica                                                                                                                                                                                                                                                                                         |
| Impacto                          | La contraseña y usuario para entrar a este servicio es *root:*, lo cual es un problema de seguridad crítico. Cualquier atacante que lo intente podría adquirir privilegios de administrador en la base de datos con tan solo hacer o bien una prueba manual básica o un ataque de fuerza bruta. |
| Sistemas afectados               | Metasploitable 3                                                                                                                                                                                                                                                                                |
| Prueba de concepto (POC)         | Realizamos un escaneo de reconocimiento utilizando `nmap` y descubrimos un servicio MySQL. <br><br>Una vez tengamos el puerto. Con el exploit `mysql_login` y el diccionario de contraseñas `unix_passwords.txt` obtenemos la contraseña:<br><br>![](./img/Pasted%20image%2020240407185448.png)       |
| Link de referencia               | https://www.cvedetails.com/cwe-details/521/Weak-Password-Requirements.html                                                                                                                                                                                                                      |

# Metodologías

## Herramientas utilizadas

- Nmap 7.94SVN
- Metasploit Framework 6.4.1-dev-
- Tenable© Nessus 10.7.2

## Procedimiento

### Fase 1: Reconocimiento

En primer lugar se han realizado escaneos automatizados utilizando la herramienta _Tenable© Nessus_, de la cual obtenemos un reporte que utilizaremos para guiar nuestra auditoría. 

Del reporte obtenemos información crucial que utilizaremos en la auditoría, como el nivel de riesgo que supone la vulnerabilidad para la seguridad de la máquina auditada, posibles CVEs que utilizaremos para guiarnos en su posterior intento de explotación y prueba de concepto (PoC).

Adicionalmente se realiza otro escaneo de puertos, servicios y posibles vulnerabilidades utilizando la herramienta _Nmap_ para listarlos, junto a los scripts por defecto de la herramienta, que se cruzarán con los resultados del reporte de _Nessus_ para mayor rigor.

### Fase 2: Explotación
Teniendo esta información disponible, se procederá a hacer uso del framework de pentesting _Metasploit_ para automatizar el uso de exploits debidamente elaborados para realizar una explotación de las vulnerabilidades descubiertas en la anterior fase de análisis. 

Una vez se realice un hallazgo, se documentará añadiendo su categoría y código en la clasificación CVE o CWE, su puntuación según CVSS asignada y en su defecto el cálculo de la misma por el auditor, una explicación concisa de la prueba de concepto realizada para llevar a cabo la explotación de esa vulnerabilidad, en la cual si es necesario se llevará a cabo la censura de la información sensible mediante el pixelado de la imagen. 

Finalmente se aportará un enlace de referencia a la vulnerabilidad en cuestión.

# Conclusión

En base a los hallazgos recabados en los análisis realizados, y las posteriores pruebas de pentesting llevadas a cabo, hemos llegado a las siguientes conclusiones:

- En el servidor Windows Server 2008 R2 se ha logrado explotar la vulnerabilidad CVE-2017-0143, que afecta al protocolo SMB, permitiéndonos acceder al servidor.

- El segundo servidor, denominado como Windows Server Metasploitable 3, presenta 4 vulnerabilidades críticas, 7 de nivel alto y 4 de nivel medio. Estas afectan a servicios críticos del sistema tales como SMB, RDP o ManageEngine Desktop.

Teniendo en cuenta los hallazgos de las pruebas de pentesting en los servidores evaluados, es evidente que La Descuidada S.A. enfrenta desafíos significativos en términos de seguridad de la información.

La explotación exitosa de la amplia gama de vulnerabilidades críticas, de alto y medio nivel encontradas resaltan la necesidad urgente de mejorar las prácticas de seguridad de la empresa.
