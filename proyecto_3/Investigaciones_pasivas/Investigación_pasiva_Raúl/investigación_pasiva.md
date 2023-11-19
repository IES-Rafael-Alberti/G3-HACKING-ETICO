# Investigación pasiva de pantheon.io

## Información del dominio

Lo primero que he hecho a sido buscar información sobre el dominio utilizando las herramientas whois.domaintools.com , whois y who.is:

Lo más relevante que he encontrado ha sido:

La dirección ip: 23.185.0.253 a la cual le hecho una resolución inversa y me ha devuelto 3 dominios mas que se encuentran en alojados en la misma dirección IP:

1.	arkbrunelprimary.org	
2.	betoforgovernor.com	
3.	childcareforeveryfamily.org

La ubicación de la IP:	United States - California - San Francisco

ASN: AS54113 FASTLY, US (registered Oct 04, 2011)

Registry Domain ID: c8a58af5ce394c2a878e7eb001d1ac89-DONUTS

Con la ayuda de netcraft también he podiso sacar mucha información relevante:

https://sitereport.netcraft.com/?url=https://pantheon.io

Ya no he podido encontrar más información ya que el dominio se encuentra protegido por https://www.gandi.net.


## Servidores DNS:

Tras probar varias herramientas la que más información me ha ofrecido ha sido 

Con la ayuda de DNSRECON he podido sacar algunas de las direcciones IP de los registros encontrados anteriormente:

```
└─$ dnsrecon -d pantheon.io
[*] std: Performing General Enumeration against: pantheon.io...
[-] DNSSEC is not configured for pantheon.io
[*]      SOA ns-148.awsdns-18.com 205.251.192.148
[*]      NS ns-924.awsdns-51.net 205.251.195.156
[-]      Recursion enabled on NS Server 205.251.195.156
[*]      NS ns-1096.awsdns-09.org 205.251.196.72
[-]      Recursion enabled on NS Server 205.251.196.72
[*]      NS ns-1857.awsdns-40.co.uk 205.251.199.65
[-]      Recursion enabled on NS Server 205.251.199.65
[*]      NS ns-148.awsdns-18.com 205.251.192.148
[-]      Recursion enabled on NS Server 205.251.192.148
[*]      MX aspmx2.googlemail.com 142.250.153.26
[*]      MX aspmx3.googlemail.com 142.251.9.27
[*]      MX alt1.aspmx.l.google.com 142.250.153.27
[*]      MX alt2.aspmx.l.google.com 142.251.9.27
[*]      MX aspmx.l.google.com 64.233.166.27
[*]      A pantheon.io 23.185.0.253
[*]      TXT pantheon.io amazonses:RlvLmxzcHOsiBlOKC3l3WHjCh6g9X8x8JcAFdMlW9BI=
[*]      TXT pantheon.io asv=6522b472ea8016fba67687ca648b4f19
[*]      TXT pantheon.io atlassian-domain-verification=MPUQoKJCCFX7kRgKt7jqKlvQp+rF+4coyVIkxbw5CF1PZ24laDjMzXfgAY2VZMm8
[*]      TXT pantheon.io docker-verification=df12737e-922c-4a2e-ac9b-0c5a97da58c5
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
[*]      TXT _dmarc.pantheon.io v=DMARC1; p=none; pct=100; sp=none; rua=mailto:3523e61d@inbox.ondmarc.com; ruf=mailto:3523e61d@inbox.ondmarc.com; adkim=r; aspf=r; fo=1; rf=afrf; ri=86400
[*] Enumerating SRV Records
[-] No SRV Records Found for pantheon.io


```

Utilizando la herramienta DNSDumpster he podido capturar toda la información adquirida anteriormente de una forma más clara y más información sobre más registros de los que he podido deducir que utilizan un servidor web/proxy nginx con la versión 1.17.8.

Datos/SUBDOMINIOS/pantheon.io-202311171820.xlsx

## Subdominios:

Con la ayuda de la herramienta sublist3r he podido adquirir 147 subdominios:

Utilizando el comando: 

```
python sublist3r.py -v -d pantheon.io -t 3

```

