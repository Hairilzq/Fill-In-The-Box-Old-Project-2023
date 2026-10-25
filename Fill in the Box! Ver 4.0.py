import pygame
import sys
import random
import time
from pathlib import Path

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Fill in the Box!")
main_font = pygame.font.SysFont("cambria", 20) 
secondary_font = pygame.font.SysFont("cambria", 50)
third_font = pygame.font.SysFont("cambria", 35)
forth_font = pygame.font.SysFont("cambria", 27)

# Added - Asset directory path for loading images
ASSET_DIR = Path(__file__).resolve().parent / "Game_Assets"
def load_image(filename):
    return pygame.image.load(str(ASSET_DIR / filename))


BG = pygame.transform.scale(load_image("RoomBackground.png"), (800, 600))
Box = pygame.transform.scale(load_image("BoxSprite.png"), (400,300))
Board = pygame.transform.scale(load_image("WoodenFrameSprite.png"), (800, 600))
UI_bar = pygame.transform.scale(load_image("UIBarSprite.png"), (740, 100))
Win_BG = pygame.transform.scale(load_image("WinBackground.png"), (800, 600))
Menu_BG = pygame.transform.scale(load_image("Fill_intheBox!MainScreen.png"), (800, 600))

Play = False
Endlessmode = False
Speedrunmode = False
Complete = False
Hardmode = False

#Button Class---------------
class Button():
    def __init__(self, image, x_pos, y_pos, text_input): 
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "black")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.clicked = False

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
            #Button function

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "green") #Colour change customisable (text only)
        else:
            self.text = main_font.render(self.text_input, True, "black")

#Arrow keys--------------------------
arrow_right_button_surface = load_image("ArrowRightSprite.png")
arrow_right_button_surface =  pygame.transform.scale(arrow_right_button_surface, (75, 50))
arrow_right_button = Button(arrow_right_button_surface, 760, 120, " ")

arrow_left_button_surface = load_image("ArrowLeftSprite.png")
arrow_left_button_surface =  pygame.transform.scale(arrow_left_button_surface, (75, 50))
arrow_left_button = Button(arrow_left_button_surface, 40, 120, " ")

continue_button_surface = pygame.transform.scale(arrow_right_button_surface, (150, 100))
continue_button = Button(continue_button_surface, 400, 500, "Continue")

Endless_surf = load_image("ButtonImageWood.png")
Endless_surf =  pygame.transform.scale(Endless_surf, (300, 100))
Endless = Button(Endless_surf, 400, 380, "Endless mode!")

Speedrun_surf = load_image("ButtonImageWood.png")
Speedrun_surf =  pygame.transform.scale(Speedrun_surf, (300, 100))
Speedrun = Button(Speedrun_surf, 400, 460, "Speedrun mode!")

Hard_surf = load_image("ButtonImageWood.png")
Hard_surf =  pygame.transform.scale(Hard_surf, (300, 100))
Hard = Button(Hard_surf, 400, 540, "Hard mode!")

#Icon buttons--------------------------
Book = load_image("BookSprite.png") #image customisable
Book = pygame.transform.scale(Book, (150, 100)) #button size
Book_button = Button(Book, 330, 120, "Book") #follow class parameter (modify pos)

Toaster = load_image("ToasterSprite.png") #image customisable
Toaster = pygame.transform.scale(Toaster, (150, 100)) #button size
Toaster_button = Button(Toaster, 180, 120, "Toaster") #follow class parameter (modify pos)

Shoe = load_image("ShoeSprite.png") #image customisable
Shoe = pygame.transform.scale(Shoe, (180, 110)) #button size
Shoe_button = Button(Shoe, 480, 120, "Shoe") #follow class parameter (modify pos)

Clock = load_image("ClockSprite.png") #image customisable
Clock = pygame.transform.scale(Clock, (235, 155)) #button size
Clock_button = Button(Clock, 630, 120, "Clock") #follow class parameter (modify pos)

Plate = load_image("PlateSprite.png")
Plate =  pygame.transform.scale(Plate, (120, 70))
Plate_button = Button(Plate, 180, 120, "Plate")

Microwave = load_image("MicrowaveSprite.png")
Microwave =  pygame.transform.scale(Microwave, (150, 100))
Microwave_button = Button(Microwave, 330, 120, "Microwave")

Bottle = load_image("BottleSprite.png")
Bottle =  pygame.transform.scale(Bottle, (225, 150))
Bottle_button = Button(Bottle, 500, 130, "Bottle")

Bag = load_image("BagSprite.png")
Bag =  pygame.transform.scale(Bag, (150, 100))
Bag_button = Button(Bag, 630, 120, "Bag")

Pencil = load_image("PencilSprite.png")
Pencil =  pygame.transform.scale(Pencil, (200, 125))
Pencil_button = Button(Pencil, 180, 120, "Pencil")

Toy = load_image("ToySprite.png")
Toy =  pygame.transform.scale(Toy, (180, 130))
Toy_button = Button(Toy, 330, 120, "Toy")

Hat = load_image("HatSprite.png")
Hat =  pygame.transform.scale(Hat, (200, 150))
Hat_button = Button(Hat, 500, 130, "Hat")

