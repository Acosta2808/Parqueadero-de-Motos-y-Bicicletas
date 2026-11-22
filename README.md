<div align="center">

# 🅿️ Control de parqueadero de motos y bicicletas
### Parqueadero Campus Seguro

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Tipo](https://img.shields.io/badge/Tipo-Aplicaci%C3%B3n%20de%20consola-0B3F99)
![Estado](https://img.shields.io/badge/Estado-Proyecto%20de%20aula-C21A1F)

</div>

Sistema de consola para administrar un parqueadero de motos y bicicletas: control de ingresos y salidas, cupos y ocupación, cobro por tiempo de permanencia, novedades de seguridad, cierre de turno y reportes de caja, con acceso por usuario y rol (administrador y operario).

> Proyecto de Aula · Primer semestre · Tecnología en Desarrollo de Software
> Fundación Universitaria Tecnológico Comfenalco · Caso de estudio 03 (Grupo 3)

## 📑 Contenido

- [Problema que atiende](#-problema-que-atiende)
- [Funcionalidades](#-funcionalidades)
- [Cómo ejecutarlo](#-cómo-ejecutarlo)
- [Menús y ejemplo de uso](#-menús-y-ejemplo-de-uso)
- [Cómo funciona](#-cómo-funciona)
- [Funciones](#-funciones)
- [Datos del programa](#-datos-del-programa)
- [Pruebas sugeridas](#-pruebas-sugeridas)
- [Limitaciones](#-limitaciones)
- [Autores](#-autores)

---

## 🎯 Problema que atiende

El parqueadero llevaba el registro de vehículos en un cuaderno y contaba los cupos a simple vista. Eso generaba datos incompletos, conteos que cambiaban y usuarios que preguntaban si había espacio antes de entrar. El programa centraliza el control de entradas, salidas, cupos y recaudo en un solo lugar.

## ✨ Funcionalidades

**Acceso por rol:** inicio de sesión con usuario y contraseña. Rechaza usuarios inexistentes, cuentas desactivadas y contraseñas incorrectas.

**Administrador**
- Gestionar vigilantes: crear, editar el nombre, activar o desactivar la cuenta, restablecer la contraseña y ver la lista.
- Configurar las tarifas y la capacidad de cada zona.
- Consultar la auditoría y la caja, registrar tiquetes anulados y exportar un reporte a `reporte_parqueadero.txt`.
- Consultar la disponibilidad.

**Operario (vigilante)**
- Registrar el ingreso de motos (por placa) y bicicletas (por cédula o código del tiquete), con marca, color y novedades iniciales.
- Registrar la salida: calcula el tiempo de permanencia, muestra el monto y pide confirmar el pago.
- Registrar novedades de seguridad sobre un vehículo que está dentro.
- Cerrar turno con el total recaudado.
- Consultar la disponibilidad.

**Disponibilidad:** vehículos ocupados, cupos libres y porcentaje de ocupación por tipo, con alerta cuando llega al 90 % o más.

## 🚀 Cómo ejecutarlo

Requiere Python 3. No usa librerías externas, solo `datetime` de la biblioteca estándar.

```bash
python Parqueadero.py
```

**Usuarios de prueba**

| Usuario | Contraseña | Rol |
|---|---|---|
| `admin` | `admin123` | Administrador |
| `operario` | `operario123` | Operario |

## 📋 Menús y ejemplo de uso

### Menú administrador

```
1. Gestionar usuarios
2. Configurar tarifas
3. Configurar capacidad
4. Consultar auditoría y caja
5. Consultar disponibilidad
6. Cerrar sesión
```

### Menú operario

```
1. Registrar ingreso
2. Registrar salida y cobrar
3. Registrar novedad de seguridad
4. Cerrar turno
5. Consultar disponibilidad
6. Cerrar sesión
```

### Ejemplo de uso (operario)

```
Usuario: operario
Contraseña: operario123
Bienvenido, operario - Rol: OPERARIO

Seleccione una opción: 1
Tipo (1 Moto, 2 Bicicleta): 1
Placa: abc123
Marca: Honda
Color: Rojo
Novedades iniciales (Enter si ninguna):
Ingreso registrado: Moto - ABC123

Seleccione una opción: 5
Moto ocupadas: 1 de 50 - libres: 49 - ocupación: 2.0 %
Bicicleta ocupadas: 0 de 30 - libres: 30 - ocupación: 0.0 %

Seleccione una opción: 2
Placa o código: abc123
Tiempo transcurrido: 1 minutos
Monto a cobrar por Moto: 3000
¿Confirmar pago? (s/n): s
Pago confirmado y salida registrada.
```

## 🔧 Cómo funciona

1. El programa pide iniciar sesión y, según el rol, abre el menú de administrador o el de operario.
2. Cada menú es un ciclo `while` que se repite hasta cerrar la sesión.
3. Cada opción llama a una función que valida los datos y aplica las reglas.
4. Los datos se guardan en listas mientras el programa está abierto.
5. Al registrar una salida, el pago se suma a la caja del operario y a la caja global.
6. El administrador puede exportar el reporte de caja a un archivo de texto.

**Reglas del caso**

| Regla | Detalle |
|---|---|
| Capacidad inicial | 50 motos y 30 bicicletas (se puede cambiar) |
| Identificación | Moto: placa en mayúsculas. Bicicleta: cédula o código del tiquete |
| Ingreso | Se rechaza si la identificación está vacía, si el vehículo ya está dentro o si no hay cupo |
| Tiempo | Se cobra por minutos transcurridos, mínimo 1 minuto |
| Alerta | Se muestra cuando la ocupación es mayor o igual a 90 % |

**Tarifas iniciales (configurables)**

| Tipo | Fracción | Hora | Día | Mes |
|---|---|---|---|---|
| Moto | 2.000 | 3.000 | 30.000 | 150.000 |
| Bicicleta | 1.000 | 2.000 | 15.000 | 75.000 |

## 🧩 Funciones

| Función | Qué hace |
|---|---|
| `iniciar_sesion()` | Valida usuario, estado de la cuenta y contraseña |
| `gestionar_usuarios()` | Crea, edita, activa o desactiva vigilantes y restablece contraseñas |
| `configurar_tarifas()` | Muestra y modifica las tarifas de cada tipo |
| `configurar_capacidad()` | Cambia la capacidad de motos y bicicletas |
| `registrar_ingreso()` | Valida tipo, identificación y cupo, y guarda el vehículo con su hora |
| `registrar_salida()` | Calcula el tiempo, cobra, registra el pago y retira el vehículo |
| `registrar_novedad()` | Agrega un incidente a un vehículo que está dentro |
| `cerrar_turno()` | Guarda el total recaudado del operario y reinicia su caja |
| `consultar_disponibilidad()` | Calcula cupos libres, % de ocupación y alerta del 90 % |
| `mostrar_auditoria()` | Muestra ingresos globales, pagos, turnos y tiquetes anulados |
| `exportar_reporte()` | Escribe `reporte_parqueadero.txt` |
| `buscar_usuario()`, `buscar_vehiculo()`, `buscar_tarifa()` | Devuelven la posición en la lista o -1 |
| `contar_vehiculos()`, `calcular_tiempo()` | Cuentan vehículos por tipo y calculan minutos |
| `menu_admin()`, `menu_operario()`, `main()` | Coordinan los menús y el programa |

## 📦 Datos del programa

- `usuarios`: `[nombre, contraseña, rol, activo]`
- `tarifas`: `[tipo, fracción, hora, día, mes]`
- `capacidad`: `[tipo, cupos]`
- `vehiculos`: `[identificador, tipo, marca, color, novedades, operario, hora_ingreso]`
- `transacciones`: `[identificador, tipo, operario, monto, estado]`
- `turnos_cerrados` y `tiquetes_anulados`: historial de cierres y anulaciones.
- `caja_global` y `caja_operario`: totales recaudados.

## ✅ Pruebas sugeridas

| Prueba | Resultado esperado |
|---|---|
| Iniciar sesión con contraseña incorrecta | Error de contraseña |
| Iniciar sesión con una cuenta desactivada | Error de cuenta desactivada |
| Ingresar dos veces la misma placa | Error: el vehículo ya está dentro |
| Ingresar una moto con la zona llena | Alerta de que no hay cupos |
| Consultar disponibilidad con 90 % o más | Muestra la alerta |
| Registrar salida de un vehículo que no existe | Aviso de que no se encontró |
| Registrar salida y confirmar el pago | Suma el monto a la caja del operario |
| Cerrar turno | Guarda el total y reinicia la caja del operario |
| Exportar reporte | Crea `reporte_parqueadero.txt` |

## 🚧 Limitaciones

- **El cobro usa una tarifa de prueba fija** de $3.000 por minuto. Las tarifas que configura el administrador todavía no se usan al cobrar.
- Los datos viven en memoria: al cerrar el programa se pierden. Lo único que se guarda es el reporte de texto.
- Las contraseñas se guardan sin cifrar.
- Al cambiar la capacidad no se revisa cuántos vehículos hay dentro.
- No tiene interfaz web ni móvil, ni pagos en línea.

## 👥 Autores

David Pérez · Diego Acosta · Leonadis Palencia · Kelldryn Martínez · Edwin Matos
