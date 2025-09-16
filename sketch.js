// sketch.js - Lógica para dibujar con p5.js

/**
 * La función setup() se ejecuta una vez al inicio.
 */
function setup() {
  // Crear un lienzo de 600x600 píxeles donde dibujaremos
  createCanvas(600, 600);
  // Cambiar el modo de ángulo a grados para que sea más intuitivo (0-360)
  angleMode(DEGREES);
}

/**
 * La función draw() se ejecuta en bucle, creando la animación.
 */
function draw() {
  // Dibujar un fondo de cielo azul
  background(135, 206, 235);

  // --- DIBUJO DEL GIRASOL ---

  // Mover el punto de origen (0,0) al centro del lienzo.
  // Esto hace que sea más fácil dibujar formas centradas y rotarlas.
  translate(width / 2, height / 2);

  // Tallo
  strokeWeight(10); // Grosor de la línea
  stroke(34, 139, 34); // Color verde oscuro para el borde
  line(0, 100, 0, 250); // Dibuja una línea desde abajo del centro hacia abajo

  // Hojas
  noStroke(); // Quitar el borde para las hojas
  fill(50, 205, 50); // Color verde lima
  ellipse(-40, 150, 80, 25); // Dibuja una elipse para la hoja izquierda
  ellipse(40, 180, 80, 25); // Dibuja una elipse para la hoja derecha

  // Pétalos amarillos
  // Primero dibujamos los pétalos para que el centro quede por encima
  fill(255, 223, 0); // Color amarillo dorado
  noStroke();
  for (let i = 0; i < 12; i++) {
    // Rotamos el lienzo en cada iteración para dibujar el siguiente pétalo
    rotate(360 / 12);
    // Dibuja una elipse (el pétalo) a cierta distancia del centro
    ellipse(0, 80, 50, 100);
  }

  // Centro del girasol (semillas)
  fill(139, 69, 19); // Color marrón
  ellipse(0, 0, 100, 100); // Dibuja un círculo en el nuevo origen (el centro)
}
