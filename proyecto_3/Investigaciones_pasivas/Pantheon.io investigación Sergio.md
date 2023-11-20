## Pantheon

**Ubicación:** 717 California St. San Francisco, California 94108, US

- Linkedin account: https://www.linkedin.com/company/getpantheon?trk=public_profile_topcard-current-company

**E-mail extensión:** @pantheon.io

### Dominios anteriores a 2023:

- pantheonsite.io
- pantheon.io

Ambos dominios estaban a nombre de David Timothy Strauss

### Whois y NSLOOKUP

**Name Servers:**

Sacados con el comando whois y con nslookup buscado la dirección IP de los DNS encontrados.

Name Server: NS-148.AWSDNS-18.COM </br>
```

Respuesta no autoritativa:
Nombre:  NS-148.AWSDNS-18.COM
Addresses:  2600:9000:5300:9400::1
            205.251.192.148

AWSDNS-18.COM
        primary name server = g-ns-594.AWSDNS-18.COM
        responsible mail addr = awsdns-hostmaster.amazon.COM
        serial  = 1
        refresh = 7200 (2 hours)
        retry   = 900 (15 mins)
        expire  = 1209600 (14 days)
        default TTL = 86400 (1 day)
```
Name Server: NS-1096.AWSDNS-09.ORG </br>
```
Respuesta no autoritativa:
Nombre:  NS-1096.AWSDNS-09.ORG
Addresses:  2600:9000:5304:4800::1
            205.251.196.72

AWSDNS-09.ORG
        primary name server = g-ns-715.AWSDNS-09.ORG
        responsible mail addr = awsdns-hostmaster.amazon.com
        serial  = 1
        refresh = 7200 (2 hours)
        retry   = 900 (15 mins)
        expire  = 1209600 (14 days)
        default TTL = 86400 (1 day)
```
Name Server: NS-1857.AWSDNS-40.CO.UK </br>
```
Respuesta no autoritativa:
Nombre:  NS-1857.AWSDNS-40.CO.UK
Addresses:  2600:9000:5307:4100::1
            205.251.199.65

 AWSDNS-40.CO.UK
        primary name server = g-ns-360.AWSDNS-40.CO.UK
        responsible mail addr = awsdns-hostmaster.amazon.com
        serial  = 1
        refresh = 7200 (2 hours)
        retry   = 900 (15 mins)
        expire  = 1209600 (14 days)
        default TTL = 86400 (1 day)
```
Name Server: NS-924.AWSDNS-51.NET </br>
```
Respuesta no autoritativa:
Nombre:  NS-924.AWSDNS-51.NET
Addresses:  2600:9000:5303:9c00::1
            205.251.195.156

AWSDNS-51.NET
        primary name server = g-ns-1395.AWSDNS-51.NET
        responsible mail addr = awsdns-hostmaster.amazon.com
        serial  = 1
        refresh = 7200 (2 hours)
        retry   = 900 (15 mins)
        expire  = 1209600 (14 days)
        default TTL = 86400 (1 day)
```

### dnsrecon

He ejecutado dnsrecon en una máquina kali para comparar los registros dados también para pantheon.io.

