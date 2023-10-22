## Metodología para auditoría de Iot 

### Justificación de la elección:

Elección: OWASP-FSTM (Firmware Security Testing Methodology)

Tras realizar una investigación en profundidad de las posibles metodologías para realizar auditorías de Iot (Internet de las cosas) me he decantado por la metodología OWASP-FSTM ya que cubre todas las etapas que en mi opinión necesitaría dicha auditoria. Es una metodología bastante completa y muy recomendada por los expertos en el área de Iot. Además, es bastante flexible por lo que podremos adaptarla a diferentes dispositivos y entornos con los que trabajemos en nuestra empresa.

### Descripción

La metodología OWASP-FSTM (Firmware Security Testing Methodology) es una guía que se centra en la comprobación de seguridad del firmware de los dispositivos Iot. Se basa en las mejores prácticas de seguridad y cubre todas las fases del proceso para realizar auditorías de Iot, desde la recolección de información de los dispositivos hasta la explotación de los mismos, por lo que nos ayudará a realizar un análisis completo y detallado para poder entregárselos a las empresas o usuarios que nos contraten.

### Fases de la metodología OWASP-FSTM

La metodología OWASP-FSTM consta de 9 fases. En nuestro caso creo que le añadiría una fase más que se llamará "Informes" o "Documentación" donde le reflejaríamos a la empresa todos los resultados obtenidos y como podrían mejorarlos.

#### 1. Reconocimiento y búsqueda de información: 

Esta fase consiste en recopilar toda la información técnica y documental posible de los dispositivos y analizar de forma física los dispositivos.
   
En nuestro caso la utilizaríamos para buscar toda la información posible relacionada con la arquitectura, sistema operativo, firmware, etc... Esto lo haríamos visitando las páginas web de los fabricantes y con el uso de herramientas que nos permitan ver esta información.
   
#### 2. Obtención del firmware: 

Esta fase consiste en obtener el firmware del dispositivo.

En nuestro caso lo descargaríamos de la página oficial del fabricante si es posible y sino lo buscaríamos en otra fuente como páginas web con reputación, repositorios de github, etc...
   
#### 3. Analizar el firmware: 

Esta fase consiste en examinar las características del firmware obtenido en la fase anterior.

En nuestro caso analizaríamos el firmware a fondo con la ayuda de herramientas para buscar todas las vulnerabilidades posibles.
   
#### 4. Extraer el sistema de archivos: 

Esta fase consiste en realizar la extracción del sistema de archivos contenidos en el firmware.

Utilizaríamos herramientas especializadas en la extracción de sistemas de datos como por ejemplo la herramienta binwalk.  
   
#### 5. Análisis del contenido del sistema de archivos: 

En esta fase nos centrarémos en analizar todos los datos extraídos en la fase anterior para buscar información relevante a nivel de seguridad.

En nuestro caso utilizaríamos herramientas especializadas para ello como pueden ser file, strings y herramientas de ingeniería inversa como Ghidra o IDA. Con estas herramientas detectaríamos todas las posibles vulnerabilidades que pudiera haber en los datos del firmware.
   
#### 6. Emulación del firmware: 

Esta fase consiste en la ejecución del firmware fuera del dispositivo.

Ejecutaríamos el firmware de forma completa o por partes en un entorno seguro y controlado como por ejemplo con Qemu.
   
#### 7. Análisis dinámico: 

Esta fase consiste en realizar pruebas de seguridad dinámicas del dispositivo y las interfaces de las aplicaciones para encontrar todas las vulnerabilidades posibles.

En nuestro caso haríamos lo mismo que en la fase anterior pero esta vez intentando encontrar un mayor número de vulnerabilidades. Esto lo haríamos por ejemplo combinando Quemu con herramientas de Fuzzing como ClusterFuzz o FormatFuzzer.
   
#### 8. Análisis en tiempo de ejecución: 

Esta fase consiste en analizar los ejecutables durante el tiempo de ejecución en el dispositivo con el fin de encontrar problemas de seguridad.

En esta fase usaríamos herramientas de depuración como Eclipse CDT, NetBeans o gdbgui para detectar, identificar y comprobar puntos críticos del ejecutable, ya sea de forma parcial o completa.
   
#### 9. Explotación: 

Esta fase se centraría en explotar todas las vulnerabilidades descubiertas en las fases anteriores para obtener ejecución de código arbitrario, elevación de privilegios, etc.

En esta fase de explotación utilizaríamos todas las técnicas posibles para conseguir vulnerar el dispositivo mediante el uso de herramientas como Metaexploit, exploits de desbordamiento de búfer o inyección de código, scripts, etc...

#### 10. Documentación: 

Esta fase la he querido incluir yo para realizar un informe completo y detallado donde especifiquemos todas las vulnerabilidades encontradas y como se podrían solucionar si fuera posible así como algunas medidas de seguridad que deben aplicar la empresa para mejorar la seguridad de la misma.


### Bibliografía

https://owasp.org/www-project-internet-of-things/
https://www.tarlogic.com/es/blog/analisis-de-seguridad-en-iot-owasp/
https://www.tarlogic.com/es/blog/owasp-fstm-reconocimiento-informacion/
https://www.tarlogic.com/es/blog/owasp-fstm-obtencion-firmware-iot/
https://auditordeciberseguridad.es/implementando-itdr-10-acciones-para-proteger-el-directorio-activo-3/
https://www.tarlogic.com/es/blog/owasp-fstm-etapa-3-analisis-del-firmware/
https://www.tarlogic.com/es/blog/owasp-fstm-extraccion-sistema-ficheros/
https://www.tarlogic.com/es/blog/owasp-fstm-analisis-sistema-ficheros/
https://www.tarlogic.com/es/blog/owasp-fstm-etapa-6-emulacion-del-firmware/
https://www.tarlogic.com/es/blog/owasp-fstm-analisis-dinamico/
https://www.tarlogic.com/es/blog/owasp-fstm-analisis-en-tiempo-de-ejecucion/
https://www.tarlogic.com/es/blog/owasp-fstm-etapa-9-explotacion-de-ejecutables/
https://www.tarlogic.com/es/blog/analisis-de-seguridad-iot-owasp-fstm/
https://github.com/scriptingxss/owasp-fstm
https://www.tarlogic.com/es/glosario-ciberseguridad/fstm/