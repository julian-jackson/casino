import pygame, os, ui, pickle, random, time, math

pygame.init()
win = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption("Casino")

RESOLUTION = [1280, 720]
resolution = [0 , 0]

PATH = os.path.dirname(__file__)
x_scaler = 0
y_scaler = 0

run = True
pre_game = True
playing = False
after_spin = False

with open(f'user.dat', 'rb') as f:
    user_name = pickle.load(f)

with open(f'{user_name}', 'rb') as f:
    user_data = pickle.load(f)

class Player:
    def __init__(self):
        self.bool_choice = ""
        self.total_score = 0
        self.previous_scores = []


class RankHandler:
    def __init__(self, elo, x, y):
        self.x = x
        self.y =y 
        self.elo = elo
        self.ranks_list = {
            "iron": 0,
            "bronze": 500,
            "silver": 600,
            "gold": 700,
            "plat": 800,
            "diamond": 900,
            "master": 1000,
        }
        if self.ranks_list["iron"] < elo < self.ranks_list["bronze"]:
            self.rank = "iron"
        elif ranks_list["bronze"] < elo < self.ranks_list["silver"]:
            self.rank = "bronze"
        elif ranks_list["silver"] < elo < self.ranks_list["gold"]:
            self.rank = "silver"
        elif ranks_list["gold"] < elo < self.ranks_list["plat"]:
            self.rank = "gold"
        elif ranks_list["plat"] < elo < self.ranks_list["diamond"]:
            self.rank = "plat"
        elif ranks_list["diamond"] < elo < self.ranks_list["master"]:
            self.rank = "diamond"         
        elif ranks_list["master"] < elo:
            self.rank = "master"    
        self.rank_icon_path = PATH + "/"+self.rank+".png"
        self.icon = pygame.image.load(self.rank_icon_path)

    def draw(self, win):
        win.blit(self.icon, (self.x, self.y))

rank_handler = RankHandler(elo=user_data["elo"], x=50, y=500)  

class MusicHandler:
    def __init__(self, file):
        self.menu_music = pygame.mixer.music.load(file)
    def music(self):
        pygame.mixer.music.play(self.menu_music)

# music_file = PATH + "/menu.mp3"
# menu_music = pygame.mixer.music.load(music_file)
# pygame.mixer.music.play(loops=0, start=0.0, fade_ms = 0)

class UINumbers:
    def __init__(self, x, y, rows, max_columns, sector_width, sector_height, border_width, border_colour):
        self.x = x
        self.y = y
        self.rows = rows
        self.max_columns = max_columns
        self.sector_width = sector_width
        self.sector_height = sector_height
        self.border_width = border_width
        self.border_colour = border_colour
    def draw(self, win):
        x_col = 0
        y_col = 0
        j = 0

        row_count = math.ceil(13 / self.max_columns)
        for row in range(row_count):
            for column in range(self.max_columns):
                if j > len(wheel.numbers) - 1:
                    j = len(wheel.numbers) - 1  
                    break                
                pygame.draw.rect(win, self.border_colour, (self.x + x_col, self.y + y_col, self.sector_width, self.sector_height))

                if wheel.active_number < wheel.numbers[j]:
                    pygame.draw.rect(win, wheel.low_colour, (self.x + x_col+ self.border_width / 2, self.y + y_col+ self.border_width / 2, self.sector_width - self.border_width, self.sector_height - self.border_width))
                    current_number = ui.TextBox(x=self.x + x_col+ self.sector_width/3, y=self.y +y_col+ self.sector_height/4, font_size=30, font_colour=(200,200,200), text=str(wheel.numbers[j]))

                if wheel.active_number > wheel.numbers[j]:
                    pygame.draw.rect(win, wheel.high_colour, (self.x + x_col + self.border_width / 2, self.y + y_col+ self.border_width / 2, self.sector_width - self.border_width, self.sector_height - self.border_width))
                    current_number = ui.TextBox(x=self.x +x_col + self.sector_width/3, y=self.y+y_col + self.sector_height/4, font_size=30, font_colour=(150,150,150), text=str(wheel.numbers[j]))

                current_number.draw(win)

                j += 1
                    
                y_col += self.sector_height

            x_col += self.sector_width
            y_col = 0



