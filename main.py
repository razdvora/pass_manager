from tkinter import *
from tkinter import messagebox
import pyperclip
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[random.choice(letters) for letter in range(nr_letters)]
    password_symbol =[random.choice(symbols) for symbol in range(nr_symbols)]
    password_number = [random.choice(numbers) for number in range(nr_numbers)]

    password_list= password_symbol+password_letters+password_number

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)









# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email =email_entry.get()
    password= password_entry.get()
    if len(website)==0 or len(email)==0:
        messagebox.showwarning(title="Oops",message="Please don't leave any fields empty!")
        is_ok=False
    else:
     is_ok=  messagebox.askokcancel(title=website,message=f"These are the details entered:\nEmail: {email} \nPassword: {password}\nIs it ok to save?")

    if is_ok:
      with open("../../python programs/passwords.txt","a") as data_file:
         data_file.write(f"{website}|| {email} || {password}\n")
         website_entry.delete(0,END)
         email_entry.delete(0,END)
         email_entry.insert(0, "Razdvora232@gmail.com")
         password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas =Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#label



website_label =Label(text="Website:")
website_label.grid(row=1,column=0)
email_label =Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label =Label(text="Password:")
password_label.grid(row=3,column=0)

#Entries
website_entry =Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"Razdvora232@gmail.com")
password_entry=Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2)
#Buttons
generate_btn= Button(text="Generate Password",width=18,command=generate_password)
generate_btn.grid(row=3,column=3)
add_btn=Button(text="Add",width=30,command=save)
add_btn.grid(row=4,column=1,columnspan=2)

window.mainloop()