```
dnsrecon -d pantheon.io
[*] std: Performing General Enumeration against: pantheon.io...
[-] DNSSEC is not configured for pantheon.io
[*]      SOA ns-148.awsdns-18.com 205.251.192.148
[*]      SOA ns-148.awsdns-18.com 2600:9000:5300:9400::1
[*]      NS ns-1096.awsdns-09.org 205.251.196.72
[*]      NS ns-1096.awsdns-09.org 2600:9000:5304:4800::1
[*]      NS ns-148.awsdns-18.com 205.251.192.148
[*]      NS ns-148.awsdns-18.com 2600:9000:5300:9400::1
[*]      NS ns-1857.awsdns-40.co.uk 205.251.199.65
[*]      NS ns-1857.awsdns-40.co.uk 2600:9000:5307:4100::1
[*]      NS ns-924.awsdns-51.net 205.251.195.156
[*]      NS ns-924.awsdns-51.net 2600:9000:5303:9c00::1
[*]      MX aspmx.l.google.com 74.125.206.26
[*]      MX aspmx2.googlemail.com 142.250.153.26
[*]      MX aspmx3.googlemail.com 142.251.9.27
[*]      MX alt1.aspmx.l.google.com 142.250.153.26
[*]      MX alt2.aspmx.l.google.com 142.251.9.26
[*]      MX aspmx.l.google.com 2a00:1450:400c:c02::1b
[*]      MX aspmx2.googlemail.com 2a00:1450:4013:c16::1b
[*]      MX aspmx3.googlemail.com 2a00:1450:4025:c03::1b
[*]      MX alt1.aspmx.l.google.com 2a00:1450:4013:c16::1b
[*]      MX alt2.aspmx.l.google.com 2a00:1450:4025:c03::1a
[*]      A pantheon.io 23.185.0.253
[*]      AAAA pantheon.io 2620:12a:8000::253
[*]      AAAA pantheon.io 2620:12a:8001::253
[*]      TXT pantheon.io docusign=a75f7cdb-a22b-45a7-b456-635e1eb0b35e
[*]      TXT pantheon.io fastly-domain-delegation-g6VtYXKROXetTkEvfvtE-446542-20211112
[*]      TXT pantheon.io globalsign-domain-verification=zfCNvJt0iTcEchLrE0nrimsdl4h4m4zVTSJYOcrlcJ
[*]      TXT pantheon.io google-site-verification=YfoV70Zhm06tcjmrL3KMIviav8qq-I3cWY0jr0BvHsQ
[*]      TXT pantheon.io miro-verification=a22d018251f307c6f5e6e8f566e664cdf3d45d9a
[*]      TXT pantheon.io pendo-domain-verification=4de1218d-d75a-4363-9055-86bb06097a05
[*]      TXT pantheon.io segment-site-verification=ldXBuNyiLmz2S3qxkLwcrDBESLFWZ0aX
[*]      TXT pantheon.io status-page-domain-verification=5p5f33w3857z
[*]      TXT pantheon.io v=spf1 include:_u.pantheon.io._spf.smart.ondmarc.com ~all
[*]      TXT pantheon.io adobe-idp-site-verification=08da2afbd8a0dba4c7ebe96281c1662469681b1060ede2b079c25b4460601c25
[*]      TXT pantheon.io amazonses:RlvLmxzcHOsiBlOKC3l3WHjCh6g9X8x8JcAFdMlW9BI=
[*]      TXT pantheon.io asv=6522b472ea8016fba67687ca648b4f19
[*]      TXT pantheon.io atlassian-domain-verification=MPUQoKJCCFX7kRgKt7jqKlvQp+rF+4coyVIkxbw5CF1PZ24laDjMzXfgAY2VZMm8
[*]      TXT pantheon.io docker-verification=df12737e-922c-4a2e-ac9b-0c5a97da58c5
[*]      TXT _dmarc.pantheon.io v=DMARC1; p=none; pct=100; sp=none; rua=mailto:3523e61d@inbox.ondmarc.com; ruf=mailto:3523e61d@inbox.ondmarc.com; adkim=r; aspf=r; fo=1; rf=afrf; ri=86400
[*] Enumerating SRV Records
[-] No SRV Records Found for pantheon.io
```
---

## Empleados

Esta información ha sido encontrada usando linkdin, clearbit connect para encontrar los correos de pantheon.io.

### Información CEO/co-fundador

**Nombre:** Zachary Rosen </br>
**Localización:** San Francisco, California, Estados Unidos

- **Web personal:** https://about.me/zack
- **Twiter:** https://twitter.com/zack

**Educación:** University of Illinois Urbana-Champaign

**E-Mail Empresarial:** zack@pantheon.io

---

### Información CTO/Co-fundador

**Nombre:** David Timothy Strauss </br>
**Localización:** San Francisco, California, Estados Unidos

- Linkedin account: https://www.linkedin.com/in/davidstrauss
- Cuenta de twitter: https://twitter.com/davidstrauss

**Educación:** The University of Texas Austin

**E-Mail Empresarial:** david@pantheon.io

---

### Información Co-fundador y director de estrategia

**Nombre:** Josh Koenig </br>
**Localización:** San Francisco, California, Estados Unidos

- Linkedin account: https://www.linkedin.com/in/joshkoenig
- Blog: https://www.outlandishjosh.com/
- Twitter: https://twitter.com/outlandishjosh

**Educación:** New York University

**E-Mail Empresarial:** josh@pantheon.io

---

### Senior Director, Ventas Estrategia y operaciones

**Nombre:** John Romano </br>
**Localización:** San Francisco, California, Estados Unidos

- Linkedin account: https://www.linkedin.com/in/john-romano18/

**Educación:** Northeastern University

**E-Mail Empresarial:** john.romano@pantheon.io

---

### Directora de marketing de Pantheon

**Nombre:** Christy Marble </br>
**Localización:** Seattle, Washington, Estados Unidos

- Linkedin account: https://www.linkedin.com/in/christymarble/

**E-Mail Empresarial:** christy.marble@pantheon.io

---

### Senior IT Manager

**Nombre:** Steven Juanes </br>
**Localización:** San Francisco, California, Estados Unidos

- Linkedin account: https://www.linkedin.com/in/steven-juanes-jr/

**Educación:** San Jose State University

**E-Mail Empresarial:** steven@pantheon.io

--- 

### Senior CRM Administrator

**Nombre:** Hien Ferber </br>
**Localización:** San Francisco, California, Estados Unidos

- Linkedin account: https://www.linkedin.com/in/hien-ferber/

**Educación:** RMIT University

**E-Mail Empresarial:** hien.ferber@pantheon.io

---

