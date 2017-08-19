import pygame
from pygame.sprite import Sprite

class ShipBullet(Sprite):
	"""A class to represent the bullet aka ShipBullet fired from a ship."""
	def __init__(self, ai_settings, screen, ship):
		"""Initializes ShipBullet settings."""
		super().__init__()
		self.ai_settings = ai_settings
		self.screen = screen
		
		# Loads image and get image rect.
		self.image = pygame.image.load('images/projectiles/ships/bullet.bmp')
		self.rect = self.image.get_rect()
		
		# Position the bullet that will be fired out of the ship/object.
		self.rect.centery = ship.rect.centery + 16
		self.rect.right = ship.rect.right - 50
		
		# Float values to a new variable if not decimals will not be registered.
		self.x = float(self.rect.x)
		
	def update(self):
		"""Updates the position of the ShipBullet."""
		# ShipBullet will be fired to the right, so just add the x like so.
		self.x += self.ai_settings.ship_bullet_speed_factor
		
		# Float values are converted to integers and assigned back to the rect.
		self.rect.x = self.x
		
	def draw_bullet(self):
		"""Draws the ShipBullet onto the screen."""
		# Only for individual bullets, sprites are prefered to use 
		# self.draw(self.screen) or shipbullets.draw(screen)
		self.screen.blit(self.image, self.rect)

class HelicopterBullet(Sprite):
	"""A class to represent the HelicopterBullet fired from a helicopter."""
	def __init__(self, ai_settings, screen, heli):
		"""Initializes the HelicopterBullet settings."""
		super().__init__()
		self.ai_settings = ai_settings
		self.screen = screen
		
		# Loads the image and get image rect.
		self.image = pygame.image.load('images/projectiles/hostiles/helicopterbullet.bmp')
		self.rect = self.image.get_rect()
		
		# Position the HelicopterBullet that will be fired out from a helicopter.
		self.rect.centery = heli.rect.centery + 13
		self.rect.left = heli.rect.left# + 20
		
		# Float values to a new variable if not decimals will not be registered.
		self.x = float(self.rect.x)
		
	def update(self):
		"""Updates the position of the HelicopterBullet."""
		# HelicopterBullet will be fired to the left, so just minus x like so.
		self.x -= self.ai_settings.helicopter_bullet_speed_factor
		
		# Float values are converted to integers and assinged back to the rect.
		self.rect.x = self.x
		
	def draw_bullet(self):
		"""Draws the HelicopterBullet onto the screen."""
		# Only for individual bullets, sprites are prefered to use 
		# self.draw(self.screen) or helibullets.draw(screen)
		self.screen.blit(self.image, self.rect)
