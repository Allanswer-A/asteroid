# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from  player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	print( "Starting asteroids!")
	print( f"Screen width: {SCREEN_WIDTH}")
	print( f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0 
	asteroids = pygame.sprite.Group()
	drawable   = pygame.sprite.Group()
	updatable  = pygame.sprite.Group()
	shoots  = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	Player.containers = (drawable, updatable)
	Shot.containers = (drawable, updatable ,shoots)
	AsteroidField.containers = (updatable,)
	player = Player( SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)	
	asfield = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		screen.fill("black")
		
		for sprite in drawable:
			sprite.draw(screen)
		dt = clock.tick(60) / 1000
		updatable.update(dt)
		for ast in asteroids:
			if player.collision(ast):
				print("Game over!")
				raise Exception("Game over!")

		for ast in asteroids:
			for shot in shoots:
				if shot.collision(ast):
					ast.split()
					shot.kill()

		pygame.display.flip()



if __name__ == "__main__":
	main()