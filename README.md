# Proyecto Urban Grocers 



## Descripción del Proyecto
Este proyecto comprueba la creación de Kits de productos de la aplicación ***Urban Grocers***. Principalmente el comportamiento del nombre asignado a cada kit. El proyecto abarca una lista de comprobación para la creación de kit a partir de un usuario o usuaria.

Esto se realiza mediante los Endpoints 
"/api/v1/users" - Creación de Usuarios
"/api/v1/kits" - Creación de Kits

Cada test envía una solicitud POST con valores distintos según la lista de comprobación que se describe a continuación, con el objetivo de obtener un código 201 (Prueba Positiva) o código 400 (Prueba Negativa). 

### Lista de comprobación  

| N° | Descripción| Resultado Esperado|
|----|------------|-------------------|
|1| El número permitido de caracteres (1): kit_body = { "name": "a"}| Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
|2| El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a {cadena de 511 caracteres}"}|Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
|3|El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }|Código de respuesta: 400
|4|El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a {cadena de 512 caracteres}” }|Código de respuesta: 400
|5|Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }|Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
|6|Se permiten espacios: kit_body = { "name": " A Aaa " }|Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
|7|Se permiten números: kit_body = { "name": "123" }|Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud
|8|El parámetro no se pasa en la solicitud: kit_body = { }|Código de respuesta: 400
|9|Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }|Código de respuesta: 400




## Tecnologías y Técnicas Utilizadas 

**Tecnologías**
- Python 3 : Lenguaje de las Pruebas.
- Librería pytest: ejecución de pruebas y reporte de resultados.
- Librería requests: envío de peticiones HTTP a la API.
- Git y GitHub: Control de Versiones a partir de Pull / Push requests y Commits para version final.

**Técnicas**
- Pruebas de API
- Análisis de valores límite
- Pruebas Negativas y Positivas (Positive Assert & Negative Assert)

## Documentación
La documentación de la API se generó con [apiDoc](https://cnt-2cb43fd0-4827-4144-88b0-e517a81c674a.containerhub.tripleten-services.com/docs/#api-Main.Kits-CreateKit).

Utilizar la sección Main.User (Creación de Cuenta) y Main.Kits(Crear un Kit)

De esta manera accedemos a los endpoints, encabezados, cuerpos de la solicitud y demás parámetros necesarios para nuestras pruebas.

#### Para generarla y verla:
- Inicia el servidor de Urban Grocers.
- Según obtengas la URL del servidor, copia y pega el link del servidor en tu navegador
- Agrega "/docs/" al final de la URL

## Flujo de las Pruebas

1. Se crea un usuario nuevo a partir del método POST en el endpoint /api/v1/users con los siguientes requisitos:

|Endpoint|Header|Body|
|:-------|:----:|---|
|/api/v1/users|"Content-Type": "application/json"|{"firstName": "Santiago","phone": "+10005553535","address": "8042 Lancaster Ave.Hamburg, NY" }

2. Se crea un kit con el valor especificado en el campo "name" a probar:

|Endpoint|Header|Body|
|:-------|:----:|---|
|/api/v1/kits|{"Content-Type": "application/json","Authorization": "Bearer jknnFApafP4awfAIFfafam2fma}"|"name" : "Kit"

3. Se hace el respectivo test, dependiendo del resultado esperado, siendo un positive assert o negative assert.

## Obligatorio

- Instalar las Librerías ***requests*** y ***pytest***
- Configurar la URL del servidor en configuration.py URL_SERVICE = 

****Es posible modificar los valores utilizados para los tests en 'data.py', pero no es obligatorio.***

- Los Tests se realizan en 'create_kit_name_kit_test.py' 


## Hallazgos

A partir de los test realizados, se encontraron los siguientes Hallazgos:

- 5 de los tests ejecutados fueron **APROBADOS**, en específico los N° 1, 2, 5, 6 y 7. 
  - El test N°1 nos confirma que el servicio acepta un nombre con mínimo 1 caracter.
  - El test N°2 nos confirma que el número máximo permitido de caracteres (boundary value) 511 es aceptado en el nombre de kit por el servicio.
  - El test N°5 nos confirma que el servicio acepta nombres de kit que incluyen caracteres especiales.
  - El test N°6 nos confirma que el servicio acepta nombres de kit que incluyen espacios.
  - El test N°7 nos confirma que el servicio acepta nombres de kit que incluyen números.

- 4 de los test ejecutados fueron **NO APROBADOS**, en específico los N° 3, 4, 8 y 9. Esto se debe a que el servidor valida el campo ***name*** cuándo no debería. 

  - El test N°3 nos informa que cuándo un nombre de kit tiene 0 carácteres, este es creado (Obtenido: código 201), cuando no debería serlo (Esperado: código 400)
  - El test N°4 nos informa que el nombre de kit acepta más carácteres que el límite de 511 ya que este se crea (Obtenido: código 201, cuando no debería crearse por pasarse del límite (Esperado: código 400)
  - El test N°8 nos informa que cuándo no hay ningún parámetro en el cuerpo de la solicitud (kit_body={}) este es creado (Obtenido: código 201, cuando no debería serlo (Esperado: código 400)
  - El test N°9 nos informa que cuándo se pasa un parámetro de tipo "número", el kit es creado (Obtenido: código 201), cuando no debería serlo (Esperado: código 400)

### 5/9 pruebas son aprobadas; el servidor no valida 4 casos.

## 👤 Autor

Santiago Pachon - [GitHub](https://github.com/SantiagoPachon-prog)