Eraser = load_image("EraserSprite.png")
Eraser =  pygame.transform.scale(Eraser, (175, 125))
Eraser_button = Button(Eraser, 630, 120, "Eraser")

#Game variables---------------------------
Min_size = 20
Max_size = 35
Max_weight = 5
Min_budg =  200
Max_budg = 300
#-------------------
Item_list = {
    "Pencil": random.randint(1,3),
    "Eraser": random.randint(1,3),
    "Bottle": random.randint(2,5),
    "Hat": random.randint(2,5),
    "Shoe": random.randint(4,7),
    "Bag": random.randint(4,7),
    "Plate": random.randint(4,7),
    "Book": random.randint(4,7),
    "Toy": random.randint(5,7),
    "Toaster": random.randint(8,10),
    "Microwave": random.randint(8,10),
    "Clock": random.randint(8,10)
    }

Item_list_price = {
        "Pencil": random.randint(1,10),
        "Eraser": random.randint(1,10),
        "Bottle": random.randint(1,10),
        "Hat": random.randint(20,55),
        "Shoe": random.randint(15,35),
        "Bag": random.randint(20,55),
        "Plate": random.randint(20,55),
        "Book": random.randint(10,35),
        "Toy": random.randint(45,65),
        "Toaster": random.randint(65,100),
        "Microwave": random.randint(75,150),
        "Clock": random.randint(65,100)
        }

Box_list = []
Box_Cap = 0
itemss = ["Plate", "Microwave", "Bottle", "Bag", "Book", "Toaster", "Shoe", "Clock", "Pencil", "Eraser", 'Toy', "Hat"]
Main_item = random.choice(itemss)
Box_size = random.randint(Min_size, Max_size)

if Item_list[Main_item] < 4:
    Box_size = random.randint(20,27)
    
Budget = random.randint(Min_budg, Max_budg)
Cost = 0

if Box_size >= 31:
    Budget = random.randint(290, 340)
            
elif Box_size >= 27:
    Budget = random.randint(275,320)

roster_display = 2
start_time = time.time()
Play_amount = 0
Wins = 0
Pass = 0
Main_text = "Add an item!"
switch = 1
Win = False
condition = False
    
Roster_list_3 = ["Plate", "Microwave", "Bottle", "Bag"]
Roster_list_2 = ["Book", "Toaster", "Shoe", "Clock"]
Roster_list_1 = ["Pencil", "Eraser", 'Toy', "Hat"]

Penc_up = False
Toy_up = False
Hat_up = False
Eras_up = False
Book_up = False
Toaster_up = False
Shoe_up = False
Plate_up = False
Micro_up = False
Bott_up = False
Bag_up = False
Clock_up = False

#Functions---------------------------------
def draw(BG, Box, Board, UI_bar, Elapsed_time, Play_amount, Box_size, Box_Cap, Cost, Budget, Main_text, Wins, Main_item):
    screen.blit(BG, (0,0))
    screen.blit(Box, (195, 300))
    screen.blit(Board, (0, -180))
    screen.blit(UI_bar, (25, 230))

    Time_display = secondary_font.render(f"Time: {Elapsed_time}s", 1, "white")
    screen.blit(Time_display, (25, 520))

    Play_display = secondary_font.render(f"Played: {Play_amount}", 1, "white")
    screen.blit(Play_display, (25, 460))

    if Hardmode:
        Box_Cap_display = third_font.render(f"Box Cap: {Box_Cap}/???", 1, "white")
        screen.blit(Box_Cap_display, (545, 460))
    else:
        Box_Cap_display = third_font.render(f"Box Cap: {Box_Cap}/{Box_size}", 1, "white")
        screen.blit(Box_Cap_display, (545, 460))

    if Hardmode:
        Budget_display = forth_font.render(f"Budget: ${Cost}/???", 1, "white")
        screen.blit(Budget_display, (545, 500))
    else:
        Budget_display = forth_font.render(f"Budget: ${Cost}/${Budget}", 1, "white")
        screen.blit(Budget_display, (545, 500))

    Text_display = third_font.render(f"{Main_text}", 1, "white")
    screen.blit(Text_display, (65, 260))

    Wins_display = secondary_font.render(f"Wins: {Wins}", 1, "white")
    screen.blit(Wins_display, (25, 400))

    if Hardmode:
        Item_display = forth_font.render(f"Required: {Main_item}", 1, "white")
        screen.blit(Item_display, (545, 530))

def sec_draw(Win_BG):
    if Hardmode:
        Win_BG = pygame.transform.scale(load_image("WinA.png"), (800, 600))
        
    screen.blit(Win_BG, (0,0))

def third_draw(Menu_BG):
    screen.blit(Menu_BG, (0,0))

def summary_draw(BG, Play_amount, Elapsed_time):
    screen.blit(BG, (0,0))
    
    Time_display = secondary_font.render(f"Time: {Elapsed_time}s", 1, "black")
    screen.blit(Time_display, (250, 215))

    Play_display = secondary_font.render(f"Moves: {Play_amount}", 1, "black")
    screen.blit(Play_display, (250, 295))

