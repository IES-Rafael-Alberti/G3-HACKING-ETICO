---
marp: true
theme: default
_class: lead
paginate: true
backgroundColor: #fff
color: white
backgroundImage: url('https://fcit.usf.edu/matrix/wp-content/uploads/2019/03/CircuitBoard-K-Wide.jpg')
---

![bg left:30% 50%](./img/imago-iesra-1.png)

# Hacking ético

# **Proyecto 1 - Hack-Proof Inc.**
## Grupo 3

Raúl Ladrón de Guevara López
Juan Manuel cumbrera
Christian Romero Oliva

---

# **Introducción**

## Objetivos de la presentación

- Exploración de vulnerabilidades en nuestro tema seleccionado que es Sistemas Operativos.
- Comprender en qué consisten y como pueden explotarse.
- Aumentar la conciencia sobre la importancia de medidas preventivas para garantizar un entorno digital seguro.


---

# **CVE-2016-2414 - Minikin Android**

- Vulnerabilidad en *Minikin*, que es componente de Android encargado de renderizar las fuentes en la interfaz gráfica. 
- Minikin tenía un error en su implementación que provocaba un error donde se intentaba escribir datos en bucle (con la tabla cmap) en una dirección de memoria inválida, lo que desemboca en una denegación de servicio (DoS)

---

## ¿Como podríamos explotarla?
Un archivo .TTF malicioso que modifique la tabla cmap 

---

# **CVE-2023-41995 - Desbordamiento de búfer en el kernel de Linux**
- La vulnerabilidad se encuentra en el subsistema de mensajería del kernel, el cual se utiliza para procesar los mensajes enviados entre los procesos. 
- Se produce porque el kernel de Linux no libera correctamente la memoria después de que se haya utilizado, lo cual implica que un posible atacante pueda proporcionar un mensaje malicioso que el kernel procesará incorrectamente, provocando un desbordamiento de búfer.
- Afecta a las versiones de iOS y iPadOS anteriores a la 17 y a las versiones de macOS anteriores a la 14.

---

## **¿Cómo podriamos explotarla?**

- Para explotar y hacer uso de esta vulnerabilidad, un atacante debe enviar un mensaje malicioso al subsistema de mensajería del kernel de Linux. Dicho mensaje debe ser lo suficientemente grande como para provocar un desbordamiento de búfer.

## **¿Qué impacto tendría?**

- **Confidencialidad:** El atacante podría acceder a datos confidenciales, como contraseñas, información financiera o datos personales.
- **Integridad:** El atacante podría modificar o destruir datos.
- **Disponibilidad:** El atacante podría interrumpir los servicios o sistemas.

---

## **¿Cómo se podría evitar?**

- **Actualizar el kernel a la última versión.** Las últimas versiones del kernel de Linux corrigen la vulnerabilidad.
- **Instalar un firewall.** Esto permitiría bloquear el tráfico entrante no autorizado.
- **Mantener los sistemas actualizados con las últimas actualizaciones de seguridad.**
- **Mantener actualizado el antivirus.**

---

# **CVE-2023-39191 - Kernel de Linux eBPF**


- Esta vulnerabilidad se produce debido a una falta de validación de entrada en el subsistema _eBPF_. 

- _eBPF_ se puede utilizar para una variedad de propósitos, como la supervisión del rendimiento, el filtrado de tráfico y la creación de reglas de firewall.

- Significa que un atacante puede proporcionar datos maliciosos a un programa eBPF que el kernel ejecutará sin verificar.

---

## **¿Cómo podriamos explotarla?**

- Para explotar esta vulnerabilidad, un atacante debe tener privilegios _CAP_BPF_. (Cargar y moficar programas BPF en el kernel)
- Una vez que el atacante tenga dichos privilegios, podrá proporcionar datos maliciosos a un programa eBPF, los cuales serán ejecutados por el kernel.

## **¿Qué impacto tendría?**

- **Confidencialidad:** El atacante podría acceder a datos confidenciales, como contraseñas, información financiera o datos personales.
- **Integridad:** El atacante podría modificar o destruir datos.
- **Disponibilidad:** El atacante podría interrumpir los servicios o sistemas.

---

## **¿Cómo se podría evitar?**

- **Actualizar los sistemas a la última versión del kernel de Linux.** Esta versión corrige la vulnerabilidad CVE-2023-39191.
- **Limitar el acceso a los privilegios CAP_BPF.** Solo los usuarios autorizados deben tener estos privilegios.
- **Implementar controles de acceso para proteger los programas eBPF.** Estos controles pueden ayudar a evitar que los atacantes proporcionen datos maliciosos a los programas eBPF.
- **Monitorear los sistemas en busca de signos de explotación de esta vulnerabilidad.** Los administradores de sistemas deben estar atentos a los signos de actividad maliciosa, como intentos de ejecutar código arbitrario en el contexto del kernel.

