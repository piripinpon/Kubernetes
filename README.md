# 📘 Proyecto: Calculadora en Kubernetes

Este proyecto despliega una aplicación de calculadora usando **Docker**, **Kubernetes** y un servicio **NodePort** para exponerla hacia el exterior.

Incluye:

* API hecha en Python + Flask
* Dockerfile para construir la imagen
* Deployment de Kubernetes
* Service para exponer la API
* Diagramas explicativos

---

# 🧩 Arquitectura del Proyecto

## 🔷 Diagrama general de Arquitectura

```
+------------------------------+
|        Usuario/Cliente       |
|  (Navegador / Postman)       |
+--------------+---------------+
               |
               |  HTTP Request (localhost:30000)
               v
+------------------------------+
|        Service (NodePort)    |
|  - Expone puerto 30000       |
|  - Redirige al puerto 5000   |
+--------------+---------------+
               |
               |  Redirección interna del cluster
               v
+------------------------------+
|       Deployment             |
|  - 2 réplicas                |
|  - Selector: app=calculadora |
+--------------+---------------+
   |                        |
   | Pod 1                  | Pod 2
   v                        v
+--------+            +--------+
| Flask  |            | Flask  |
| API    |            | API    |
| 5000   |            | 5000   |
+--------+            +--------+
```

El Service balancea el tráfico entre los pods gracias a que comparten la etiqueta:

# 📄 Archivos del Proyecto

## 1️⃣ app.py — Lógica de la Calculadora (API Flask)

Este archivo contiene la lógica de la calculadora en forma de API.
Ejemplo:

* `/sumar?a=10&b=5` → `{ "resultado": 15 }`

Funciona sobre el puerto **5000**.

---

## 2️⃣ Dockerfile — Construcción de la Imagen

Define cómo construir la imagen con:

* Python base
* Dependencias
* Copia de archivos
* Comando de inicio

La imagen final se sube a Docker Hub para que Kubernetes pueda descargarla.

---

## 3️⃣ deployment.yaml — Define los Pods y Réplicas

Crea un **Deployment** con:

* 2 réplicas
* La imagen `alexis246/calculadora-k8s:v1`
* Puerto 5000 expuesto en cada contenedor

<img width="486" height="135" alt="image" src="https://github.com/user-attachments/assets/7f4519a6-dea1-4ea7-aac4-be7a5b5d470e" />


Kubernetes mantendrá siempre las dos réplicas activas.

---

## 4️⃣ service.yaml — Expone la API hacia tu PC

Este archivo crea un **Service NodePort**, que:

* Abre el puerto **30000** en tu PC (host)
* Redirige a los puertos 5000 de los pods

<img width="298" height="89" alt="image" src="https://github.com/user-attachments/assets/24e5ad42-3043-4ea7-bfc9-4a0d8414187d" />

URL resultante:

```
http://localhost:30000/sumar?a=10&b=5
```

---

# 🚀 Flujo de despliegue

1. **Construcción de imagen Docker**
2. **Carga de imagen a Docker Hub**
3. **Aplicación del Deployment** con 2 pods
4. **Service NodePort** expone la API localmente
5. El usuario accede mediante `localhost:30000`

# Resulatado del localhost

<img width="569" height="243" alt="Captura de pantalla 2025-11-14 105209" src="https://github.com/user-attachments/assets/7f959cb5-4578-43d9-be44-99f3e269f995" />

# Comandos ejecutados en CMD para desarrollo de actividad

Aqui damos de alta el puerto donde estara el flask
<img width="1098" height="377" alt="image" src="https://github.com/user-attachments/assets/d09c36ef-5fc3-4bba-bf47-9babc7eebfa5" />

Aqui hacemos que el puerto 30000 corra como salida en nuestra PC, usando estos comandos hacemos que cambie a 1.
<img width="833" height="194" alt="image" src="https://github.com/user-attachments/assets/21a66771-763a-47ff-9ac5-45ee60e814b4" />