def ypos():
    Pos_num = []
    if len(Box_list) == 1:
        Pos_num = Pos_num + [483]
    elif len(Box_list) == 2:
        Pos_num = Pos_num + [483] + [483]
    elif len(Box_list) == 3:
        Pos_num = Pos_num + [483] + [483] + [483]
    elif len(Box_list) == 4:
        Pos_num = Pos_num + [483] + [483] + [483] + [522]
    elif len(Box_list) == 5:
        Pos_num = Pos_num + [483] + [483] + [483] + [522] + [522]
    elif len(Box_list) == 6:
        Pos_num = Pos_num + [483] + [483] + [483] + [522] + [522] + [522]
    return Pos_num

def xpos():
    Posx_num = []
    if len(Box_list) == 1:
        Posx_num = Posx_num + [340]
    elif len(Box_list) == 2:
        Posx_num = Posx_num + [340] + [400]
    elif len(Box_list) == 3:
        Posx_num = Posx_num + [340] + [400] + [470]
    elif len(Box_list) == 4:
        Posx_num = Posx_num + [340] + [400] + [470] + [340]
    elif len(Box_list) == 5:
        Posx_num = Posx_num + [340] + [400] + [470] + [340] + [400]
    elif len(Box_list) == 6:
        Posx_num = Posx_num + [340] + [400] + [470] + [340] + [400] + [470]
    return Posx_num

def buttonInBox():
    global condition, Pencil, Eraser, Toy, Hat, Microwave, Plate, Bottle, Bag, Shoe, Toaster, Book, Clock, Penc_up, Eras_up, Shoe_up, Toaster_up, Micro_up, Hat_up, Toy_up, Plate_up, Bott_up, Bag_up, Book_up, Clock_up
    y_pos_b = ypos()
    x_pos_b = xpos()
    
    for i in Box_list:
        if i == "Pencil":
            Penc_pos = y_pos_b.pop()
            Penc_posx = x_pos_b.pop()
            Pencil =  pygame.transform.scale(Pencil, (100, 55))
            Pencil_button = Button(Pencil, Penc_posx, Penc_pos, "Pencil")
            Pencil_button.changeColor(pygame.mouse.get_pos())
            Pencil_button.update()
            
            if condition:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Pencil_button.checkForInput(pygame.mouse.get_pos()):
                        print("Removed Pencil")
                        remove_item("Pencil",1)
                        condition = False
                        Penc_up = False
            
        if i == "Toy":
            Toys_pos = y_pos_b.pop()
            Toys_posx = x_pos_b.pop()
            Toy =  pygame.transform.scale(Toy, (90, 65))
            Toy_button = Button(Toy, Toys_posx, Toys_pos, "Toy")
            Toy_button.changeColor(pygame.mouse.get_pos())
            Toy_button.update()

            if condition:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Toy_button.checkForInput(pygame.mouse.get_pos()):
                        print("Remove Toy")
                        remove_item("Toy",1)
                        condition = False
                        Toy_up = False
            
        if i == "Hat":
            Hats_pos = y_pos_b.pop()
            Hats_posx = x_pos_b.pop()
            Hat =  pygame.transform.scale(Hat, (100, 75))
            Hat_button = Button(Hat, Hats_posx, Hats_pos, "Hat")
            Hat_button.changeColor(pygame.mouse.get_pos())
            Hat_button.update()

            if condition:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Hat_button.checkForInput(pygame.mouse.get_pos()):
                        print("Remove Hat")
                        remove_item("Hat",1)
                        condition = False
                        Hat_up = False
            
        if i == "Eraser":
             Eras_pos = y_pos_b.pop()
             Eras_posx = x_pos_b.pop()
             Eraser =  pygame.transform.scale(Eraser, (90, 65))
             Eraser_button = Button(Eraser, Eras_posx, Eras_pos, "Eraser")
             Eraser_button.changeColor(pygame.mouse.get_pos())
             Eraser_button.update()

             if condition:
                 if event.type == pygame.MOUSEBUTTONDOWN:
                    if Eraser_button.checkForInput(pygame.mouse.get_pos()):
                        print("Remove Eraser")
                        remove_item("Eraser",1)
                        condition = False
                        Eras_up = False
            
        if i == "Book":
            Books_pos = y_pos_b.pop()
            Books_posx = x_pos_b.pop()
            Book = pygame.transform.scale(Book, (75, 50))
            Book_button = Button(Book, Books_posx, Books_pos, "Book")
            Book_button.changeColor(pygame.mouse.get_pos())
            Book_button.update()

            if condition:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Book_button.checkForInput(pygame.mouse.get_pos()):
                        print("Remove Book")
                        remove_item("Book",2)
                        condition = False
                        Book_up = False
            
        if i == "Toaster":
            Toas_pos = y_pos_b.pop()
            Toas_posx = x_pos_b.pop()
            Toaster = pygame.transform.scale(Toaster, (75, 50)) 
            Toaster_button = Button(Toaster, Toas_posx, Toas_pos, "Toaster")
            Toaster_button.changeColor(pygame.mouse.get_pos())
            Toaster_button.update()

            if condition:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Toaster_button.checkForInput(pygame.mouse.get_pos()):
                        print("Remove Toaster")
                        remove_item("Toaster",2)
                        condition = False
                        Toaster_up = False
            
        if i == "Shoe":
            Shoes_pos = y_pos_b.pop()
            Shoes_posx = x_pos_b.pop()
            Shoe = pygame.transform.scale(Shoe, (90, 55))
            Shoe_button = Button(Shoe, Shoes_posx, Shoes_pos, "Shoe")
            Shoe_button.changeColor(pygame.mouse.get_pos())
            Shoe_button.update()

            if condition:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Shoe_button.checkForInput(pygame.mouse.get_pos()):
                        print("Remove Shoe")
                        remove_item("Shoe",2)
                        condition = False
                        Shoe_up = False
                    
        if i == "Clock":
            Cloc_pos = y_pos_b.pop()
            Cloc_posx = x_pos_b.pop()
            Clock = pygame.transform.scale(Clock, (117, 75))
            Clock_button = Button(Clock, Cloc_posx, Cloc_pos, "Clock")
            Clock_button.changeColor(pygame.mouse.get_pos())
            Clock_button.update()

            if condition:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Clock_button.checkForInput(pygame.mouse.get_pos()):
                        print("Remove Clock")
                        remove_item("Clock",2)
                        condition = False
                        Clock_up = False

        if i == "Plate":
            Plat_pos = y_pos_b.pop()
            Plat_posx = x_pos_b.pop()
            Plate =  pygame.transform.scale(Plate, (60, 35))
            Plate_button = Button(Plate, Plat_posx, Plat_pos, "Plate")
            Plate_button.changeColor(pygame.mouse.get_pos())
            Plate_button.update()

            if condition:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Plate_button.checkForInput(pygame.mouse.get_pos()):
                        print("Remove Plate")
                        remove_item("Plate",3)
                        condition = False
                        Plate_up = False

        if i == "Microwave":
            Micr_pos = y_pos_b.pop()
            Micr_posx = x_pos_b.pop()
            Microwave =  pygame.transform.scale(Microwave, (75, 50))
            Microwave_button = Button(Microwave, Micr_posx, Micr_pos, "Microwave")
            Microwave_button.changeColor(pygame.mouse.get_pos())
            Microwave_button.update()

            if condition:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Microwave_button.checkForInput(pygame.mouse.get_pos()):
                        print("Remove Microwave")
                        remove_item("Microwave",3)
                        condition = False
                    Micro_up = False

        if i == "Bottle":
            Bott_pos = y_pos_b.pop()
            Bott_posx = x_pos_b.pop()
            Bottle =  pygame.transform.scale(Bottle, (112, 75))
            Bottle_button = Button(Bottle, Bott_posx, Bott_pos, "Bottle")
            Bottle_button.changeColor(pygame.mouse.get_pos())
            Bottle_button.update()

            if condition:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Bottle_button.checkForInput(pygame.mouse.get_pos()):
                        print("Remove Bottle")
                        remove_item("Bottle",3)
                        condition = False
                        Bott_up = False

        if i == "Bag":
            Bags_pos = y_pos_b.pop()
            Bags_posx = x_pos_b.pop()
            Bag =  pygame.transform.scale(Bag, (75, 50))
            Bag_button = Button(Bag, Bags_posx, Bags_pos, "Bag")
            Bag_button.changeColor(pygame.mouse.get_pos())
            Bag_button.update()

            if condition:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Bag_button.checkForInput(pygame.mouse.get_pos()):
                        print("Remove Bag")
                        remove_item("Bag",3)
                        condition = False
                        Bag_up = False
                    
