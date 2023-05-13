# Proyecto Hackaton FundEsplai: Modalidad Backend.

El proyecto se trata de una aplicación web de registro y autenticación de usuarios utilizando el framework Django. La aplicación está diseñada para permitir que los usuarios se registren y autentiquen en la aplicación, y una vez que han iniciado sesión, puedan acceder a un área de miembros privada donde pueden ver su información personal.

La aplicación utiliza una base de datos SQLite para almacenar la información de usuario y sesión, lo que significa que es una solución fácil y liviana para proyectos más pequeños que no necesitan una base de datos más grande o compleja.

El proyecto también utiliza una serie de características y paquetes de Django, como:

Django Forms: para manejar el formulario de registro de usuarios y de inicio de sesión.
Django Authentication: para manejar la autenticación de usuarios y el manejo de sesiones.
Django Middleware: para manejar la verificación de autenticación y redirigir a los usuarios a la página de inicio de sesión si no están autenticados.
Django Views: para manejar la lógica del backend que permite a los usuarios registrarse, iniciar sesión y ver su información personal.
Django Templates: para renderizar las páginas HTML y mostrar la información al usuario.
Django URL Routing: para dirigir a los usuarios a las diferentes vistas de la aplicación.
En general, la aplicación es una solución simple y eficaz para el registro y la autenticación de usuarios en una aplicación web utilizando Django.

# Instalación y ejecución(En modo local) del servidor en windows.
Previo a la instalación:
1. Instala python si no lo tienes instalado: puedes hacerlo desde este enlace: https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe Ya te instalara la versión necesaria. Al instalar python asegurate de marcar la casilla de añadir la variable al PATH. (![image](https://github.com/victor9889/hackaton_Backend/assets/115695594/44b9307e-bdf8-4217-97ec-ce64b9326057)

Instalación:
1. Crear una carpeta y posicionarse dentro de ella desde un terminal.
2. Exportar el proyecto en esa carpeta. Descomprimiendolo o con el comando: git clone https://github.com/victor9889/hackaton_Backend.git
3. Creamos el entorno virtual para django con el comando: python -m venv nombre_de_tu_entorno_virtual
4. Activamos el entorno virtual con este comando: "Ruta_al_directorio/nombre_de_tu_entorno_virtual/scripts/activate"
5. Instalamos Django: pip install Django.
6. Instalamos los requerimientos que vienen en requirements.txt con el comando: pip install -r hackaton_Backend/requirements.txt
7. El servidor está listo para ponerse en marcha con el comando: python hackaton_Backend/manage.py runserver. Podemos acceder a el a través de : http://127.0.0.1:8000/

# Por qué el uso de estas tecnologías:
- Django es un framework web de alto nivel que se utiliza comúnmente para desarrollar aplicaciones web. Se basa en el patrón Modelo-Vista-Controlador (MVC) y proporciona una gran cantidad de características integradas, como el enrutamiento de URL, la autenticación, la gestión de formularios y la administración de bases de datos, lo que permite a los desarrolladores crear aplicaciones de manera rápida y eficiente. 
- SQLite, es una base de datos SQL incorporada y fácil de usar que se utiliza comúnmente en aplicaciones web y móviles. Es una opción popular para proyectos más pequeños debido a su tamaño y facilidad de configuración. En lugar de un servidor de base de datos separado, SQLite se ejecuta como una biblioteca vinculada a la aplicación y almacena la base de datos en un solo archivo, lo que la hace fácil de configurar y administrar.

# Cálidad del código con SonarQube:
![3682558a-6c90-4e75-bd09-c67ba93d7ef0](https://github.com/victor9889/hackaton_Backend/assets/115695594/2ce4cf37-42de-46e9-83e9-738466e64f9e)