---

# **CVE-2023-44466 - Desbordamiento de búfer**

- Es una vulnerabilidad de desbordamiento de búfer en el módulo de mensajería del kernel de Linux.

- Esto tiene su origen en el sistema de ficheros _Ceph_, ya que el módulo de mensajería es utilizado por Ceph para recibir paquetes TCP de una dirección IP. 

- Antes de que se complete cualquier autorización, cualquier dispositivo con esa dirección IP puede enviar un paquete que produzca desbordamiento de búfer en el kernel.

---

## **¿Cómo podriamos explotarla?**

- Para explotar esta vulnerabilidad, un atacante debe tener acceso al sistema vulnerable. 
- Una vez que este haya conseguido acceso al sistema, podrá enviar un mensaje malicioso al subsistema de mensajería del kernel de Linux, el cual lo procesará de forma incorrecta, produciendo así un desbordamiento del búfer. Esto podría permitir al atacante ejecutar código arbitrario en el contexto del kernel.

---

## **¿Qué impacto tendría?**

- **Confidencialidad:** El atacante podría acceder a datos confidenciales, como contraseñas, información financiera o datos personales.
- **Integridad:** El atacante podría modificar o destruir datos.
- **Disponibilidad:** El atacante podría interrumpir los servicios o sistemas (_DoS_).

---

## **¿Cómo se podría evitar?**

- **Actualizar los sistemas a la última versión del kernel de Linux.** Esta versión corrige la vulnerabilidad CVE-2023-44466.
- **Limitar el acceso al subsistema de mensajería del kernel de Linux.** Solo los usuarios autorizados deben tener acceso a este subsistema.
- **Monitorear los sistemas en busca de signos de explotación de esta vulnerabilidad.** Los administradores de sistemas deben estar atentos a los signos de actividad maliciosa, como intentos de enviar mensajes maliciosos al subsistema de mensajería del kernel de Linux.

---

# **CVE-2020-7384 - MSFVENOM**

- El framework msfvenom de Metaexploit permite a un usuario malintencionado crear y publicar APK's que permiten la ejecución de comandos controlados por el atacante en el dispositivo android donde se ha instalado.

- Esta vulnerabilidad afecta a cualquier versión android.

---

## **¿Cómo podriamos explotarla?**

Para explotar esta vulnerabilidad lo unico que necesitariamos es una máquina con kali linux para crear el apk que contendrá una reverse shell hacia nuestra máquina, de esta manera cuando se instale en un dispositivo, tendremos control total sobre ese dispositivo.

---

## **¿Qué impacto tendría?**

- Disponibilidad: El atacante podría controlar el dispositivo por lo que podría borrar datos, bloquear el acceso, etc...
- Integridad: El atacante podría modificar o eliminar datos lo que podria dañar el dispositivo o la información que contiene.
- Confidencialidad: El atacante podría robar datos como contraseñas, fotos, datos bancarios, etc... lo que comprometeria la privacidad y los datos podrian ser utilizados para cometer fraude o robar su identidad.

---

## **¿Cómo se podría evitar?**

-No descargar nunca apk's desconocidas que suelen ofrecernos servicios de pago de forma gratuita ya que estas suelen tener malware.

-Actualizar siempre el móvil a la última versión disponible.

-Tener instalado siempre un antivirus/antimalware en el dispositivo.

---

# **Conclusión:**

- Enfatiza la importancia de entender componentes de sistemas a bajo nivel para una ciberseguridad efectiva.
- Destaca la importancia de mantener sistemas actualizados para prevenir vulnerabilidades.
- Fomenta el uso de medidas de seguridad como firewalls, antivirus y sistemas de detección de intrusiones.

---

# **Recomendaciones:**

- Utilizar antivirus/antimalware y escáneres de vulnerabilidades.
- Implementar firewalls y cambiar puertos de servicios.
- Mantener sistemas actualizados y monitorear signos de actividad maliciosa.
- Fomentar una cultura de conciencia en ciberseguridad para minimizar riesgos.

---

# **Referencias:**

- [NIST](https://nvd.nist.gov/vuln) y [ExploitDB](https://www.exploit-db.com/): Recursos valiosos para información de vulnerabilidades.
- [Marp](https://marp.app/): Una herramienta útil para crear presentaciones basadas en markdown.

---