def buttonInRosters(x):
    global condition, Roster_list_1, Roster_list_2, Roster_list_3, Box_list, Penc_up, Eras_up, Shoe_up, Toaster_up, Micro_up, Hat_up, Toy_up, Plate_up, Bott_up, Bag_up, Book_up, Clock_up

    if "Pencil" in Box_list and condition == False:
        Penc_up = True
    if "Toy" in Box_list and condition == False:
        Toy_up = True
    if "Hat" in Box_list and condition == False:
        Hat_up = True
    if "Eraser" in Box_list and condition == False:
        Eras_up = True
    if "Book" in Box_list and condition == False:
        Book_up = True
    if "Toaster" in Box_list and condition == False:
        Toaster_up = True
    if "Shoe" in Box_list and condition == False:
        Shoe_up = True
    if "Clock" in Box_list and condition == False:
        Clock_up = True
    if "Plate" in Box_list and condition == False:
        Plate_up = True
    if "Microwave" in Box_list and condition == False:
        Micro_up = True
    if "Bottle" in Box_list and condition == False:
        Bott_up = True
    if "Bag" in Box_list and condition == False:
        Bag_up = True
        
    if condition:
        buttonInBox()
        
    else:
        buttonInBox()
        if x == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Pencil_button.checkForInput(pygame.mouse.get_pos()):
                    if "Pencil" in Box_list and condition == False:
                        pass
                    else:
                        print("Placed Pencil")
                        add_item("Pencil",x)

                if Toy_button.checkForInput(pygame.mouse.get_pos()):
                    if "Toy" in Box_list and condition == False:
                        pass
                    else:
                        print("Placed Toy")
                        add_item("Toy",x)
                                    
                if Hat_button.checkForInput(pygame.mouse.get_pos()):
                    if "Hat" in Box_list and condition == False:
                        pass
                    else:
                        print("Placed Hat")
                        add_item("Hat",x)
                                    
                if Eraser_button.checkForInput(pygame.mouse.get_pos()):
                    if "Eraser" in Box_list and condition == False:
                        Eras_up = True
                    else:
                            print("Placed Eraser")
                            add_item("Eraser",x)
                            
            if not Penc_up:
                Pencil_button.update()
                Pencil_button.changeColor(pygame.mouse.get_pos())

            if not Toy_up:
                Toy_button.update()
                Toy_button.changeColor(pygame.mouse.get_pos())

            if not Hat_up:
                Hat_button.update()
                Hat_button.changeColor(pygame.mouse.get_pos())

            if not Eras_up:
                Eraser_button.update()
                Eraser_button.changeColor(pygame.mouse.get_pos())
            
        if x == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Book_button.checkForInput(pygame.mouse.get_pos()):
                    if "Book" in Box_list and condition == False:
                        pass
                    else:
                            print("Placed Book")
                            add_item("Book", x)
                                
                if Toaster_button.checkForInput(pygame.mouse.get_pos()):
                    if "Toaster" in Box_list and condition == False:
                        pass
                    else:
                            print("Placed Toaster")
                            add_item("Toaster",x)
                         
                                    
                if Shoe_button.checkForInput(pygame.mouse.get_pos()):
                    if "Shoe" in Box_list and condition == False:
                        pass
                    else:
                            print("Placed Shoe")
                            add_item("Shoe",x)
                                    
                if Clock_button.checkForInput(pygame.mouse.get_pos()):
                    if "Clock" in Box_list and condition == False:
                        pass
                    else:
                            print("Placed Clock")
                            add_item("Clock",x)

            if not Book_up:               
                Book_button.update()
                Book_button.changeColor(pygame.mouse.get_pos())

            if not Toaster_up:
                Toaster_button.update()
                Toaster_button.changeColor(pygame.mouse.get_pos())

            if not Shoe_up:
                Shoe_button.update()
                Shoe_button.changeColor(pygame.mouse.get_pos())

            if not Clock_up:
                Clock_button.update()
                Clock_button.changeColor(pygame.mouse.get_pos())
                
        if x == 3:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Plate_button.checkForInput(pygame.mouse.get_pos()):
                    if "Plate" in Box_list and condition == False:
                        pass
                    else:
                            print("Placed Plate")
                            add_item("Plate",x)
         
                if Microwave_button.checkForInput(pygame.mouse.get_pos()):
                    if "Microwave" in Box_list and condition == False:
                        pass
                    else:
                            print("Placed Microwave")
                            add_item("Microwave",x)
                                    
                if Bottle_button.checkForInput(pygame.mouse.get_pos()):
                    if "Bottle" in Box_list and condition == False:
                        pass
                    else:
                            print("Placed Bottle")
                            add_item("Bottle",x)
                                    
                if Bag_button.checkForInput(pygame.mouse.get_pos()):
                    if "Bag" in Box_list and condition == False:
                        pass
                    else:
                        print("Placed Bag")
                        add_item("Bag",x)

            if not Plate_up:
                Plate_button.update()
                Plate_button.changeColor(pygame.mouse.get_pos())

            if not Micro_up:
                Microwave_button.update()
                Microwave_button.changeColor(pygame.mouse.get_pos())

            if not Bott_up:
                Bottle_button.update()
                Bottle_button.changeColor(pygame.mouse.get_pos())

            if not Bag_up:
                Bag_button.update()
                Bag_button.changeColor(pygame.mouse.get_pos())

