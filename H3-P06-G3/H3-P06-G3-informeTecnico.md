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

**Linux Server Metasploitable 3**
![ME3Wnessus](./img/tablametasploitable3linux.png)

**Máquina Kioptrix**
![ME3Wnessus](./img/tablakioptrix.png)

**Máquina W1r3s**
![guillermonessus](./img/tablaw1r3s.png)

Además se ha encontrado una vulnerabilidad con el CVE: CVE-2018-15473 de SSH que no se encuentra entre los análisis realizados.

### Tabla de hallazgos

#### Vulnerabilidades Ubuntu Metasploitable 3

| Descripción de la vulnerabilidad |  El módulo mod_copy en ProFTPD 1.3.5 permite a atacantes remotos leer y escribir en archivos de su elección mediante los comandos site cpfr y site cpto.|
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |        [CVE-2015-3306](https://nvd.nist.gov/vuln/detail/CVE-2015-3306)                                                    |
| CVSS v3                          |            [9.8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator)                                                  |
| Severidad                        |                       Alta                                       |
| Impacto                          |     Un atacante puede leer información sensible, modificar archivos, crearlos e intentar ganar privilegios de administrador en el sistema.                                                         |
| Sistemas afectados               |       Ubuntu Metasploitable 3                                                       |
| Prueba de concepto (POC)         |       ![proftpd](./img/proftpd.png)                                                       |
| Remediación                      |     Actualizar a una versión posterior a ProFTPD 1.3.5.                                                         |
| Link de referencia               |     [https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure](https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure)                                                         |
<br>

| Descripción de la vulnerabilidad | La versión de Drupal que se ejecuta en el servidor web remoto se ve afectada por una vulnerabilidad de ejecución de código remoto en el módulo Coder, específicamente en el archivo coder_upgrade.run.php, debido a una validación incorrecta de la entrada proporcionada por el usuario a la función unserialize(). Un atacante remoto no autenticado puede explotar esto, a través de una solicitud especialmente diseñada, para ejecutar código PHP arbitrario. |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |     [CVE-2018-7600](https://nvd.nist.gov/vuln/detail/CVE-2018-7600)                                                                                    |
| CVSS v3                          |         [9.8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator)                                                                                    |
| Severidad                        |                  Alta                                        |
| Impacto                          |         Un atacante podría ejecutar código malicioso en la máquina, acceder a información que se encuentre en el servidor web y modificarla.                                                     |
| Sistemas afectados               |             Ubuntu Metasploitable 3                                                 |
| Prueba de concepto (POC)         |            ![drupal](./img/drupal_coder_exec.png)                                                  |
| Remediación                      |     Actualizar la versión de drupal a una versión posterior a la 7.x-2.6 o eliminar el módulo de drupal.                                                         |
| Link de referencia               |         [https://attack.mitre.org/techniques/T1059/004/](https://attack.mitre.org/techniques/T1059/004/)                                                     |

<br>

| Descripción de la vulnerabilidad | El servidor web remoto ejecuta una versión de Drupal que se ve afectada por una vulnerabilidad de inyección SQL debido a una falla en la API de abstracción de la base de datos de Drupal, que permite a un atacante remoto utilizar solicitudes especialmente diseñadas que pueden resultar en una ejecución SQL arbitraria. Esto puede provocar una escalada de privilegios, una ejecución arbitraria de PHP o una ejecución remota de código. |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |    [CVE-2014-3704](https://nvd.nist.gov/vuln/detail/CVE-2014-3704)                                                                                     |
| CVSS v3                          |        [9.8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)                                                                                     |
| Severidad                        |                                 Alta                      |
| Impacto                          |        Un atacante podría ejecutar código malicioso en la máquina, acceder a información que se encuentre en el servidor web y modificarla.                                                      |
| Sistemas afectados               |             Ubuntu Metasploitable 3                                                                                                 |
| Prueba de concepto (POC)         |      ![drupalgeddon](./img/drupalgeddon.png)                                                        |
| Remediación                      |         Actualizar a una versión superior a la 7.32 de Drupal.                                                     |
| Link de referencia               |              [https://attack.mitre.org/techniques/T1059/004/](https://attack.mitre.org/techniques/T1059/004/)                                                 |

<br>

| Descripción de la vulnerabilidad | El servidor web Apache que se ejecuta en el host remoto se ve afectado por una vulnerabilidad de divulgación de información. Un atacante remoto no autenticado puede aprovechar esto enviando una solicitud manipulada para mostrar una lista de un directorio remoto, incluso si existe un archivo de índice válido en el directorio. |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |         [CVE-2001-0731](https://nvd.nist.gov/vuln/detail/CVE-2001-0731)                                                                                |
| CVSS v3                          |                               [5.3](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator)                                                              |
| Severidad                        |                          Medio                            |
| Impacto                          |     Un atacante puede listar los directorios del servidor web.                                                         |
| Sistemas afectados               |             Ubuntu Metasploitable 3                                                                                                 |
| Prueba de concepto (POC)         |      ![directorylist](./img/directorylist.png)                                                      |
| Remediación                      |                                 Modificar el fichero .htaccess para deshabilitar el listado de directorios y actualizar a una versión superior de apache.                             |
| Link de referencia               |       [https://attack.mitre.org/techniques/T1592/](https://attack.mitre.org/techniques/T1592/)

<br>

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

### Fase 3: Escalada de privilegios

### Fase 4: Persistencia

# Conclusión

En base a los hallazgos recabados en los análisis realizados, y las posteriores pruebas de pentesting llevadas a cabo, hemos llegado a las siguientes conclusiones:

