<div align="center">
🅿️ Control de ingresos, salidas y cupos
Parqueadero Campus Seguro
</div>

Sistema de control para parqueaderos de motos y bicicletas que reemplaza el cuaderno y el conteo a ojo. Permite registrar entradas y salidas, saber al instante cuántos cupos quedan y qué tan lleno está el parqueadero, y llevar el control de novedades como ingresos sin placa y fichas perdidas, para atender mejor y reducir errores.

Proyecto de Aula · Primer semestre · Tecnología en Desarrollo de Software Fundación Universitaria Tecnológico Comfenalco · Caso de estudio 03 (Grupo 3)

📑 Contenido
Problema que atiende
Funcionalidades
Cómo ejecutarlo
Menú y ejemplo de uso
Cómo funciona
Casos de prueba
Alcance y limitaciones
Autores
🎯 Problema que atiende

El parqueadero lleva el registro de vehículos en un cuaderno y cuenta los cupos a simple vista. Esto genera datos incompletos (ingresos sin placa, fichas perdidas), conteos que cambian y usuarios que preguntan si hay espacio antes de entrar. El programa centraliza ese control en un solo lugar.

✨ Funcionalidades
Registrar ingreso de motos y bicicletas. Si el vehículo no tiene placa, se acepta y se marca como SIN PLACA (novedad).
Registrar salida buscando la placa del vehículo y liberando su cupo.
Consultar disponibilidad: cupos libres y porcentaje de ocupación por tipo, con alerta cuando la ocupación llega al 90 % o más.
Registrar fichas perdidas y mostrar el total acumulado.
Resumen semanal: promedio de ingresos de la semana y día de mayor ingreso.
📏 Reglas del caso
Regla	Detalle
Capacidad	60 cupos para motos y 30 para bicicletas
Tipos permitidos	Solo moto (1) y bicicleta (2)
Ingreso sin placa	Se acepta y se guarda como SIN PLACA
Salida	Solo si hay vehículos dentro y la placa existe
Alerta	Se muestra cuando la ocupación es mayor o igual a 90 %
🧰 Requisitos
Python 3.6 o superior (usa f-strings).
No requiere instalar librerías externas.
🚀 Cómo ejecutarlo
bash
python parqueadero.py

Cambia parqueadero.py por el nombre real del archivo si es diferente.

📋 Menú y ejemplo de uso
Menú principal
--- MENÚ PRINCIPAL ---
1. Registrar ingreso de vehículo
2. Registrar salida de vehículo
3. Consultar disponibilidad y % de ocupación
4. Registrar ficha perdida
5. Ver resumen semanal (Precálculo)
6. Salir
Ejemplo de uso
Digite una opción (1 a 6): 1
Tipo de vehículo (1 para Moto, 2 para Bicicleta): 1
Ingrese la placa o identificación (dejar en blanco si no tiene): ABC123
¡Ingreso de Moto registrado con éxito!
Cupos disponibles de motos: 59

Digite una opción (1 a 6): 3
Motos ocupadas: 1 de 60 (Libres: 59) | Ocupación: 1.7%
Bicicletas ocupadas: 0 de 30 (Libres: 30) | Ocupación: 0.0%
🔧 Cómo funciona
Un ciclo while muestra el menú hasta que se elige la opción 6.
La opción se lee como texto; si no es válida, el programa muestra un error y vuelve al menú.
Cada opción llama a una función que valida los datos y aplica las reglas.
Los contadores y las listas se actualizan y se devuelven al menú.
El programa muestra el resultado, el aviso o la alerta.
🧩 Funciones
Función	Qué hace
mostrar_menu()	Muestra las 6 opciones del menú
registrar_vehiculo()	Valida tipo y cupo, guarda placa y tipo, y suma 1 al contador
registrar_salida()	Busca la placa en la lista, elimina el registro y resta 1
consultar_disponibilidad()	Calcula cupos libres, porcentaje de ocupación y alerta del 90 %
registrar_ficha_perdida()	Suma 1 a las fichas perdidas y muestra el total
resumen_semanal()	Calcula el promedio de la semana y el día de mayor ingreso
main()	Inicia los datos y coordina el menú
📦 Datos del programa
motos_actuales y bicis_actuales: vehículos dentro por tipo.
fichas_perdidas: total de fichas perdidas.
lista_placas y lista_tipos: placa y tipo de cada vehículo que está dentro.
Capacidades fijas: 60 motos y 30 bicicletas.
✅ Casos de prueba sugeridos
ID	Entrada	Resultado esperado
CP-01	Ingreso de 1 moto y consulta	59 cupos libres y ocupación de 1.7 %
CP-02	31 ingresos de bicicletas	Acepta 30, rechaza el 31 y muestra alerta
CP-03	Tipo distinto de 1 o 2	Mensaje de tipo de vehículo no válido
CP-04	Ingreso de moto sin placa	Se acepta y se guarda como SIN PLACA
CP-05	Salida sin vehículos dentro	Aviso de que no hay vehículos
CP-06	Resumen semanal	Promedio 121.2 y miércoles con 132 ingresos
CP-07	Ingreso y salida de 1 moto	0 motos dentro y 60 cupos libres
🚧 Alcance y limitaciones

Incluye: registro de ingresos y salidas, cupos y porcentaje de ocupación, novedades (sin placa y fichas perdidas) y resumen semanal.

No incluye (mejoras futuras):

Guardar los datos en archivos o base de datos. Al cerrar el programa, los datos se pierden.
Aplicación web o móvil.
Pagos o cobros en línea.
Inteligencia artificial, sensores o cámaras.

El resumen semanal usa los ingresos fijos del caso de estudio (lunes 118, martes 126, miércoles 132, jueves 121 y viernes 109), no los pide al usuario.

👥 Autores

David Pérez · Diego Acosta · Leonadis Palencia · Kelldryn Martínez · Edwin Matos
El resumen semanal usa los ingresos fijos del caso de estudio (lunes 118, martes 126, miércoles 132, jueves 121 y viernes 109), no los pide al usuario.

## Autores

David Pérez · Diego Acosta · Leonadis Palencia · Kelldryn Martínez · Edwin Matos
