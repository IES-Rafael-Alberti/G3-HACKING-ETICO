# Investigación de Tipos de Ataque relacionados con los correos eletrónicos

## 1. Tipos y clasificación de ataques

### 1. Phishing

El phishing es una técnica de estafa en la que se hace uso de técnicas de ingeniería social para engañar a un usuario con el fin de obtener información privada, beneficios económicos o incluso para instalar malware en el dispositivo.

Dentro del phising existen múltiples variantes como:

- Deceptive Phishing (Phishing clásico): Consiste suplantar la identidad mediante el envío de un correo electrónico por parte de un ciberdelincuente a un usuario simulando ser una entidad legítima (red social, banco, institución pública, etc.) con el objetivo de robarle información privada, realizarle un cargo económico o infectar el dispositivo. Para ello, adjuntan archivos infectados o enlaces a páginas fraudulentas en dicho correo electrónico.
  
- Spear phishing (dirigido a individuos específicos): Consiste en un tipo de estafa muy similar al phishing clásico, pero con la diferencia de que van dirigidos a una o varias víctimas en concreto. Este tipo de correos electrónicos se preparan de manera bastante más sofisticada ya que primero estudian a las víctimas (sus gustos, preferencias, etc..) y luego elaboran el correo electrónico según el perfil estudiado de la víctima por lo que es mucho más efectivo ya que es más complicado que un usuario lo detecte.

- Whaling (Caza de la ballena): Esta estafa consiste en la suplantación de identidad de altos cargos de las empresas, como directores generales, directores de operaciones, presidentes o personas importantes dentro de esta para que compartan credenciales, acceder a redes que están muy protegidas o simplemente robar dinero o datos. Emplean tácticas más avanzadas y sofisticadas que otros tipos de ataques hasta el punto de realizar una investigación y planificación previa.
Se utilizan nombres, direcciones, cargos u otra información personal para crear una apariencia más sólida y creíble para el ataque.

- Pharming: Es un método en el que el tráfico de la navegación, vinculado a un correo recibido, se redirige para que el usuario crea que está navegando en el sitio web deseado. En realidad, se conecta al sitio web del ciberdelincuente, lo que puede resultar en la obtención de credenciales o información personal con el fin de usurpar la identidad de alguien.
Este tipo de ataque suele aprovechar la navegación en línea de las víctimas al corromper el sistema de nombres de dominio (DNS). El atacante envenena el DNS y lo modifica de manera que los usuarios visiten sitios web maliciosos en lugar de los sitios legítimos, sin que ellos lo sepan.

- También existen más variantes como por ejemplo, el Vishing (phishing a través de llamadas telefónicas) o como el Smishing (phishing a través de mensajes de texto), Angler Phishing (Dirigido a los usuarios de las redes sociales), etc.. pero en estos no me centraré ya que no entran en el área de los correos electrónicos.

### 2- Spoofing

El email spoofing consiste en la suplantación de identidad por correo electrónico, que se produce cuando un atacante envía un correo electrónico a un usuario haciéndose pasar por otra persona o empresa. Esto se consigue camuflando la dirección de correo electrónico de forma que la sustituyen por una legítima. Un ejemplo puede ser que el atacante use paypa1.com en vez de paypal.com. La mayoría de usuarios a los que van destinados estos correos no se suelen fijar bien en la dirección si el nombre le resulta familiar o simplemente ni la leen por lo que no se dan cuenta de que se trata de una dirección de correo falsa.

Los atacantes consiguen camuflar las direcciones de correo electrónico debido a la falta de seguridad del protocolo simple de transferencia de correo (SMTP), que no admite cifrado, autenticación ni otras medidas de seguridad similares. Por ejemplo, los servidores de correos más reconocidos como pueden ser Gmail o Outlook utilizan este protocolo por lo que es muy fácil para los atacantes hacer este cambio de dirección.

Si bien es similar al phishing, estos dos ataques son distintos. El phishing busca robar información personal o credenciales a través de engaños o estafas, mientras que el email spoofing su objetivo principal es suplantar la identidad de alguien en un correo electrónico, lo que puede llevar a ataques de phishing, pero su objetivo principal es la suplantación de identidad.

### 3. Spam

El spam de correos electrónicos es un tipo de comunicación masiva que se envía principalmente por motivos comerciales. A los atacantes que realizan el envió de este tipo de correos se les suele llamar "Spammers". Estos correos electrónicos suelen contener publicidad no deseada, promociones, malware, enlaces a sitios web falsos o contenido irrelevante. 

