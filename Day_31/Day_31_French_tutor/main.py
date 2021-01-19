import tkinter
import pandas
import random
import gtts
from playsound import playsound
import os


# ---------------------------- UI CONSTANT ------------------------------- #

RED = "#e2979c"
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- IMAGE FILES ------------------------------- #

NEXT_IMG = "images/next.png"
SPEAKER_IMG = "images/speakers.png"
ENGLISH_IMG = "images/english.png"
CARD_FRONT_IMG = "images/card_front.png"
CARD_BACK_IMG = "images/card_back.png"
FONT_NAME = "Arial"

# ---------------------------- VARIABLE CONSTANT ------------------------------- #

current_card = {}
to_learn = {}

# ---------------------------- GET DATA FILE ------------------------------- #

try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    original_data =pandas.pandas.read_csv("data/french_words.csv")
    original_data.to_dict(orient="records")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = random.choice(to_learn)

# ---------------------------- CHANGE WORD ------------------------------- #


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_text, text=f"French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_card_Img)


def flip_card():
    canvas.itemconfig(lang_text, text=f"English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_card_img)


def speak_word():
    fre_text = current_card["French"]
    audio2 = gtts.gTTS(f"{fre_text}", lang="fr")
    audio2.save("data/word.mp3")
    playsound("data/word.mp3")
    os.remove("data/word.mp3")

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("French Tutor")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)


title_label = tkinter.Label(text="French Tutor")
title_label.config(fg=RED, bg=BACKGROUND_COLOR, font=(FONT_NAME, 30, "bold"))
title_label.grid(column=1, row=0)


canvas = tkinter.Canvas(width=800, height=526)
front_card_Img = tkinter.PhotoImage(file=CARD_FRONT_IMG)
back_card_img = tkinter.PhotoImage(file=CARD_BACK_IMG)
canvas_image = canvas.create_image(400, 263, image=front_card_Img)
lang_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "bold"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=1, row=1)


next_Img = tkinter.PhotoImage(file=NEXT_IMG)
next_btn = tkinter.Button(image=next_Img, bg=BACKGROUND_COLOR, command=next_card)
next_btn.grid(row=2, column=2)

speak_Img = tkinter.PhotoImage(file=SPEAKER_IMG)
speak_btn = tkinter.Button(image=speak_Img, bg=BACKGROUND_COLOR, command=speak_word)
speak_btn.grid(row=2, column=1)

eng_img = tkinter.PhotoImage(file=ENGLISH_IMG)
eng_btn = tkinter.Button(image=eng_img, bg=BACKGROUND_COLOR, command=flip_card)
eng_btn.grid(row=2, column=0)

next_card()

window.mainloop()
