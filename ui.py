import pygame

class TextBox:
    def __init__(self, x = 0, y= 0, font_size = 64, font_colour = (0, 0, 0), text="Placeholder"):
        self.x = x
        self.y = y
        self.text = text
        self.font_size = font_size
        self.font_colour = font_colour
    def draw(self, win):
        my_surface = pygame.font.Font(None, self.font_size).render(self.text, True, self.font_colour)
        win.blit(my_surface, (self.x, self.y))

class Background:
    def __init__(self, colour=(255, 255, 255)):
        self.colour = colour
    def draw(self, win):
        win.fill(self.colour) 

class Panel:
    def __init__(self, x=0, y=0, width=64, height=64, colour=(200, 200, 200)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))     

class Button:
    def __init__(self, x=0, y=0, width=64, height=64, passive_colour=(255, 255, 255), active_colour=(0, 0, 0), font_size=32, active_font=(255, 255, 255), passive_font=(0, 0, 0), border_width=10, icon_type="Text", icon="Demo", item_id="default"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.passive_colour = passive_colour
        self.active_colour = active_colour
        self.colour = passive_colour
        self.border_width = border_width

        self.font_size = font_size
        self.active_font = active_font
        self.passive_font = passive_font
        self.font_colour = passive_font
        self.font = pygame.font.Font(None, self.font_size)

        self.icon_type = icon_type
        self.icon = icon
        self.item_id = item_id
        self.active = False

        text_surface = self.font.render(self.icon, True, self.font_colour)
        text_surface_rect = pygame.Surface(text_surface.get_size())
        self.rect = pygame.Rect(self.x, self.y, text_surface_rect.get_width(), text_surface_rect.get_height())

    def draw(self, win):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mouse):
            self.active = True
        else:
            self.active = False

        if click[0] and self.rect.collidepoint(mouse):
            return self.item_id

        if self.active:
            self.colour = self.active_colour
            self.font_colour = self.active_font
        else:
            self.colour = self.passive_colour
            self.font_colour = self.passive_font

        text_surface = self.font.render(self.icon, True, self.font_colour)

        text_surface_rect = pygame.Surface(text_surface.get_size())
        text_surface_rect.fill(self.colour)
        text_surface_rect.blit(text_surface, (0, 0))
        win.blit(text_surface_rect, (self.x, self.y))

class DropDown:
    def __init__(self, x=0, y=0, width=125, height=50, text="Menu", font_colour=(255, 255, 255), passive_colour=pygame.Color("gray15"), active_colour=pygame.Color("lightskyblue3"), items=["Hello", "World", "Hitler"]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.box = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = text
        self.active = False
        self.passive_colour = passive_colour
        self.active_colour =  passive_colour
        self.font_colour = font_colour
        self.colour = self.passive_colour
        self.font = pygame.font.Font(None, 48)
        self.items = items
        self.option_rects = []
    def draw(self, win):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        menu_id = []
        if click[0]:
            i = 0
            for rect in self.option_rects:
                if rect.collidepoint(mouse):
                    menu_id.append(self.items[i])
                    #print(self.items[i])
                i += 1
                    


            if self.box.collidepoint(mouse):
                self.active = True
            else:
                self.active = False
        if self.active:
            self.colour = self.active_colour
        else:
            self.colour = self.passive_colour

        if self.active:
            y_offset = 0
            i = 0
            for item in self.items:
                temp_rect = pygame.draw.rect(win, self.colour, (self.x, self.y + y_offset, self.width, self.height))
                if temp_rect not in self.option_rects:
                    self.option_rects.append(temp_rect)
                text_surface = self.font.render(self.items[i], True, self.font_colour)
                win.blit(text_surface, (self.x + 5, self.y + 5 + y_offset))
                y_offset += 50
                i += 1
        pygame.draw.rect(win, self.colour, self.box)
        text_surface = self.font.render(self.text, True, self.font_colour)
        win.blit(text_surface, (self.x + 5, self.y + 5))
        return menu_id

class InputBox:
    def __init__(self, x=0, y=0, width=96, height=32, passive_colour=pygame.Color("gray15"), active_colour=pygame.Color("lightskyblue3")):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.box = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = ""
        self.active = False
        self.passive_colour = passive_colour
        self.active_colour =  active_colour
        self.colour = self.passive_colour
        self.font = pygame.font.Font(None, 48)
            
    def keydown_update(self, event):
        keys = pygame.key.get_pressed()
        if self.active == True:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_e and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                self.text = ""
            else:
                self.text += event.unicode 
            return self.text
        
    def draw(self, win):
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        if click[0]:
            if self.box.collidepoint(mouse):
                self.active = True
            else:
                self.active = False
        if self.active:
            self.colour = self.active_colour
        else:
            self.colour = self.passive_colour

        pygame.draw.rect(win, self.colour, self.box, 3)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        win.blit(text_surface, (self.x + 5, self.y + 5))
