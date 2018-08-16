# Configurador HG 659
<p>Este programa es un configurador para equipos Huawei HG659.</p>
<p>Instalacion:</p>
<ul>
	<li>1. Descargar el codigo fuente a la computadora con <code>git clone https://github.com/sebvif/hgconfig.git</code>.</li>
	<li>2. Ir al directorio recien creado con <code>cd hgconfig</code>.</li>
	<li>3. Generar un virtualenv con <code>virtualenv venv</code> y activalo con <code>source venv/bin/activate</code>.</li>
	<li>4. Instalar las librerias requeridas con <code>pip install -r requirements.txt</code>.</li>
</ul>
<p>Utilizacion:</p>
<ul>
	<li>1. Asegurar que este activo el virtual env.</li>
	<li>2. Con la base de datos de la semana, actualizar la 'Sheet1' del archvio <code>scripts_auxiliares/BD.xlsx</code>.</li>
	<li>3. Ir al directorio de scripts_auxiliares con <code>cd scripts_auxiliares</code>.</li>
	<li>4. Generar los archivos de configuracion con <code>python lineas.py</code> y verificar su existencia en el directorio <code>scripts_auxiliares/config</code>.</li>
	<li>5. Copiar los nombres de los archvios de configuracion (generados por <code>lineas.py</code>) en la columna B de la 'Sheet1' del archivo <code>serial_dev.xlsx</code>.</li>
	<li>6. Escanear el numero de serie de los equipos a configurar en la columna A de la 'Sheet1' del archivo <code>serial_dev.xlsx</code>.</li>
	<li>7. Regresar al directorio base con <code>cd ..</code> e iniciar la aplicacion web con <code>flask run</code>.</li>
</ul>
<p>Recordar que el servicio genieacs debe estar corriendo para que la aplicacion funcione correctamente.</p>