```

www.pantheon.io
answers.pantheon.io
api.pantheon.io
api-sandbox.pantheon.io
billing-history-webhook-receiver.pantheon.io
bragreply.pantheon.io
brandtheon.pantheon.io
chat.pantheon.io
community.pantheon.io
www.community.pantheon.io
decoupled.pantheon.io
prod-router.decoupled.pantheon.io
sandbox-router.decoupled.pantheon.io
dev-canary.pantheon.io
dev-nmtc.pantheon.io
dev-ns-tech.pantheon.io
discover.pantheon.io
discuss.pantheon.io
fe1.edge.pantheon.io
fe2.edge.pantheon.io
5649391675244544.fe2.edge.pantheon.io
fe3.edge.pantheon.io
5639445604728832.fe3.edge.pantheon.io
fe4.edge.pantheon.io
5659313586569216.fe4.edge.pantheon.io
policy-docs-api-sandbox.edrt.pantheon.io
enterwebopssummit.pantheon.io
goto.pantheon.io
grafana-ingress.pantheon.io
helpdesk.pantheon.io
insecure-terminus.pantheon.io
guide.itsupport.pantheon.io
joe-test-le.pantheon.io
ing-test.sandbox-antonpetryk.sandbox-02.us-east4.sandbox.k8s.pantheon.io
ingress-hermes-test.sandbox-antonpetryk.sandbox-02.us-east4.sandbox.k8s.pantheon.io
ingress-test.sandbox-antonpetryk.sandbox-02.us-east4.sandbox.k8s.pantheon.io
ingress2-test.sandbox-antonpetryk.sandbox-02.us-east4.sandbox.k8s.pantheon.io
ingress3-test.sandbox-antonpetryk.sandbox-02.us-east4.sandbox.k8s.pantheon.io
ingress4-test.sandbox-antonpetryk.sandbox-02.us-east4.sandbox.k8s.pantheon.io
ingress5-test.sandbox-antonpetryk.sandbox-02.us-east4.sandbox.k8s.pantheon.io
vcr.joecorall.sandbox-03.us-west1.sandbox.k8s.pantheon.io
policy-docs-mtls-test.sandbox-oleksiimiroshnyk.sandbox-04.us-west2.sandbox.k8s.pantheon.io
policy-docs-test.sandbox-oleksiimiroshnyk.sandbox-04.us-west2.sandbox.k8s.pantheon.io
learn.pantheon.io
learning.pantheon.io
legal.pantheon.io
linuxsecaudit.pantheon.io
live-clomedia.pantheon.io
live-prcmacro.pantheon.io
router.sfo.office.pantheon.io
partners.pantheon.io
pmc.pantheon.io
pmt-staging.pantheon.io
bugfix-devpmt-808.pmt-staging.pantheon.io
check-dev-deployment.pmt-staging.pantheon.io
devpmt-621-add-site-label.pmt-staging.pantheon.io
devpmt-654-service-plan-levels.pmt-staging.pantheon.io
devpmt-655-migration-stops.pmt-staging.pantheon.io
devpmt-656-failed-add-user.pmt-staging.pantheon.io
devpmt-656-migration-failed.pmt-staging.pantheon.io
devpmt-659-update-testuser-creds.pmt-staging.pantheon.io
devpmt-661-deployment-to-prod-cluster.pmt-staging.pantheon.io
devpmt-661-deployment-to-prod-cluster2.pmt-staging.pantheon.io
devpmt-669-investigate-fails.pmt-staging.pantheon.io
devpmt-675-update-terminus-version-on-pm.pmt-staging.pantheon.io
devpmt-681-additional-ui-tests.pmt-staging.pantheon.io
devpmt-689-github-actions.pmt-staging.pantheon.io
devpmt-689-github-actions-2.pmt-staging.pantheon.io
devpmt-778-update-terminus-version.pmt-staging.pantheon.io
feat-dev-pmt-800-material-ui.pmt-staging.pantheon.io
feat-devpmt-664-repeat-prev-migration.pmt-staging.pantheon.io
feat-devpmt-806-update-github-actions.pmt-staging.pantheon.io
feat-pmts-18-skip-settings-files.pmt-staging.pantheon.io
feature-debug-tests.pmt-staging.pantheon.io
feature-deployment-history.pmt-staging.pantheon.io
feature-devpmt-447.pmt-staging.pantheon.io
feature-devpmt-623.pmt-staging.pantheon.io
feature-devpmt-654-service-plan-levels.pmt-staging.pantheon.io
feature-devpmt-662.pmt-staging.pantheon.io
feature-devpmt-674.pmt-staging.pantheon.io
feature-devpmt-679-react-unit.pmt-staging.pantheon.io
feature-drupal7-bugfix.pmt-staging.pantheon.io
feature-e2e-tests.pmt-staging.pantheon.io
feature-pmtdev-637-bitbucket-pipelines.pmt-staging.pantheon.io
feature-retry-failed-tasks.pmt-staging.pantheon.io
feature-user-seed.pmt-staging.pantheon.io
feature-users-seeder.pmt-staging.pantheon.io
fix-bulk-operations-layout.pmt-staging.pantheon.io
fix-deployments.pmt-staging.pantheon.io
fix-devpmt-618-undefined-offset.pmt-staging.pantheon.io
fix-devpmt-639-select-destroy.pmt-staging.pantheon.io
fix-devpmt-678-new-migration-checkboxes.pmt-staging.pantheon.io
fix-devpmt-690.pmt-staging.pantheon.io
fix-devpmt-691-account-organizations.pmt-staging.pantheon.io
fix-devpmt-692-repeat-each-migration.pmt-staging.pantheon.io
fix-e2e-test-run.pmt-staging.pantheon.io
integrate-vrt2.pmt-staging.pantheon.io
master.pmt-staging.pantheon.io
staging.pmt-staging.pantheon.io
vpn-support-feature.pmt-staging.pantheon.io
vrt-staging.pmt-staging.pantheon.io
vrt-test.pmt-staging.pantheon.io
wraith-staging.pmt-staging.pantheon.io
sales.pantheon.io
api-gateway.sandbox-antonpetryk.sbx02.pantheon.io
kuard.sandbox-antonpetryk.sbx02.pantheon.io
secure-terminus.pantheon.io
slackin.pantheon.io
social.pantheon.io
sso-stage.pantheon.io
sso-test.pantheon.io
status.pantheon.io
styleguide-unfpa-global.pantheon.io
styx-fe1-australia-southeast1.pantheon.io
styx-fe2-australia-southeast1.pantheon.io
styx-fe3-australia-southeast1.pantheon.io
styx-fe4-australia-southeast1.pantheon.io
buildhook.svc.pantheon.io
decoupled.svc.pantheon.io
decoupled-notification.svc.pantheon.io
decoupled-subscription.svc.pantheon.io
payment-service-webhook-receiver.svc.pantheon.io
prod-decoupled.svc.pantheon.io
api-gateway.prod-decoupled.svc.pantheon.io
github-auth.prod-decoupled.svc.pantheon.io
github-listener.prod-decoupled.svc.pantheon.io
subscription-proxy.prod-decoupled.svc.pantheon.io
webhook-listener.prod-decoupled.svc.pantheon.io
dev-decoupled.sandbox.svc.pantheon.io
api-gateway.dev-decoupled.sandbox.svc.pantheon.io
github-auth.dev-decoupled.sandbox.svc.pantheon.io
github-listener.dev-decoupled.sandbox.svc.pantheon.io
subscription-proxy.dev-decoupled.sandbox.svc.pantheon.io
webhook-listener.dev-decoupled.sandbox.svc.pantheon.io
integration-decoupled.sandbox.svc.pantheon.io
zuora-payment-service-webhook-receiver.sandbox.svc.pantheon.io
sandbox-decoupled.svc.pantheon.io
sandbox-vcs.svc.pantheon.io
auth.sandbox-vcs.svc.pantheon.io
vcs.svc.pantheon.io
auth.vcs.svc.pantheon.io
vcs-auth.svc.pantheon.io
webhook.svc.pantheon.io
zuora-payment-service-webhook-receiver.svc.pantheon.io
test-canary.pantheon.io
test-vinyl-institute.pantheon.io
varnishcheck.pantheon.io

```

