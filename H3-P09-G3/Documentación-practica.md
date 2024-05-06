# Documentación de la demostración práctica

En este anexo se recoge una serie de detalles más técnicos acerca de la demostración que se va a realizar en clase con el HackRF One, la cuál consistirá en una demostración de la capacidad como transceptor (receptor y transmisor) y en una prueba de _Jamming_, básicamente una inhibición de señal por parte del dipositivo.

## Materiales

Los materiales necesarios para la demostración son los siguientes:

### Hardware

- HackRF One
- Antena
- Ordenador portátil con sistema operativo linux (Ubuntu)
- Router WiFi con capacidad de transmitir en bandas 5GHz y 2.4GHz
- Radio AM/FM
- Llave inálambrica de coche

### Software
- GNU Radio 3.10.7
- GQRX 2.17.5
- App Móvil WiFi Analyzer

## Capacidad receptora del HackRF One

En esta parte de la demostración se utilizará el software **GQRX** para utilizar el HackRF One como receptor de las ondas de radio comunes como son las comprendidas en las bandas AM/FM, básicamente las frecuencias de radio que la mayoría de cadenas emisoras utilizan para retransmitir programas o música. 

Para ello tan solo tendremos que configurar la frecuencia de recepción del HackRF One en **valores comprendidos entre 88 a 108 MHz** mediante el software **GQRX** para recibir algún que otro programa de radio y visualizar el espectrograma que estas ondas capturan.

También se realizará una prueba en la que se clona la señal para abrir un coche a distancia y se podrá visualizar y capturar con el HackRF

## Transmisión en bandas FM/AM

En esta parte de la demostración se utilizará el software **GNU Radio** con ayuda de pruebas de concepto y esquemas realizados y publicados en blog de radiofrecuencias por *Marc Steele*, el cual los facilita y aporta una documentación más técnica que podrá consultarse en caso de requerir más información acerca de la prueba.

En esta sección de la demostración se procederá a emitir una canción en una frecuencia que no esté ocupada por ninguna cadena emisora utilizando el esquema proporcionado, el cual consite en la construcción visual de un script de python al final. Se intentará transmitir en las bandas FM y AM, probablemente siendo esta última muy poco clara y apenas perceptible. 

Se propondrá también un pequeño ejercicio de ingeniería social utilizando esta técnica.

## Jamming de señales Wifi 5GHz y 2.4GHz

En esta última parte de la demostración se intentará realizar un ejercicio de pentesting más directo el cual consiste en inhibir una señal WiFi tanto de 2.4GHz como de 5GHz mediante el uso de otro esquema de GNU Radio proporcionado por el repositorio **CleverJAM** del usuario **jhonnybonny**. 

Para esta parte se hará uso de GNU Radio para que el HackRF emita una señal de ruido gausiano configurada adecuadamente para interferir las ondas Wifi

## Referencias

- Marc Steele. Construcción de un transmisor FM de muy baja potencia con HackRF One. Recuperado de https://www.dlineradio.co.uk/articles/building-a-very-low-power-fm-transmitter-with-hackrf-one/

- CleverJAM. Recuperado de https://github.com/jhonnybonny/CleverJAM

- Marc Steele. Construcción de un transmisor AM con HackRF One. Recuperado de https://www.dlineradio.co.uk/articles/building-an-am-transmitter-with-hackrf-one/