def game_function():
    global Box_list, Max_weight, Box_Cap, Cost, Item_list, Item_list_price, condition, Roster_list_1, Roster_list_2, Roster_list_3, Play_amount, Main_text
    
    if len(Box_list) > Max_weight:
        if condition == False:
            print("The box is too heavy!")
            print(" ")
            Main_text = "The box is too heavy! Remove an item!"
            condition = True
        
    elif Box_Cap > Box_size:
        if condition == False:
            print("The box is overflowing!")
            print(" ")
            Main_text = "The box is overflowing! Remove an item!"
            condition = True
           
    elif Cost > Budget:
        if condition == False:
            print("The box's items are overbudget!")
            print(" ")
            Main_text = "The box is overbudget! Remove an item!"
            condition = True
            
    else:
        Main_text = "There's space left! Add an item!"
        condition = False

def game_function_hard():
    global condition, Box_list, Max_weight, Box_Cap, Cost, Item_list, Item_list_price, Roster_list_1, Roster_list_2, Roster_list_3, Play_amount, Main_text, Main_item
    
    if len(Box_list) > Max_weight:
        if condition == False:
            print("The box is too heavy!")
            print(" ")
            Main_text = "The box is too heavy! Remove an item!"
            condition = True
        
    elif Box_Cap > Box_size:
        if condition == False:
            print("The box is overflowing!")
            print(" ")
            Main_text = "The box is overflowing! Remove an item!"
            condition = True
           
    elif Cost > Budget:
        if condition == False:
            print("The box's items are overbudget!")
            print(" ")
            Main_text = "The box is overbudget! Remove an item!"
            condition = True
            
    else:
        if Main_item not in Box_list and Box_Cap == Box_size:
            if condition == False:
                print("Main item not inside")
                Main_text = "Required item is not in the box!"
                condition = True
                
        else:
            Main_text = "There's space left! Add an item!"
            condition = False
        
