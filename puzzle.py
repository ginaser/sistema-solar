import sys
import random

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
import pygame

from utils import ImagenSprite, SuperficieSprite, COLORES

class ClaseBase(object):

    def convertir_porcentaje(self, ancho, alto):
        '''translates percentages to screen positions'''
        x = (ancho / 100.0) * self.ancho
        y = (alto / 100.0) * self.alto
        return x, y

class Main(ClaseBase):
    '''clase principal de inicio de juego'''

    def correr(self):
        '''Inicia el juego!'''
        self.superficie = pygame.display.get_surface()
        rect_superficie = self.superficie.get_rect()
        self.ancho = rect_superficie.width
        self.alto = rect_superficie.height
        self.superficie.fill(COLORES['blanco'])
        self.fuente = pygame.font.SysFont("monospace", 60)
        texto = self.fuente.render("BIENVENID@S!", 1, COLORES['verde'])
        self.superficie.blit(texto, self.convertir_porcentaje(25, 40))

        pygame.display.update()
        self.detectar_click()

    def detectar_click(self):
        while True:
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    try:
                        pygame.quit()
                        sys.exit()
                        return
                    except Exception, e:
                        return
                elif event.type == pygame.MOUSEBUTTONUP:
                    #mandamos a la siguiente pantalla
                    Rompecabeza((self.ancho, self.alto)).correr()
                else:
                    continue


class Rompecabeza(ClaseBase):

    lista_imagenes = [ '1', '2', '3', '4',]

    grupo_imagenes = pygame.sprite.Group()
    grupo_cuadros = pygame.sprite.Group()
    grupo_resueltas = pygame.sprite.Group()
    imagen_activa = None

    def __init__(self, tamano_pantalla):
        self.ancho, self.alto = tamano_pantalla
        self.superficie = pygame.display.get_surface()
        self.fondo = pygame.Surface((self.ancho, self.alto))
        self.fondo.fill(COLORES['gris'])
        self.fuente = pygame.font.SysFont("monospace", 30)

    def correr(self):
        #poniendo el fondo
        self.desordenar_lista()
        self.superficie.blit(self.fondo, (0, 0))

        texto = self.fuente.render("Arma el Sistema Solar", 1, COLORES['verde'])
        self.superficie.blit(texto, self.convertir_porcentaje(25, 5))

        #dibujamos los cuadros meta
        self.inicializar_cuadros()
        self.dibujar_cuadros()

        #dibujamos los cuadros de la OLPC
        self.inicializar_imagenes()
        self.dibujar_imagenes()

        pygame.display.update()
        self.detectar_click()

    def inicializar_imagenes(self):
        self.grupo_imagenes.empty()
        #self.grupo_imagenes.clear()
        x, y = self.convertir_porcentaje(5, 80)

        for img in self.lista_imagenes:
            #creamos un sprite por cada imagen
            nombre_archivo = 'img/%s.png' % img
            sprite = ImagenSprite(nombre_archivo, (x, y), nombre=img, escalar=(100, 100))
            self.grupo_imagenes.add(sprite)

            #aumentamos x para que no se solape
            x += sprite.rect.width + 20

    def dibujar_imagenes(self):
        #dibujamos todos
        self.grupo_imagenes.draw(self.superficie)
        self.grupo_resueltas.draw(self.superficie)

    def inicializar_cuadros(self):
        self.grupo_cuadros.empty()
        #self.grupo_cuadros.clear()
        x, y = self.convertir_porcentaje(40, 30)

        sprite = SuperficieSprite(COLORES['rojo'], (100, 100),  (x, y), nombre='1')
        self.grupo_cuadros.add(sprite)

        x += 100
        sprite = SuperficieSprite(COLORES['verde'], (100, 100),  (x, y), nombre='2')
        self.grupo_cuadros.add(sprite)

        x -= 100
        y += 100
        sprite = SuperficieSprite(COLORES['blanco'], (100, 100),  (x, y), nombre='3')
        self.grupo_cuadros.add(sprite)

        x += 100
        sprite = SuperficieSprite(COLORES['negro'], (100, 100),  (x, y), nombre='4')
        self.grupo_cuadros.add(sprite)


    def dibujar_cuadros(self):
        self.grupo_cuadros.draw(self.superficie)


    def detectar_click(self):
        while True:
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    try:
                        pygame.quit()
                        sys.exit()
                        return
                    except Exception, e:
                        return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    imagenes_tocadas = [s for s in self.grupo_imagenes\
                                       if s.rect.collidepoint(pos)]

                    if imagenes_tocadas:
                        self.imagen_activa = imagenes_tocadas[0]
                        print self.imagen_activa
                    else:
                        self.imagen_activa = None
                        continue

                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.imagen_activa:
                        #detectamos donde cae
                        pos = pygame.mouse.get_pos()
                        cuadros_tocados = [s for s in self.grupo_cuadros\
                                           if s.rect.collidepoint(pos)]
                        if cuadros_tocados:
                            cuadro = cuadros_tocados[0]
                            if self.imagen_activa.nombre == cuadro.nombre:
                                self.superficie.blit(self.fondo, self.imagen_activa.rect, self.imagen_activa.rect)
                                self.imagen_activa.mover(self.superficie, self.fondo,
                                                         (cuadro.rect.left, cuadro.rect.top))
                                #eliminamos la imagen del grupo
                                self.imagen_activa.remove(self.grupo_imagenes)
                                self.imagen_activa.add(self.grupo_resueltas)
                                self.lista_imagenes.remove(self.imagen_activa.nombre)
                                self.dibujar_cuadros()
                                self.dibujar_imagenes()
                                pygame.display.update()
                                #TODO: Aca aumentar puntaje, revisar si ya gana
                            else:
                                self.superficie.blit(self.fondo, self.imagen_activa.rect, self.imagen_activa.rect)
                                self.imagen_activa.mover(self.superficie, self.fondo,
                                                         self.imagen_activa.posicion_inicial)
                                self.dibujar_cuadros()
                                self.dibujar_imagenes()
                                pygame.display.update()
                        else:
                            self.superficie.blit(self.fondo, self.imagen_activa.rect, self.imagen_activa.rect)
                            self.imagen_activa.mover(self.superficie, self.fondo,
                                                        self.imagen_activa.posicion_inicial)
                            self.dibujar_cuadros()
                            self.dibujar_imagenes()
                            pygame.display.update()

                    self.imagen_activa = None
                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    if self.imagen_activa:
                        #borramos la anterior posicion
                        self.superficie.blit(self.fondo, self.imagen_activa.rect, self.imagen_activa.rect)
                        self.imagen_activa.mover(self.superficie, self.fondo,
                                                 pos)
                        self.dibujar_cuadros()
                        self.dibujar_imagenes()
                        pygame.display.update()

                    else:
                        print 'no hay imagen activa'
                else:
                    continue

    def desordenar_lista(self):
        random.shuffle(self.lista_imagenes)



if __name__ == "__main__":
    main = Main((800, 600))
    main.correr()
