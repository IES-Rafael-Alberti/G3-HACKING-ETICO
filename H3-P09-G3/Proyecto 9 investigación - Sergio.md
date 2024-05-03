# Investigación Hackrf One

## ¿Qué es Hackrf One?¿Cuáles son sus características?

La HackRF One es un SDR. El término SDR o "Software Defined Radio" por sus siglas en inglés se utiliza para definir dispositivos que implementan en software los componentes encargados de modular y demodular señales de radio en lugar de hacerlo por hardware. La idea es tener un dispositivo capaz de recibir y transmitir distintos protocolos de radio solo teniendo que configurar su software para hacerlo.

**Características** 

- Frecuencia de funcionamiento de 1MHz a 6GHz.
- Transceptor semidúplex.
- 20 millones de muestras por segundos.
- Muestras de cuadraturas de 8 bits.
- Compatible con GNU Radio, SDR#, SDR-Console, SdrAngel, Remote SDR v5 etc..
- Filtro de banda base y ganancia RX y TX configurable por software.
- Alimentación del puerto de antena controlada por software.
- Conector de antena SMA hembra.
- Entrada y salida de reloj SMA hembra para sincronización exterior.
- Botones para programar.
- Puerto interno para expansión.
- USB2.0 de alta velocidad.
- Alimentado por USB.
- Hardware de código abierto.

## Usos comunes de Hackrf One

Hackrf One permite varios usos, como hacer ingienería inversa a cualquiekr protocolo de radiofrecuencias pero también permite lo siguiente:

- Analizar, reproduce y emula mandos de vehículos, alarmas, mados para garajes, etc.
- Permite bloquear, manipular o ajustar señales de GPS para dispositivos con esta cualidad.
- Captura y analiza GMS.
- Sniffing, captura y analiza el tráfico Bluetooth y BLE.
- Analizar y comunicarse con todas las etiquetas RFDI.
- Rastreo ADB-S, comunicación por satélite, detección de paquetes y análisis de señales.

## Usos por atacantes y para pentesting

Como hemos visto en los usos comunes de Hackrf One, un atacante podría por ejemplo bloquear señales hacia su victima como señales GPS.

Pueden grabar y repetir señales de radio para emular cualquier tipo de señal y usarla como por ejemplo para abrir la puerta de un vehículo.

También puede ser utilizado para ataques de tipo lateral permitiendo al atacante visualizar el monitor de su victima y ver en pleno directo o grabar dicha visualización.

Por lo tanto, teniendo en cuenta las posibilidades de un atacante con este dispositivo, podemos visualizar las posbilidades de uso para un pentesting a dispositivos Wireless. Pudiendo hacer con él, un sniff de señales Wifi o de bluetooth permitiendonos analizar dichas señales, repetirlas o emularlas.

## Referencias

- [https://www.astroradio.com/p/hackrf-one/](https://www.astroradio.com/p/hackrf-one/)
- [https://lab401.com/es-es/products/hackrf-one](https://lab401.com/es-es/products/hackrf-one)
- [https://www.jtsec.es/es/entrada-blog/111/usos-comunes-y-puesta-en-marcha-de-una-hackrf-one](https://www.jtsec.es/es/entrada-blog/111/usos-comunes-y-puesta-en-marcha-de-una-hackrf-one)

