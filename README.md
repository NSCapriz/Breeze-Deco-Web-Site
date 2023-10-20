# Breeze Deco Project

![logo](BreezeDecoba/blog/static/blog/assets/img/logo.jpg "Logo Project")

* Descripción:<br>
	*Es un proyecto que representa un sitio web de un emprendimiento comercial dedicado a productos relacionados con la decoración de interiores.*

* Tecnologías utilizadas:<br>
    - Se utilizó el lenguaje de Marcado de Hipertexto **HTML** para estructurar y desplegar la página web y sus contenidos.
	- Se utilizó el leguaje de programación de **Python** y el framework **Django** para la estructura del backend.
	- Se utilizó **CSS** y el framework **Bootstrap** para darle estilo a los templates que componen el proyecto.

    ![logo python](https://fiverr-res.cloudinary.com/images/q_auto,f_auto/gigs/103951771/original/ae1c0fe2509aeed62fb1b5f24aa94466227a25a7/do-anything-related-to-python-django.png)

* Funciones y aplicaciones:<br>
	 *El presente proyecto cuenta con las aplicaciónes blog, login, register y profile, lo cual permiten modularizar las distintas funciones y componentes que componen el proyecto.*
	- Cuenta con herencia de HTML a raíz del archivo base.html .
	- Se establecieron clases en los archivos models de cada aplicación del proyecto.
	- Se insertarón formularios en los arhivos HTML para insertar datos a las clases preestablecidas.
	- Se insertó un formulario para  la busqueda de productos en la BD.
	- Se desarrollo un foro donde solo los usuarios registrados en la web puedan realizar publicaciones.
	- Se desarrollo un area de administración al que solo cuenta con acceso el admin general, a los fines de consultar datos particulares, crear, editar o borrar datos de la BD, desde la misma página.
	- Se agregaron metodos __str__ a las clases a fin que en el area de administración propia del proyecto, se visualicen de mejor forma los objetos.



* Funcionamiento para los usuarios:
	* Los usuarios no registrados solo podrán acceder a las principales páginas del sitio web (Inicio, Nosotros, Productos y Contacto), contando con la posibilidad de registrarse, recomendar productos, buscar productos o bien realizar consultas.
	* Por su parte, los usuarios que se hayan registrado o decidan registrarse, podran logearse y editar sus datos personales, cambiar su contraseña o bien subir un avatar / foto de perfil, que los identifique. Asimismo, podrá acceder al apartado del foro de la página, donde podrán realizar publicaciones / posteos que deseen.
	* El administrador general, cuenta además de las anteriores posibilidades, con la capacidad para poder administrar los datos de la BD, desde la misma página una vez que se encuentre logeado.

* Dato:
	* En la base de datos de prueba, se ha creado un super user -- **Usuario:** AdminGeneral **Password:** AdminPass123 

* Autor del proyecto:
	**Nicolás Capriz**

* Estado del proyecto:
	**En proceso de desarrollo**. Se espera agregar mayores funcionalidades a futuro.