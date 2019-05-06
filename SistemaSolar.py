import arcade
import random
import math
import os

Spritescale = 0.3


class Planeta:
    def __init__(self, raio=100, x=0, y=0, cor=(255, 255, 0), centro=(0, 0)):
        self.raio = raio
        self.x = x
        self.y = y
        self.cor = cor
        self.centro = centro
        self.raioDistancia = math.sqrt((self.x - self.centro[0])**2 + (self.y - self.centro[1])**2)
        self.angulo=0

    def atualizar(self, deltaT):
        self.x = self.centro[0] + (self.raioDistancia) * math.cos(math.radians(self.angulo))
        self.y = self.centro[1] + (self.raioDistancia) * math.sin(math.radians(self.angulo))
        self.angulo += 5

    def cria_planeta(self):
        arcade.draw_circle_filled(
            self.x, self.y,
            self.raio,
             self.cor)

        
class Estrelas:
    def __init__(self, lim_x=0, lim_y=0):
        self.localizaçaoestrelas = ["sprites/estrela1.png", "sprites/estrela2.png", 
                                                           "sprites/estrela3.png", "sprites/estrela4.png",
                                                           "sprites/estrela5.png"]
        self.listaestrelas = []
        self.N = 200
        self.lim_x = lim_x
        self.lim_y = lim_y

    def cria_estrela(self):

        for i in range(self.N):
            x =  random.randint(0,self.lim_x)
            y = random.randint(0,self.lim_y)
            estrela = None
            tipostar = random.randint(0, 4)
            estrela = arcade.Sprite(self.localizaçaoestrelas[tipostar], Spritescale)

            estrela.center_x = x
            estrela.center_y = y

            self.listaestrelas.append(estrela)

class Sistema:
    def __init__(self, comprimento=1200, altura=800):
        self.comprimento = comprimento 
        self.altura = altura
        self.centro = (self.comprimento/2, self.altura/2)
        self.backgorund = (0, 0, 0)
        self.sol = Planeta(raio=50, x=self.centro[0], y=self.centro[1])
        
        self.estrelas = Estrelas(self.comprimento, self.altura)
        self.estrelas.cria_estrela()

        self.terra = Planeta(raio=10, x=(comprimento/2) + 200,y=self.altura/2, cor=(0, 0, 255), centro=self.centro)
        self.time = 0
        
    def atualizar(self, deltaT):
        self.time += deltaT
        self.terra.atualizar(deltaT)
        
    def desenhar(self, a):

        arcade.start_render()
        for i in range(200):
            self.estrelas.listaestrelas[i].draw()

        self.terra.cria_planeta()
        self.sol.cria_planeta()
        
    def run(self):
        arcade.open_window(self.comprimento, self.altura,'Sistema Solar')
        arcade.set_background_color(self.backgorund)
       
       
        arcade.schedule(self.atualizar, 1/60)
        arcade.schedule(self.desenhar, 1/60)
        arcade.run()
        arcade.close_window()

if __name__ == "__main__":

    Sistema_solar = Sistema()

    
    Sistema_solar.run()