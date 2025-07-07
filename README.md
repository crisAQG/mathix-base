# 📐 Mathix

Mathix es una librería modular y expandible de matemáticas y física, diseñada para proyectos educativos, científicos y de videojuegos (incluyendo el juego en proceso de creacion Proyect-Genesis). Incluye módulos para aritmética, física, aleatorización, geometría, inteligencia artificial y más.

> **Versión actual:** `v1.11`
> **Autor:** Cristian Quezada Gana

---

## 📦 Contenido por módulos

### 1. arithmetic.py

#### Operaciones aritméticas generalizadas:

abs(x) — valor absoluto.

floor(x) — redondeo hacia abajo.

ceil(x) — redondeo hacia arriba.

gcd(a, b) — máximo común divisor.

lcm(a, b) — mínimo común múltiplo.

pow(base, exp) — potencia.

sqrt(x) — raíz cuadrada (con aproximación iterativa).

### 2. algebra.py

#### Operaciones algebraicas generalizadas:

exp(x) — función exponencial.

log(base) — función logarítmica.

solve\_quadratic(a, b, c) — solución de función cuadrática.

simplify\_addition(expr) — simplificación de sumas en expresión.

### 3. statistics.py

#### Estadística básica e intermedia:

binomial\_probability(n, k, p) — distribución binomial.

normal\_pdf(x) — distribución gaussiana (o normal) basada en el valor x del eje horizontal.

mean(data) — media de un conjunto de datos.

variance(data) — varianza de un conjunto de datos.

median(data) — mediana de un conjunto de datos.

### 4. discrete\_probability.py

#### Probabilidades discretas:

combinations(n, r) — combinaciones de n elementos tomados de r en r.

permutations(n, r) — permutaciones de n elementos tomados de r en r.

### 5. geometry\_2d.py

#### Geometría computacional:

distance(p1, p2) — distancia euclidiana entre dos puntos (x1, y1), (x2, y2).

manhattan\_distance(p1, p2) — distancia entre dos puntos (x1, y1), (x2, y2) en un espacio euclidiano con un sistema de coordenadas cartesianas.

angle\_between(v1, v2) — ángulo formado entre dos vectores (en radianes).

rotate\_point(px, py, cx, cy, angle\_rad) — rota un punto (px, py) alrededor de (cx, cy) en radianes.

line\_intersects(p1, p2, q1, q2) — determina si los segmentos p1-p2 y q1-q2 se cruzan.

point\_in\_polygon(point, polygon) — determina si un punto está dentro de un polígono (método ray casting).

### 6. trigonometry.py

#### Trigonometría básica e intermedia (medida en radianes):

sin(x) — seno de x.

cos(x) — coseno de x.

tan(x) — tangente de x.

arcsin(x) — arco-seno de x.

arccos(x) — arco-coseno de x.

arctan(x) — arco-tangente de x.

### 7. calculus.py

#### Conceptos de cálculo (límites, derivadas e integrales):

limit(f, x) — límite de la función f cuando x se acerca a x = n.

derivative(f, x) — derivada de una función con respecto a x.

integral(f, a, b) — integral de la función f con respecto al límite inferior a y el límite superior b.

symbolic\_derivative(expr) — derivada simbólica de la función expr.

symbolic\_integral(expr) — integral simbólica de la función expr.

### 8. matrix.py

#### Operaciones de matrices bidimensionales:

matrix\_add(A, B) — suma de matrices.

matrix\_subtract(A, B) — resta de matrices.

matrix\_multiply(A, B) — multiplicación de matrices.

matrix\_transpose(A) — matriz transpuesta.

matrix\_determinant(A) — determinante de una matriz.

### 9. random.py

#### Módulo random():

random() — número flotante entre 0 y 1.

randint(a, b) — número entero entre a y b.

uniform(a, b) — número flotante aleatorio entre a y b.

choice(seq) — retorna un elemento aleatorio de una lista.

shuffle(seq) — reorganiza aleatoriamente una lista.

sample(seq, k) — retorna una lista con k elementos únicos aleatorios de una lista seq.

choices(population, k, weights) — selecciona k elementos aleatorios con reemplazo. Soporta pesos personalizados.

### 10. noise2.py

#### Módulo noise2():

get(x, y) — retorna valores normalizados entre 0 y 1 en base a x e y, escalados por la amplitud.

### 11. ai\_logic.py

#### Módulo ai\_logic():

chase\_target(enemy\_pos, target\_pos, speed) — persecución.

flee\_target(enemy\_pos, threat\_pos, speed) — huida.

patrol(waypoints, current\_index, position, speed) — patrullaje entre puntos.

can\_see(pos\_a, pos\_b, max\_distance) — visión por rango.

#### Módulo priority\_target\_ai():

select\_target(visible\_targets) — lista de prioridades en tuplas a elegir.

update\_priorities(new\_priorities) — permite reordenar prioridades en tiempo real.

#### Módulo pathfinder():

find\_path(start, goal) — deduce la ruta más corta en el mapa para recorrer.

### 12. interpolation.py

#### Interpolación y suavizado:

lerp(a, b, t) — interpolación lineal entre a y b con t en \[0, 1].

inverse\_lerp(a, b, value) — devuelve el t tal que lerp(a, b, t) == value.

remap(in\_min, in\_max, out\_min, out\_max, value) — remapea value de un rango a otro.

ease\_in/out (cuadrático y cúbico) — suavizado de animaciones o desplazamientos.

### 13. physics\_2d.py

#### Módulo physics\_2d():

apply\_gravity(velocity, gravity\_scale) — aplica gravedad escalada a un vector de velocidad.

apply\_friction(velocity) — aplica fricción reduciendo la velocidad (top-down logic).

update\_position(position, velocity) — actualiza la posición de un objeto según su velocidad actual.

bounce(velocity, normal, elasticity) — calcula el vector de rebote contra una superficie con una normal dada.

limit\_speed(velocity, max\_speed) — limita la magnitud de la velocidad al valor máximo permitido.

handle\_piercing(projectile) — gestiona lógica de perforación del proyectil (atraviesa enemigos).

---

## 📥 Instalación

### Desde GitHub:

```bash
pip install git+https://github.com/crisAQG/mathix-base.git
```

---

## ⚖️ Licencia

MIT — Puedes usarla, modificarla o distribuirla libremente, siempre dando crédito.