Algunos ejemplos pueden ser:

- Ofertas para ganar dinero rápido.
- Ofertas incitantes como descuentos o promociones.
- Mensajes de préstamos o créditos no solicitados.
- Notificaciones de facturas falsas.

Aunque en la mayoría de los casos no se considera dañino, puede resultar molesto y difícil de filtrar. También es importante destacar que el spam puede llevar a la pérdida de productividad y tiempo para los usuarios, ya que deben dedicar tiempo a eliminar o ignorar estos correos no deseados.
Para combatir el spam, se utilizan filtros de correo electrónico que intentan bloquear estos mensajes no deseados antes de que lleguen a la bandeja de entrada del usuario.

### 4. Scam

El scam son los intentos de estafas llevadas a cabo a través de correos electrónicos, cuyo objetivo es engañar al usuario para que cometan una acción legítima, pero en realidad no lo son. En la mayoría de los casos, se pretende estafar económicamente pero también se utiliza para instalar malware o robar información.

Algunos ejemplos pueden ser:

- Correos de servicios donde piden actualizar información.
- Donaciones.
- Premios de lotería.
- Pago de donaciones a ONGs falsas.
- Servicios de renovación como por ejemplo seguros de coches o plataformas de streaming (Netflix, Twitch, HBO, etc...)
- Soporte o asistencia técnica.

El funcionamiento del scam se divide en tres etapas:

- 1 etapa: Los estafadores establecen contacto con la víctima a través de correos electrónicos no solicitados e intenta atraer la atención de la víctima y establecer una comunicación inicial.
  
- 2 etapa: Una vez que se ha establecido el contacto, el estafador comienza a engañar o manipular a la víctima ofreciéndole ofertas, soporte o algunos de los ejemplos que especifico arriba.

- 3 etapa: Una vez que se ha conseguido engañar a la víctima, el atacante recibe dinero, información confidencial o simplemente infecta el dispositivo de la víctima con malware.


### 5. Malware

Malware o “software malicioso” es un término amplio que describe cualquier programa o código malicioso que es dañino para los sistemas. Los ataques de malware a través del correo electrónico son muy habituales y generan una amenaza persistente y creciente en el mundo actual. Los atacantes lo usan para robar, cifrar o borrar datos, alterar o secuestrar funciones básicas del dispositivo e incluso para espiar su actividad sin su permiso.

Como existen muchos tipos de malware y mis compañeros también lo van a detallar y a explicar, mostraré algunos ejemplos de los más comunes que se distribuyen por correo electrónico:

#### - Troyanos (Caballos de Troya): 
Es un tipo de archivo que contiene malware y que comúnmente se camuflar dentro de un software legítimo adjunto a un correo electrónico. Aunque el correo electrónico y el archivo adjunto parezcan legítimos y procedan de una fuente fiable, cuando la víctima hace clic en ellos, el malware se instala en su ordenador. Los troyanos pueden utilizarse para robar datos, controlar el equipo para ser usado por una red de bots (BotNet) o incluso borrar completamente todos los archivos del disco duro.

Algunos ejemplos de troyanos relacionados con los correos electrónicos pueden ser:

- Mailfinders: Este troyano está diseñado para recopilar direcciones de correos electrónicos desde un dispositivo y luego enviarlos a los atacantes a través de un correo, un servidor FTP u otros medios. Una vez el atacante consigue todos estos correos electrónicos, los utiliza para realizar spam de todo tipo de correos.

- Emotet: Es un troyano que a menudo se distribuye a través de correos electrónicos de phishing. Funciona de tal manera que, si hay una red conectada, se propaga utilizando una lista de contraseñas comunes y averigua el camino hacia otros sistemas conectados en un ataque de fuerza bruta.

- Dridex: Es un troyano bancario que ha sido conocido por propagarse a través de correos electrónicos de phishing. Los correos electrónicos contienen documentos maliciosos de Microsoft Word o Excel que, cuando se abren, descargan y ejecutan el malware.

- TrickBot: Es un conocido troyano bancario que se utiliza principalmente para robar información financiera y realizar actividades maliciosas en los dispositivos infectados.

