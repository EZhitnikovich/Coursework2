import pygame_menu
from pygame_menu.themes import Theme

menuTheme = Theme()

menuTheme.background_color = pygame_menu.baseimage.BaseImage(image_path="sprites/background.png",
                                                             drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
                                                             drawing_offset=(0, 0))

menuTheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE_TITLE
menuTheme.title_background_color = (90, 52, 145)
menuTheme.title_font_color = (90, 52, 145)
menuTheme.widget_font = "comic sans ms"
menuTheme.title_font = "comic sans ms"
menuTheme.menubar_close_button = False
