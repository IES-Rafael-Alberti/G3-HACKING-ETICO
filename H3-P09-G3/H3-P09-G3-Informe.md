# Índice

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [¿Qué es Hackrf One? ¿Cuáles son sus características?](#qué-es-hackrf-one--cuáles-son-sus-características)
3. [Software del Hackrf One](#software-del-hackrf-one)
4. [Circuito del Hackrf One](#circuito-del-hackrf-one)
5. [Usos comunes de Hackrf One](#usos-comunes-de-hackrf-one)
6. [Usos por atacantes y para pentesting](#usos-por-atacantes-y-para-pentesting)
7. [Referencias](#referencias)

# Resumen Ejecutivo

HackRF One es un periférico SDR que ofrece una amplia gama de funcionalidades gracias a su versatilidad y características técnicas avanzadas. Este dispositivo opera en un rango de frecuencia de 1 MHz a 6 GHz, con un ancho de banda de 20 MHz y una sensibilidad de recepción de hasta -121 dBm. Con una potencia de transmisión de +10 dBm y una interfaz Hi-Speed USB 2.0, el HackRF One es compacto y fácil de usar. Sus características adicionales incluyen muestras de cuadratura de 8 bits, compatibilidad con una amplia gama de software SDR, filtros configurables por software y control de alimentación de antena. Desde 2014, HackRF One es compatible con varios softwares SDR, lo que le brinda a los usuarios flexibilidad y opciones para adaptarse a sus necesidades específicas. Además de sus usos legítimos, HackRF One también puede ser utilizado por atacantes con fines maliciosos, por lo que es importante comprender las posibilidades de uso indebido de este dispositivo y considerar las medidas de seguridad adecuadas.

# ¿Qué es Hackrf One? ¿Cuáles son sus características?

HackRF One es un periférico SDR. El término de SDR o "Software Defined Radio" por sus siglas en inglés se utiliza para definir dispositivos que implementan en software los componentes encargados de modular y demodular señales de radio en lugar de hacerlo por hardware. La idea es tener un dispositivo capaz de recibir y transmitir distintos protocolos de radio solo teniendo que configurar su software para hacerlo.

**Características** 

- **Rango de frecuencia:** 1 MHz a 6 GHz
- **Ancho de banda:** 20 MHz
- **Sensibilidad de recepción:**
    - 121 dBm a 10 MHz
    - 117 dBm a 1 GHz
    - 110 dBm a 6 GHz
- **Sample rate:** 20 MS/s (millones de muestras por segundo)
- **Potencia de transmisión:** +10 dBm (100 mW)
- **Interfaz:** Hi-Speed USB 2.0
- **Formato de muestreo:** 8 bits
- **Alimentación:** USB
- **Dimensiones:**
    - Tamaño: 100 mm x 60 mm x 21 mm
    - Peso: 86 g
- **Muestras de cuadratura:** 8 bits (I de 8 bits y Q de 8 bits)
- **Compatibilidad con software:** 
  - Compatible con las principales suites SDR a través de múltiples plataformas como GNU Radio, SDR#, SDR_Radio, Universal Radio Hacker, QSpectrumAnalyzer1, así como otros programas como SDR-Console, SdrAngel, Remote SDR v5, entre otros.
- **Características adicionales:**
    - Filtro de ganancia de banda base y banda RX y TX configurables por software
    - Alimentación de puerto de antena controlada por software (50 mA a 3,3 V)
    - Conector de antena: SMA hembra
    - Conector SMA para reloj de entrada y salida hembra para sincronización
    - Botones convenientes para la programación
    - Encabezados internos para expansión
- **Transceptor:** Semidúplex
- **Puerto interno para expansión**
- **Código abierto:** Hardware de código abierto

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
- Análisis software y hardware del SDR HackRF One. Recuperado de [https://digibug.ugr.es/bitstream/handle/10481/48019/RodriguezHaro_PFC_SDR_HackRF.pdf?sequence=1](https://digibug.ugr.es/bitstream/handle/10481/48019/RodriguezHaro_PFC_SDR_HackRF.pdf?sequence=1)
- [https://www.wimo.com/es/hackrf-one](https://www.wimo.com/es/hackrf-one)
- [https://www.amazon.es/HackRF-Software-Definida-ANT500-Adaptador/dp/B01K1CCHR0/ref=sr_1_5?adgrpid=1295225132299712&dib=eyJ2IjoiMSJ9.uhYU1kaYKizrG9Jx0BgQhr3h6jbAa9arPMcfJ6VAht_XbQnweT6fMTI9qrebmnKHvcvv8GEL9DxsN_ZP8SJHDkQD6HX1W3IEBlxfXHe36Q6D8XRs1bZQMAoBfhTAOw-_9KTixaJmr-bJhWo1OpWXmkHkH5uJiIHIcBa_dhSm-diDq1iQLKxQo1mgrSskTku0y5b74s6Pcg-aU64ikYRGtWeWetme_eFTeP5Ug10p6nm8SMa31taIVqZTWrTGLkNXWvPmL417Q6IJebxxOC0h69l-wYpwS6UeXC07JNlC_hc.BMpLK-EmYI0sdYS7c_-ZwbBAHI0uyfvxcv737MHuq6s&dib_tag=se&hvadid=80951659589295&hvbmt=bp&hvdev=c&hvlocphy=3178&hvnetw=o&hvqmt=p&hvtargid=kwd-80951805084598%3Aloc-170&hydadcr=11864_1899374&keywords=hackrf+one&qid=1715016674&sr=8-5](https://www.amazon.es/HackRF-Software-Definida-ANT500-Adaptador/dp/B01K1CCHR0/ref=sr_1_5?adgrpid=1295225132299712&dib=eyJ2IjoiMSJ9.uhYU1kaYKizrG9Jx0BgQhr3h6jbAa9arPMcfJ6VAht_XbQnweT6fMTI9qrebmnKHvcvv8GEL9DxsN_ZP8SJHDkQD6HX1W3IEBlxfXHe36Q6D8XRs1bZQMAoBfhTAOw-_9KTixaJmr-bJhWo1OpWXmkHkH5uJiIHIcBa_dhSm-diDq1iQLKxQo1mgrSskTku0y5b74s6Pcg-aU64ikYRGtWeWetme_eFTeP5Ug10p6nm8SMa31taIVqZTWrTGLkNXWvPmL417Q6IJebxxOC0h69l-wYpwS6UeXC07JNlC_hc.BMpLK-EmYI0sdYS7c_-ZwbBAHI0uyfvxcv737MHuq6s&dib_tag=se&hvadid=80951659589295&hvbmt=bp&hvdev=c&hvlocphy=3178&hvnetw=o&hvqmt=p&hvtargid=kwd-80951805084598%3Aloc-170&hydadcr=11864_1899374&keywords=hackrf+one&qid=1715016674&sr=8-5)
- [https://lab401.com/es-es/products/hackrf-one](https://lab401.com/es-es/products/hackrf-one)
