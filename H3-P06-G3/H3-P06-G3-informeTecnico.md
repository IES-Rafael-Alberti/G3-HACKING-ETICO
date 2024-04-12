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

#### Vulnerabilidades Windows Server 2008 R2 Standard

| Descripción de la vulnerabilidad |   |
|----------------------------------|---|
| CVE/CWE                          |   |
| CVSS v3                          |   |
| Severidad                        |   |
| Impacto                          |   |
| Sistemas afectados               |   |
| Prueba de concepto (POC)         |   |
| Remediación                      |   |
| Link de referencia               |   |

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