Con la ayuda de la herramienta amass he podido recolectar una gran cantidad de servidores DNS, subdominios, direcciones IP, etc.. que he almacenado en un fichero csv:

Datos/SUBDOMINIOS/amaas_resultados.csv

## Certificados

Con la ayuda de la herramienta crt.sh he adquirido una gran cantidad de certificados los cuales los he exportado a un fichero pdf: 

<Datos/CERTIFICADOS/crt.sh _ pantheon.io.pdf>

## Información de empleados

Empleados:

- Zark Rosen - CEO de la empresa
CEO, Co-founder at Pantheon
https://www.linkedin.com/in/zacharyrosen/
zack@pantheon.io

- Meredith Brown
Product Leader & GM
https://www.linkedin.com/in/brownmeredith/
Twiter: meredithbrownsf

- John Gardiner
CXO of hyper growth, PE-backed tech and data companies
https://www.linkedin.com/in/johngardiner3/
Twitter: JohnGardiner1

- Atoosa Campbell 
Director, Field & Partner Marketing at Pantheon Platform
https://www.linkedin.com/in/atoosa/

- Elisha Feliciano 
Field Marketing Manager
https://www.linkedin.com/in/elishahonestfeliciano/

- Amanda Klimek 
Workplace Experience Manager at Pantheon & Independent Fine Artist
https://www.linkedin.com/in/amanda-klimek-2769b71b/overlay/contact-info/
web personal: amandaklimek.com