#### - Gusanos:
Son un tipo de malware que tienen la peculiaridad de replicarse para propagarse a otras dispositivos. Utiliza la red para propagarse, aprovechando las fallas de seguridad en el dispositivo de destino para acceder a él.
<br>
Un ejemplo muy común es el del gusano ILOVEYOU que se propagó a través de un correo electrónico con un asunto que decía "ILOVEYOU". Este afectó a millones de dispositivos en todo el mundo en el año 2000. Una vez abierto, el virus se replicaba y se enviaba a todos los contactos en la libreta de direcciones de la víctima.

#### - Backdoors (Puertas traseras): 
Este tipo de malware permite al atacante tener control remoto total en el dispositivo infectado. 
El atacante puede hacer lo que quiera en el dispositivo, como, por ejemplo, enviar y recibir archivos, ejecutar archivos, mostrar mensajes, borrar datos, reiniciar el equipo, etc...
  
#### - Rootkits: 
Este de malware es diseñado para no ser detectado por los sistemas operativos y los antivirus/ antimalwares y trabajar en segundo plano. Con este tipo de malware consiguen tener acceso al dispositivo durante un periodo más largo.

#### - Keyloggers: 
Es un tipo de malware que se ejecuta en nuestro dispositivo en segundo plano y que permite registrar todas las pulsaciones de teclas que se realicen en este.

#### - Ransomware: 

Es un tipo de malware que impide a los usuarios acceder a su sistema o a sus archivos personales y que exige el pago de un rescate para poder acceder de nuevo a ellos.

Es muy común que los atacantes o ciberdelincuentes utilicen ataques como el phishing o el spam para incluir este malware en el contenido del correo electrónico de alguna forma.

### 6. Apropiación de cuentas de correo electrónico

La apropiación de cuentas de correos electrónicos es una práctica muy común entre los ciberdelincuentes. 
Los atacantes se apropian de los correos electrónicos de los usuarios reales con la intención de realizar actividades como controlar sus mensajes, robar información, enviar malware a otras cuentas, realizar spam.

Existen muchas técnicas que usan los atacante para apropiarse de las cuentas:

- Phishing: Podrían engañar a al usuario redirigiéndolos a sitios web falsos donde tienen que ingresar sus credenciales.

- Fuerza bruta: Consiste en ir probando diferentes combinaciones de contraseñas hasta que encuentran la correcta. Puede ser lento y requiere paciencia, pero puede ser efectivo si la contraseña es débil.

- Ataque de diccionario: Los atacantes utilizan herramientas que prueban una lista de contraseñas comunes y palabras para adivinar la contraseña de la cuenta.

- Reutilización de contraseñas: Es muy común que los usuarios utilicen la misma contraseña para varios servicios o páginas web por lo que si alguno de estos servicios sufre una brecha de seguridad en la que se filtran credenciales los atacantes podrían comprobar esas mismas credenciales en otros servicios o páginas web.

- Ingeniería social: Consiste en manipular a la víctima para que revele sus credenciales de correo electrónico. Por ejemplo, haciéndose pasar por alguien de confianza, por alguien de alguna empresa y utilizar excusas o justificaciones para obtener la información.

- Malware: El malware infecta el dispositivo de la víctima por lo que se podría utilizar por ejemplo un keylogger para obtener las credenciales. Otro ejemplo seria usar malware capaz de robar las cookies de inicio de sesión o tokens de acceso.

- Recuperación de contraseñas débiles: Si la opción de recuperación de contraseña se basa en información personal que es fácil de obtener (como una pregunta de seguridad que se puede responder buscando en las redes sociales), los atacantes pueden restablecer la contraseña de la cuenta.

- Explotación de vulnerabilidades: El atacante podría aprovechar vulnerabilidades en los protocolos del servidor de correo para acceder a las cuentas de los usuarios.

### 7. Interceptación de correos electrónicos

La interceptación de correos electrónicos es una actividad que implica que el atacante pueda leer o incluso modificar los correos electrónicos que se envían desde una persona a otra, situándose en medio de la comunicación (man-in-the-middle). 
Los atacantes interceptan los mensajes para robar la información que contienen, o para llevar a cabo ataques en los que se hacen pasar por ambas partes de una conversación.
El método más común para hacerlo es la monitorización de los paquetes de datos de la red en las redes de área local, ya que interceptar un correo electrónico mientras viaja por Internet es muy complicado.

### 8. E-mail Bombing

