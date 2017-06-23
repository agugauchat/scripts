import pilasengine
import random

pilas = pilasengine.iniciar()

class Bala(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "bala.png"
        self.figura_de_colision = pilas.fisica.Rectangulo(0,0, 35, 0, False)
        self.escala = 0.23
        self.y = 260
        self.contador = 0
        self.x = random.randint(-270, 270)
        self.aprender(pilas.habilidades.EliminarseSiSaleDePantalla)
    def actualizar(self):
        if mario.escala != 0.255:
            self.y -= 4   
        else:
            self.eliminar() 

class Vida(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "vida.png"
        self.figura_de_colision = pilas.fisica.Rectangulo(0,0, 35, 0, False)
        self.escala = 0.4
        self.y = 260
        self.contador = 0
        self.x = random.randint(-270, 270)
        self.aprender(pilas.habilidades.EliminarseSiSaleDePantalla)
    def actualizar(self):
        if mario.escala != 0.255:
            self.y -= 4  
        else:
            self.eliminar() 

class Mario(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "mario.png"
        self.figura_de_colision = pilas.fisica.Rectangulo(0,0, 60, 50, False)
        self.escala = 0.14
        self.abajo = -231
        self.centro_y = 173
        self.aprender(pilas.habilidades.EliminarseSiSaleDePantalla)
    def actualizar(self):
        if self.escala != 0.255:
            if pilas.control.izquierda and self.x!= -290:
                self.x -= 5
                self.espejado = True
            if pilas.control.derecha and self.x!= 290:
                self.x += 5
                self.espejado = False
        if self.escala == 0.255:
            self.y -= 1

pilas.avisar("Usa las flechas para que no te toquen las balas.")
mario = Mario(pilas)
balas = []
vidas = []

def crear_bala():
    bala = Bala(pilas)
    balas.append(bala)
    return True

def crear_vida():
    vida = Vida(pilas)
    vidas.append(vida)
    return True

pilas.tareas.agregar(0.3, crear_bala)
pilas.tareas.agregar(1, crear_vida)


def eliminar(mario, balas):
    if mario.escala == 0.14:
        mario.figura_de_colision = pilas.fisica.Rectangulo(0,0, 95, 95, False)
        mario.escala = 0.24
        mario.abajo = -231
        mario.centro_y = 173
        balas = []
    else:
        mario.imagen = "mariomuerto.png"
        mario.abajo = -225
        mario.escala = 0.255
        texto = pilas.actores.Texto("Game Over", y=0, x=65, ancho=200)
        texto.escala = 2

pilas.colisiones.agregar(mario, balas, eliminar)

fondo = pilas.fondos.Tarde()

pilas.ejecutar()