# Proyecto 3

Este repositorio contiene el código para el proyecto 3 de Programación Web de *CS50 con Python y JavaScript* implementando la aplicación *Pizza* en *Django*.

## Estructura de archivos

De acuerdo con las especificaciones de Django, este repositorio contiene un directorio principal para todo el *Pizza*, así como un directorio para cada una de las dos aplicaciones Django: *Pedidos* y *Usuarios*

### Pizza

Solo ha habido cambios muy pequeños en los archivos de este directorio en relación con su contenido predeterminado cuando se crearon con el comando `startproject` de Django.

Esos cambios incluyen

* *settings.py*: Algunas líneas adicionales al final para permitir el uso de algunas funciones adicionales como *Crispy Forms*.

* *urls.py*: Patrones de URL para incluir las URL especificadas en el módulo de usuarios y pedidos.

### Pedidos

La Aplicación de Pedidos contiene toda la lógica para la implementación tanto del Menú como del proceso de pedido. De hecho, contiene todo excepto la funcionalidad de registro / inicio de sesión de usuario.

En el directorio de plantillas se puede encontrar la plantilla de diseño principal que luego se amplía con las plantillas para la página de menú / índice (index.html), la página del carrito de compras (cart.html), la página de adición de artículo (add.html) y la descripción general del pedido (orderlist.html).

En hemos optado por crear los siguientes modelos:

* *MenuItem*: Este es un elemento del menú como una pizza de queso regular pequeña (cada tamaño es un elemento de menú diferente)
* *Coberturas*: Coberturas que se pueden agregar a una pizza.
* *Extras*: Extras que se pueden agregar a un producto. (Actualmente, solo queso extra para todos los subs y cebollas, etc. para Steak + Cheese Sub). Qué extras se pueden agregar a qué producto se controla a través de una relación de muchos a muchos.
* *OrderItem*: artículo que se ha configurado y agregado a un pedido. Contiene una referencia ForeignKey al MenuItem, así como muchas a muchas relaciones que describen qué ingredientes o extras se han agregado.
* *Pedido*: Un pedido contiene todos los artículos de pedido que se han agregado a este pedido y se les asigna un estado (Abierto (carrito de compras), Pendiente, Completado, Cancelado)

Para permitir que un usuario personalice y agregue un artículo de pedido, he usado un ModelForm de django basado en el modelo de artículo de pedido.

### Usuarios

Para el registro, en parte, confío completamente en la vista de inicio de sesión incorporada, mientras que para el registro he personalizado ligeramente la vista usando una versión ligeramente modificada del UserCreationForm incorporado que agrega nombre y apellido.
Para mejorar la estética de los formularios, les doy formato usando * Crispy * Forms en mis plantillas.

## Toque personal / Ver y cancelar pedidos

Mi toque personal, estaba agregando una página adicional para el usuario donde puede ver todos sus pedidos pendientes, completados y cancelados, así como también poder cancelar sus pedidos pendientes en caso de que cambie de opinión.