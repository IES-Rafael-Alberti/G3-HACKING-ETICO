# Índice

# Resumen Ejecutivo

# Tabla de Riesgos

# Test de penetración

## Vulnerabilidades Windows Server 2008 R2 Standard

| Descripción de la vulnerabilidad |El servidor SMBv1 en Microsoft Windows Vista SP2; Windows Server 2008 SP2 y R2 SP1; Windows 7 SP1; Windows 8.1; Windows Server 2012 Gold y R2; Windows RT 8.1 y Windows 10 Gold, 1511 y 1607 y Windows Server 2016 permite a atacantes remotos ejecutar código arbitrario a través de paquetes manipulados, vulnerabilidad también conocida como "Windows SMB Remote Code Execution Vulnerability"|
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |              [CVE-2017-0143](https://nvd.nist.gov/vuln/detail/cve-2017-0143)                                                |
| CVSS v3                          |                    [8.1](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2017-0143&vector=AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H&version=3.0&source=NIST)                                          |
| Severidad                        |                    Alta                                          |
| Impacto                          | Si un atacante consigue acceder a la máquina usando esta vulnerabilidad, puede obtener acceso de manera remota a la máquina y por lo tanto podría leer, modificar, crear o borrar información importante, escalar privilegios, hacer landing a otras máquinas de la red y obtener persistencia.   |
| Sistemas afectados               |                     Windows server 2008 R2 Standard                                   |
| Prueba de concepto (POC)        |        ![eternalguillermo](./img/eternalguillermo.png)                                                      |
| Remediación                      |   Actualizar el Sistema Operativo a una versión más reciente ya que se ha parcheado esta vulnerabilidad.                                                     |
| Link de referencia               |       [https://attack.mitre.org/techniques/T1210/](https://attack.mitre.org/techniques/T1210/)                                                       |

<br>
<br>

## Vulnerabilidades Windows Server Metasploitable 3

| Descripción de la vulnerabilidad |El servidor SMBv1 en Microsoft Windows Vista SP2; Windows Server 2008 SP2 y R2 SP1; Windows 7 SP1; Windows 8.1; Windows Server 2012 Gold y R2; Windows RT 8.1 y Windows 10 Gold, 1511 y 1607 y Windows Server 2016 permite a atacantes remotos ejecutar código arbitrario a través de paquetes manipulados, vulnerabilidad también conocida como "Windows SMB Remote Code Execution Vulnerability"|
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |              [CVE-2017-0143](https://nvd.nist.gov/vuln/detail/cve-2017-0143)                                                |
| CVSS v3                          |                    [8.1](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2017-0143&vector=AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H&version=3.0&source=NIST)                                          |
| Severidad                        |                    Alta                                          |
| Impacto                          | Si un atacante consigue acceder a la máquina usando esta vulnerabilidad, puede obtener acceso de manera remota a la máquina y por lo tanto podría leer, modificar, crear o borrar información importante, escalar privilegios, hacer landing a otras máquinas de la red y obtener persistencia.   |
| Sistemas afectados               |                     Windows Server Metasploitable 3                                        |
| Prueba de concepto (POC)        |        ![eternalguillermo](./img/eternalblueme3w.png)                                                      |
| Remediación                      |   Actualizar el Sistema Operativo a una versión más reciente ya que se ha parcheado esta vulnerabilidad.                                                     |
| Link de referencia               |       [https://attack.mitre.org/techniques/T1210/](https://attack.mitre.org/techniques/T1210/) |

<br>
<br>

| Descripción de la vulnerabilidad |                                                El servicio de protocolo de escritorio remoto (RDP) en Microsoft Windows Server 2008 R2 Service Pack 1 y R2 y Windows 7 Gold y SP1 permite a atacantes remotos causar una denegación de servicio (la aplicación se bloquea) a través de una serie de paquetes modificados, también conocido como "Terminal Server Denial of Service Vulnerability."              |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |                                                    [CVE-2012-0152](https://nvd.nist.gov/vuln/detail/CVE-2012-0152)         |
| CVSS v3                          |                                            [7.5](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H&version=3.0)                  |
| Severidad                        |                                      Alta                        |
| Impacto                          |                                  Un atacante puede realizar un ataque de denegación de servicio y bloquear la máquina                           |
| Sistemas afectados               |                                           Windows Server Metasploitable 3                |
| Prueba de concepto (POC)        |                                                      ![ms12-020](./img/ms12-020.png)        |
| Remediación                      |                                  Instalar las actualizaciones de seguridad más recientes o desactivar el acceso remoto a la máquina a través de RDP.                            |
| Link de referencia               |                                              [https://attack.mitre.org/techniques/T1498/](https://attack.mitre.org/techniques/T1498/)                |

<br>
<br>

| Descripción de la vulnerabilidad |                                              Un atacante remoto no autenticado podría aprovechar esta vulnerabilidad para leer archivos de aplicaciones web desde un servidor vulnerable. En los casos en que el servidor vulnerable permite la carga de archivos, un atacante podría cargar código JavaServer Pages (JSP) malicioso dentro de una variedad de tipos de archivos y activar esta vulnerabilidad para obtener la ejecución remota de código.        |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |                                   [CVE-2020-1745](https://nvd.nist.gov/vuln/detail/CVE-2020-1745)     |
| CVSS v3                          |                                       [9.8](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2020-1745&vector=AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H&version=3.1&source=NIST)                       |
| Severidad                        |                                  Alta                            |
| Impacto                          |                               Un atacante puede leer cualquier archivo de la aplicación web pudiendo acceder a información importante.                         |
| Sistemas afectados               |                                         Windows Server Metasploitable 3                    |
| Prueba de concepto (POC)        |                                                       ![ajptomcat](./img/ajptomcat.png)       |
| Remediación                      |                               Deshabilitar AJP y usar en su lugar HTTP o HTTPS                               |
| Link de referencia               |                                          [https://attack.mitre.org/techniques/T1659/](https://attack.mitre.org/techniques/T1659/)                    |

<br>
<br>

| Descripción de la vulnerabilidad |                                                 La lista de usuarios LanMan del host remoto se puede obtener mediante SNMP.|
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |                                      [CVE-1999-0499](https://nvd.nist.gov/vuln/detail/CVE-1999-0499)                        |
| CVSS v3                          |                                      [5.3](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator)                        |
| Severidad                        |                                   Medio                           |
| Impacto                          |                                      Un atacante podría tener acceso a una lista de usuarios dentro del protocolo SNMP.                        |
| Sistemas afectados               |                                           Windows Server Metasploitable 3                   |
| Prueba de concepto (POC)        |                                                     ![snmpuser](./img/snmpuser.png)         |
| Remediación                      |                                  Desactivar el protocolo si no se utiliza                            |
| Link de referencia               |                                           [https://attack.mitre.org/techniques/T1087/](https://attack.mitre.org/techniques/T1087/)                   |

<br>
<br>

| Descripción de la vulnerabilidad |                                                 La lista de servicios LanMan que se ejecutan en el host remoto se puede obtener mediante SNMP. |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |                                   [CVE-1999-0499](https://nvd.nist.gov/vuln/detail/CVE-1999-0499)                             |
| CVSS v3                          |                                     [5.3](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L&version=3.0)                         |
| Severidad                        |                                       Medio                       |
| Impacto                          |                                  Un atacante podría ver los servicios de red que se están usando en el sistema a través de SNMP para posible explotación de los mismos.                            |
| Sistemas afectados               |                                        Windows Server Metasploitable 3                      |
| Prueba de concepto (POC)        |                                                    ![networksnmp](./img/networksnmp.png)          |
| Remediación                      |                                   Desactivar el protocolo si no se utiliza  |
| Link de referencia               |                                        [https://attack.mitre.org/techniques/T1046/](https://attack.mitre.org/techniques/T1046/)                      |

<br>
<br>

| Descripción de la vulnerabilidad |                                                  OpenSSH hasta la versión 7.7 es propenso a una vulnerabilidad de enumeración de usuarios debido a que no retrasa el rescate de un usuario de autenticación no válido hasta que el paquete que contiene la petición haya sido analizado completamente. Esto está relacionado con auth2-gss.c, auth2-hostbased.c, y auth2-pubkey.c.            |
|----------------------------------|--------------------------------------------------------------|
| CVE/CWE                          |                                     [CVE-2018-15473](https://nvd.nist.gov/vuln/detail/cve-2018-15473)                         |
| CVSS v3                          |                                     [5.3](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?name=CVE-2018-15473&vector=AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N&version=3.1&source=NIST)                         |
| Severidad                        |                                      Medio                        |
| Impacto                          |                                Un atacante podría ver los usuarios que tiene el sistema para luego ejecutarle fuerza bruta.                              |
| Sistemas afectados               |                                           Windows Server Metasploitable 3                   |
| Prueba de concepto (POC)        |                ![sshuser](./img/sshuser.png)                                              |
| Remediación                      |                          Actualizar OpenSSH a una versión más moderna.                                    |
| Link de referencia               |       [https://attack.mitre.org/techniques/T1087/](https://attack.mitre.org/techniques/T1087/)|

# Metodologías

## Herramientas

# Conclusión