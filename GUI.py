import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk


#                                               --------> Functions for start window




def close_window():
    if start:
        start.destroy()
    if game_win:
        game_win.destroy()
    if setting_window:
        setting_window.destroy()

def min_window(main, other, other1):
    main.iconify()
    other.withdraw()
    other1.withdraw()

def start_game():
    game_win.deiconify()
    start.after(1000, lambda: start.withdraw())
    

def setting_window():
    setting_window.deiconify()
    start.after(1000, lambda: start.withdraw())

#                                                --------> Funtions for Game window
def go_to_start_fg():
    start.deiconify()
    game_win.after(1000, lambda: game_win.withdraw())

def go_to_start_fs():
    start.deiconify()
    setting_window.after(1000, lambda: setting_window.withdraw())

#                                                --------> Funtions for Settings window
def dark_mode():
    setting_window.config(bg="black")
    setting_label.config(bg="black",fg="white")
    mode_label.config(bg="black", fg="white")
    sound_label.config(bg="black", fg="white")
    on_btn.config(bg="black", fg="white")
    off_btn.config(bg="black", fg="white")
    game_win.config(bg="black")
    image_frame.config(bg="black")
    text_frame.config(bg="black")
    text_box.config(bg="black", fg="white")
    inventory_frame.config(bg="black")
    invent_listbox.config(bg="black", fg="white")
    inventory_label.config(bg="black", fg="white")

def light_mode():
    setting_window.config(bg="#D2B48C")
    setting_label.config(bg="#D2B48C",fg="black")
    mode_label.config(bg="#D2B48C", fg="black")
    sound_label.config(bg="#D2B48C", fg="black")
    on_btn.config(bg="white", fg="black")
    off_btn.config(bg="white", fg="black")
    game_win.config(bg="#D2B48C")
    image_frame.config(bg="#D2B48C")
    text_frame.config(bg="#D2B48C")
    text_box.config(bg="#D2B48C", fg="black")
    inventory_frame.config(bg="#D2B48C")
    invent_listbox.config(bg="#D2B48C", fg="black")
    inventory_label.config(bg="#D2B48C", fg="black")
    
#                                              -------->  Game Mechanics

stage=1


inventory={}
def print_lines(file, start, end):

    
    with open(file, 'r') as file_new:
        for i, line in enumerate(file_new, 1):
            if start <= i <= end:
                text_box.insert(tk.END, line.strip() + '\n\n')
    
def clear_box():
    text_box.config(state="normal")
    text_box.delete(1.0, tk.END)

def update_invent(items, rarity):
    invent_listbox.insert(tk.END, f" {items} : {rarity}")

def mech(choice):
    global stage
    
    if stage==1:
        file_path=r"Resources\City-level1.txt"
        image_label.config(image=img_city)
        handle_stg_1(choice,file_path)
    elif stage==2:
        file_path=r"Resources\Forest-level2.txt"
        image_label.config(image=img_forest)
        handle_stg_2(choice, file_path)

def handle_stg_1(choice, file_path):
    global stage
    if choice=="start":
        inventory["Sword"]="Common"
        update_invent("Sword", "Standard Knight Sword")
        text_box.config(state="normal")
        print_lines(file_path, 3, 10)
        text_box.config(state="disabled")
        choice_btn_1.config(text="Gate")
        choice_btn_2.config(text="Canal")
    
    if choice=="Gate":
        clear_box()
        text_box.config(state="normal")
        print_lines(file_path, 18, 19)
        text_box.config(state="disabled")
        choice_btn_1.config(text="Search the guards")
        choice_btn_2.config(text="Leave Immediatly!")
    elif choice=="Canal":
        clear_box()
        text_box.config(state="normal")
        print_lines(file_path, 13, 15)
        text_box.config(state="disabled")
        choice_btn_1.config(text="Next")
        choice_btn_2.config(text="")
        stage=2

    if choice=="Search the guards":
        clear_box()
        text_box.config(state="normal")
        print_lines(file_path, 26, 28)
        text_box.config(state="disabled")
        inventory["Gold Coins"]=50
        update_invent("Gold Coins", 50)
        choice_btn_1.config(text="Next")
        choice_btn_2.config(text="")
        stage=2
    elif choice=="Leave Immediatly!":
        clear_box()
        text_box.config(state="normal")
        print_lines(file_path, 23, 23)
        text_box.config(state="disabled")
        choice_btn_1.config(text="Next")
        choice_btn_2.config(text="")
        stage=2

