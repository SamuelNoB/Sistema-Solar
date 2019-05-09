import arcade
import random
import math
import os


class Planeta:
    def __init__(self, x=0, y=0,centro=(0, 0), nomearquivo = ""):
        self.x = x
        self.y = y
        self.centro = centro
        self.raioDistancia = math.sqrt((self.x - self.centro[0])**2 + (self.y - self.centro[1])**2)
        self.angulo=0
        self.Nome = nomearquivo
        self.planeta = None

    def atualizar(self, deltaT):
        self.x = self.centro[0] + (self.raioDistancia) * math.cos(math.radians(self.angulo))
        self.y = self.centro[1] + (self.raioDistancia) * math.sin(math.radians(self.angulo))
        self.angulo += 1.5

    def cria_planeta(self):

        self.planeta = arcade.Sprite(self.Nome, 1)
        self.planeta.center_x = self.x
        self.planeta.center_y = self.y
        

class Estrelas:
    def __init__(self, lim_x=0, lim_y=0):
        
        self.listaestrelas = []
        self.N = 350
        self.lim_x = lim_x
        self.lim_y = lim_y

    def cria_estrela(self):
        for i in range(self.N):
            Spritescale = random.randint(3, 9)
            Spritescale = Spritescale/10
            x =  random.randint(0,self.lim_x)
            y = random.randint(0,self.lim_y)
            estrela = None
            
            estrela = arcade.Sprite("sprites/estrela1.png", Spritescale)

            estrela.center_x = x
            estrela.center_y = y

            self.listaestrelas.append(estrela)


class Sistema:
    def __init__(self, comprimento=1200, altura=800):
        self.comprimento = comprimento 
        self.altura = altura
        self.centro = (self.comprimento/2, self.altura/2)
        self.backgorund = (0, 0, 0)
        self.sol = Planeta(x=self.centro[0], y=self.centro[1],centro=self.centro, nomearquivo="sprites/Sol.png")
        
        self.estrelas = Estrelas(self.comprimento, self.altura)
        self.estrelas.cria_estrela()

        self.terra = Planeta(x=(comprimento/2) + 200,y=self.altura/2, centro=self.centro, nomearquivo="sprites/planeta.png")
        self.time = 0
        
    def atualizar(self, deltaT):
        self.time += deltaT
        self.terra.atualizar(deltaT)
        
    def desenhar(self, a):

        arcade.start_render()
        for i in range(self.estrelas.N):
            self.estrelas.listaestrelas[i].draw()

        self.terra.cria_planeta()
        self.sol.cria_planeta()
        
        self.terra.planeta.draw()
        self.sol.planeta.draw()
        
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