El ataque de bombardeo de correos electrónicos consiste en enviar grandes volúmenes de correos electrónicos a una dirección en específico con la intención de desbordar el buzón y saturar el servidor de correos donde está alojado. Su función es la misma que un ataque de denegación de servicio (ataque DoS) pero en este caso contra las cuentas de correos.
Estos mensajes se almacenan en el servidor hasta que el dueño de dicha cuenta de correo los lea. Cuando el dueño abra su correo, el último mensaje tardará demasiado tiempo en abrirse y la dirección de correo electrónico quedará inservible. También una cosa a tener en cuenta es que en ocasiones el e-mail bombing se utiliza para intentar distraer a los usuarios, a las empresas y organizaciones, y de esta forma pasar por alto otros correos importantes que puedan recibir.


## 2. Tipos de auditoría ofensiva

### Auditoria de correos electrónicos

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

## 3. Metodología

### Justificación de la Elección:

Elección: OWASP

Tras investigar todas las metodologías posibles me he encontrado con el inconveniente de que no existe una metodología especifica o perfecta para este área de correos electrónicos por lo que me he decantado por la metodología de OWASP ya que me parece que comparten muchos campos en común como pruebas de configuración, análisis de vulnerabilidades, pruebas de autenticación, pruebas de autorización y pruebas de servicios web y además proporciona un enfoque completo y sistemático para el análisis y las pruebas de penetración que ofrezco en los servicios de mi auditoria. También es flexible y se puede adaptar a necesidades específicas de nuestra empresa o de nuestros clientes.

### Fases de la metodología OWASP

La metodología de OWASP tiene muchas variantes en cuanto al número sus fases por lo que me centraré en describir las 4 fases que yo considero más importantes para nuestra empresa: 

- 1. Reconocimiento: En esta fase recolectamos toda la información posible sobre el sistema de correo electrónico de la empresa, sus políticas de seguridad, configuraciones, protocolos, versiones, etc...

- 2. Análisis de vulnerabilidades: En esta fase analizamos toda la información obtenida en la fase anterior y buscamos y listamos todas las posibles vulnerabilidades que podemos explotar. 
Por ejemplo, también podemos buscar CVE's conocidas de algunos protocolos que se estén utilizando.

- 3. Explotación: En esta fase nos dedicaremos a explotar todas las vulnerabilidades posibles listadas en la fase anterior para comprometer el sistema de correos y comprobar los puntos débiles de este.

- 4. Informes: En esta fase se generará un informe que resuma los hallazgos de la auditoría y las recomendaciones para mejorar la seguridad del sistema de correo electrónico.


## Herramientas de monitorización

...

## Bibliografía