def handle_stg_2(choice, file_path):
    global stage

    if choice=="Next":
        clear_box()
        text_box.config(state="normal")
        print_lines(file_path, 1, 16)
        text_box.config(state="disabled")
        choice_btn_1.config(text="Wait Patiently")
        choice_btn_2.config(text="Explore")

    if choice=="Wait Patiently":
        clear_box()
        text_box.config(state="normal")
        print_lines(file_path, 24, 27)
        text_box.config(state="disabled")
        choice_btn_1.config(text="Ask About Celestial Summit")
        choice_btn_2.config(text="Say Nothing")
    elif choice == "Explore":
        clear_box()
        text_box.config(state="normal")
        print_lines(file_path, 22, 27)
        text_box.config(state="disabled")
        choice_btn_1.config(text="Ask About Celestial Summit")
        choice_btn_2.config(text="Say Nothing")
    
    if choice=="Ask About Celestial Summit":
        clear_box()
        text_box.config(state="normal")
        print_lines(file_path, 30, 32)
        print_lines(file_path, 36, 40)
        text_box.config(state="disabled")
        choice_btn_1.config(text="Ask About the Witch's Plan")
        choice_btn_2.config(text="Trust Lyra's Judgment")
    elif choice == "Say Nothing":
        clear_box()
        text_box.config(state="normal")
        print_lines(file_path, 36, 40)
        text_box.config(state="disabled")
        choice_btn_1.config(text="Ask About the Witch's Plan")
        choice_btn_2.config(text="Trust Lyra's Judgment")

    if choice=="Ask About the Witch's Plan":
        clear_box()
        text_box.config(state="normal")
        print_lines(file_path, 43, 44)
        print_lines(file_path, 49, 52)
        text_box.config(state="disabled")
        choice_btn_1.config(text="Agree to Take Lyra Along")
        choice_btn_2.config(text="Refuse to Take Lyra Along")
    elif choice == "Trust Lyra's Judgment":
        clear_box()
        text_box.config(state="normal")
        print_lines(file_path, 49, 52)
        text_box.config(state="disabled")
        choice_btn_1.config(text="Agree to Take Lyra Along")
        choice_btn_2.config(text="Refuse to Take Lyra Along")

    if choice=="Agree to Take Lyra Along":
        clear_box()
        text_box.config(state="normal")
        print_lines(file_path, 55, 56)
        text_box.config(state="disabled")
        stage=3
        choice_btn_1.config(text="")
        choice_btn_2.config(text="*Work in Progress*")
    elif choice == "Refuse to Take Lyra Along":
        clear_box()
        text_box.config(state="normal")
        print_lines(file_path, 59, 60)
        text_box.config(state="disabled")
        stage=3
        choice_btn_1.config(text="")
        choice_btn_2.config(text="*Work in Progress*")

    



#                                                -------->  Start_Window

start = tk.Tk()
start.title("Hearth Bound")
start.attributes("-fullscreen", True)
start_img_pil = Image.open(r"Resources\fantasy-1.jpg")
start_img = ImageTk.PhotoImage(start_img_pil)
start_label = tk.Label(start, image=start_img)
start_label.place(relwidth=1, relheight=1)

start_btn=tk.Button(start,text="START",width=10, height=1, bg="grey", command=start_game, relief="groove", font=("Viner Hand ITC", 20, "bold"))
start_btn.place(relx=0.5, rely=0.6, anchor="n")
 
setting_btn=tk.Button(start, text="SETTINGS", width=10, height=1,bg="grey", command=setting_window, relief="groove", font=("Viner Hand ITC", 20, "bold"))
setting_btn.place(relx=0.5, rely=0.8, anchor="center")

start_close_btn=tk.Button(start, bg="brown", text="X", width=4, height=1, command=close_window, borderwidth=2, relief="ridge")
start_close_btn.place(relx=1, rely=0, anchor="ne")

start_min_btn=tk.Button(start, bg="grey", text="___", width=4, height=1, command=lambda: min_window(start,game_win,setting_window), borderwidth=2, relief="ridge")
start_min_btn.place(relx=0.972, rely=0, anchor="ne")


#                                                   --------> Game Window


global game_win
game_win=tk.Toplevel(start)
game_win.title("Hearth Bound")
game_win.attributes("-fullscreen", True)
game_win.config(bg="#D2B48C")
game_win.withdraw()

game_back_btn=tk.Button(game_win, width=6, height=1, text="<--", bg="grey", relief="groove", command=go_to_start_fg, font=("Calibri", 14, "bold"))
game_back_btn.place(relx=0.03, rely=0.03, anchor="center")

game_close_btn=tk.Button(game_win, bg="brown", text="X", width=4, height=1, command=close_window, borderwidth=2, relief="ridge")
game_close_btn.place(relx=1, rely=0, anchor="ne")

game_min_btn=tk.Button(game_win, bg="grey", text="___", width=4, height=1, command= lambda: min_window(game_win,start,setting_window), borderwidth=2, relief="ridge")
game_min_btn.place(relx=0.972, rely=0, anchor="ne")
#                                                                --> Image Frame resoution: 409 x 675
image_frame=tk.Frame(game_win, bg="#D2B48C", borderwidth=5, relief="ridge")
image_frame.place(x=20, y=70, relwidth=0.3, relheight=0.88)

