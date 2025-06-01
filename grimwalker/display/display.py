import sdl2, sdl2.ext
import grimwalker.display.sprite.spriteManager

class Window(sdl2.ext.Window):
	def __init__(self, title=f"GRIMWALKER Engine {grimwalker.__version__}", size: tuple):
		super().__init__(title, size)
		self.sprite_manager = SpriteManager()