# Índice

- [Resumen Ejecutivo](#resumen-ejecutivo)
- [Tabla de Riesgos](#tabla-de-riesgos)
- [Evaluación](#evaluacion)
    - [Breve Resumen](#breve-resumen)
    - [Tabla de Hallazgos](#tabla-de-hallazgos)
      - [PC-1](#vulnerabilidades-ubuntu-metasploitable-3)
      - [PC-2](#vulnerabilidades-kioptrix)
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

## Tabla de hallazgos

### Vulnerabilidades PC

| Descripción de la vulnerabilidad | La implementación del Protocolo de escritorio remoto (RDP) en Microsoft Windows XP SP2 y SP3, Windows Server 2003 SP2, Windows Vista SP2, Windows Server 2008 SP2, R2 y R2 SP1, y Windows 7 Gold y SP1 no procesa correctamente los paquetes en la memoria. que permite a atacantes remotos ejecutar código arbitrario enviando paquetes RDP manipulados que activan el acceso a un objeto que (1) no se inicializó correctamente o (2) se eliminó, también conocido como "vulnerabilidad del protocolo de escritorio remoto". |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |        [CVE-2012-0002](https://nvd.nist.gov/vuln/detail/CVE-2012-0002)                                                    |
| CVSS v3                          |            [7.5](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator)                                                  |
| Severidad                        |                       Alta                                       |
| Impacto                          | Un atacante puede hacer una denegación de servicios y generar un pantallazo azúl a la máquina obligando a su reinicio.                                                     |
| Sistemas afectados               |       PC-1                                    |
| Prueba de concepto (POC)         |       ![ms12-020](img/Pasted%20image%2020240425104902.png)                                                |
| Remediación                      | Desactivar el puerto 3389 si no va a ser utilizado o actualizar a Windows.                                                      |
| Link de referencia               |     [https://attack.mitre.org/techniques/T1499/](https://attack.mitre.org/techniques/T1499/)                                                        |
<br>

| Descripción de la vulnerabilidad | Existe una vulnerabilidad de ejecución remota de código en los Servicios de Escritorio remoto, anteriormente conocidos como Servicios de Terminal Server, cuando un atacante no autenticado se conecta al sistema de destino mediante RDP y envía solicitudes especialmente diseñadas, también conocida como 'Vulnerabilidad de ejecución remota de código de los Servicios de Escritorio remoto'. |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |     [CVE-2019-0708](https://nvd.nist.gov/vuln/detail/cve-2019-0708)                                                                                    |
| CVSS v3                          |         [8.8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2019-0708&vector=AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H&version=3.0&source=NIST)                                                                                    |
| Severidad                        |                  Alta                                        |
| Impacto                          | Un atacante podría obtener acceso a la máquina como administrador o generar una denegación de servicio.                                                   |
| Sistemas afectados               |             PC-1                                                |
| Prueba de concepto (POC)         |                                                          |
| Remediación                      |                                                   Desactivar el puerto 3389 si no va a ser utilizado o actualizar a Windows.       |
| Link de referencia               |         [https://attack.mitre.org/techniques/T1210/](https://attack.mitre.org/techniques/T1210/)                                                     |

<br>

| Descripción de la vulnerabilidad | El complemento mail-masta 1.0 para WordPress incluye archivos locales en count_of_send.php y csvexport.php. |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          | [CVE-2016-10956](https://nvd.nist.gov/vuln/detail/CVE-2016-10956)                                                                                     |
| CVSS v3                          |        [7.5](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2016-10956&vector=AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N&version=3.1&source=NIST)                                                                                     |
| Severidad                        |                                 Alta                      |
| Impacto                          |Permite generar una denegación de servicios explotando el servidor de correo electrónico.                                                    |
| Sistemas afectados               |             PC-2                                                                                                 |
| Prueba de concepto (POC)         |                                                            |
| Remediación                      |         Actualizar mailman a una versión superior.                                              |
| Link de referencia               |              [https://attack.mitre.org/techniques/T1499/004/](https://attack.mitre.org/techniques/T1499/004/)                                                  |

<br>

| Descripción de la vulnerabilidad | Una vulnerabilidad de inclusión de archivos locales (LFI) en interface/forms/LBF/new.php en OpenEMR < 7.0.0 permite a usuarios remotos autenticados ejecutar código a través del parámetro formname. |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          | [CVE-2023-22973](https://nvd.nist.gov/vuln/detail/CVE-2023-22973)                                                                               |
| CVSS v3                          |                  [8.8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2023-22973&vector=AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H&version=3.1&source=NIST)                                                                        |
| Severidad                        |                          Alta                            |
| Impacto                          |                     Un atacante puede ejecutar comandos para ejecutar código malicioso.                               |
| Sistemas afectados               |             PC-2                                                                                           |
| Prueba de concepto (POC)         |                                                          |
| Remediación                      |                             |
| Link de referencia               |   [https://attack.mitre.org/techniques/T1659/](https://attack.mitre.org/techniques/T1659/)|  

# Metodologías                                     
## Herramientas utilizadas

- Nmap 7.94SVN
- Metasploit Framework 6.4.1-dev-
- WPScan 3.8.25
- Chisel 1.7.7
- Chisel 1.9.1

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

