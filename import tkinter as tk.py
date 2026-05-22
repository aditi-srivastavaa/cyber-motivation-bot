import tkinter as tk
import random

# MAIN WINDOW
root = tk.Tk()
root.title("Cyber Motivation Generator")
root.geometry("700x450")
root.config(bg="#090b1a")

# MOTIVATION QUOTES
quotes = [
    "Your future self is watching you right now.",
    "One focused day can change your entire life.",
    "Discipline creates freedom.",
    "You are building the life people dream about.",
    "MIT isn't impossible for someone who refuses to quit.",
    "Small progress is still progress.",
    "You were not made to stay average.",
    "Consistency beats motivation.",
    "Late nights become success stories.",
    "Study like your future depends on it — because it does.",
    "You are closer than you think.",
    "Your dream life is built one session at a time."
]

# TITLE
heading = tk.Label(
    root,
    text="CYBER MOTIVATION",
    font=("Orbitron", 24, "bold"),
    fg="#ff0055",
    bg="#090b1a"
)
heading.pack(pady=25)

# QUOTE BOX
quote_label = tk.Label(
    root,
    text="Click the button for motivation ✨",
    wraplength=550,
    justify="center",
    font=("Consolas", 16),
    fg="#d6b3ff",
    bg="#11152b",
    padx=25,
    pady=25,
    relief="ridge",
    bd=3
)
quote_label.pack(pady=40)

# FUNCTION
def generate_quote():
    quote = random.choice(quotes)
    quote_label.config(text=quote)

# BUTTON
motivate_button = tk.Button(
    root,
    text="GENERATE",
    command=generate_quote,
    font=("Orbitron", 15, "bold"),
    fg="white",
    bg="#7b2cff",
    activebackground="#ff0055",
    activeforeground="white",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2"
)
motivate_button.pack(pady=20)

# FOOTER
footer = tk.Label(
    root,
    text="Built with Python ✦",
    font=("Consolas", 10),
    fg="#5d6cff",
    bg="#090b1a"
)
footer.pack(side="bottom", pady=15)

# RUN APP
root.mainloop()