- Sara Drohan:
sara.drohan@pantheon.io
Sara (Tyler) Drohan 
Enterprise Account Executive at Pantheon Platform

- David Timothy Strauss
CTO/co-founder of Pantheon; systemd co-maintainer; Drupal Security
Team member; founding member of 1st Fedora Server WG
Idioma: German
david@pantheon.io
+1 512 577 5827
CTO/co-founder of Pantheon
https://www.linkedin.com/in/davidstrauss/

https://twitter.com/DavidStrauss

https://www.instagram.com/davidstrauss/

Educación:
The University of Texas at AustinThe University of Texas at Austin
B.S., Computer ScienceB.S., Computer Science
2003 - 2007

The University of Texas at AustinThe University of Texas at Austin
B.A., Plan IIB.A., Plan II
2003 - 2007

Voluntariado:
Event Hosting and Technology AssistanceEvent Hosting and Technology Assistance
ConcrnConcrn
mar. 2016 - actualidad · 7 años 9 mesesmar. 2016 - actualidad · 7 años 9 meses
Lucha contra la pobreza

Data Pipeline LeadData Pipeline Lead
Covid Act NowCovid Act Now
mar. 2020 - may. 2020 · 3 mesesmar. 2020 - may. 2020 · 3 meses
Salud

- Greg Anderson
greg@pantheon.io
Lives in Anderson, CA
PRIMARY RESIDENCE:
613 Yarmouth Rd. Palos Verdes Estates
Anderson, CA 90274
PHONE NUMBERS:
310-701-7198
https://www.instagram.com/greganderson/
https://www.instagram.com/gregoanderson/


- Brian Perry
brian.perry@pantheon.io

- Josh König
josh@pantheon.io
CSO
Co-Founder & Chief Strategy Officer at Pantheon Platform
https://www.linkedin.com/in/joshkoenig/overlay/contact-info/
blog personal: https://www.outlandishjosh.com/


Empresa:

news@pantheon.io

diversityinclusion@pantheon.io

press@pantheon.io

info@pantheon.io

## Telefonos

Con la ayuda de la herramienta truecaller he podido determinar la ubicación y la compañia de telefono que utiliza el CTO de la empresa además de una dirección de correo extra:

M - Verizon Wireless
(512) 577-5827
Address
Austin, Tx, United States ⸱ Local time 06:53
Email
david@davidstrauss.net


## robots y sitemap

El archivo robots.txt indica a los rastreadores de los buscadores a qué URLs de tu sitio pueden acceder.


Sitemap.xml es el archivo o una url que contiene todas y cada una de las páginas de una web.

Ambos ficheros los he almacenado en la carpeta datos:

Datos/Robots.txt
Datos/sitemap.xml

## Tecnologias que usa el dominio:

He utilzado las herramientas wappalizer y whatweb:

Gestor de Contenido: Drupal 9
Analítica: VWO

Seguridad:
HSTS
reCAPTCHA

Tipografía: Google Font API

Miscelánea:
Webpack
Open Graph
Module Federation

Servidor Web: Nginx 1.17.8

Herramienta de Cache: Varnish 1.1

Lenguaje de programación: PHP

CDN: Fastly

Base de Datos: MariaDB
Tag Manager: Google Tag Manager

Librerías JavaScript:
jQuery UI 1.13.2
jQuery 3.6.3

PaaS: Pantheon
Proxy reverso: Nginx 1.17.8

Cookie compliance:
OneTrust

A/B testing: VWO

RUM: New Relic

Performance: Priority Hints


## Mas info de empleados:

A través de la herramienta dehashed he podido encontrar que la cuenta de correo david@davidstrauss.net esta registrada en Zomato, Dropbox, Canvas, MyFitnessPal, Zynga, LastFM, Disqus, eatstreet, houzz_com, LinkedIn, livejournal_com.

## Más información sobre servidores

Con la ayuda de Shodan he podido detectar 2 posibles servidores los cuales son interesantes:

![Alt text](<2023-11-17 20_27_25-pantheon.io - Shodan Search.png>)

Podemos ver los puertos que estan abiertos en el servidor así como las versiones de los servicios:

![Alt text](<2023-11-17 20_29_55-.png>)
