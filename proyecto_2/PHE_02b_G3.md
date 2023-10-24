# Proyecto 2: Offensive Audit Services

<br/>

![Portada](img/Cabecera_Auditoría_seg_infor.jpg)

**Autores:** *Grupo 3*

**Integrantes:**
- Raúl Ladrón de Guevara García
- Juan Manuel Cumbrera López
- Christian Romero Oliva
- Sergio Guerrero Merlo

## Índice

- [Introducción](#introducción)
- [Tipos de Ataque clasificados por área](#tipos-de-ataques-clasificados-por-área)
  - [Investigación de Tipos de Ataques](#investigación-de-tipos-de-ataques)
    - [Ataques en Correos Electrónicos](#ataques-en-correos-electrónicos)
    - [Ataques en la Red](#ataques-en-la-red)
    - [Ataques en el Área Web](#ataques-en-el-área-web)
    - [Ataques en Software](#ataques-en-software)
- [Tipos de Auditorías Ofensivas ofrecidas](#tipos-de-auditorías-ofensivas-ofrecidas)
    - [Auditoría de Correos Electrónicos](#1-auditoría-de-correos-electrónicos)
    - [Auditoría de Red Inalámbrica](#2-auditoría-de-red-inalámbrica)
    - [Auditoría Externa o Perimetral](#3-auditoría-externa-o-perimetral)
    - [Auditoría IOT](#4-auditoria-iot)
    - [Auditoría de Seguridad de Software](#5-auditoría-de-seguridad-de-software)
- [Metodologías de Pentesting utilizadas](#metodologías-de-pentesting-utilizadas)
    - [Metodología para Auditorías de Correos Electrónicos](#1-metodología-para-auditorías-de-correos-electrónicos)
    - [Metodología para Auditorías de IOT](#2-metodología-para-auditorías-de-iot)
    - [Metodología OWISAM para Redes Inalámbricas](#3-metodología-owisam-para-redes-inalámbricas)
    - [Metodología PTES](#4-metodología-ptes)
- [Herramientas de Pentesting](#herramientas-de-pentesting)
    - [Herramientas para Pentesting de Correos Electrónicos](#herramientas-para-pentesting-de-correos-electrónicos)
    - [Herramientas para Pentesting de Redes](#herramientas-para-pentesting-de-redes)
    - [Herramientas para Pentesting de Software](#herramientas-para-pentesting-de-software)
- [Conclusión](#conclusión)
- [Bibliografía](#bibliografía)

## Introducción

En el mundo actual en la era digital la evolución es frenética y constante. Este hecho supone grandes avances en materia informática, lo que lleva a mejorar las vidas de millones de personas, ofreciendo facilidades y soluciones que en años pasados se antojaban como ‘fantásticas’, y en algunos casos hasta ’futuristas’. La realidad, sin embargo, no está carente de ciertos problemas, y esto se debe principalmente a dos factores, el factor humano, ya sea debido a un descuido o el desconocimiento por parte de un trabajador o particular, o por la maldad inherente a ciertas personas, que les mueve a querer perpetrar acciones ilegales contra empresas y/o particulares, ya sea por motivo de lucro, por motivos políticos o incluso simplemente sólo por el placer de hacerlo; y las múltiples vulnerabilidades y fallos de seguridad en sistemas existentes, que abren una puerta a una infinidad de posibles ataques, lo que conforma el mundo de la ciberseguridad. 

Debido a estas dos poderosas razones, hemos podido ver un aumento exponencial de las amenazas cibernéticas, lo que ha llevado a profesionales de la seguridad ofensiva a comprender, clasificar y abordar una amplia variedad de tipos de ataques capaces de poner en peligro la seguridad de las organizaciones. Estos profesionales se dan a la tarea de estudiar estos ataques, analizarlos a profundidad y clasificarlos, para así poder entenderlos en términos de sus características, métodos y objetivos, para poder determinar cuáles son los más críticos desde el punto de vista de una organización.

Además de clasificar estos ataques, también se busca diseñas estrategias de auditoría ofensiva, lo cual es un componente esencial en el ámbito de la ciberseguridad. Las auditorías ofensivas nos permiten identificar debilidades y vulnerabilidades en sistemas, aplicaciones y redes antes que los atacantes las puedan explotar.

## Tipos de Ataques clasificados por área

Como antes hemos explicado, el modus vivendi de los profesionales de la ciberseguridad orbita en torno a la búsqueda y estudio de las vulnerabilidades y fallos de seguridad informáticos, analizando y comprendiendo los diversos tipos de ataques que los sistemas y aplicaciones pueden sufrir, anticipándose a ellos. 

Precisamente por ese motivo llevaremos a cabo una investigación y subsiguiente clasificación de la amplia gama de tipos de ataques posibles, así como de los tipos de auditorías ofensivas que ofrecemos, exponiendo una descripción de los susodichos servicios.

Cuando hablamos de tipos de ataques informáticos, nos viene a la mente una gran cantidad y diversidad de formas, comúnmente maliciosas, de acceder de una forma no autorizada a sistemas e incluso controlarlos, obtener datos confidenciales, e incluso producir daños en los equipos, redes, sistemas y servicios que sufran estos ataques cibernéticos. El mundo de la informática es amplio, así como por extensión lo es el de la ciberseguridad, y es por ello que hemos de comprender la rama de posibles áreas donde estos cibercrímenes son perpetrados.

Por motivos de comprensión y de organización, dividiremos este abanico de ataques entre las diferentes áreas susceptibles de sufrir ataques, que son el software, los servicios de mensajería electrónica, las páginas web, las redes informáticas y el IOT (Internet of Things).

### Investigación de Tipos de Ataques

Cuando hablamos de tipos de ataques informáticos, nos viene a la mente una gran cantidad y diversidad de formas, comúnmente maliciosas, de acceder de una forma no autorizada a sistemas e incluso controlarlos, obtener datos confidenciales, e incluso producir daños en los equipos, redes, sistemas y servicios que sufran estos ataques cibernéticos. El mundo de la informática es amplio, así como por extensión lo es el de la ciberseguridad, y es por ello que hemos de comprender la rama de posibles áreas donde estos cibercrímenes son perpetrados.

Por motivos de comprensión y de organización, dividiremos este abanico de ataques entre las diferentes áreas susceptibles de sufrir ataques, que son el software, los servicios de mensajería electrónica, las páginas web, las redes informáticas y el IOT (Internet of Things).

#### Ataques en Correos Electrónicos

##### 1. Phishing

El **phishing** es una técnica de estafa en la que se hace uso de técnicas de ingeniería social para engañar a un usuario con el fin de obtener información privada, beneficios económicos o incluso para instalar malware en el dispositivo.

Dentro del phising existen múltiples variantes como:

- **Deceptive Phishing (Phishing clásico):** Consiste en suplantar la identidad mediante el envío de un correo electrónico por parte de un ciberdelincuente a un usuario simulando ser una entidad legítima (red social, banco, institución pública, etc.) con el objetivo de robarle información privada, realizarle un cargo económico o infectar el dispositivo. Para ello, adjuntan archivos infectados o enlaces a páginas fraudulentas en dicho correo electrónico.
  
- **Spear phishing (dirigido a individuos específicos):** Consiste en un tipo de estafa muy similar al phishing clásico, pero con la diferencia de que van dirigidos a una o varias víctimas en concreto. Este tipo de correos electrónicos se preparan de manera bastante más sofisticada ya que primero estudian a las víctimas (sus gustos, preferencias, etc..) y luego elaboran el correo electrónico según el perfil estudiado de la víctima por lo que es mucho más efectivo ya que es más complicado que un usuario lo detecte.

- **Whaling (Caza de la ballena):** Esta estafa consiste en la suplantación de identidad de altos cargos de las empresas, como directores generales, directores de operaciones, presidentes o personas importantes dentro de esta para que compartan credenciales, acceder a redes que están muy protegidas o simplemente robar dinero o datos. Emplean tácticas más avanzadas y sofisticadas que otros tipos de ataques hasta el punto de realizar una investigación y planificación previa.
Se utilizan nombres, direcciones, cargos u otra información personal para crear una apariencia más sólida y creíble para el ataque.

- **Pharming:** Es un método en el que el tráfico de la navegación, vinculado a un correo recibido, se redirige para que el usuario crea que está navegando en el sitio web deseado. En realidad, se conecta al sitio web del ciberdelincuente, lo que puede resultar en la obtención de credenciales o información personal con el fin de usurpar la identidad de alguien.
Este tipo de ataque suele aprovechar la navegación en línea de las víctimas al corromper el sistema de nombres de dominio (DNS). El atacante envenena el DNS y lo modifica de manera que los usuarios visiten sitios web maliciosos en lugar de los sitios legítimos, sin que ellos lo sepan.

- También existen más variantes como por ejemplo, el Vishing (phishing a través de llamadas telefónicas) o como el Smishing (phishing a través de mensajes de texto), Angler Phishing (Dirigido a los usuarios de las redes sociales), etc.. pero en estos no me centraré ya que no entran en el área de los correos electrónicos.

##### 2. Spoofing

El **email spoofing** consiste en la suplantación de identidad por correo electrónico, que se produce cuando un atacante envía un correo electrónico a un usuario haciéndose pasar por otra persona o empresa. Esto se consigue camuflando la dirección de correo electrónico de forma que la sustituyen por una legítima. Un ejemplo puede ser que el atacante use paypa1.com en vez de paypal.com. La mayoría de usuarios a los que van destinados estos correos no se suelen fijar bien en la dirección si el nombre le resulta familiar o simplemente ni la leen por lo que no se dan cuenta de que se trata de una dirección de correo falsa.

Los atacantes consiguen camuflar las direcciones de correo electrónico debido a la falta de seguridad del protocolo simple de transferencia de correo (SMTP), que no admite cifrado, autenticación ni otras medidas de seguridad similares. Por ejemplo, los servidores de correos más reconocidos como pueden ser Gmail o Outlook utilizan este protocolo por lo que es muy fácil para los atacantes hacer este cambio de dirección.

Si bien es similar al phishing, estos dos ataques son distintos. El phishing busca robar información personal o credenciales a través de engaños o estafas, mientras que el email spoofing su objetivo principal es suplantar la identidad de alguien en un correo electrónico, lo que puede llevar a ataques de phishing, pero su objetivo principal es la suplantación de identidad.

##### 3. Spam

El spam de correos electrónicos es un tipo de comunicación masiva que se envía principalmente por motivos comerciales. A los atacantes que realizan el envió de este tipo de correos se les suele llamar "Spammers". Estos correos electrónicos suelen contener publicidad no deseada, promociones, malware, enlaces a sitios web falsos o contenido irrelevante. 

Algunos ejemplos pueden ser:

- Ofertas para ganar dinero rápido.
- Ofertas incitantes como descuentos o promociones.
- Mensajes de préstamos o créditos no solicitados.
- Notificaciones de facturas falsas.

Aunque en la mayoría de los casos no se considera dañino, puede resultar molesto y difícil de filtrar. También es importante destacar que el spam puede llevar a la pérdida de productividad y tiempo para los usuarios, ya que deben dedicar tiempo a eliminar o ignorar estos correos no deseados.
Para combatir el spam, se utilizan filtros de correo electrónico que intentan bloquear estos mensajes no deseados antes de que lleguen a la bandeja de entrada del usuario.

##### 4. Scam

El scam son los intentos de estafas llevadas a cabo a través de correos electrónicos, cuyo objetivo es engañar al usuario para que cometan una acción legítima, pero en realidad no lo son. En la mayoría de los casos, se pretende estafar económicamente pero también se utiliza para instalar malware o robar información.

Algunos ejemplos pueden ser:

- Correos de servicios donde piden actualizar información.
- Donaciones.
- Premios de lotería.
- Pago de donaciones a ONGs falsas.
- Servicios de renovación como por ejemplo seguros de coches o plataformas de streaming (Netflix, Twitch, HBO, etc...)
- Soporte o asistencia técnica.

El funcionamiento del scam se divide en tres etapas:

- 1: Los estafadores establecen contacto con la víctima a través de correos electrónicos no solicitados e intenta atraer la atención de la víctima y establecer una comunicación inicial.
  
- 2: Una vez que se ha establecido el contacto, el estafador comienza a engañar o manipular a la víctima ofreciéndole ofertas, soporte o algunos de los ejemplos que especifico arriba.

- 3: Una vez que se ha conseguido engañar a la víctima, el atacante recibe dinero, información confidencial o simplemente infecta el dispositivo de la víctima con malware.


##### 5. Malware

**Malware o “software malicioso”** es un término amplio que describe cualquier programa o código malicioso que es dañino para los sistemas. Los ataques de malware a través del correo electrónico son muy habituales y generan una amenaza persistente y creciente en el mundo actual. Los atacantes lo usan para robar, cifrar o borrar datos, alterar o secuestrar funciones básicas del dispositivo e incluso para espiar su actividad sin su permiso.

Como existen muchos tipos de malware y mis compañeros también lo van a detallar y a explicar, mostraré algunos ejemplos de los más comunes que se distribuyen por correo electrónico:

###### 5.1. Troyanos (Caballos de Troya)

Es un tipo de archivo que contiene malware y que comúnmente se camuflar dentro de un software legítimo adjunto a un correo electrónico. Aunque el correo electrónico y el archivo adjunto parezcan legítimos y procedan de una fuente fiable, cuando la víctima hace clic en ellos, el malware se instala en su ordenador. Los troyanos pueden utilizarse para robar datos, controlar el equipo para ser usado por una red de bots (BotNet) o incluso borrar completamente todos los archivos del disco duro.

Algunos ejemplos de troyanos relacionados con los correos electrónicos pueden ser:

- **Mailfinders:** Este troyano está diseñado para recopilar direcciones de correos electrónicos desde un dispositivo y luego enviarlos a los atacantes a través de un correo, un servidor FTP u otros medios. Una vez el atacante consigue todos estos correos electrónicos, los utiliza para realizar spam de todo tipo de correos.

- **Emotet:** Es un troyano que a menudo se distribuye a través de correos electrónicos de phishing. Funciona de tal manera que, si hay una red conectada, se propaga utilizando una lista de contraseñas comunes y averigua el camino hacia otros sistemas conectados en un ataque de fuerza bruta.

- **Dridex:** Es un troyano bancario que ha sido conocido por propagarse a través de correos electrónicos de phishing. Los correos electrónicos contienen documentos maliciosos de Microsoft Word o Excel que, cuando se abren, descargan y ejecutan el malware.

- **TrickBot:** Es un conocido troyano bancario que se utiliza principalmente para robar información financiera y realizar actividades maliciosas en los dispositivos infectados.

###### 5.2. Gusanos

Son un tipo de malware que tienen la peculiaridad de replicarse para propagarse a otras dispositivos. Utiliza la red para propagarse, aprovechando las fallas de seguridad en el dispositivo de destino para acceder a él.
<br>
Un ejemplo muy común es el del gusano ILOVEYOU que se propagó a través de un correo electrónico con un asunto que decía "ILOVEYOU". Este afectó a millones de dispositivos en todo el mundo en el año 2000. Una vez abierto, el virus se replicaba y se enviaba a todos los contactos en la libreta de direcciones de la víctima.

###### 5.3. Backdoors (Puertas traseras)

Este tipo de malware permite al atacante tener control remoto total en el dispositivo infectado. 
El atacante puede hacer lo que quiera en el dispositivo, como, por ejemplo, enviar y recibir archivos, ejecutar archivos, mostrar mensajes, borrar datos, reiniciar el equipo, etc...
  
###### 5.4. Rootkits

Este de malware es diseñado para no ser detectado por los sistemas operativos y los antivirus/ antimalwares y trabajar en segundo plano. Con este tipo de malware consiguen tener acceso al dispositivo durante un periodo más largo.

###### 5.5. Keyloggers
Es un tipo de malware que se ejecuta en nuestro dispositivo en segundo plano y que permite registrar todas las pulsaciones de teclas que se realicen en este.

###### 5.6. Ransomware

Es un tipo de malware que impide a los usuarios acceder a su sistema o a sus archivos personales y que exige el pago de un rescate para poder acceder de nuevo a ellos.

Es muy común que los atacantes o ciberdelincuentes utilicen ataques como el phishing o el spam para incluir este malware en el contenido del correo electrónico de alguna forma.

##### 6. Apropiación de cuentas de correo electrónico

La apropiación de cuentas de correos electrónicos es una práctica muy común entre los ciberdelincuentes. 
Los atacantes se apropian de los correos electrónicos de los usuarios reales con la intención de realizar actividades como controlar sus mensajes, robar información, enviar malware a otras cuentas, realizar spam.

Existen muchas técnicas que usan los atacante para apropiarse de las cuentas:

- **Phishing:** Podrían engañar a al usuario redirigiéndolos a sitios web falsos donde tienen que ingresar sus credenciales.

- **Fuerza bruta:** Consiste en ir probando diferentes combinaciones de contraseñas hasta que encuentran la correcta. Puede ser lento y requiere paciencia, pero puede ser efectivo si la contraseña es débil.

- **Ataque de diccionario:** Los atacantes utilizan herramientas que prueban una lista de contraseñas comunes y palabras para adivinar la contraseña de la cuenta.

- **Reutilización de contraseñas:** Es muy común que los usuarios utilicen la misma contraseña para varios servicios o páginas web por lo que si alguno de estos servicios sufre una brecha de seguridad en la que se filtran credenciales los atacantes podrían comprobar esas mismas credenciales en otros servicios o páginas web.

- **Ingeniería social:** Consiste en manipular a la víctima para que revele sus credenciales de correo electrónico. Por ejemplo, haciéndose pasar por alguien de confianza, por alguien de alguna empresa y utilizar excusas o justificaciones para obtener la información.

- **Malware:** El malware infecta el dispositivo de la víctima por lo que se podría utilizar por ejemplo un keylogger para obtener las credenciales. Otro ejemplo seria usar malware capaz de robar las cookies de inicio de sesión o tokens de acceso.

- **Recuperación de contraseñas débiles:** Si la opción de recuperación de contraseña se basa en información personal que es fácil de obtener (como una pregunta de seguridad que se puede responder buscando en las redes sociales), los atacantes pueden restablecer la contraseña de la cuenta.

- **Explotación de vulnerabilidades:** El atacante podría aprovechar vulnerabilidades en los protocolos del servidor de correo para acceder a las cuentas de los usuarios.

##### 7. Interceptación de correos electrónicos

La interceptación de correos electrónicos es una actividad que implica que el atacante pueda leer o incluso modificar los correos electrónicos que se envían desde una persona a otra, situándose en medio de la comunicación (man-in-the-middle). 
Los atacantes interceptan los mensajes para robar la información que contienen, o para llevar a cabo ataques en los que se hacen pasar por ambas partes de una conversación.
El método más común para hacerlo es la monitorización de los paquetes de datos de la red en las redes de área local, ya que interceptar un correo electrónico mientras viaja por Internet es muy complicado.

##### 8. E-mail Bombing

El ataque de bombardeo de correos electrónicos consiste en enviar grandes volúmenes de correos electrónicos a una dirección en específico con la intención de desbordar el buzón y saturar el servidor de correos donde está alojado. Su función es la misma que un ataque de denegación de servicio (ataque DoS) pero en este caso contra las cuentas de correos.

Estos mensajes se almacenan en el servidor hasta que el dueño de dicha cuenta de correo los lea. Cuando el dueño abra su correo, el último mensaje tardará demasiado tiempo en abrirse y la dirección de correo electrónico quedará inservible. También una cosa a tener en cuenta es que en ocasiones el e-mail bombing se utiliza para intentar distraer a los usuarios, a las empresas y organizaciones, y de esta forma pasar por alto otros correos importantes que puedan recibir.

#### Ataques en la Red

##### 1. Ataque de denegación de servicio o Denial of Service (DoS)

Este tipo de ataque apunta a colapsar una red inundandola de tráfico. Lo hace mediante envío de muchas peticiones, por lo tanto los recursos se desbordan, el sitio no puede responder, se apaga y se vuelve innacesible.

Dentro de este tipo de ataques hay muchos tipos, entre ellos el ICMP Flood Attack que es un tipo de degenación de servicio que envia una gran cantidad de paquetes ICMP Echo Request.

Además de este ataque, existen varias posibilidades más como el Ping of the Dead igual al anterior pero con un tamaño de los paquetes de 65536 bytes.

Hay varios tipos de ataque DoS con técnicas distintas además de los ya mencionados. Entre ellos estan los siguientes más conocidos:

- TearDrop Attack: Consiste en el envío de una serie de paquetes muy grandes, con el objetivo de que el destino no sea capaz de ensamblar esos paquetes., saturando el sistema operativo y bloqueándose. Es posible que el ataque pare y necesite que sea reiniciado para que pueda volver a funcionar correctamente.
- Jolt Dos Attack: Este tipo de ataque consiste en fragmentar un paquete ICMP, con el objetivo que la victima no pueda volver a reensamblarlo. Esto hace que el uso de CPU aumente y tenga cuello de botella. El objetivo es que la máquina victima se vuelva lenta debido a que la CPU está muy ocupada ensamblando los paquetes.
- Land Attack: Consiste en enviar un paquete TCP SYN falso donde la dirección IP del objetivo se utiliza tanto como origen como de destino, con el objetivo de que cuando se reciba el paquete, la máquina objteivo se confunda y no sepa donde enviar el paquete y bloquearse. Es un ataque fácilmente reconocido por los Sistemas Operativos, Firewall y antivirus.
- Smurf Attack: Consiste en enviar una gran cantidad de mensajes ICMP Echo Request a la dirección IP de broadcast con la IP de origen de la victima. La victima recibirá todas las respuesta ICMP Echo Reply de toda la red, haciendo que se sature. Se debe hacer IP Spoofing para falsificar la dirección IP de origen, este ataque se explicará más adelante.
- SYN Flood: Este ataque es uno de los más utilizados, consiste en enviar paquetes TCP con el flag SYN activasdo, con el objetivo de enviar una gran cantidad de paquetes a un servidor y abrirle diferentes conexiones, saturandolo por completo. Se utiliza un ataque IP Spoofing como en el ataque anterior para falsificar la dirección IP de origen. Se puede evitar fácilmente con firewall o limitando el número de paquetes TCP SYN que se pueden recibir.
- Fraggle DoS Attack: Este ataque enviar mucho tráfico UDP a una dirección IP broadcast, estos paquetes tiene la IP de origen de la victima, como anteriormente, este ataque también necesita que se haga un IP Spoofing para el ataque La red entregará el tráfico de red a todos los hosts y los equipos responderan. Esto ocasionará que la máquina objetivo reciba una gran cantidad de tráfico que no sea capaz de gestionar de manera adecuada, y será incapaz de trabajar con normalidad.

##### 2. Ataque de denegación de servicio o Distributed Denial of Service (DDoS)

Este ataque es un ataque DoS que utiliza múltiples dispositivos (Equipos remotos, bots o zombis) para que la red objetivo se vea desbordada, esto hace que el servidor se sobrecargue de forma más rápida que con un ataque DoS. 

Un ejemplo de este ataque es el que recibió AWS en Febrero de 2020 que generó un tráfico de 2,3 terabits por segundos. Los atacantes usaron servidores web pirateados del protocolo CLDAP. este protocolo es de los más usado en los últimos años.

##### 3. Spoofing de DNS y Spoofing IP

El spoofing de DNS consiste en alterar el DNS para por ejemplo redigir el tráfico a una página web falsa que emula una legítima.

Esto permite que la victima introduzca un nombre de usuario y contraseña y el atacante puede robar su información de acceso.

En el Spoofing IP se suplanta la dirección IP de origen de un determinado equipo, de esta forma se pueden enviar TCP, UDP o IP con una dirección IP falsa.

##### 4. ARP Spoofing

Este ataque permite atacar a equipos que esten en la misma red local, ya sea cableada o inalámbrica.

El atacante se hace pasar por el router haciendo que todo el tráfico de la red hacia internet pase directamente por él, pudiendo leer, modificar o bloquear este tráfico.

##### 5. Ataque Man in the Middle (MitM)

El atacante en este tipo de ataques intercepta una comunicación entre dos personas de forma secreta e incluso puede alterarla.

En este ataque se puede por ejemplo hacer en una red WiFi no cifrada. Las victimas no saben que el atacante está espiando o modificando la comunicación.

##### 6. Tunelización de DNS

Se usa el protocolo DNS para comunicar tráfico que no pertenece al tráfico DNS por el puerto 53. Por ejemplo se puede enviar HTTP y otro tipo de tráfico.

También se puede utilizar para tráfico VPN de tunelización DNS, manipular las solicitudes DNS a fin de exfiltrar los datos de un sistema comprometido y para encubrir tráfico saliente ocultando los datos que se suelen compartir mediante una conexión a internet. 

##### 7. Ataque de inundación MAC

Este tipo de ataques es uno de los más comunes y consiste en inundar la tabla CAM de un Switch con diferentes MAC como dirección de origen, con el objetivo de que el Switch acabe funcionando como un HUB.

##### 8. TCP Session Hijacking

Consiste en tomar posesión de una sesión TCP que ya existe y la victima ya está utilizando. 

Este tipo de ataque se debe utilizar en un momento concreto que es en el inicio de las conexiones TCP que es donde se realiza la autenticación. 

#### Ataques en el Área Web

El área de web es una de las áreas de acción más comunes de las empresas. Muchas empresas de todos los tamaños se fundamentan en el correcto funcionamiento de una página web, ya sea porque es su medio de contacto con sus clientes, porque es una parte fundamental de su soporte o porque es de hecho su producto. 

Por ello, el área de web puede resultar de crucial interés para todo tipo de perfiles de clientes. Se han enumerado en esta sección los ataques más destacables que podemos encontrar y una descripción de los mismos

##### 1. Inyección de SQL
Una inyección SQL en web consiste como bien dice el nombre en introducir código malicioso en algún lugar de la web que lo permita, normalmente formularios, parámetros de la misma URL o barras de búsqueda. Este código aprovechará la forma en la que una aplicación web maneja las entradas de usuario, poniendo a prueba la forma en la que se validan o sanitizan.

Para comprenderlo mejor podríamos pensar en este caso:

Supongamos que una aplicación web realiza en algún punto la siguiente consulta a la hora de realizar una autenticación:

```sql
SELECT * 
FROM usuarios 
WHERE nombre_usuario = 'user' 
AND contraseña = '1234';
```

Pensando en esta posibilidad, un usuario malicioso podría intentar introducir un código malicioso como el siguiente:

```sql
usuario' OR '1'='1'; --
```

Si el campo donde se introdujo ese código no está validado ni sanitizado, lo que el servidor procesará será lo siguiente:

```sql
SELECT * 
FROM usuarios 
WHERE nombre_usuario = 'user' 
OR '1'='1'; 
--' AND contraseña = 'contraseña123';
```

El atacante ha utilizado el operador lógico `OR` para añadir la condición verdadera  `'1'='1'`, y luego ha añadido dos guiones `--` que crearían un comentario, eludiendo la comprobación de la contraseña. 

De esta manera un atacante sortea el proceso de autenticación con facilidad y sin ni siquiera conocer la contraseña.

##### 2. Cross-Site Scripting

El Cross-Site Scripting o XSS, son principalmente ataques que permiten la ejecución de código malicioso que ha sido inyectado en sitios benignos y fiables, provocando que los usuarios que también visiten o utilicen esa página web se vean afectados por la acción maliciosa. Los problemas de seguridad que se pueden provocar por este problema abarcan desde una suplantación de la identidad hasta el robo de información sensible.

Este tipo de ataque intenta evadir la *política del mismo origen* (SOP, Same-Origin Policy), la cual consiste de una manera resumida en que un documento o script de un origen concreto ( entendiéndose origen como la combinación entre dominio, protocolo y puerto ) no podrá afectar ni interactuar con un recurso de otro origen.

Estos ataques podemos clasificarlos en 3 categorías principales:

**XSS Almacenados**
En este caso, el código inyectado se almacena permanentemente en los servidores o el código de la página o aplicación web concretos, provocando que cada vez que un cliente recupere datos del servidor se traiga consigo el script malicioso de nuevo. Suelen darse en cajas de comentarios, mensajes del foro incluso secciones como tweets de twitter podrían ser vulnerables.

**XSS Reflejados**
En los XSS reflejados, el código malicioso lo inyecta un usuario en el momento y el servidor lo muestra de vuelta en una petición HTTP. Suelen ser menos peligrosos que los anteriores.

**XSS Basados en el DOM**
Los XSS basados en el DOM se producen cuando un atacante logra inyectar código en el DOM de la web, siendo ésta la abstracción lógica que indica la jerarquía de los elementos de la página web. En este caso la página en sí misma no cambia, pero el código del cliente se ejecuta de manera distinta y probablemente maliciosa.
![[que-es-dom.png]]

Un ejemplo de XSS podría ser el siguiente:

Supongamos un sitio web con un buscador y una caja de comentarios que tiene debilidades en su implementación y no validan el código adecuadamente. Esto permite que por ejemplo podamos inyectar código directamente en ese buscador, por ejemplo algo tan simple como:

```html
<script>alert("Este es un ataque XSS!");</script>
```

Se consideraría un XSS Reflejado, ya que en principio el código actuaría en la respuesta HTTP de la búsqueda. 

Al inyectarlo en la caja de comentarios por ejemplo, podríamos conseguir que ese código se quedase almacenado en la base de datos de esa web, por lo que estaríamos hablando de un XSS Almacenado.
 
Y si por ejemplo integrásemos una etiqueta `<script>` y luego consiguiéramos ejecutar un código como éste:

```javascript
const script = document.createElement("script");
script.textContent = `console.log("Hi there");`;
document.body.appendChild(script);
```

Estaríamos realizando un XSS basado en el DOM.

##### 3. Cross-Site Request Forgering
Este tipo de ataque consiste en trucar a un usuario para que realice una acción en una aplicación en la que está logueado.

Por ejemplo se podría trucar a un usuario para que realice una solicitud a una aplicación web en la que ya está autenticado, y siendo así, la aplicación no podría distinguir entre una solicitud maliciosa y una legítima. 

Se podría conseguir muy fácilmente de la siguiente manera:

Supongamos que ésta es una petición normal para que un banco nos haga una transferencia de 100€:

```HTTP
GET http://netbank.com/transfer.do?acct=PersonB&amount=100€ HTTP/1.1
```

Es importante la parte de `acct=PersonB`, ya que indica el usuario que recibirá la transacción.

Un atacante podría modificar esta petición para que la petición se le haga a él:

```http
GET http://netbank.com/transfer.do?acct=USUARIOATACANTE&amount=100€ HTTP/1.1
```

Ya estaría *forjada* la petición, ahora solo tendría que distribuirse. Esto sería el ejemplo de como podríamos camuflarla en un formulario:

```html
<body onload="document.forms[0].submit()">
   <form action="http://netbank.com/transfer.do" method="POST">
     <input type="hidden" name="acct" value="USUARIOATACANTE"/>
     <input type="hidden" name="amount" value="100€"/>
     <input type="submit" value="Reclama tu premio!!!!"/>
   </form>
 </body>
```

Este sería un esquema su funcionamiento:

![[CSRF.png]]

##### 3. Session Hijacking

El *session hijacking* o secuestro de sesión consiste en valerse de un token de inicio de sesión, una cookie o un session ID y utilizarlo para tomar el control. Una vez que la sesión ha sido robada, el atacante pasará totalmente desapercibido y ni siquiera ha tenido que preocuparse de averiguar la contraseña.

Para entender bien este ataque, debemos comprender qué es una sesión HTTP.

> Las sesiones HTTP debido a que este protocolo no tiene un *estado*, es decir, no existe algo constante que monitorice si la sesión está activa. Los desarrolladores necesitaban algo para no tener que obligar al usuario a autenticarse cada vez que pulsara un link (múltiples conexiones de un mismo usuario). Para ello crearon la *sesión*, parámetros que almacenan mientras el usuario está logueado en el sistema y se destruye cuando éste cierra su sesión.
> 
> Los ID de sesión suelen ser cadenas largas alfanuméricas y aleatorias comúnmente almacenadas en cookies o URLs entre otras.

Sabiendo como funcionan las sesiones, deducimos que si consiguiéramos hacernos con ese id de sesión podríamos hacer *hijack* a esa sesión, hay diferentes técnicas para conseguirlo:

- **Session Sniffing**: El atacante usaría un analizador de tráfico o un proxy para capturar precisamente el tráfico de una red, escrutarlo y sacar un ID o cookie de sesión de ello.
- **Tokens predecibles**: Muchos servidores y páginas web utilizar algoritmos y patrones predefinidos para generar los ID de sesión. Un atacante podría probar patrones conocidos o deducir el patrón tras recopilar una serie de ellos y analizarlos.
- **Man-in-the-browser**: En este caso, el atacante debería de infectar a una víctima con por ejemplo un troyano, para que realizara peticiones desde su navegador a una web concreta y se la mandase a él, pudiendo analizar esas peticiones y sacar el ID de sesión del usuario infectado.
- **XSS**: El anteriormente mencionado, podría tratarse de un script para extraer cookies o IDs directamente.
- **Session fixation attacks**: Este tipo de ataque consiste en un atacante que ha conseguido robar o crear un ID de formato válido para una web, y luego intenta trucar a un usuario para que lo use para autenticarse (es decir, que lo *fije*), ganando control sobre la cuenta de ese usuario. Las técnicas para conseguir que un usuario fije un ID varían desde tokens ocultos en formularios, cookies o URLs.

****

##### 4. Ataques DoS y DDoS

Los ataques de Denegación de Servicio (*Denial Of Service* o *DoS*) tienen como objetivo saturar la capacidad de un sistema, red o servicio al inundarlo con un gran volumen de tráfico falso. Existen dos variantes principales de este tipo de ataque:

**DoS**: Denegación de servicio a secas. Es la denegación de servicio provocada por un aluvión de peticiones desde un solo equipo a otro concreto.

**DDoS**: Denegación de servicio *Distribuida*. En esta variante se utilizan múltiples equipos para hacer peticiones simultáneamente a un solo equipo. Habitualmente se crean *botnets* o *redes zombies*, que son básicamente grandes conjuntos de equipos infectados para hacer peticiones en masa.

Dentro de los ataques DoS, existen varios tipos:

- Ataques para consumir los recursos de red y colapsar el servicio de un dispositivo
- Alteración de una configuración de un protocolo, habitualmente causándole un error a través de la explotación de una vulnerabilidad
- Interrupciones de comunicaciones por TCP (TCP Reset)
- Obstrucción de la comunicación entre los usuarios y la víctima.
- Explotación de vulnerabilidades en un sistema para lograr que el mismo deje de funcionar

En cuanto a los ataques DDoS, existen 3 tipos principales que destacar:

- **Ataque Volumétrico**: El tipo de ataque mayoritario, consiste en enviar una gran cantidad de datos mediante técnicas de creación de tráfico masivo como redes de bots. Principalmente se podrían subdividir en:
	- *Inundación UDP*: Se utilizan paquetes UDP (*User Datagram Protocol*), un tipo de paquete más ligero que el TCP frecuentemente utilizado en aplicaciones que requieren latencia baja (juegos, streaming).
	- *Inundación ICMP*: ICMP es el protocolo de mensajes de control de internet, utilizado para enviar mensajes de control y diagnóstico en redes IP. Los sistemas están obligados a contestar estos mensajes, por lo que suelen ser una elección interesante.
	- *Reflejo de DNS*: Este ataque se orquesta normalmente con la ayuda de un bot que mande solicitudes a múltiples servidores DNS con la IP de la víctima, que resuelven las peticiones y reenvía los datos a la misma víctima, sobrecargando sus sistemas.
- **Ataque de protocolo**: Los ataques DDoS de protocolo intentan agotar los recursos de la capa 3 (sesión) y 4 (transporte) del modelo OSI, donde se encuentran firewalls o servidores. Podemos diferenciar 2 tipos:
	- *Inundación SYN*: En el momento de una conexión a internet, se activa el protocolo TCP que requiere tres pasos para funcionar: Envío de un paquete SYN, otro envío de paquete SYN-ACK para confirmar la conexión y uno ACK para completarla. Este tipo de ataque envía muchos paquetes SYN, *sin* enviar el paquete de confirmación, por lo que un servidor queda a la espera de los paquetes de confirmación
	- *Ataque Smurf*: En este ataque se envían paquetes ICMP con la dirección de IP de la víctima a una extensa red de dispositivos que se ven obligados a dar una respuesta, por lo que se dirigen todas a la IP de la víctima. Su nombre fue tomado de "The Smurfs" (*Los pitufos*), capaces de derrotar a un enemigo mas grande que ellos siendo muchos.
- **Ataque a la capa de aplicación**: Ataques dirigidos a la capa 7 de OSI, de aplicación, generalmente se suelen realizar a través de múltiples peticiones HTTP.

##### 5. Credential Stuffing

El relleno de credenciales por fuerza bruta (*Credential Stuffing*) implica intentar adivinar contraseñas probando muchas combinaciones posibles. Normalmente los atacantes utilizarían una herramienta que automatice este proceso y utilizarán un *diccionario*, construido normalmente de filtraciones de credenciales. Realmente se considera un subconjunto de la categoría ataques de fuerza bruta, sin embargo estos ataques suelen intentar adivinar las contraseñas sin contexto ni pistas, mientras que en estos ataques mayormente se suelen utilizar credenciales expuestas.

Un ejemplo sería un ataque en el que un atacante utiliza un programa automatizado para probar sistemáticamente diversas combinaciones de nombres de usuario y contraseñas hasta encontrar la correcta.

##### 6. API Abuse

El abuso de API implica el uso indebido de una interfaz de programación de aplicaciones (API), como realizar solicitudes no autorizadas o manipuladas.

Para entender este tipo de ataque por supuesto es necesario entender en qué consiste una API.

> Una API (Application Programming Inteface) es un componente de software que proporciona una fuente de datos o recursos a varios solicitantes, como podrían ser aplicaciones, webs o servicios. Funcionan habitualmente mediante peticiones HTTP y tienen bien definidas las formas de solicitar datos mediante llamadas concretas, formatos de devolución específicos y convenciones que deberían ser respetadas. 

Sabiendo esto, podremos entender que existen atacantes que realizan un proceso de ingeniería inversa a diferentes APIs para comprender como funcionan y así realizar *API Call Hijack* (Secuestro de llamada de una API), suele hacerse con por ejemplo servidores proxies que interceptan una petición y ésta se modifica para por ejemplo devolver una vista de un sitio web malicioso, siendo éste tan solo uno de los ejemplos. 

Por supuesto las APIs también se ven afectadas por ataques DDoS provocados normalmente por pequeñas llamadas que solicitan cantidades enormes de datos, lo que consume muchos recursos del servidor. También, reciben ataques de atacantes que utilizan *botnets* cargadas con datos de datos robados de cuentas de usuario para conseguir combinaciones válidas.  

Las APIs reciben ataques también de *Web Scraping*, que en sí no tiene por que ser un ciberataque, pero en este caso existen cibercriminales que mediante llamadas masivas a una API consiguen clonar en su totalidad un sitio web, con intención de falsearlo y utilizarlo como trampa para otras actividades maliciosas.

##### 7. Third-Party Code Exploitation

El abuso de código de terceros implica explotar vulnerabilidades en códigos externos, como por ejemplo CMS (Wordpress, Joomla!), librerías de desarrollo, plugins de servicios de terceros o incluso vulnerabilidades en el propio javascript.

Este tipo de ataque puede darse debido a que directamente muchos atacantes buscan vulnerabilidades en componentes de terceros muy utilizados por la comunidad, aunque existen distintos casos en los que por ejemplo los cibercriminales se hacen pasar por vendedores y creadores de software web de terceros que contienen puertas traseras y vulnerabilidades que puedan explotar más tarde.

Existen también casos en los que muchos cibercriminales distribuyen parches de seguridad falsos, que añaden debilidades a la infraestructura de una aplicación.

Un ejemplo sería un atacante que aprovecha una vulnerabilidad en un plugin de WordPress para inyectar código malicioso en un sitio web y comprometer la seguridad del mismo.

##### 8. Zero-Days attack

Las vulnerabilidades zero-day son un punto más a tener en cuenta en las aplicaciones web y son una de las más críticas. 

Básicamente consisten en brechas de seguridad desconocidas para el fabricante y en varias ocasiones incluso para la comunidad general, por lo que no tienen parche ni arreglo. Una vulnerabilidad *Zero-day* debe de venir junto a un *exploit Zero-day* para que efectivamente podamos considerarlo peligrosa de verdad, ya que muchas de ellas son tan difíciles de explotar que se abandonan.

No tienen por que encontrarse en una página o aplicación web en sí, una vulnerabilidad en un navegador o servicio web concreto podría llegar a explotarse y causar grandes estragos.

Como ejemplo de ataque zero day en web podríamos mencionar la [CVE-2020-0674](https://nvd.nist.gov/vuln/detail/cve-2020-0674) que consistía en un fallo de manejo de objetos en memoria del navegador ya anticuado Internet Explorer. El error permitía ejecutar código de manera remota. 

En la siguiente sección detallamos los servicios ofrecidos por nuestra empresa en las diferentes áreas en las que nos especializamos. 

Basándonos en la anterior clasificación de ataques, hemos definido las siguientes auditorías como servicio.

#### Ataques en Software

El *software* es un conjunto de programas, aplicaciones y datos que permiten que un equipo informático realice tareas específicas. Es la parte lógica y no física de un sistema que le permite funcionar y llevar a cabo diversas funciones tales como el procesamiento de datos, la gestión del hardware o la ejecución de aplicaciones. Como podremos imaginar, cualquier software no está exento de la posibilidad de sufrir diversos tipos de ciberataques, los cuales clasificaremos y analizaremos, con el fin de comprender mejor cómo funcionan y qué buscan lograr.

Antes de comenzar a clasificar las formas usadas por los atacantes para vulnerar un sistema debemos entender la diferencia entre un *exploit* y un *virus*. Mientras que un exploit es un software malicioso usado para aprovechar las vulnerabilidades de un sistema objetivo, un virus se acopla en un programa legítimo para camuflarse, y al ser ejecutado, el código malicioso entra en escena, copiándose en programas y ficheros del sistema.

##### 1. Ataque de Fuerza Bruta Estándar

*Características*

- Es un ataque de fuerza bruta es un método utilizado para descubrir contraseñas o claves de cifrado desconocidas. 
- Este tipo de ataque trata de probar todas las combinaciones posibles de caracteres, números y símbolos hasta encontrar la correcta.

*Métodos*

- A través de un software especializado, los atacantes automatizan este proceso, probando miles de combinaciones por segundo. 
- Es común enfocarse en encontrar contraseñas débiles.

*Objetivos*

- El objetivo principal es el de obtener acceso no autorizado a cuentas, sistemas o datos protegidos por contraseña.
- Suele ser usado en cuentas online, sistemas protegidos por contraseñas o incluso en el descifrado de datos.

##### 2. Ataque de Fuerza Bruta de Diccionario

*Características*

- A diferencia del tipo de ataque anterior, en un ataque de diccionario se utiliza una lista predefinida de palabras y combinaciones de caracteres. 
- Estos ataques suelen ser más eficientes que los de fuerza bruta, ya que se centran en contraseñas comunes y más probables.

*Métodos*

- Uso de software especializado o scripts en su defecto, que automatizan la prueba de contraseñas en la lista del diccionario. 
- Se puede personalizar el diccionario para adaptarlo al objetivo.

*Objetivos*

- El objetivo principal es adivinar la contraseña de un usuario, cuenta, sistemas o datos protegidos.
- Tras la obtención de la contraseña, el objetivo suele ser robar información confidencial, acceder a sistemas no autorizados, etc.

*Ejemplos*

- Aircrack-ng

##### 3. Ataque de Fuerza Bruta con Algoritmo de Búsqueda Inteligente

*Características*

- Es un tipo de ataque de fuerza bruta en el que los atacantes usan algoritmos diseñados para predecir las combinaciones de contraseñas más probables.
- El ataque usa una base de información conocida de la víctima, así como de pautas usuales al crear contraseñas.  

*Métodos*

- Uso de software especializado o scripts en su defecto, aunque existe la posibilidad de usar una IA para esta tarea.

*Objetivos*

- El objetivo es el mismo que los demás ataques de fuerza bruta, que es obtener un acceso no autorizado a una cuenta de un usuario online, adivinar contraseñas, y acceder a sistemas o datos protegidos.

##### 4. Ataque de Fuerza de Fuerza Bruta Híbrido

*Características*

- Este tipo de ataque combina tanto los ataques de fuerza bruta comunes como los ataques de diccionario.
- Se suele crear un diccionario con contraseñas comunes, y a través de fuerza bruta estándar agregar caracteres especiales o números.

*Métodos*

- Uso de software especializado o scripts en su defecto.

*Objetivos*

- Estos ataques buscan poder acceder de forma no autorizada a sistemas, cuentas de usuario, contraseñas o información confidencial.

##### 5. Ataque de Escalada de Privilegios

*Características*

- Intento por parte del atacante de lograr un nivel de acceso o privilegios en un sistema superior al concedido inicialmente. 
- Esta clase de ataque suelen servirse de vulnerabilidades y fallos en la configuración de seguridad de sistemas para obtener dichos privilegios.
- El atacante suele buscar cuentas de root o administrador.
- Se distinguen entre la escalada de privilegios vertical, donde el atacante eleva sus privilegios desde una cuenta con privilegios de nivel bajo; y la escalada de privilegios horizontal, donde el atacante a pesar de usar una cuenta con bajos privilegios, gana acceso a datos y funcionalidades a las que no debería poder acceder.

*Métodos*

- No existe un solo método para lograr una escalada de privilegios, dado que esto varía de un sistema operativo a otro. 
- Algunas de las técnicas usadas por atacantes para lograr dichos privilegios incluyen la inyección de código o la suplantación de identidad.
- Estos ataques pueden suceder en sistemas locales, donde el atacante ya tiene acceso al mismo, o en sistemas remotos, donde se ha comprometido previamente una cuenta con un nivel menor de privilegios.

*Objetivos*

- El objetivo principal de este tipo de ataque es lograr un mayor control sobre un sistema, abriendo la puerta a atacantes a acciones que previamente les serían imposibles, tales como acceder a datos confidenciales, instalar malware o incluso modificar el propio sistema a su antojo.

##### 6. Rootkit

*Características*

- Tipo de software malicioso diseñado para ocultarse en un sistema objetivo y proporcionar a los atacantes acceso no autorizado al mismo. 
- El término “rootkit” viene de “root”, que alude a los mayores privilegios en sistemas UNIX, lo que serían privilegios de administración en Windows.
- Los rootkits suelen funcionar ocultándose de los usuarios y de los sistemas de seguridad.
- Pueden llegar a modificar el SO, aumentando su control del mismo y asegurando su persistencia. 

*Métodos*

- Este tipo de malware suele instalarse en los sistemas objetivo de diferentes maneras, ya sea a través del uso de la ingeniería social como el phishing, ocultos en software de otra índole, aparentemente inocuo, etc.

*Objetivos*

- El principal objetivo es el de otorgar a los atacantes acceso al sistema infectado, así como de mantener dicho acceso de forma persistente.
- El objetivo de los atacantes es robar contraseñas o datos financieros, información confidencial o alterar o destruir el sistema objetivo.

*Ejemplos*

- Uroburos (2014). El rootkit Uroburos tenía como objetivo robar datos en compañías de alto perfil, pudiendo afectar desde empresas hasta organizaciones gubernamentales.
- Rustock (2006). Este rootkit tenía el siguiente *modus operandi*: infectar equipos informáticos de toda índole, desde ordenadores personales hasta sistemas empresariales, para convertirlos en *bots*, agregándolos a una *botnet* dedicada a enviar spam de manera masiva.

##### 7. Troyano

*Características*

- Malware destinado a camuflarse como un programa legítimo e inocuo, y así otorgar acceso no autorizado a un sistema a los atacantes. 
- Aunque pueda parecer lo mismo que un rootkit, la diferencia radica en la detección de ambos por parte del sistema, ya que el rootkit se enfoca más en ocultar su presencia tanto del usuario como de sus sistemas de seguridad, mientras que el troyano trata de ejecutar acciones maliciosas en el sistema directamente. 

*Métodos*

- Esta clase de software malicioso puede transmitirse en correos de phishing, descarga de software pirata, enlaces malintencionados, la explotación de alguna vulnerabilidad, o incluso documentos o imágenes.

*Objetivos*

- Al igual que un rootkit, los troyanos pueden dar acceso no autorizado a un sistema, y también suelen utilizarse para robar todo tipo de información.
- Los troyanos suelen usarse para crear puertas traseras (backdoors) en los sistemas atacados.
- También poseen capacidades de espionaje tales como el uso de keyloggers (software que registra las pulsaciones de teclado) o capturar la pantalla.

*Ejemplo*

- URSNIF. Troyano especializado en robar datos bancarios, contraseñas, y datos personales. Ezste malware además, puede ser usado como puente para instalar más malware en el sistema

##### 8. Adware

*Características*

- El adware es un tipo de software diseñado para mostrar anuncios no deseados en el sistema objetivo, y suelen manifestarse como banners, pop-ups, etc. 

*Métodos*

- Comúnmente el adware se instala en un sistema formando parte de un software legítimo.

*Objetivos*

- El objetivo principal del adware es generar ingresos para los anunciantes y desarrolladores del mismo.
- Algunos tipos de adware pueden llegar a recopilar información del usuario, a fin de poder mostrar publicidad personalizada a estas personas, o directamente vender esta información a otras empresas.

*Ejemplo*

- Appearch. Adware que usa software gratuito instalado como medio para poder colarse en el sistema, ya que es instalado junto con el software gratis aparentemente inocuo. Una vez instalado, llena el navegador de la víctima con publicidad basura.

##### 9. Spyware

*Características*

- El spyware es un tipo de software malicioso diseñado para ser capaz de recopilar información de la víctima.
- Este tipo de malware se oculta, funcionando en segundo plano.
- Es capaz de rastrear la navegación en Internet, registrar pulsaciones de teclado y robar contraseñas o información sensible.

*Métodos*

- El spyware se suele instalar de forma encubierta en un sistema objetivo, a través de descargas de programas pirata, phishing o incluso unido a software legítimo.
- Una vez que se instala funciona de forma sigilosa, en segundo plano.

*Objetivos*

- El objetivo consiste en la recopilación de información del usuario infectado.
- Estos datos pueden incluir tarjetas de crédito, contraseña, historial de Internet o correos electrónicos.

*Ejemplo*

- Pegasus. Malware de espionaje (spyware) diseñado por la compañia israelí NSO Group. Pegasus puede instalarse de diversas formas en los móviles de sus víctimas, habiendo hecho uso para su ventaja de varias vulnerabilidades 0-Day. Este spyware es capaz de afectar tanto a iOS como a Android.

##### 10. Gusano

*Características*

- Clase de malware que funciona propagándose a través de redes y sistemas informáticos, sin necesidad de intervención humana.
- La diferencia con otros tipos de virus o malware no necesitan ir adjuntos a archivos o programas, dado que se replican de forma automática.

*Métodos*

- Los gusanos aprovechan vulnerabilidades para propagarse por redes y sistemas informáticos.
- Una vez infectado un sistema, el gusano analiza la red en busca de otros objetivos a los que copiarse, y si no los encuentra usará Internet para esa misma tarea.

*Objetivos*

- El objetivo principal y razón de la existencia de un gusano es propagarse a otros sistemas, infectándolos para poder seguir propagándose.
- Algunos gusanos pueden contener payloads maliciosos.

*Ejemplos*

- Morris Worm (1998). El gusano Morris fué el primer gusano que causó un impacto significativo en Internet, siendo desarrollado por el entonces estudiante de postgrado, Robert Tappan Morris.
- Sasser Worm (2004). Gusano que explotaba una vulnerabilidad en sistemas Windows, bloqueando y reiniciando los equipos. Este gusano fué desarrollado por un estudiante alemán de 18, el cual fué capturado y condenado.

##### 11. Botnets

*Características*

- El término “botnet” viene de la expresión robot network o red de robots.
- Esta es una red de sistemas infectados (“bots” o “zombis”) por un atacante.

*Métodos*

- Los bots que componen una botnet suelen integrarse a esta a través de malware que los infectó previamente.
- Una vez infectado, el bot se comunica con un servidor de Comando y Control (C&C), controlado por el atacante.
- Algunas botnet tienen varios C&C.

*Objetivos*

- Ataques DDoS.
- Distribución de Spam.
- Robo de Datos.
- Infección de más dispositivos.
- Cryptojacking o minado de criptomonedas.

*Ejemplos*

- CONFICKER (2008). Botnet dedicada a los ataques DDoS y al envío masivo de spam. Llegó a infectar entre 9 y 15 millones de equipos.

- GAMEOVER ZEUS (2012). Con su origen en Rusia, esta botnet infectó entre medio millón y un millón de equipos, y está diseñada para propagar entre los bots el malware CryptoLocker, que es un malware de tipo RansomWare, el cual encripta los equipos de las víctima y pide un rescate a cambio de la clave de desencriptado.

##### 12. Rogueware

*Características*

- El rogueware es un software malicioso y fraudulento, diseñado para aparentar ser un software legítimo y/o de seguridad, cuando realmente lleva a cabo acciones ilegales.
- Suelen venderse como programas diseñados para mejorar el rendimiento de un dispositivo, pero realmente realizan acciones maliciosas.

*Métodos*

- El rogueware suele contraerse a través de descargar software de sitios no oficiales ni confiables, phishing, etc.
- Una vez instalado, este tipo de software muestra alertas de “supuestos problemas” que requieren de nuestra atención de forma inmediata.
- Incluso existen casos que poseen una versión “premium”, que no ofrece ningún beneficio real, siendo además de una intrusión informática, una estafa.

*Objetivos*

- El objetivo prioritario del rogueware es el lucro y la estafa a las víctimas a través de la venta de un software falso, que no sólo no los protege, sino que los daña.
- El rogueware es además capaz de robar información del usuario y su sistema.
- También posee la capacidad de instalar malware adicional.

*Ejemplo*

- WinWebSec. Familia de supuestos escáneres que emulan ser un sistema de seguridad legítimo, pero en realidad pueden llegar a infectar el equipo, convirtiéndolo en un *bot*. Algunos ejemplos son Live Security Platinum, Smart Protection y Win XP Security System.

## Tipos de Auditorías Ofensivas ofrecidas

A fin de garantizar la seguridad de los sistemas, redes y dispositivos de los clientes, ofrecemos diversos tipos de auditorías ofensivas, con un enfoque práctico y directo. Este enfoque nos permite llegar a la raíz de los posibles problemas, fallos y/o debilidades en configuraciones de seguridad, localizar contraseñas débiles o encontrar vulnerabilidades críticas que pudieran ser explotadas por cibercriminales.

Antes de comenzar es importante proponer acuerdos, establecer límites y estudiar las regulaciones y normas de su compañía, a fin de delimitar el área que auditar, así como los horarios a los que llevar a cabo la auditoría en cuestión. Otro aspecto a tener en cuenta es discutir el tipo de prueba a llevar a cabo, siendo las opciones a elegir las siguientes:

- **Pruebas de Caja Negra (Black Box Testing).** En las pruebas de caja negra, los analistas de seguridad no conocemos los detalles internos y exactos del funcionamiento de su sistema, dado que el enfoque debe simular un ataque por parte de un elemento externo a la empresa, identificando vulnerabilidades sin acceso al código o a la estructura interna del sistema.
- **Pruebas de Caja Gris (Gray Box Testing).** Las pruebas de caja gris otorgan un conocimiento parcial del sistema al analista de ciberseguridad, ofreciendo detalles sobre el diseño o arquitectura del sistema, pero sin entrar en el código del mismo. Esto permite realizar pruebas con un enfoque mayor en un área concreta.
- **Pruebas de Caja Blanca (White Box Testing).** En las pruebas de caja blanca, a los evaluadores se les da un conocimiento completo del sistema, incluido el acceso al código fuente y la arquitectura interna del mismo. Esto da la posibilidad de llevar a cabo pruebas complejas, profundas y exhaustivas, con el objeto de identificar vulnerabilidades y/o fallos en el código del sistema.

Conociendo esto, se explicarán los tipos de auditorías ofensivas. Estas se dividen entre las diferentes áreas informáticas, y el objetivo de cada tipo es centrar los esfuerzos en un área concreta, para mayor efectividad y profundidad de las pruebas.

### 1. Auditoría de correos electrónicos

La auditoría ofensiva de correos electrónicos nos puede ayudar mucho ya que con ella podemos evaluar la seguridad para identificar y corregir vulnerabilidades que podrían ser explotadas por atacantes. 

En esta auditoría ofreceremos dos servicios. Uno centrado en analizar la configuración del sistema de correos y otro centrado en realizar pruebas de penetración para comprobar la seguridad de los sistemas:

#### 1. Análisis de la configuración del sistema de correo electrónico: 

El análisis de las configuraciones del sistema de correo electrónico es una parte muy importante a tener en cuenta ya que nos ayudará a analizar todas las posibles malas configuraciones que existan en el servidor de correos. 

En este primer servicio trataremos los siguientes puntos:

- Configuración de los servidores: En este apartado analizaremos todas las configuraciones del servidor exhaustivamente para encontrar los posibles puntos débiles que existan. También se comprobarán las versiones de las actualizaciones de seguridad del servidor.
  
- Políticas de seguridad: En este apartado analizaremos las políticas de seguridad que se están utilizando para proteger el servidor.
  
- Protocolos utilizados: En este apartado comprobaremos la seguridad de los protocolos utilizados en el servidor de correos como SMTP, POP, IMAP, MX o DKIM.
  
- Informe sobre los resultados obtenidos: Le entregaremos a la empresa un informe detallado donde indicaremos todas las vulnerabilidades, malas configuraciones, versiones desactualizadas, protocolos inseguros, etc...

#### 2. Pruebas de penetración de correo electrónico

En este servicio nos centraremos en explotar todas las vulnerabilidades encontradas en el primer servicio utilizando técnicas de pentesting para demostrar a la empresa todas las vulnerabilidades que tienen listadas en un informe o documento.

En este segundo servicio nos centraremos en los siguientes puntos:

- Realizaremos ataques por fuerza bruta y por diccionario a las cuentas.

- Explotaremos protocolos, puertos y configuraciones que no sean seguros.

- Enviaremos correos electrónicos de phishing para intentar engañar a los usuarios para que revelen información personal o de la empresa.
  
- Enviaremos correos electrónicos con malware para que lo descarguen y lo ejecuten en el sistema.
  
- Enviaremos correos de spam para comprobar si los filtros antispam funcionan correctamente.

- Realizaremos bombardeos de correos (email bombing).

- Utilizaremos técnicas de ingeniería social de forma física dentro de la empresa.

- Utilizaremos scripts, exploits y herramientas para intentar vulnerar el servidor de correos.

- Realizaremos pruebas de autenticación y autorización.

Obviamente todos estos ataques se realizarán con el consentimiento de la empresa y sin poner en riesgo los datos.

### 2. Auditoría de red inalámbrica

El proceso de auditar las conexiones Wi-Fi se realiza con la intención de determinar el nivel de seguridad y confidencialidad que proporcionan este tipo de redes. Normalmente en este tipo de redes se suelen encontrar configuraciones ni cifrados óptimos. Se ofrecerá el servicio de Pentesting con esta auditoría.

Esta auditoría tiene como intención englobar todos los sistemas referentes a la red inalámbrica, segmentos de red, IP's etc.

La auditoría de red inalámbrica tiene dos fases, de reconocimiento del entorno y de descubrimiento de la infraestructura. Se utilizan analizadores de red para visualizar los distintos tipos de cifrado, el número de puntos de acceso, los canales por los que se emiten, el número de clientes conectados y a que puntos de acceso, calidad de la señal, etc.

Después se utilizan técnicas de análisis de vulnerabilidades sobre router, técnicas de suplantación de identidad, envenenamiento de la red y técnicas de ataques a contraseñas.

Esta auditoría tiene como beneficio proporcionar información veraz y fiable del estado de seguridad de la red WLAN de la organización, poniendo barreras de protección y control para determinar la seguridad de dicha red.

### 3. Auditoría Externa o Perimetral

La auditoría externa o perimetral consiste en realizar un examen detallado y crítico con el fin de expresar un criterio profesional sobre la eficiencia y el funcionamiento de una prganización a la hora de desarrollar una gestión determinada. PAra esta auditoría se ofrecerá el servicio de Pentesting.

El objetivo es estudiar el nivel de seguridad de los elementos públicos pr parte de la empresa, por ello, se estudiará el estado de seguridad del perimetro analizando las posibles entradas desde el exterior a la DMZ y zonas internas.

El alcance de esta auditoría se encuentra la aplicación o servicios web, extranet, intranet, sistemas perimetrales etc.

Dispone de dos fases de recolección de información, footprinting y fingerprinting. Con ellas, se realiza la recogida de información global y pública de internet para analizarla y determinar que roles disponen los sistemas perimetrales, puertos abiertos, versiones de productos públicas, etc.

Trás recolectar la información se numera y analiza para encontrar las vulnerabilidades existentes.

Una vez haber identificado los posibles vectores de acceso y vulnerabilidades, se planifican los metodos de ataque con mayor viabilidad y efectividad, por lo que habrá que buscar como acceder al sistema.

Gracias a esto se dispone de los vectores de acceso, configuraciones erróneas y vulnerabilidades existentes en el perimtro, permitiendonos corregir y subsanar estas brechas de seguridad.

### 4. Auditoria IoT

En los últimos años la cantidad de dispositivos conectados que existen han ido incrementando exponencialmente, desde dispositivos como relojes, básculas o pulseras, hasta dispositivos implicados en la seguridad de nuestros hogares.

Gracias a esto este tipo de dispositivos presenta un aumento de superficie expuesta a actores maliciosos, tanto para las empresas que los gestiona como para los clientes que conviven con ellos.

El objetivo de la auditoria IoT es evaluar el estado de seguridad de estas tecnologías, clasificando los ataques dependiendo de la naturaleza del dispositivo y los datos gestionados por él. Permitiremos al cliente conocer el estado de la seguridad de su infraestructura, incluyendo las soluciones a los problemas encontrados.

El alcance de esta auditoria hace referencia a cualquier dispositivo conectado a internet, como por ejemplo los ya mencionados anteriormente relojes, básculas, seonsores, la nube u otros medios de almacenamiento.

Los beneficios de este tipo de auditoria son conocer potenciales problemas en los dispositivos, incluyendo vulnerabilidades en componentes del sistema operativo que ejecute.

Estudiar los posibles fallos de seguridad en el flujo de datos del dispositivo, tanto en conexiones locales a través de redes de corto alcance, como en su procesamiento posterior en servidores si los hubiese, así como sus posibles soluciones tanto a nivel técnico como de diseño.

Análisis de las posibles implicaciones de seguridad derivadas de la arquitectura y tecnologías usadas por el dispositivo IoT. Identificacar las debilidades en el dispositivo físico mediante pruebas de hardware hacking y análisis del ifrmware del dispositivo con ingienería inversa.

### 5. Auditoría de Seguridad de Software

Una de las áreas más importantes en el panorama actual de la tecnología y de la información en general es el software, dado el papel fundamental que este desempeña en la operación de las organizaciones. 

No es de extrañar que este sea uno de los puntos clave por los que los atacantes suelen encontrar vulnerabilidades y fallos de seguridad y/o de configuración, usándolos para perpetrar sus ataques y acceder de forma no autorizada a los sistemas ajenos. Es por ello que ofrecemos una auditoría exclusiva al ámbito del software, analizando los programas en la red y sistemas de su empresa, ofreciendo un informe detallado de los resultados encontrados, ofreciendo soluciones para fortalecer su seguridad, la de su compañía y de sus empleados.

Nuestra Auditoría de Seguridad Ofensiva orientada al Software está diseñada para simular los ataques de cibercriminales reales, con el objetivo de identificar vulnerabilidades, fallos en configuraciones de seguridad, contraseñas débiles o por defecto en todas las aplicaciones y programas utilizados en su organización. Este estudio le permitirá mantener a salvo sus sistemas y datos confidenciales, mejorando su seguridad.

Comenzando por el entorno donde se llevarán a cabo las pruebas, existe la opción de realizarse de forma interna o externa a su organización, según los intereses que tenga el cliente. Obviamente, ambos enfoques ofrecen resultados distintos, así como enfoques distintos:

- *Auditoría Interna.* Una auditoría interna se realiza teniendo acceso a la red interna de la empresa cliente, llevando a cabo las pruebas de penetración o pentesting desde allí, pudiendo incluir las propias oficinas, su Intranet o una VPN. En esta clase de auditoría el experto en seguridad actúa como un usuario que previamente disponía de acceso a la red de la empresa.
- *Auditoría Externa.* Las auditorías externas se llevan a cabo desde fuera de la red de la organización, no teniendo acceso a los sistemas internos o datos de la empresa cliente. A diferencia del tipo de auditoría interna, en esta el auditor asume el papel de un atacante externo, el cual obviamente carece de un acceso autorizado a los sistemas de la empresa.

Una vez que hemos elegido si queremos una auditoría externa o interna, también debemos optar entre enfoques diferentes a la hora de realizar las pruebas, dado que estas podrán tener una mayor superficie para realizarlas, o llegar a una mayor profundidad en el sistema de la empresa cliente, obteniendo resultados más concretos en un área. Estos tres enfoques son los siguientes:

- *Análisis de Vulnerabilidades (Vulnerability Assessment).* Los análisis de vulnerabilidades consisten en la identificación y la recopilación de vulnerabilidades, fallos de configuraciones de seguridad, contraseñas débiles o por defecto, y en general fallos en la seguridad general de la empresa que puedan proporcionar un vector de ataque a un posible atacante. Este tipo de pruebas son las que cubren una mayor superficie, pero alcanzan un nivel de penetración menor en los sistemas de la empresa cliente.	
- *Test de Penetración (Pentesting).* Los tests de pentesting buscan realizar simulaciones de ataque controladas a la infraestructura, red y sistemas de la empresa cliente, con el fin de lograr resultados más precisos que un análisis superficial. Estas pruebas siempre se realizan siguiendo un código ético y cumpliendo unas normas acordadas con el cliente, tales como vetar ciertas partes de la infraestructura de la red de la empresa, limitar el pentesting a ciertas horas, etc.  Normalmente en esta clase de pruebas no es necesario hacer hincapié en el ocultamiento de los sistemas de seguridad de la empresa, y en la discreción, dado que la misión consiste en obtener el mayor número de fallas de seguridad posibles, sin preocuparse del sigilo. 
- *Red Teaming.* Las pruebas de Red Team podría decirse que son las más realistas de las tres, dado que alcanzan el mayor nivel de profundidad posible en los sistemas de la empresa, simulando un ataque real por parte de cibercriminales. Este tipo de prueba no posee constricciones de ningún tipo, pudiendo usar técnicas de Ingeniería Social como el Spear-Phishing, así como buscar ocultarse de los sistemas de seguridad de la empresa o explotar vulnerabilidades, tal y como lo haría un atacante real. El objetivo consiste no sólo en analizar las vulnerabilidades y fallos de seguridad de la compañía, sino en evaluar también la capacidad de respuesta de la misma.

Ya elegido el tipo exacto de pruebas que desea para su empresa, pasaremos a explicar el esquema general de la auditoría, desde la realización de las pruebas hasta la presentación del informe con los resultados obtenidos.

Se ha de remarcar que este es un mero esquema general con un enfoque claro en la seguridad del software de la empresa, haciendo hincapié en esta área concreta. Si se elige un enfoque de análisis externo, obviamente se obtendrá una evaluación general de la seguridad de sus programas, pero careciendo de un nivel alto de detalles.

Para enfocarnos en el entorno del software, respetando es esquema construido para ejecutar la auditoría ofensiva, orientándola al software, se deberán incluir las siguientes pruebas:

- **Ataques de Fuerza Bruta.** Se recomienda poner a prueba las constraseñas encontradas haciendo uso de ataques de fuerza bruta, tanto estándar, como de diccionario, híbridos e incluso con algoritmos de búsqueda inteligente.

- **Uso de exploits.** El uso de exploits es ampliamente utilizado por agresores en ataques reales, a fin de obtener un acceso no autorizado al sistema objetivo, por lo que el uso de estos es recomendado para entender las técnicas empleadas por los atacantes.

- **Ingeniería Social.** Si el cliente contrata una auditoría ofensiva con un enfonque de Red Teaming, se llevarían a cabo estrategias de ingeniería socialcon el fin de obtener acceso a sistemas no autorizados, tal y como lo harían atacantes reales. Esto se puede emplear en un ámbito de software, accediendo a herramientas empresariales que hagan uso de sistemas de autentificación.

- **Uso generalizado de malware (Troyanos, Rootkits, Spyware, etc).** Lo que se busca con esto es usar malware diseñado para lograr un acceso permanente a los sistemas de la empresa, creando incluso puertas traseras (*backdoors*) que faciliten el acceso a los mismos. El objetivo no es damnificar dichos sistemas, sino evaluar la capacidad de respuesta de los equipos de seguridad de la empresa, y buscar formas de sobrepasar las defensas informáticas de la misma, a fin de mitigar ataques reales a futuro.

- **Análisis de fallos a nivel de código.** Es necesario usar herramientas que evalúen de forma automática el código de diferentes aplicaciones de la empresa, con el objetivo de encontrar fallos de seguridad que puedan llevar a accesos no autorizados e incluso posibles vulnerabilidaes.

## Metodologías de Pentesting utilizadas

Las pruebas de pentesting son importantes en el ámbito de la seguridad informática, dado que poniendo a prueba los sistemas en los que realizan las pruebas, logran obtener resultados y, por ende, posibles soluciones o mitigaciones a fallos de seguridad y vulnerabilidades.

### 1. Metodología para Auditorías de Correos Electrónicos

#### Justificación de la Elección:

**Elección:** OWASP

Tras investigar todas las metodologías posibles me he encontrado con el inconveniente de que no existe una metodología especifica o perfecta para este área de correos electrónicos por lo que me he decantado por la metodología de OWASP ya que me parece que comparten muchos campos en común como pruebas de configuración, análisis de vulnerabilidades, pruebas de autenticación, pruebas de autorización y pruebas de servicios web y además proporciona un enfoque completo y sistemático para el análisis y las pruebas de penetración que ofrezco en los servicios de mi auditoria. También es flexible y se puede adaptar a necesidades específicas de nuestra empresa o de nuestros clientes.

#### Fases de la metodología OWASP

La metodología de OWASP tiene muchas variantes en cuanto al número sus fases por lo que me centraré en describir las 4 fases que yo considero más importantes para nuestra empresa: 

- **1. Reconocimiento:** En esta fase recolectamos toda la información posible sobre el sistema de correo electrónico de la empresa, sus políticas de seguridad, configuraciones, protocolos, versiones, etc...

- **2. Análisis de vulnerabilidades:** En esta fase analizamos toda la información obtenida en la fase anterior y buscamos y listamos todas las posibles vulnerabilidades que podemos explotar. 
Por ejemplo, también podemos buscar CVE's conocidas de algunos protocolos que se estén utilizando.

- **3. Explotación:** En esta fase nos dedicaremos a explotar todas las vulnerabilidades posibles listadas en la fase anterior para comprometer el sistema de correos y comprobar los puntos débiles de este.

- **4. Informes:** En esta fase se generará un informe que resuma los hallazgos de la auditoría y las recomendaciones para mejorar la seguridad del sistema de correo electrónico.

### 2. Metodología para Auditorías de Iot

#### Justificación de la elección:

**Elección:** OWASP-FSTM (Firmware Security Testing Methodology)

Tras realizar una investigación en profundidad de las posibles metodologías para realizar auditorías de Iot (Internet de las cosas) me he decantado por la metodología OWASP-FSTM ya que cubre todas las etapas que en mi opinión necesitaría dicha auditoria. Es una metodología bastante completa y muy recomendada por los expertos en el área de Iot. Además, es bastante flexible por lo que podremos adaptarla a diferentes dispositivos y entornos con los que trabajemos en nuestra empresa.

#### Descripción

La metodología OWASP-FSTM (Firmware Security Testing Methodology) es una guía que se centra en la comprobación de seguridad del firmware de los dispositivos Iot. Se basa en las mejores prácticas de seguridad y cubre todas las fases del proceso para realizar auditorías de Iot, desde la recolección de información de los dispositivos hasta la explotación de los mismos, por lo que nos ayudará a realizar un análisis completo y detallado para poder entregárselos a las empresas o usuarios que nos contraten.

#### Fases de la metodología OWASP-FSTM

La metodología OWASP-FSTM consta de 9 fases. En nuestro caso creo que le añadiría una fase más que se llamará "Informes" o "Documentación" donde le reflejaríamos a la empresa todos los resultados obtenidos y como podrían mejorarlos.

##### 1. Reconocimiento y búsqueda de información: 

Esta fase consiste en recopilar toda la información técnica y documental posible de los dispositivos y analizar de forma física los dispositivos.
   
En nuestro caso la utilizaríamos para buscar toda la información posible relacionada con la arquitectura, sistema operativo, firmware, etc... Esto lo haríamos visitando las páginas web de los fabricantes y con el uso de herramientas que nos permitan ver esta información.
   
##### 2. Obtención del firmware: 

Esta fase consiste en obtener el firmware del dispositivo.

En nuestro caso lo descargaríamos de la página oficial del fabricante si es posible y sino lo buscaríamos en otra fuente como páginas web con reputación, repositorios de github, etc...
   
##### 3. Analizar el firmware: 

Esta fase consiste en examinar las características del firmware obtenido en la fase anterior.

En nuestro caso analizaríamos el firmware a fondo con la ayuda de herramientas para buscar todas las vulnerabilidades posibles.
   
##### 4. Extraer el sistema de archivos: 

Esta fase consiste en realizar la extracción del sistema de archivos contenidos en el firmware.

Utilizaríamos herramientas especializadas en la extracción de sistemas de datos como por ejemplo la herramienta binwalk.  
   
##### 5. Análisis del contenido del sistema de archivos: 

En esta fase nos centrarémos en analizar todos los datos extraídos en la fase anterior para buscar información relevante a nivel de seguridad.

En nuestro caso utilizaríamos herramientas especializadas para ello como pueden ser file, strings y herramientas de ingeniería inversa como Ghidra o IDA. Con estas herramientas detectaríamos todas las posibles vulnerabilidades que pudiera haber en los datos del firmware.
   
##### 6. Emulación del firmware: 

Esta fase consiste en la ejecución del firmware fuera del dispositivo.

Ejecutaríamos el firmware de forma completa o por partes en un entorno seguro y controlado como por ejemplo con Qemu.
   
##### 7. Análisis dinámico: 

Esta fase consiste en realizar pruebas de seguridad dinámicas del dispositivo y las interfaces de las aplicaciones para encontrar todas las vulnerabilidades posibles.

En nuestro caso haríamos lo mismo que en la fase anterior pero esta vez intentando encontrar un mayor número de vulnerabilidades. Esto lo haríamos por ejemplo combinando Quemu con herramientas de Fuzzing como ClusterFuzz o FormatFuzzer.
   
##### 8. Análisis en tiempo de ejecución: 

Esta fase consiste en analizar los ejecutables durante el tiempo de ejecución en el dispositivo con el fin de encontrar problemas de seguridad.

En esta fase usaríamos herramientas de depuración como Eclipse CDT, NetBeans o gdbgui para detectar, identificar y comprobar puntos críticos del ejecutable, ya sea de forma parcial o completa.
   
##### 9. Explotación: 

Esta fase se centraría en explotar todas las vulnerabilidades descubiertas en las fases anteriores para obtener ejecución de código arbitrario, elevación de privilegios, etc.

En esta fase de explotación utilizaríamos todas las técnicas posibles para conseguir vulnerar el dispositivo mediante el uso de herramientas como Metaexploit, exploits de desbordamiento de búfer o inyección de código, scripts, etc...

##### 10. Documentación: 

Esta fase la he querido incluir yo para realizar un informe completo y detallado donde especifiquemos todas las vulnerabilidades encontradas y como se podrían solucionar si fuera posible así como algunas medidas de seguridad que deben aplicar la empresa para mejorar la seguridad de la misma.

### 3. Metodología OWISAM para Redes Inalámbricas

#### Justificación de su uso

OWISAM es la metodología más utilizada para las auditorias de redes Wi-Fi. Esta metodologia fue creada específicamente para su uso en redes Wireless y define perfectamente las restricciones que pueden abarcar este tipo de redes y las fases para auditar correctamente trabajando sobre los estándares de red 802.11.

#### Descripción

**Elección:** OWISAM

La metodología Open Wireless Security Assessment Methodology (OWISAM) tiene como objetivo poner en común controles de seguridad que se deben verificar sobre redes inalámbricas, ayudando a diferentes administradores de redes, de sistema y analista de seguridad a identificar riesgo a los que minimizar el impacto de futuros ataques de infraestructuras Wireless basadas en el estándar 802.11.

Esta metodología consiste en 64 controles técnicos agrupados en 10 categorías para poder garantizar una auditoría de seguridad optima en infraestructura inalámbrica.

#### Restricciones a tener en cuenta

Debemos conocer las restricciones que tiene la infraestructura Wi-Fi en el alcance, existen varios tipos de restricciones:

- Área geográfica: Está definido para aquellas redes y dispositivos ubicados en un área geográfica concreta, como una oficina. Debemos asegurarnos que los dispositivos a analizar realmente pertenecen a la organización y verificar su ubicación física antes de iniciar las pruebas.
- ESSID: Se identifica una o varias redes Wi-Fi en base a su nombre.
- BSSID: Se identifica la dirección MAC de los dispositivos y redes a verificar, esto permite centrar las pruebas sobre los dispositivos clientes obviando el resto de ruido en la red.
- Pruebas de fuerza bruta: Se debe definir si dentro de las pruebas se autoriza al auditor realizar pruebas de verificación de usuarios y contraseñas contra los mecanimos de autenticación y en que condiciones para evitar bloquear cuentas de usuarios o realizar DoS como efecto secundario.
- Ataques DoS: Identificar que pruebas están permitidas en este ámbito y que dispositivos deben de ser excluidos.
- Ventana horaria: Posiblemente se necesitará realizar las pruebas en un horario concreto.
- Análisis activo: Revisión de seguridad inalámbrica que se considera una revisión activa del auditor siempre y cuando esté autorizado a interactuar con los dispositivos incluidos en el alcance.
- Análisis de perimetro: Puede ser necesario realizar las pruebas de análisis y ataques desde el exterior del perimetro de la organización.
- Visibilidad de las pruebas: Se puede establecer que las pruebas se realicen de un modo que pasen inadvertidas por parte del personal de la empresa.

#### Fases de OWISAM

Además de estas restricciones, existen una serie de fases que se emplean en el análisis de seguridad wi-Fi, son 7 fases y son las siguientes:

1. Planificación: Realizamos los pasos previos al análisis técnico.
2. Recopilación de información: Análisis pasivo de dispositivos.
3. Identificación de dispositivos: Extración  de información relevante de la infraestructura.
4. Ataques: Identificar debilidades en los dispositivos Wi-Fi.
5. Acceso a la red: Análisis e interacción con la infraestructura.
6. Pruebas sobre normativa y directivas: Verificación del cumplimiento de los controles normativos.
7. Generación de resultados: Documentación de informes, análisis final de evidencias y clasificación de riesgos.

### 4. Metodología PTES

#### Justificación de la elección

**Elección:** PTES (Penetration Testing Execution Standard)

Se ha elegido implementar la metodología PTES (Penetration Testing Execution Standard), que posee un enfoque en un amplio espectro de áreas. Esta metodología está diseñada para poder ser aplicada tanto en redes y sistemas, aplicaciones web, redes, aplicaciones (software), ingeniería social e incluso seguridad física. Esta elección se hace debido al hecho de no existir una metodología concreta para el ámbito del software, pero sí una que cubre en gran medida, la mayoría de campos relevantes en el campo de la seguridad informática.

#### Descripción

La metodología de Evaluación de Seguridad de Pentesting Estándar (*PTES*) está compuesta por un conjunto de estándares y directrices definidos con el objetivo de estandarizar las pruebas de penetración o pentesting en el ámbito de la seguridad informática. 

#### Fases de la Metodología PTES

La metodología PTES proporciona una forma clara y estructurada de auditar la seguridad de múltiples ámbitos. Para lograr esto, esta metodología dispone de una serie de fases, las cuales expondremos a continuación:

1. **Fase de Interacción Previa.** Fase inicial, en la que se planifica el pentesting, definiendo los objetivos del mismo, el alcance que va a tener, acordar una autorización con la empresa objetivo, así como llevar a cabo una recopilación básica de información.

2. **Fase de Recopilación de Información.** En esta fase se comienza a analizar el objetivo, llevándose a cabo a través de fuentes OSINT. Con esto obtenemos información detallada sobre la organización objetivo, incluyendo sus sistemas, aplicaciones y recursos de red. Este análisis puede llegar a cubrir el escaneo de puertos, enumeración de servicios y repopilación de información sobre empleados y archivos. 

3. **Fase de Modelado de Amenazas.** Esta fase consiste en analizar tanto el entorno interno como el externo del objetivo en busca de elementos susceptibles de ser explotados por posibles atacantes, pudiendo llevar a futuros ataques contra la organización objetivo. Su propósito es doble: primero, identificar los activos que serán objeto de la auditoría, evaluando su valor para la empresa y su importancia en los procesos de la organización; y en segundo lugar, evaluar quiénes podrían ser los posibles atacantes y su capacidad, se busca comprender y describir las amenazas en profundidad. Esta fase permite perfilar los tipos de ataques más probables, que serán los que se considerarán principalmente en las etapas posteriores del proceso.

4. **Fase de Análisis de Vulnerabilidades.** Fase en la que se realiza el proceso de análisis de vulnerabilidades y fallos en la configuración de los sistemas del objetivo, adelantándose al posible atacante. Una configuración de seguridad errónea, una contraseña débil o por defecto o un diseño inseguro pueden facilitar un posible ataque, y son objetivos en esta fase del pentesting.

5. **Fase de Explotación.** Una vez recopilada una lista de fallos de seguridad y vulnerabilidades, los pentesters o expertos en seguridad informática comienzan el proceso de acceso al sistema objetivo, saltándose los mecanismos de seguridad sirviéndose de exploits y apoyándose en las vulnerabilidades descubiertas. El fin último es lograr el control del sistema bajo prueba.

6. **Fase de Post-Explotación.** Una vez logrado el acceso al sistema, se busca lograr una persistencia en el mismo, así como llevar a cabo movimientos laterales cuyo objetivo sea alcanzar el control de otros activos. Con estas acciones se busca, a través del acceso conseguido, analizar y recopilar la información con mayor valor posible.

7. **Fase de Reporte.** Es la última fase, y consiste en la elaboración de un informe que detallen las conclusiones de las pruebas de pentesting. En este documento se resumen los resultados obtenidos, se evalúan los riesgos identificados y se sugiere un plan para reducir o gestionar dichos riesgos.

Finalmente, se elimina cualquier acceso y rastro dejado durante el pentesting, lo que devuelve el sistema a su estado original.

## Herramientas de Pentesting

### Herramientas para Pentesting de Correos Electrónicos

#### 1. Herramientas OSINT (Open Source INTelligence)

Estas herramientas nos serán muy útil para nuestra auditoría de correos electronicos ya que nos ahorrará mucho tiempo buscando direcciones de correos de los empleados de la empresa, direcciones IP, nombres de los servidores, arquitectura de red, etc...

**Herramientas:**

En esta sección se han definido las herramientas más adecuadas para cada área que nuestra empresa utilizará. 

Son las siguientes:

##### - The Harvester: Gratis

Es una herramienta para la obtención de informacióna a través de los diferentes motores de los principales buscadores y servicios utilizados, o si lo preferimos haciendo fuerza bruta, resoluciones inversas, etc…
 
##### - Hunter.io: 34€/mes, 408€/año (500 busquedas mensuales)

Es un portal web que permite buscar los emails de personas que trabajan en una empresa con solo introducir su página web.

##### - MAILSHUNT: 

Esta extensión de navegador enumera todas las direcciones de correo electrónico de las personas que trabajan en una empresa en concreto.

##### - MXTOOLBOX: $129/month

MxToolbox no es tan útil para correos electrónicos de dominios de correo electrónico conocidos como Gmail, pero si nuestro objetivo utiliza su propio servidor de intercambio de correo (lo que suelen hacer la gran mayoría de las grandes empresas), nos puede ayudar, ya que identificar la dirección IP de un servidor de intercambio de correo puede ser un buen punto de partida para nuestra investigación (podremos observar las direcciones IP compartidas, los nombres de los servidores, su arquitectura de red, etc).
MxToolbox también ofrece un servicio de análisis de encabezados de correo electrónico.

##### - Maltego: 999 EUR / año

Maltego es un servicio que tiene el potencial de encontrar información sobre personas y empresas en Internet, permitiendo cruzar datos para obtener servidores de correo entre otras cosas.

#### NMAP: Gratis

Nmap es una herramienta que permite encontrar qué dispositivos se están ejecutando en la red, descubrir puertos y servicios abiertos y detectar vulnerabilidades.

Nmap es indispensable para nuestra empresa ya que nos permitirá identificar servidores de correo, enumerar cuentas de correo, detectar cuentas de correo, etc...

#### Wireshark: Gratis

Es una herramienta de análisis de tráfico de red que se utiliza para capturar y analizar paquetes de datos que se transmiten a través de una red. 

Esta herramienta también nos resultará muy util ya que podremos para analizar todo el tráfico de la red de la empresa e identificar correos electrónicos sospechosos, recopilar evidencia de actividad y evaluar la seguridad de los servidores de correo.

#### Network Miner: Gratis

Es similar a Wireshark.
Es una herramienta de análisis de tráfico de red que puede ser utilizada para capturar y analizar paquetes de datos que se transmiten a través de una red. 

Esta herramienta también nos resultará muy util ya que podremos para analizar todo el tráfico de la red de la empresa e identificar correos electrónicos sospechosos, recopilar evidencia de actividad y evaluar la seguridad de los servidores de correo.

#### Nessus:  1 año - 4482,49 €

Nessus es una herramienta de escaneo de vulnerabilidades desarrollada por Tenable Network Security. Es una de las herramientas de escaneo de vulnerabilidades más populares del mundo, y es utilizada por organizaciones y empresas de todos los tamaños para evaluar sus sistemas y redes en busca de vulnerabilidades conocidas.

Creemos que nessus es una herramienta bastante completa y bastante útil ya que es analizador de vulnerabilidades más potente del mercado por lo que nos ahorra mucho tiempo para encontrarlas ya que dispone de escaneo de puertos y servicios, escaneos de aplicaciones web, escaneos de configuración y escaneos de software.

#### SpoofCheck: Gratis

Esta herramienta se encarga de ir comprobando una serie de condiciones para verificar si un servidor de correos es spoofeable o no.

Nos será bastante útil ya que podremos comprobar si el servidor de correos es vulnerable o no ejecuntando la herramienta por lo que nos ahorrará tiempo.

#### Splunk: el precio depende de los datos usados

Es una plataforma de análisis de datos en tiempo real que permite recopilar, almacenar, analizar y visualizar datos generados por los dispositivos.

En nuestra empresa necesitamos de un SIEM que nos ayude a mejorar la eficiencia de nuestras auditorías y creemos que Splunk es la mejor opción ya que es bastante flexible y se paga por la cantidad de datos utilizados.

### Herramientas para Pentesting de Redes

#### NMAP: Gratis

NMAP es una de las herramientas credas para administradores, auditores y profesionales de seguridad. Tiene muchas funcionalidades, entre ellas permite la ejecución de scripts personalizados que permiten la identifiaciones de informaciones específicas.

Opera realizando un escaneo de objetivos que pueden ser redes y hosts, esntén abiertos a internet o no. También escanea puertas de servicios que estén abiertas, determina el tipo de servicio, versión y los sistemas operacionales. Con ella podemos hacer un barrido de la red y obtener respuestas de todos los dispositivos que estén conectados a la misma.

#### NetCat: Gratis

Conocido como nc, es una de las herramientas más antiguas. Fue creada para interactuar con puertas de servicios directamente a través de la entrega de una dirección IP, una puerta y un protocolo. Esta herramienta también puede transferir archivos y establecer sesiones de host a host.

#### Kismet Wireless: Gratis

Es un sistema de detección de intrusos, detector de redes inalámbricas y rastreador de contraseñas, funciona con otras tarjetas inalámbricas y admite el modo de monitoreo sin formato.

Es la mejor herramienta para probar redes inalámbricas y piratear LAN inalámbrica o wardriving. Identifica redes de forma pasiva y recopila paquetes y detecta redes ocultas y sin baliza con la ayuda del tráfico de datos.

Funciona principalmente con redes Wi-Fi(IEEE 802.11) y se le pueden ampliar sus funcionalidades mediante numerosos complementos. Funciona en sistemas Linux, Ubuntu y más.

#### NetStumbler: Gratis

Se utiliza para evitar wardriving, funciona en sistemas operativos Windows. Es capaz de detectar redes IEEE 802.11g, 802 y 802.11b. La versión más actualizada se llama MiniStumbler

#### Aircrack-ng: Gratis

Ofrece una variedad de herramientas de línes de comandos que verifican y evalúan la seguridad de la red Wi-Fi. Se dedica a actividades como ataque, monitoreo, prueba y descifrar contraseñas de redes inalámbricas WEP/WAP/WPA2.

Su funcionamiento se basa en tomar los paquetes de la red, y analizarlos mediante contraseñas recuperadas.

#### Wireshark: Gratis

Se utiliza para analizar paquetes de datos, también puede realizar inspecciones profundas de gran cantidad de protocolos establecidos. Podemos exportar los resultados del análisis a muchos formatos de archivo diferentes.

Realiza capturas en vivo y análisis fuera de línea.

#### Ettercap: Gratis

Es un sniffer/interceptor/logger para redes LAN con switchs, que soportan la disección activa y pasiva de muchos protocolos e incluye muchas características para el análisis de la red y el host anfitrión.

Filtra contenido y puede rastrear conexiones en vivo.

#### Angry IP Scanner: Gratis

Sirve para escanear direcciones IP y puertos. Puede usarse en internet o en LAN y es compatible con varios Sistemas Operativos. Permite realizar un rastreo y exportar los resultados en distintos formatos.

#### TCPDump y WinDump: Gratis

TCPDump es una herramienta diseñada para analizar el tráfico que circula por la red. Basada en línea de comandos y permite capturar y representar todo el tráfico que pasa por la red.

La versión de Windows se llama WinDump y requiere la instalación previa de WinPCAP.

### Herramientas para Pentesting de Software

En este apartado incluimos un abanico de aplicaciones destinadas al uso del pentesting en el ámbito de la seguridad del software. Para ello hemos elegido cuidadosamente una serie de herramientas que nos facilitarán dicho trabajo:

- **Nessus.** Herramienta de evaluación de vulnerabilidades en sistemas operativos. Esta herramienta se compone de dos módulos, siendo *Nessusd* y *Nessus Client*. El primero se encarga de realizar el escaneo, mientras que el segundo controla las exploraciones y muestra los resultados acerca de las vulnerabilidades encontradas.
Este software es capaz de escanear puertos, así como los dispositivos conectados a una red, es capaz de detectar servicios, identificando los que son usados por las aplicaciones del sistema, identifica vulnerabilidades y finalmente, realiza un sondeo, asegurándose de no cometer falsos positivos. El precio oscila entre 500€ a 4482,49€ la versión más cara, aunque existe la posibilidad de solicitar una demo gratutita por 7 días.

- **Metasploit.** Plataforma de pruebas de penetración y desarrollo de exploits ampliamente utilizada en al ámbito de seguridad informática. Esta herramienta permite el desarrollo y prueba de exploits, ofreciendo una amplia biblioteca, de modo que el pentester tan sólo tiene que elegir el que necesite en cada momento; también permite escanear y enumerar servicios en una red y recopilar información en sistemas objetivo. Metasploit incluye también una shell remota, permitiendo acceder a sistemas previamente comprometidos, ejecutando comandos de forma remota; ofrece un sistema de gestión de sesiones de explotación en una misma consola, y provee al pentester de un sistema de genración de informes. Esta herramienta es gratuita, pero existe una versión Pro por 14000€.

- **John the Ripper.** Software de crackeo de contraseñas muy útil en tests de penetración por su capacidad de poner a prueba la robustez de contraseñas frente a ataques de fuerza bruta, llegando a romper hashes MD5 y SHA-1, pudiendo detectar el tipo de hash utilizado. Esta herramienta es ampliamente utilizada y funciona tanto en Windows como en sistemas Linux. Existen tres versiones, siendo la gratuita; John the Ripper Pro, que cuesta x€ y finalmente tenemos John the Ripper Jumbo, costando x€.

<br/>

## Presupuesto de inversión inicial

En función a las necesidades de nuestra empresa se ha estimado un presupuesto para la inversión inicial teniendo en cuenta algunos gastos legales la comunidad autónoma de Andalucía.

| Recursos        | Precio/año       |
|---------------------|------------------|
| **Hunter.io**      | 408€             |
| **MXToolBox**      | 1569.84€         |
| **Maltego**        | 999€             |
| **Nessus**         | 4482,49€         |
| **Splunk**         | 1698,65          |
| **Burpsuite**      | 445€         |
| ****         |          |
| **Portátil Slimbook Pro X 15 AMD (Para 4 trabajadores)**   |  3996€    |
| **Salario (Para 4 trabajadores)**  | 88000€ |
| **Gastos legales** | 5000€ |
|---------------------|------------------|
| **Total**             | **106498.98€**  |

## Conclusión

Como se ha discutido con anterioridad, vivimos en un mundo sumido por completo en las tecnologías de la información, y absolutamente dependiente de estas. Este hecho es una gran muestra de la evolución tecnológica de la humanidad desde mediados del siglo 20, donde se idearon los primeros ordenadores

## Bibliografía

A fin de aportar claridad y orden, se ha dividido la bibliografía por áreas de trabajo investigadas. 

### Bibliografía para la investigación de redes

- [https://blog.invgate.com/es/tipos-de-ciberataque](https://blog.invgate.com/es/tipos-de-ciberataque)
- [https://www.cisco.com/c/es_mx/products/security/common-cyberattacks.html#~tipos-de-ciberataques](https://www.cisco.com/c/es_mx/products/security/common-cyberattacks.html#~tipos-de-ciberataques)
- [https://www.f5.com/es_es/glossary/syn-flood-attack](https://www.f5.com/es_es/glossary/syn-flood-attack)
- [https://www.redeszone.net/tutoriales/seguridad/listado-completo-ataques-redes-como-evitarlos/](https://www.redeszone.net/tutoriales/seguridad/listado-completo-ataques-redes-como-evitarlos/)
- [https://afsh4ck.gitbook.io/ethical-hacking-cheatsheet/introduccion/introduccion/metodologia-osstmm](https://afsh4ck.gitbook.io/ethical-hacking-cheatsheet/introduccion/introduccion/metodologia-osstmm)
- [https://www.hackbysecurity.com/servicios-empresas/auditoria-informatica/auditoria-externa-o-perimetral](https://www.hackbysecurity.com/servicios-empresas/auditoria-informatica/auditoria-externa-o-perimetral)
- [https://ostec.blog/es/aprendizaje-descubrimiento/pentest-las-10-mejores-herramientas-usadas-en-el-mercado/](https://ostec.blog/es/aprendizaje-descubrimiento/pentest-las-10-mejores-herramientas-usadas-en-el-mercado/)
- [https://www.ctxdetectives.com/que-es-el-owisam/](https://www.ctxdetectives.com/que-es-el-owisam/)
- [https://institutotecnologicoeuropeo.com/mejores-herramientas-software-etico-para-hackers-2022/](https://institutotecnologicoeuropeo.com/mejores-herramientas-software-etico-para-hackers-2022/)
- [https://jotelulu.com/blog/5-herramientas-para-comprobar-la-seguridad-de-nuestra-red/](https://jotelulu.com/blog/5-herramientas-para-comprobar-la-seguridad-de-nuestra-red/)
- [https://ostec.blog/es/aprendizaje-descubrimiento/pentest-las-10-mejores-herramientas-usadas-en-el-mercado/](https://ostec.blog/es/aprendizaje-descubrimiento/pentest-las-10-mejores-herramientas-usadas-en-el-mercado/)
- [https://www.ctxdetectives.com/que-es-el-owisam/](https://www.ctxdetectives.com/que-es-el-owisam/)
- [https://institutotecnologicoeuropeo.com/mejores-herramientas-software-etico-para-hackers-2022/](https://institutotecnologicoeuropeo.com/mejores-herramientas-software-etico-para-hackers-2022/)
- [https://jotelulu.com/blog/5-herramientas-para-comprobar-la-seguridad-de-nuestra-red/](https://jotelulu.com/blog/5-herramientas-para-comprobar-la-seguridad-de-nuestra-red/)

### Bibliografía para la investigación de correos electrónicos

- https://www.skysnag.com/es/blog/example-of-email-based-attacks/#8_Denial-of-service_DoS_attacks
- https://www.globalsign.com/es/blog/tipos-comuns-ataques-de-phishing
- https://www.checkpoint.com/es/cyber-hub/threat-prevention/what-is-email-security/
- https://noticias.aixacorpore.es/iso-27001/ataques-por-medio-del-correo-electronico-email-spoofing/
- https://keepcoding.io/blog/tipos-de-amenazas-a-correos-electronicos/
- https://www.acronis.com/es-es/blog/posts/email-cyber-attack/
- https://powerdmarc.com/es/what-are-email-based-attacks/
- https://www.skysnag.com/es/blog/example-of-email-based-attacks/#1_Phishing
- https://www.incibe.es/ciudadania/blog/que-es-el-phishing
- https://latam.kaspersky.com/resource-center/definitions/what-is-a-whaling-attack
- https://support.microsoft.com/es-es/office/suplantaci%C3%B3n-de-identidad-phishing-y-comportamiento-sospechoso-0d882ea5-eedc-4bed-aebc-079ffa1105a3
- https://www.ing.es/seguridad-internet/vishing-que-es#:~:text=Llamada%20de%20alguien%20que%20se,tarjeta%20u%20otra%20incidencia%20grave.
- https://www.trendmicro.com/es_es/what-is/phishing/types-of-phishing.html
- https://www.uach.cl/direccion-de-tecnologias-de-informacion/seguridad/tipos-de-phishing
- https://latam.kaspersky.com/resource-center/definitions/pharming
- https://latam.kaspersky.com/resource-center/definitions/what-is-a-whaling-attack
- https://www.pandasecurity.com/es/mediacenter/seguridad/whaling/
- https://easydmarc.com/blog/es/12-tipos-de-ataques-phishing-y-como-identificarlos/
- https://www.welivesecurity.com/la-es/2015/04/17/que-es-un-backdoor/
- https://encyclopedia.kaspersky.es/knowledge/backdoor/
- https://www.cyberghostvpn.com/es_ES/privacyhub/que-es-una-puerta-trasera-backdoor/
- https://www.kaspersky.es/blog/que-es-un-rootkit/594/
- https://latam.kaspersky.com/resource-center/definitions/what-is-rootkit
- https://es.wikipedia.org/wiki/Rootkit
- https://www.avast.com/es-es/c-keylogger
- https://latam.kaspersky.com/resource-center/definitions/keylogger
- https://encyclopedia.kaspersky.es/knowledge/trojan-mailfinder/
- https://www.ninjaone.com/es/blog/como-prevenir-los-ataques-de-spoofing/
- https://powerdmarc.com/es/what-are-email-based-attacks/
- https://noticias.aixacorpore.es/iso-27001/ataques-por-medio-del-correo-electronico-email-spoofing/
- https://easydmarc.com/blog/es/que-son-los-correos-spam-y-como-podemos-prevenirlos/
- https://www.eset.com/es/caracteristicas/spam/
- https://www.strato.es/faq/correo/que-es-spam-y-como-puedo-protegerme/
- https://www.mailjet.com/es/blog/entregabilidad/que-es-spam/
- https://www.avast.com/es-es/c-spam
- https://www.proofpoint.com/es/threat-reference/email-scams
- https://medac.es/blogs/masteres-online/que-es-scam
- https://es.wikipedia.org/wiki/Scam
- https://www.pandasecurity.com/es/security-info/scam/
- https://www.uv.mx/infosegura/general/noti_scam-3/
- https://uniblog.unicajabanco.es/-que-es-el-scam-
- https://www.cloudflare.com/es-es/learning/email-security/what-is-email-security/
- https://es.linkedin.com/pulse/descifrando-las-t%C3%A1cticas-y-los-impactos-del-fraude-de-paola-noriega
- https://dynamics.microsoft.com/es-es/ai/fraud-protection/account-takeover/
- https://www.skrill.com/es/skrill-news/inside-skrill/prevencion-del-fraude-de-apropiacion-de-cuentas/
- https://www.cloudflare.com/es-es/learning/insights-bec-proactive-security/
- https://easydmarc.com/blog/es/como-hacen-los-estafadores-de-phishing-para-obtener-tu-direccion-de-correo-electronico/
- https://peritosinformaticos.es/fraude-por-cambio-de-numero-de-cuenta-bancaria-en-correos-electronicos/#:~:text=La%20t%C3%A9cnica%20de%20intercepci%C3%B3n%20de,-est%C3%A1n%20cruzando%20conversaciones%20por%20email.
- https://foro.elhacker.net/hacking/se_pueden_interceptar_correos_electronicos-t517901.0.html;msg2270313
- https://es.ccm.net/aplicaciones-e-internet/museo-de-internet/enciclopedia/10566-que-es-el-email-bombing/
- https://medium.com/@edinsonrequena/tutorial-qu%C3%A9-es-un-email-bomb-attack-y-como-crearlo-con-python-3-c566d688944a
- https://zonavirus.com/noticias/2021/e-mail-bombing-como-usan-el-spam-para-atacar_71650
- https://es.wikipedia.org/wiki/Gusano_inform%C3%A1tico
- https://www.pandasecurity.com/es/security-info/worm/
- https://www.kaspersky.es/resource-center/threats/ransomware-wannacry
- https://es.malwarebytes.com/ransomware/
- https://es.wikipedia.org/wiki/Ransomware
- https://www.fortra.com/es/blog/pentesting-herramientas-tecnicas
- https://www.disruptivos.com/auditoria-email-mejorar-resultados/
- https://blog.mailup.es/2021/02/email-auditorias/
- https://www.acronis.com/es-es/blog/posts/cyber-security-audit/
- https://secuora.es/blog/auditoria-de-ciberseguridad-red-team-conoce-por-que-necesitas-realizarla/
- https://www.hiberus.com/crecemos-contigo/pentesting-owasp-fases-metodologia/
- https://www.reydes.com/d/?q=Metodologia_de_Pruebas_OWASP
- https://www.arsys.es/blog/owasp#:~:text=6%20Conclusiones-,%C2%BFQu%C3%A9%20es%20OWASP%3F,las%20mejores%20pr%C3%A1cticas%20de%20seguridad.
- https://www.osintux.org/documentacion/the-harvester
- https://hunter.io/
- https://consejoderedaccion.org/sello-cdr/hunter-busca-correos-emails#:~:text=Hunter.io%20es%20un%20portal,solo%20introducir%20su%20p%C3%A1gina%20web.&text=Durante%20la%20investigaci%C3%B3n%20period%C3%ADstica%20es,con%20personas%20que%20no%20conocemos.
- https://medium.com/devrolabs/find-email-addresses-in-seconds-mailshunt-9f15b9692ed6
- https://blog.dopplerrelay.com/herramientas-para-investigar-problemas-de-entregabilidad/#:~:text=MXToolBox%20es%20una%20fuente%20probada,listas%20negras%20de%20correo%20electr%C3%B3nico.
- https://mxtoolbox.com/
- https://www.maltego.com/
- https://www.welivesecurity.com/la-es/2023/05/11/maltego-herramienta-muestra-tan-expuesto-estas-internet/
- https://keepcoding.io/blog/que-es-maltego-ciberseguridad/
- https://nmap.org/
- https://www.freecodecamp.org/espanol/news/que-es-nmap-y-como-usarlo-un-tutorial-para-la-mejor-herramienta-de-escaneo-de-todos-los-tiempos/
- https://openwebinars.net/blog/wireshark-que-es-y-ejemplos-de-uso/
- https://www.incibe.es/ciudadania/herramientas/wireshark
- https://www.cyberseguridad.com.mx/nessus-escaner-de-vulnerabilidades-overview/
- https://fferia.wordpress.com/nessus/
- https://behacker.pro/nessus-como-hallar-vulnerabilidades/
- https://keepcoding.io/blog/que-es-nessus/
- https://es-la.tenable.com/products/nessus
- https://www.computing.es/seguridad/splunk-la-herramienta-para-anticiparse-a-los-ataques/
- https://aprenderbigdata.com/splunk/
- https://www.flu-project.com/2016/08/simpleemailspoofer-y-spoofcheck.html

### Bibliografía para la investigación del área web

- https://www.imperva.com/learn/application-security/csrf-cross-site-request-forgery/
- https://owasp.org/www-community/Types_of_Cross-Site_Scripting
- https://lenguajejs.com/javascript/dom/que-es/
- https://developer.mozilla.org/es/docs/Glossary/Cross-site_scripting
- https://venafi.com/blog/what-session-hijacking/
- https://www.deltaprotect.com/blog/ataques-ddos-que-son
- https://academy.bit2me.com/que-son-ataques-dos/
- https://owasp.org/www-community/attacks/Credential_stuffing
- https://www.cloudflare.com/learning/bots/what-is-credential-stuffing/
-  https://www.codemotion.com/magazine/cybersecurity/cybersecurity-threats-web-developer/
- https://portswigger.net/web-security/xxe
- https://security.packt.com/json-web-token-attack/
- https://attack.mitre.org/
- https://www.dvvs.co.uk/third-party-javascript-attack/

### Bibliografía para la investigación de IoT

- [https://www.tarlogic.com/es/auditoria-seguridad-iot/](https://www.tarlogic.com/es/auditoria-seguridad-iot/)
- [https://www.isaca.org/es-es/resources/isaca-journal/issues/2018/volume-5/is-audit-basics-auditing-the-iot](https://www.isaca.org/es-es/resources/isaca-journal/issues/2018/volume-5/is-audit-basics-auditing-the-iot)
- https://github.com/scriptingxss/owasp-fstm
- https://www.tarlogic.com/es/blog/analisis-de-seguridad-en-iot-owasp/
- https://www.tarlogic.com/es/blog/owasp-fstm-reconocimiento-informacion/
- https://www.tarlogic.com/es/blog/owasp-fstm-obtencion-firmware-iot/
- https://www.tarlogic.com/es/blog/owasp-fstm-etapa-3-analisis-del-firmware/
- https://www.tarlogic.com/es/blog/owasp-fstm-extraccion-sistema-ficheros/
- https://www.tarlogic.com/es/blog/owasp-fstm-analisis-sistema-ficheros/
- https://www.tarlogic.com/es/blog/owasp-fstm-etapa-6-emulacion-del-firmware/
- https://www.tarlogic.com/es/blog/owasp-fstm-analisis-dinamico/
- https://www.tarlogic.com/es/blog/owasp-fstm-analisis-en-tiempo-de-ejecucion/
- https://www.tarlogic.com/es/blog/owasp-fstm-etapa-9-explotacion-de-ejecutables/
- https://auditordeciberseguridad.es/implementando-itdr-10-acciones-para-proteger-el-directorio-activo-3/

### Bibliografía para la investigación de software

- https://masterenciberseguridadonline.es/tipos-de-ataques-de-fuerza-bruta/
- https://winempresas.pe/blog/ataques-informaticos-causas-y-12-tipos-de-ciberataques
- https://cnipj.es/tipos-ataques-informaticos/
- https://ciberseguridad.blog/25-tipos-de-ataques-informaticos-y-como-prevenirlos/
- https://www.hackbysecurity.com/servicios-empresas/auditoria-informatica/tipos-de-auditorias-de-seguridad-informatica
- https://www.deltaprotect.com/blog/auditoria-de-seguridad-informatica
- https://resources.infosecinstitute.com/topics/hacking/popular-tools-for-brute-force-attacks/
- https://www.ciberseguridad.eus/ciberglosario/escalada-de-privilegios
- https://softwarelab.org/es/blog/que-es-un-rootkit/
- https://www.20minutos.es/tecnologia/ciberseguridad/5-troyanos-muy-peligrosos-que-te-pueden-vaciar-la-cuenta-5040746/
- https://nordvpn.com/es/blog/que-es-adware/
- https://es.gridinsoft.com/spyware
- https://softwarelab.org/es/blog/que-es-un-gusano-informatico/
- https://www.danysoft.com/los-12-peores-botnets/
- https://ayudaleyprotecciondatos.es/2021/04/23/rogueware/
- https://www.platinumciber.com/las-fases-de-un-ciberataque/
- https://www.ymant.com/blog/las-7-fases-de-un-ciberataque/
- http://www.pentest-standard.org/index.php/Main_Page
- https://keepcoding.io/blog/que-es-nessus/
- https://keepcoding.io/blog/que-es-metasploit-ciberseguridad/
- https://www.redeszone.net/tutoriales/seguridad/crackear-contrasenas-john-the-ripper/
