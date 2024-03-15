# DekaClassification: Automatización y Análisis en la competición DEKA

El proyecto **DekaClassification** es una herramienta de automatización diseñada para extraer, procesar y clasificar los resultados de las diferentes pruebas de la competición *DEKA* (de la prestigiosa marca *SPARTAN*), facilitando así a los atletas españoles la consulta de sus resultados y posición en tiempo real a nivel nacional. Este proyecto nace de la necesidad de ofrecer una solución robusta que permita consultar de manera eficiente y precisa sus resultados y posiciones en el territorio nacional.

El código realiza web scraping utilizando `Selenium` para navegar y extraer los resultados directamente desde la página oficial de *DEKA* (https://es.deka.fit/) y `BeautifulSoup` para analizar el HTML obtenido, procesando la información relevante para transformarla en datos estructurados y manejables. El software permite visualizar clasificaciones filtradas por criterios específicos, incluyendo el país de origen del competidor (*de momento sólo España*), su nombre, y la categoría de la competición (*DEKA MILE, DEKA STRONG o DEKA FIT*) ofreciendo así una perspectiva detallada y personalizada del rendimiento. 

Para aquellos usuarios que desean realizar un análisis más profundo o conservar registros de sus rendimientos, **DekaClassification** integra funcionalidades como la exportación a EXCEL gracias a `pandas`, facilitando el almacenamiento, la revisión y compartimiento de la información.

## Aplicaciones

🏃 **Atletas Competitivos:** Obtén una visión clara de tu posición a nivel nacional e identifica áreas de mejora comparando tus tiempos con los de otros competidores.

📋 **Entrenadores:** Utiliza los datos detallados para analizar el rendimiento de tus pupilos, planificar futuros entrenamientos y estrategias de competencia.

📊 **Analistas Deportivos:** Accede a un conjunto de datos rico y detallado para realizar análisis estadísticos, tendencias y reportes.


## Características Principales

🔄 **Extracción de datos en tiempo real de resultados de competencias DEKA.**

🔍 **Filtrado de resultados por país, nombre de competidor y género.**

🏅 **Cálculo de la posición del competidor y su porcentaje de superación sobre el total de participantes.**

📨 **Notificación a través de Telegram con la posición y el tiempo del competidor.**

📊 **Exportación de datos a un archivo Excel para análisis detallado fuera de línea (opcional).**

🖥️ **Resultados de Consola y Telegram**

## Uso

Para integrar la funcionalidad de notificación a través de **Telegram** en el proyecto **DekaClassification**, es necesario configurar tu propio bot y canal en Telegram. Esto permitirá que el script envíe automáticamente mensajes con los resultados de las competiciones directamente a tu canal de Telegram.

### Configuración en Telegram:

1. **Crear un Bot en Telegram:**
   - Inicia una conversación con [BotFather](https://t.me/botfather) en Telegram.
   - Utiliza el comando `/newbot` y sigue las instrucciones para crear tu bot. Se te solicitará seleccionar un nombre y un nombre de usuario para el bot.
   - Al finalizar, **BotFather** te proporcionará un `token`, que es una cadena larga de letras y números. Debes guardar este token de forma segura, ya que lo necesitarás en el script.

2. **Crear un Canal en Telegram:**
   - Crea un nuevo canal en Telegram a través de la opción "Nuevo canal".
   - Establece la visibilidad del canal como pública o privada y proporciona un nombre y descripción adecuados.
   - Añade tu bot al canal como administrador para permitirle enviar mensajes al mismo.

### Integración con el Script:

Dentro del script **DekaClassification**, localiza y rellena las siguientes líneas con la información de tu bot y canal:

```python
# TELEGRAM INFORMATION (INTRODUCE YOUR INFORMATION HERE)
token = "XXXXXXXX:XXXXXXXXXXXXXXXXXX"
chat_id = "-XXXXXXXXXXX"
```

Reemplaza XXXXXXXX:XXXXXXXXXXXXXXXXXX con el token proporcionado por BotFather y -XXXXXXXXXXX con el ID de tu canal de Telegram.

###  Opción de Desactivación:

Si no deseas utilizar la funcionalidad de notificación de Telegram o si prefieres prescindir de ella, puedes desactivarla fácilmente. Para hacerlo, simplemente comenta o elimina las siguientes líneas de código:

```python
# TELEGRAM INFORMATION (INTRODUCE YOUR INFORMATION HERE)
token = "XXXXXXXX:XXXXXXXXXXXXXXXXXX"
chat_id = "-XXXXXXXXXXX"
[...]
requests.post("https://api.telegram.org/bot" + token + "/sendMessage", data={"chat_id": chat_id, "text": "\n" + comp})
requests.post("https://api.telegram.org/bot" + token + "/sendMessage", data={"chat_id": chat_id, "text": f"\n\nPosición {my_position}/{count - 1} | Tiempo: {my_time}"})
requests.post("https://api.telegram.org/bot" + token + "/sendMessage", data={"chat_id": chat_id, "text": f"\nPor delante del {percent_position:.2f}% de todos los participantes"})
```

Con estos pasos, podrás configurar y utilizar las notificaciones de Telegram para tu proyecto **DekaClassification** o elegir omitirlas según tus necesidades.

## Resultados

**DekaClassification** provee una interfaz intuitiva y efectiva para la visualización de los resultados tanto en la consola como a través de notificaciones en Telegram, permitiendo a los usuarios acceder a la información relevante de forma inmediata y eficiente. A continuación, se presentan ejemplos de la salida de la consola y de las notificaciones de Telegram para las competiciones *DEKA MILE* y *DEKA STRONG*:

## DEKA MILE: 

### 🖥️Consola
![image](https://github.com/PyMvs/DekaClassification/assets/23172965/18ed65d1-967f-4bcc-93eb-31c3fb8b5155)

![image](https://github.com/PyMvs/DekaClassification/assets/23172965/a2c225a4-dfac-4d3b-8a88-9af7d3fa3887)


### 📱Telegram:
![image](https://github.com/PyMvs/DekaClassification/assets/23172965/408c6e41-60f2-425d-8e41-59222d21faf7)



## DEKA STRONG:

### 🖥️Consola
![image](https://github.com/PyMvs/DekaClassification/assets/23172965/c78c18d5-a796-4115-b7ff-7c47a1b42d2d)

![image](https://github.com/PyMvs/DekaClassification/assets/23172965/07a9fa1d-206d-4470-8bb9-4ad072b4ce82)


### 📱Telegram:
![image](https://github.com/PyMvs/DekaClassification/assets/23172965/a0ff3f2c-dae2-4468-ac7e-727e8708add8)


Las imágenes adjuntas muestran la interfaz de usuario de la consola y el formato en el que se presentan los datos en el grupo de Telegram, con una visualización clara y concisa de la información relevante para los competidores (todos los datos aportados son de carácter público).

