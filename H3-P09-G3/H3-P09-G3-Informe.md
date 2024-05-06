# Índice

- [Resumen Ejecutivo](#resumen-ejecutivo)
- [Tabla de Riesgos](#tabla-de-riesgos)
- [Evaluación](#evaluacion)
    - [Breve Resumen](#breve-resumen)
    - [Tabla de Hallazgos](#tabla-de-hallazgos)
      - [PC-1](#vulnerabilidades-PC1)
      - [PC-2](#vulnerabilidades-PC-2)
- [Trayectoria de ataque](#trayectoria-de-ataque)
- [Metodologías](#metodologías)
  - [Herramientas utilizadas](#herramientas-utilizadas)
  - [Procedimiento](#procedimiento)
    - [Fase 1: Reconocimiento](#fase-1-reconocimiento)
    - [Fase 2: Explotación](#fase-2-explotación)
- [Conclusión](#conclusión)

# Resumen Ejecutivo

# ¿Qué es Hackrf One? ¿Cuáles son sus características?

HackRF One es un periférico SDR. El término de SDR o "Software Defined Radio" por sus siglas en inglés se utiliza para definir dispositivos que implementan en software los componentes encargados de modular y demodular señales de radio en lugar de hacerlo por hardware. La idea es tener un dispositivo capaz de recibir y transmitir distintos protocolos de radio solo teniendo que configurar su software para hacerlo.

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

# Software del Hackrf One

Desde 2014 HackRF One funciona con varios softwares SDR. Gracias a que es de código abierto y libre de licencias de pago.

# Circuito del Hackrf One

La entrada de antena tiene dos amplificadores MGA-81 GaAs MMIC, uno sirve para la entrada, y el otro para la salida. Los amplificadores ICs pueden ser seleccionados para la entrada o salida de señal usando las teclas RF.

El bloque del amplificador va seguido de un filtro pasa bajo y otro pasa alto, los cuales se pueden usar para limitar la señal en cualquier sentido (entrada o salida).

Después del filtro, la señal llega al mezclador de RF RFFC 5072. Este mezclador puede usarse hasta los 6GHz. La señal es mezclada arriba o abajo, dependiendo de la programación del usuario y finalmente llevada al circuito de banda base.

El mezclador y los filtros pueden puentearse usando otras teclas RF, permitiendo asi que las señales IF puedan ser cambiadas directamente en los amplificadores o directamente en la antena.

El chip de la banda base se usa un componente Maxim MAX2837, el cual cubre de 2.3 a 2.7 GHz. Este chip usa filtros monoliticos que ofrecen una señal muy lineal y bajo nivel de ruido. Los datos IQ son luego llevados a un chip ADC/DAC Maxim MAX5864. 

Este usa una resolución de 8 bits. Estos conversores soportan una sample rate máxima de 20MS/s.Las señales digitales son finalmente enviadas a un CPLD Xilinx XC2C. Todo el sistema y las interfaces son controladas por un potente procesador ARM Dual Core Cortex (NXP LPC4320) y la placa soporta una memoria flash de 1MB flash.

# Usos comunes de Hackrf One

Hackrf One permite varios usos, como hacer ingienería inversa a cualquiekr protocolo de radiofrecuencias pero también permite lo siguiente:

- Analizar, reproduce y emula mandos de vehículos, alarmas, mados para garajes, etc.
- Permite bloquear, manipular o ajustar señales de GPS para dispositivos con esta cualidad.
- Captura y analiza GMS.
- Sniffing, captura y analiza el tráfico Bluetooth y BLE.
- Analizar y comunicarse con todas las etiquetas RFDI.
- Rastreo ADB-S, comunicación por satélite, detección de paquetes y análisis de señales.

# Usos por atacantes y para pentesting

Como hemos visto en los usos comunes de Hackrf One, un atacante podría bloquear señales hacia su victima como señales GPS. Pueden grabar y repetir señales de radio para emular cualquier tipo de señal y usarla como por ejemplo para abrir la puerta de un vehículo.

También puede ser utilizado para ataques de tipo lateral permitiendo al atacante visualizar el monitor de su victima y ver en pleno directo o grabar dicha visualización.

Por lo tanto, teniendo en cuenta las posibilidades de un atacante con este dispositivo, podemos visualizar las posbilidades de uso para un pentesting a dispositivos Wireless. Pudiendo hacer con él, un sniff de señales Wifi o de bluetooth permitiendonos analizar dichas señales, repetirlas o emularlas.

# Referencias

- Astroradio (s.f.) Hackrf One. Recuperado de [https://www.astroradio.com/p/hackrf-one/](https://www.astroradio.com/p/hackrf-one/)
- Lab401 (s.f.) Hackrf One. Recuperado de [https://lab401.com/es-es/products/hackrf-one](https://lab401.com/es-es/products/hackrf-one)
- Wimo (s.f.) Hackrf One. Recuperado de [https://www.wimo.com/es/hackrf-one](https://www.wimo.com/es/hackrf-one)
- Sergio, G. (12/05/2022) Usos comunes y puesta en marcha de una HackRF One. Recuperado de [https://www.jtsec.es/es/entrada-blog/111/usos-comunes-y-puesta-en-marcha-de-una-hackrf-one](https://www.jtsec.es/es/entrada-blog/111/usos-comunes-y-puesta-en-marcha-de-una-hackrf-one)