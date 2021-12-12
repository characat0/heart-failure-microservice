# Heart Failure Microservice

Microservicio en Python que predice la probabilidad de padecer una enfermedad del corazón.

Para poder ejecutar el microservicio de manera local utilizar:
```shell
git clone https://github.com/MarcoVela/heart-failure-microservice.git
cd heart-failure-microservice/
docker-compose build
docker-compose up
```
Se podrá visualizar el servicio en el puerto 8080.

## Estructura del proyecto
```text
│heart-failure-microservice <- Carpeta principal del proyecto.
│
├── training                <- Generación y almacenamiento del modelo.
│   ├── data                <- Almacenamiento de datos para reentrenamiento.
│   ├── generate_model.py   <- Script para la generación del modelo (requiere 
│   │                          datos de entrenamiento).
│   └── lgbmc.joblib        <- Modelo preentrenado por defecto.
│ 
├── constants.py            <- Definición de constantes de configuración.
├── health_check.py         <- Comprobación del funcionamiento del microservicio.
├── patient_dto.py          <- Definición de entidades para la transferencia de datos.
├── requirements.txt        <- Definición de las dependencias del microservicio.
│
├── README.md               <- Usted está aqui.
├── test_main.http          <- Solicitudes HTTP para probar los endpoints.
├── docker-compose.yml      <- Configuración para desplegar el servicio de forma rápida.
└── Dockerfile              <- Definición de los comandos para construir la imagen.
```


## Documentación

El microservicio cuenta con tres endpoints:

### GET /docs
Este endpoint tiene documentado en formato OpenApi el funcionamiento del microsevicio, referirse al mismo para los 
detalles de validación de cuerpo y salida de los endpoints.

### POST /predict
Este endpoint realiza la predicción de padecer una enfermedad del corazón, recibe en formato json los siguientes campos: 
1. Age: age of the patient [years]
2. Sex: sex of the patient [M: Male, F: Female]
3. ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: NonAnginal Pain, ASY: Asymptomatic]
4. RestingBP: resting blood pressure [mm Hg]
5. Cholesterol: serum cholesterol [mm/dl]
6. FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
7. RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions 
and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by 
Estes' criteria]
8. MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]
9. ExerciseAngina: exercise-induced angina [Y: Yes, N: No]
10. Oldpeak: oldpeak = ST [Numeric value measured in depression]
11. ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]

Y devuelve una predicción en formato json con el atributo *"prob"* indicando la probabilidad de padecer una enfermedad 
del corazón.

### GET /health
Este endpoint realiza comprobaciones de que el microservicio opere con normalidad, comprobando que el modelo de 
predicción se encuentre guardado en la ruta esperada y que sea capaz de realizar una predicción de muestra.

## Requerimientos y configuración
Para poder desplegar el microservicio se usará Docker y para pruebas locales docker-compose. Para modificar el modelo 
se deberá reemplazar el archivo trainig/lgbmc.joblib, el archivo training/generate_model.py genera el modelo, para 
ejecutarlo se deberá contar con los [datos de entrenamiento](https://www.kaggle.com/kaanboke/beginner-friendly-catboost-with-optuna/data) 
dentro de la carpeta /training/data/.