def add_item(x,y):
    global Box_list, Box_Cap, Cost, Item_list, Item_list_price, Roster_list_1, Roster_list_2, Roster_list_3, Play_amount
    Box_list = Box_list + [x]
    Box_Cap = Box_Cap + Item_list[x]
    Cost = Cost + Item_list_price[x]
    Play_amount += 1
    
    if y ==1:
        Roster_list_1.remove(x)
    if y == 2:
        Roster_list_2.remove(x)
    if y == 3:
        Roster_list_3.remove(x)
    
    print("-------------")
    print(Box_list)
    print(" ")
    print("Space taken up: " + str(Box_Cap))
    print("Current value of box: $" + str(Cost))

def remove_item(x,y):
    global Box_list, Box_Cap, Cost, Item_list, Item_list_price, Roster_list_1, Roster_list_2, Roster_list_3, Play_amount
    Box_list.remove(x)
    Box_Cap = Box_Cap - Item_list[x]
    Cost = Cost - Item_list_price[x]
    Play_amount += 1
    
    if y ==1:
        Roster_list_1.append(x)
    if y == 2:
        Roster_list_2.append(x)
    if y == 3:
        Roster_list_3.append(x)
    
    print("-------------")
    print(Box_list)
    print(" ")
    print("Space taken up: " + str(Box_Cap))
    print("Current value of box: $" + str(Cost))

