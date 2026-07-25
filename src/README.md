# Fundamentos de Python – Estructuras de control y funciones

Este proyecto es un recorrido práctico por las bases fundamentales de Python. Aquí integramos estructuras condicionales, bucles repetitivos y funciones en un solo lugar.

## 📁 Organización del Proyecto
Todo nuestro código vive dentro de la carpeta src/, dividida en tres grandes áreas:

condicionales/: Cómo tomar decisiones en el código (ejercicios con if, match-case, operadores lógicos, ternarias y cortocircuitos).

iterativas/: Cómo automatizar la repetición (bucles for y while, comprensión de listas, y controles como break o continue).

funciones/: Cómo crear herramientas reutilizables (definición básica, manejo de parámetros, *args, **kwargs, retornos y docstrings).

```
fundamentos_python_control_fun/
└── src/
    ├── condicionales/
    │   ├── if_simple.py
    │   ├── if_else.py
    │   ├── if_elif_else.py
    │   ├── match_case.py
    │   ├── operadores_logicos.py
    │   ├── condicionales_anidados.py
    │   ├── expresiones_ternarias.py
    │   └── cortocircuito.py
    ├── iterativas/
    │   ├── for_basico.py
    │   ├── comprension_listas.py
    │   ├── for_anidado.py
    │   ├── while_basico.py
    │   ├── while_eventos.py
    │   ├── break_continue.py
    │   └── pass_else.py
    └── funciones/
        ├── funcion_basica.py
        ├── parametros_argumentos.py
        ├── return_valores.py
        └── docstrings.py
```

⚙️ Lo que necesitas
Es indispensable tener instalado Python 3.10 o superior. Esto es vital porque usamos características modernas del lenguaje, como la estructura match-case.

```
# Condicionales
python3 src/condicionales/if_simple.py
python3 src/condicionales/if_else.py
python3 src/condicionales/if_elif_else.py
python3 src/condicionales/match_case.py
python3 src/condicionales/operadores_logicos.py
python3 src/condicionales/condicionales_anidados.py
python3 src/condicionales/expresiones_ternarias.py
python3 src/condicionales/cortocircuito.py

# Iterativas
python3 src/iterativas/for_basico.py
python3 src/iterativas/comprension_listas.py
python3 src/iterativas/for_anidado.py
python3 src/iterativas/while_basico.py
python3 src/iterativas/while_eventos.py
python3 src/iterativas/break_continue.py
python3 src/iterativas/pass_else.py

# Funciones
python3 src/funciones/funcion_basica.py
python3 src/funciones/parametros_argumentos.py
python3 src/funciones/return_valores.py
python3 src/funciones/docstrings.py
```

🚀 Cómo ponerlo a prueba
Para ejecutar cualquier ejercicio, abre tu terminal desde la raíz del proyecto y llama al archivo específico. Aquí tienes un ejemplo de cómo hacerlo:

python3 src/condicionales/if_simple.py

(Simplemente cambia la ruta final para explorar cualquier otro archivo de las carpetas condicionales, iterativas o funciones).