img_city_pil=Image.open(r"Resources\city.jpg")
img_forest_pil=Image.open(r"Resources\forest.jpg")
img_summit_pil=Image.open(r"Resources\Summit.jpg")
img_cha_pil=Image.open(r"Resources\charac-1.jpg")
img_city=ImageTk.PhotoImage(img_city_pil)
img_forest=ImageTk.PhotoImage(img_forest_pil)
img_summit=ImageTk.PhotoImage(img_summit_pil)
img_cha=ImageTk.PhotoImage(img_cha_pil)

image_label=tk.Label(image_frame, image=img_summit)
image_label.place(relwidth=1, relheight=1)

text_frame=tk.Frame(game_win, bg="#D2B48C", borderwidth=5, relief="ridge")
text_frame.place(x=430, y=70, relwidth=0.4382, relheight=0.88)

inventory_frame=tk.Frame(game_win, bg="#D2B48C", borderwidth=5, relief="ridge")
inventory_frame.place(x=1030, y=70, relwidth=0.23, relheight=0.88)

text_box=scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, bg="#D2B48C", state="disabled", font=("Times New Roman", 14))
text_box.pack(expand=True, fill="both")

choice_btn_1=tk.Button(text_frame, text="start", bg="grey",height=2, width=25, font=("Times New Roman",14) , command=lambda: mech(choice_btn_1.cget("text")), relief="raised")
choice_btn_1.pack(side=tk.LEFT, padx=3)

choice_btn_2=tk.Button(text_frame, text="start", bg="grey",height=2, width=25, font=("Times New Roman",14), command=lambda: mech(choice_btn_2.cget("text")), relief="raised")
choice_btn_2.pack(side=tk.RIGHT, padx=3)

cha_label=tk.Label(inventory_frame, text="Charachter", bg="#D2B48C", font=("Viner Hand ITC", 25, "bold"))
cha_label.place(relx=0.5, rely=0.05, anchor="center")

cha_frame=tk.Frame(inventory_frame, bg="#D2B48C", width=275, height=247, borderwidth=5, relief="groove")
cha_frame.place(relx=0.5, rely=0.27, anchor="center")

cha_img_label=tk.Label(cha_frame, image=img_cha)
cha_img_label.place(relwidth=1, relheight=1)

inventory_label=tk.Label(inventory_frame, text="Inventory", bg="#D2B48C", font=("Viner Hand ITC", 25, "bold"))
inventory_label.place(relx=0.5, rely=0.5, anchor="center")

invent_listbox=tk.Listbox(inventory_frame, bg="#D2B48C", width=30, height=12, font=("Times New Roman",14))
invent_listbox.place(relx=0.5, rely=0.55, anchor="n")

#                                                     --------> Settings Window

setting_window=tk.Toplevel(start)
setting_window.title("Hearth Bound")
setting_window.attributes("-fullscreen", True)
setting_window.config(bg="#D2B48C")
setting_window.withdraw()

setting_label=tk.Label(setting_window, text="SETTINGS", bg="#D2B48C", font=("Viner Hand ITC", 50, "bold"))
setting_label.place(relx=0.5, rely=0.15, anchor="center")

mode_label=tk.Label(setting_window, text="Mode", bg="#D2B48C", font=("Viner Hand ITC", 30, "bold"))
mode_label.place(relx=0.5, rely=0.3, anchor="center")

light_btn=tk.Button(setting_window, text="Light", width=5, bg="#D2B48C", command=light_mode, font=("Viner Hand ITC", 13, "bold"))
light_btn.place(relx=0.45, rely=0.38, anchor="center")

dark_btn=tk.Button(setting_window, text="Dark", width=5, bg="black", fg="white", command=dark_mode, font=("Viner Hand ITC", 13, "bold"))
dark_btn.place(relx=0.55, rely=0.38, anchor="center")

sound_label=tk.Label(setting_window, text="Sound", bg="#D2B48C", font=("Viner Hand ITC", 30, "bold"))
sound_label.place(relx=0.5, rely=0.5, anchor="center")

on_btn=tk.Button(setting_window, text="ON", width=5, bg="white", font=("Viner Hand ITC", 13, "bold"))
on_btn.place(relx=0.45, rely=0.58, anchor="center")

off_btn=tk.Button(setting_window, text="OFF", width=5, bg="white", fg="black", font=("Viner Hand ITC", 13, "bold"))
off_btn.place(relx=0.55, rely=0.58, anchor="center")

setting_back_btn=tk.Button(setting_window, width=6, height=1, text="<--", bg="grey", relief="groove", command=go_to_start_fs, font=("Calibri", 14, "bold"))
setting_back_btn.place(relx=0.03, rely=0.03, anchor="center")

start.mainloop()