#Main Game Loop--------------------------
while True:
    while not Play:
        passed_time = time.time() - start_time
        third_draw(Menu_BG)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Endless.checkForInput(pygame.mouse.get_pos()):
                    Endlessmode = True
                    Play = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Speedrun.checkForInput(pygame.mouse.get_pos()):
                    Speedrunmode = True
                    Play = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Hard.checkForInput(pygame.mouse.get_pos()):
                    Hardmode = True
                    Play = True

        Endless.changeColor(pygame.mouse.get_pos())
        Endless.update()

        Speedrun.changeColor(pygame.mouse.get_pos())
        Speedrun.update()

        Hard.changeColor(pygame.mouse.get_pos())
        Hard.update()
        
        pygame.display.update()
        
    while not Win and Endlessmode:
        elapsed_time = time.time() - start_time - passed_time
        Elapsed_time = round(elapsed_time)
        draw(BG, Box, Board, UI_bar, Elapsed_time, Play_amount, Box_size, Box_Cap, Cost, Budget, Main_text, Wins, Main_item)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_left_button.checkForInput(pygame.mouse.get_pos()):
                    if roster_display == 3:
                        roster_display = 1
                        print(roster_display)
                        
                    else:
                        roster_display += 1
                        print(roster_display)
                        
                if arrow_right_button.checkForInput(pygame.mouse.get_pos()):
                    if roster_display == 1:
                        roster_display = 3
                        print(roster_display)
                      
                    else:
                        roster_display -= 1
                        print(roster_display)

        arrow_right_button.update()
        arrow_left_button.update()

        game_function()               
        buttonInRosters(roster_display)
        
        pygame.display.update()

        if condition == False and Box_Cap == Box_size:
            if len(Box_list) <= Max_weight and Cost < Budget:
                Win = True
                    
    while Win and Endlessmode:
        sec_draw(Win_BG)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.checkForInput(pygame.mouse.get_pos()):
                    switch += 1
                    if switch > 5:
                        switch = 1
                        
                    if switch == 1:
                        BG = pygame.transform.scale(load_image("RoomBackground.png"), (800, 600))
                        Win_BG = pygame.transform.scale(load_image("WinBackground.png"), (800, 600))
                    if switch == 2:
                        BG = pygame.transform.scale(load_image("RoomBackground2.png"), (800, 600))
                        Win_BG = pygame.transform.scale(load_image("WinBackground2.png"), (800, 600))
                    if switch == 3:
                        BG = pygame.transform.scale(load_image("RoomBackground3.png"), (800, 600))
                        Win_BG = pygame.transform.scale(load_image("WinBackground3.png"), (800, 600))
                    if switch == 4:
                        BG = pygame.transform.scale(load_image("RoomBackground4.png"), (800, 600))
                        Win_BG = pygame.transform.scale(load_image("WinBackground4.png"), (800, 600))
                    if switch == 5:
                        BG = pygame.transform.scale(load_image("RoomBackground5.png"), (800, 600))
                        Win_BG = pygame.transform.scale(load_image("WinBackground5.png"), (800, 600))
                    
                    Box_list = []
                    Box_Cap = 0
                    Box_size = random.randint(Min_size, Max_size)
                    if Box_size >= 31:
                        Budget = random.randint(290, 340)
                        
                    elif Box_size >= 27:
                        Budget = random.randint(275,320)
                    Cost = 0

                    Item_list = {
                                    "Pencil": random.randint(1,3),
                                    "Eraser": random.randint(1,3),
                                    "Bottle": random.randint(2,5),
                                    "Hat": random.randint(2,5),
                                    "Shoe": random.randint(4,7),
                                    "Bag": random.randint(4,7),
                                    "Plate": random.randint(4,7),
                                    "Book": random.randint(4,7),
                                    "Toy": random.randint(5,7),
                                    "Toaster": random.randint(8,10),
                                    "Microwave": random.randint(8,10),
                                    "Clock": random.randint(8,10)
                                    }

                    Item_list_price = {
                                        "Pencil": random.randint(1,10),
                                        "Eraser": random.randint(1,10),
                                        "Bottle": random.randint(1,10),
                                        "Hat": random.randint(20,55),
                                        "Shoe": random.randint(15,35),
                                        "Bag": random.randint(20,55),
                                        "Plate": random.randint(20,55),
                                        "Book": random.randint(10,35),
                                        "Toy": random.randint(45,65),
                                        "Toaster": random.randint(65,100),
                                        "Microwave": random.randint(75,150),
                                        "Clock": random.randint(65,100)
                                        }

                    Roster_list_3 = ["Plate", "Microwave", "Bottle", "Bag"]
                    Roster_list_2 = ["Book", "Toaster", "Shoe", "Clock"]
                    Roster_list_1 = ["Pencil", "Eraser", 'Toy', "Hat"]

                    Penc_up = False
                    Toy_up = False
                    Hat_up = False
                    Eras_up = False
                    Book_up = False
                    Toaster_up = False
                    Shoe_up = False
                    Plate_up = False
                    Micro_up = False
                    Bott_up = False
                    Bag_up = False
                    Clock_up = False
                        
                    Wins += 1
                    Win = False

        continue_button.changeColor(pygame.mouse.get_pos())
        continue_button.update()
        pygame.display.update()

    while not Win and Speedrunmode:
        elapsed_time = time.time() - start_time - passed_time
        Elapsed_time = round(elapsed_time, 2)
        draw(BG, Box, Board, UI_bar, Elapsed_time, Play_amount, Box_size, Box_Cap, Cost, Budget, Main_text, Wins, Main_item)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_left_button.checkForInput(pygame.mouse.get_pos()):
                    if roster_display == 3:
                        roster_display = 1
                        print(roster_display)
                        
                    else:
                        roster_display += 1
                        print(roster_display)
                        
                if arrow_right_button.checkForInput(pygame.mouse.get_pos()):
                    if roster_display == 1:
                        roster_display = 3
                        print(roster_display)
                      
                    else:
                        roster_display -= 1
                        print(roster_display)

        arrow_right_button.update()
        arrow_left_button.update()

        game_function()               
        buttonInRosters(roster_display)
        
        pygame.display.update()

        if condition == False and Box_Cap == Box_size:
            if len(Box_list) <= Max_weight and Cost < Budget:
                Pass += 1
                Win = True

    while Win and Speedrunmode:
        if Pass == 5:
            Complete = True
            
        sec_draw(Win_BG)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        switch += 1
                        
        if switch == 1:
            BG = pygame.transform.scale(load_image("RoomBackground.png"), (800, 600))
            Win_BG = pygame.transform.scale(load_image("WinBackground.png"), (800, 600))
        if switch == 2:
            BG = pygame.transform.scale(load_image("RoomBackground2.png"), (800, 600))
            Win_BG = pygame.transform.scale(load_image("WinBackground2.png"), (800, 600))
        if switch == 3:
            BG = pygame.transform.scale(load_image("RoomBackground3.png"), (800, 600))
            Win_BG = pygame.transform.scale(load_image("WinBackground3.png"), (800, 600))
        if switch == 4:
            BG = pygame.transform.scale(load_image("RoomBackground4.png"), (800, 600))
            Win_BG = pygame.transform.scale(load_image("WinBackground4.png"), (800, 600))
        if switch == 5:
            BG = pygame.transform.scale(load_image("RoomBackground5.png"), (800, 600))
            Win_BG = pygame.transform.scale(load_image("WinBackground5.png"), (800, 600))
                    
        Box_list = []
        Box_Cap = 0
        Box_size = random.randint(Min_size, Max_size)
        if Box_size >= 31:
            Budget = random.randint(290, 340)
                        
        elif Box_size >= 27:
            Budget = random.randint(275,320)
        Cost = 0

        Item_list = {
                                    "Pencil": random.randint(1,3),
                                    "Eraser": random.randint(1,3),
                                    "Bottle": random.randint(2,5),
                                    "Hat": random.randint(2,5),
                                    "Shoe": random.randint(4,7),
                                    "Bag": random.randint(4,7),
                                    "Plate": random.randint(4,7),
                                    "Book": random.randint(4,7),
                                    "Toy": random.randint(5,7),
                                    "Toaster": random.randint(8,10),
                                    "Microwave": random.randint(8,10),
                                    "Clock": random.randint(8,10)
                                    }

        Item_list_price = {
                                        "Pencil": random.randint(1,10),
                                        "Eraser": random.randint(1,10),
                                        "Bottle": random.randint(1,10),
                                        "Hat": random.randint(20,55),
                                        "Shoe": random.randint(15,35),
                                        "Bag": random.randint(20,55),
                                        "Plate": random.randint(20,55),
                                        "Book": random.randint(10,35),
                                        "Toy": random.randint(45,65),
                                        "Toaster": random.randint(65,100),
                                        "Microwave": random.randint(75,150),
                                        "Clock": random.randint(65,100)
                                        }

        Roster_list_3 = ["Plate", "Microwave", "Bottle", "Bag"]
        Roster_list_2 = ["Book", "Toaster", "Shoe", "Clock"]
        Roster_list_1 = ["Pencil", "Eraser", 'Toy', "Hat"]

        Penc_up = False
        Toy_up = False
        Hat_up = False
        Eras_up = False
        Book_up = False
        Toaster_up = False  
        Shoe_up = False
        Plate_up = False
        Micro_up = False
        Bott_up = False
        Bag_up = False
        Clock_up = False
                        
        Win = False

        pygame.display.update()

    while Complete and Speedrunmode:
        summary_draw(BG, Play_amount, Elapsed_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

    while not Win and Hardmode:
        elapsed_time = time.time() - start_time - passed_time
        Elapsed_time = round(elapsed_time)
        BG = pygame.transform.scale(load_image("RoomBackgroundA.png"), (800, 600))
        draw(BG, Box, Board, UI_bar, Elapsed_time, Play_amount, Box_size, Box_Cap, Cost, Budget, Main_text, Wins, Main_item)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_left_button.checkForInput(pygame.mouse.get_pos()):
                    if roster_display == 3:
                        roster_display = 1
                        print(roster_display)
                        
                    else:
                        roster_display += 1
                        print(roster_display)
                        
                if arrow_right_button.checkForInput(pygame.mouse.get_pos()):
                    if roster_display == 1:
                        roster_display = 3
                        print(roster_display)
                      
                    else:
                        roster_display -= 1
                        print(roster_display)

        arrow_right_button.update()
        arrow_left_button.update()

        game_function_hard()               
        buttonInRosters(roster_display)
        
        pygame.display.update()

        if condition == False and Box_Cap == Box_size:
            if len(Box_list) <= Max_weight and Cost < Budget:
                if Main_item in Box_list:
                    Win = True
                
    while Win and Hardmode:
        sec_draw(Win_BG)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.checkForInput(pygame.mouse.get_pos()):
                    Box_list = []
                    Box_Cap = 0
                    Main_item = random.choice(itemss)
                    Box_size = random.randint(20,35)
                    if Item_list[Main_item] < 4:
                        print(" True")
                        Box_size = random.randint(20,27)
                        
                    if Box_size >= 31:
                        Budget = random.randint(290, 340)
                        
                    elif Box_size >= 27:
                        Budget = random.randint(275,320)
                        
                    Cost = 0

                    Item_list = {
                                    "Pencil": random.randint(1,3),
                                    "Eraser": random.randint(1,3),
                                    "Bottle": random.randint(2,5),
                                    "Hat": random.randint(2,5),
                                    "Shoe": random.randint(4,7),
                                    "Bag": random.randint(4,7),
                                    "Plate": random.randint(4,7),
                                    "Book": random.randint(4,7),
                                    "Toy": random.randint(5,7),
                                    "Toaster": random.randint(8,10),
                                    "Microwave": random.randint(8,10),
                                    "Clock": random.randint(8,10)
                                    }

                    Item_list_price = {
                                        "Pencil": random.randint(1,10),
                                        "Eraser": random.randint(1,10),
                                        "Bottle": random.randint(1,10),
                                        "Hat": random.randint(20,55),
                                        "Shoe": random.randint(15,35),
                                        "Bag": random.randint(20,55),
                                        "Plate": random.randint(20,55),
                                        "Book": random.randint(10,35),
                                        "Toy": random.randint(45,65),
                                        "Toaster": random.randint(65,100),
                                        "Microwave": random.randint(75,150),
                                        "Clock": random.randint(65,100)
                                        }

                    Roster_list_3 = ["Plate", "Microwave", "Bottle", "Bag"]
                    Roster_list_2 = ["Book", "Toaster", "Shoe", "Clock"]
                    Roster_list_1 = ["Pencil", "Eraser", 'Toy', "Hat"]

                    Penc_up = False
                    Toy_up = False
                    Hat_up = False
                    Eras_up = False
                    Book_up = False
                    Toaster_up = False
                    Shoe_up = False
                    Plate_up = False
                    Micro_up = False
                    Bott_up = False
                    Bag_up = False
                    Clock_up = False
                        
                    Wins += 1
                    Win = False

        continue_button.changeColor(pygame.mouse.get_pos())
        continue_button.update()
        pygame.display.update()


