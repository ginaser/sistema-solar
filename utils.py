import pygame

COLORES = {
    'blanco': (255, 255, 255),
    'negro': (0, 0, 0),
    'gris': (130, 130, 130),
    'rojo': (255, 0, 0),
    'verde': (0, 255, 0),
}

#documentacion de sprite: https://www.pygame.org/docs/ref/sprite.html
class ImagenSprite(pygame.sprite.Sprite):
    '''Clase para hacer un sprite a partir de una imagen'''

    def __init__(self, archivo, locacion=(0, 0), nombre=None, escalar=None):
        '''
            archivo: ruta del archivo
            locacion: tupla con coordenadas para definir locacion inicial de la imagen
            nombre: nombre de la imagen
            escalar: tupla para cambiar el tamano de imagen
        '''
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        #convert_alpha para conservar transparencias si tiene
        self.image = pygame.image.load(archivo).convert_alpha()
        if escalar:
            self.image = pygame.transform.scale(self.image, escalar)

        self.nombre = nombre
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = locacion
        #usado para resetear la imagen
        self.posicion_inicial = locacion

    def mover(self, pantalla, fondo,  posicion):
        self.rect.left, self.rect.top = posicion
        pantalla.blit(self.image, self.rect)

class SuperficieSprite(pygame.sprite.Sprite):
    '''Clase para hacer un sprite a partir de una superficie'''

    def __init__(self, color, tamano, locacion=(0, 0), nombre=None):
        '''
            color: el color que seleccionamos
            locacion: tupla con coordenadas para definir locacion inicial de la imagen
            nombre: nombre de la superficie
            escalar: tupla para cambiar el tamano de imagen
        '''
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(tamano)
        self.image.fill(color)

        self.nombre = nombre
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = locacion