https://www.skysnag.com/es/blog/example-of-email-based-attacks/#8_Denial-of-service_DoS_attacks
https://www.globalsign.com/es/blog/tipos-comuns-ataques-de-phishing
https://www.checkpoint.com/es/cyber-hub/threat-prevention/what-is-email-security/
https://noticias.aixacorpore.es/iso-27001/ataques-por-medio-del-correo-electronico-email-spoofing/
https://keepcoding.io/blog/tipos-de-amenazas-a-correos-electronicos/
https://www.acronis.com/es-es/blog/posts/email-cyber-attack/
https://powerdmarc.com/es/what-are-email-based-attacks/
https://www.skysnag.com/es/blog/example-of-email-based-attacks/#1_Phishing
https://www.incibe.es/ciudadania/blog/que-es-el-phishing
https://latam.kaspersky.com/resource-center/definitions/what-is-a-whaling-attack
https://support.microsoft.com/es-es/office/suplantaci%C3%B3n-de-identidad-phishing-y-comportamiento-sospechoso-0d882ea5-eedc-4bed-aebc-079ffa1105a3
https://www.ing.es/seguridad-internet/vishing-que-es#:~:text=Llamada%20de%20alguien%20que%20se,tarjeta%20u%20otra%20incidencia%20grave.
https://www.trendmicro.com/es_es/what-is/phishing/types-of-phishing.html
https://www.uach.cl/direccion-de-tecnologias-de-informacion/seguridad/tipos-de-phishing
https://latam.kaspersky.com/resource-center/definitions/pharming
https://latam.kaspersky.com/resource-center/definitions/what-is-a-whaling-attack
https://www.pandasecurity.com/es/mediacenter/seguridad/whaling/
https://easydmarc.com/blog/es/12-tipos-de-ataques-phishing-y-como-identificarlos/
https://www.welivesecurity.com/la-es/2015/04/17/que-es-un-backdoor/
https://encyclopedia.kaspersky.es/knowledge/backdoor/
https://www.cyberghostvpn.com/es_ES/privacyhub/que-es-una-puerta-trasera-backdoor/
https://www.kaspersky.es/blog/que-es-un-rootkit/594/
https://latam.kaspersky.com/resource-center/definitions/what-is-rootkit
https://es.wikipedia.org/wiki/Rootkit
https://www.avast.com/es-es/c-keylogger
https://latam.kaspersky.com/resource-center/definitions/keylogger
https://encyclopedia.kaspersky.es/knowledge/trojan-mailfinder/
https://www.ninjaone.com/es/blog/como-prevenir-los-ataques-de-spoofing/
https://powerdmarc.com/es/what-are-email-based-attacks/
https://noticias.aixacorpore.es/iso-27001/ataques-por-medio-del-correo-electronico-email-spoofing/
https://easydmarc.com/blog/es/que-son-los-correos-spam-y-como-podemos-prevenirlos/
https://www.eset.com/es/caracteristicas/spam/
https://www.strato.es/faq/correo/que-es-spam-y-como-puedo-protegerme/
https://www.mailjet.com/es/blog/entregabilidad/que-es-spam/
https://www.avast.com/es-es/c-spam
https://www.proofpoint.com/es/threat-reference/email-scams
https://medac.es/blogs/masteres-online/que-es-scam
https://es.wikipedia.org/wiki/Scam
https://www.pandasecurity.com/es/security-info/scam/
https://www.uv.mx/infosegura/general/noti_scam-3/
https://uniblog.unicajabanco.es/-que-es-el-scam-
https://www.cloudflare.com/es-es/learning/email-security/what-is-email-security/
https://es.linkedin.com/pulse/descifrando-las-t%C3%A1cticas-y-los-impactos-del-fraude-de-paola-noriega
https://dynamics.microsoft.com/es-es/ai/fraud-protection/account-takeover/
https://www.skrill.com/es/skrill-news/inside-skrill/prevencion-del-fraude-de-apropiacion-de-cuentas/
https://www.cloudflare.com/es-es/learning/insights-bec-proactive-security/
https://easydmarc.com/blog/es/como-hacen-los-estafadores-de-phishing-para-obtener-tu-direccion-de-correo-electronico/
https://peritosinformaticos.es/fraude-por-cambio-de-numero-de-cuenta-bancaria-en-correos-electronicos/#:~:text=La%20t%C3%A9cnica%20de%20intercepci%C3%B3n%20de,est%C3%A1n%20cruzando%20conversaciones%20por%20email.
https://foro.elhacker.net/hacking/se_pueden_interceptar_correos_electronicos-t517901.0.html;msg2270313
https://es.ccm.net/aplicaciones-e-internet/museo-de-internet/enciclopedia/10566-que-es-el-email-bombing/
https://medium.com/@edinsonrequena/tutorial-qu%C3%A9-es-un-email-bomb-attack-y-como-crearlo-con-python-3-c566d688944a
https://zonavirus.com/noticias/2021/e-mail-bombing-como-usan-el-spam-para-atacar_71650
https://es.wikipedia.org/wiki/Gusano_inform%C3%A1tico
https://www.pandasecurity.com/es/security-info/worm/
https://www.kaspersky.es/resource-center/threats/ransomware-wannacry
https://es.malwarebytes.com/ransomware/
https://es.wikipedia.org/wiki/Ransomware
https://www.fortra.com/es/blog/pentesting-herramientas-tecnicas
https://www.disruptivos.com/auditoria-email-mejorar-resultados/
https://blog.mailup.es/2021/02/email-auditorias/
https://www.acronis.com/es-es/blog/posts/cyber-security-audit/
https://secuora.es/blog/auditoria-de-ciberseguridad-red-team-conoce-por-que-necesitas-realizarla/
https://www.hiberus.com/crecemos-contigo/pentesting-owasp-fases-metodologia/
https://www.reydes.com/d/?q=Metodologia_de_Pruebas_OWASP
https://www.arsys.es/blog/owasp#:~:text=6%20Conclusiones-,%C2%BFQu%C3%A9%20es%20OWASP%3F,las%20mejores%20pr%C3%A1cticas%20de%20seguridad.