class Wheel:
    def __init__(self, x, y, width, height, sector_width, sector_height, passive_colour, low_colour, high_colour, border_width, border_colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.sector_width = sector_width
        self.sector_height = sector_height

        self.passive_colour = passive_colour
        self.low_colour = low_colour
        self.high_colour = high_colour

        self.border_colour = border_colour
        self.border_width = border_width

        self.numbers = []
        for x in range(13):
            self.numbers.append(x + 1)
            random.shuffle(self.numbers)

        self.active_number = 0

    def numbers_update(numbers):
        pass

    def spin(self):
        sleep_delay = 0.01
        spinning = True

        self.hidden_active_number = self.numbers[random.randint(1, len(self.numbers)-1)]
        while spinning:
            self.numbers.insert(0, self.numbers[-1])
            self.numbers = self.numbers[:-1]

            self.draw(win)
            pygame.display.update()

            time.sleep(sleep_delay)
            #sleep_delay += random.uniform(0.001, 0.005)
            sleep_delay += random.uniform(0.010, 0.050)

            if sleep_delay > 0.2 and self.hidden_active_number == self.numbers[0]:
                spinning = False

                self.active_number = self.hidden_active_number
                time.sleep(0.5)
                self.numbers.pop(0)


    def draw(self, win):
        x_offset = 0
        j = 0
        for x in range(len(self.numbers)):

            pygame.draw.rect(win, self.border_colour, (self.x + x_offset, self.y, self.sector_width, self.sector_height))


            if self.active_number < self.numbers[j]:
                pygame.draw.rect(win, self.low_colour, (self.x + x_offset + self.border_width / 2, self.y + self.border_width / 2, self.sector_width - self.border_width, self.sector_height - self.border_width))
                current_number = ui.TextBox(x=self.x + x_offset + self.sector_width/3, y=self.y + self.sector_height/4, font_size=128, font_colour=(200,200,200), text=str(self.numbers[j]))


            elif self.active_number > self.numbers[j]:
                pygame.draw.rect(win, self.high_colour, (self.x + x_offset + self.border_width / 2, self.y + self.border_width / 2, self.sector_width - self.border_width, self.sector_height - self.border_width))
                current_number = ui.TextBox(x=self.x + x_offset + self.sector_width/3, y=self.y + self.sector_height/4, font_size=128, font_colour=(150,150,150), text=str(self.numbers[j]))

            else:
                pygame.draw.rect(win, self.passive_colour, (self.x + x_offset + self.border_width / 2, self.y + self.border_width / 2, self.sector_width - self.border_width, self.sector_height - self.border_width))
                current_number = ui.TextBox(x=self.x + x_offset + self.sector_width/3, y=self.y + self.sector_height/4, font_size=128, font_colour=(150,150,150), text=str(self.numbers[j]))

            current_number.draw(win)
            x_offset += self.sector_width
            j += 1

        panel_3 = ui.Panel(x=1255 + x_scaler,y=25,width=805 + x_scaler, height=670 + y_scaler)
        panel_3.draw(win)
        pygame.draw.polygon(win, self.passive_colour, [(500, self.y - 75), (600, self.y - 75), (550, self.y - 25)])

wheel = Wheel(x=475, y=300, width=1000, height= 100, sector_width=175, sector_height=175, passive_colour=(93,43,255), low_colour=(93,43,255), high_colour=(240, 204, 24), border_width=7, border_colour=(255,255,255))
number_summary = UINumbers(x=700, y= 500, rows=4, max_columns=4, sector_width=75, sector_height=46, border_width=3, border_colour=(255,255,255))

tags = ["User: ", "ELO: ", "Played: ", "Wins: ", "Avg Rank: ", "High Score: ", "Highest ELO: "]
tags_data = [user_data["name"], user_data["elo"], user_data["games_played"], user_data["wins"], user_data["avg_rank"], user_data["high_score"], user_data["highest_elo"]]

while run:

    y_offset = 0
    stats = []

    bg = ui.Background(colour=(255,255,255))
    menu_label = ui.TextBox(x=500, y=50, font_size=60, text="Reckless Rina's Casino")
    player_stats_label = ui.TextBox(x=50, y=50, font_size=60, text="Player Stats")
    panel_1 = ui.Panel(x=25,y=25,width=400, height=670 + y_scaler)
    panel_2 = ui.Panel(x=450,y=25,width=805 + x_scaler, height=670 + y_scaler)

    play_button = ui.Button(x=1100 + x_scaler, y=wheel.y - 75, width=500, height=150, font_size=80, icon="Play", item_id="spin")

    low_button = ui.Button(x=480, y=wheel.y + 190, width=500, height=150, font_size=120, icon="Low", item_id="low")
    high_button = ui.Button(x=480, y=wheel.y + 290, width=500, height=150, font_size=120, icon="High", item_id="high")

    render_queue = [bg, panel_1, panel_2, menu_label, player_stats_label]


    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            win = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            x_scaler = event.w - RESOLUTION[0]
            y_scaler = event.h  - RESOLUTION[1]

    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    resolution[0] = RESOLUTION[0] + x_scaler
    resolution[1] = RESOLUTION[1] + y_scaler

    for item in render_queue:
        item.draw(win)

    button_commands = []

    if pre_game:
        pre_render_queue = []
        for i in range(len(tags)):
            stats.append(ui.TextBox(x=50, y=130 + y_offset, font_size=40, text=tags[i] + str(tags_data[i])))
            y_offset += 50
        for item in stats:
            pre_render_queue.append(item)

        for item in pre_render_queue:
            item.draw(win)
        button_commands.append(play_button.draw(win))
        rank_handler.draw(win)

        if "spin" in button_commands:
            playing = True
            pre_game = False


    if playing:
        wheel.spin()
        playing = False
        after_spin = True

    else:
        wheel.draw(win)


    if after_spin:
        button_commands.append(low_button.draw(win))
        button_commands.append(high_button.draw(win))

        chosen_number = ui.TextBox(x= 750, y=240, font_size=64, text="Last Number: " + str(wheel.active_number))
        chosen_number.draw(win)

        number_summary.draw(win)

        if "low" in button_commands:
            after_spin = False
            playing = True

        if "high" in button_commands:
            after_spin = False
            playing = True


    pygame.display.update()
