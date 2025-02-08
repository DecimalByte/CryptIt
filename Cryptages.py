# Version 1.0 - 05/2023
# Made by the developer/ Cree par le developeur -- Dilem Boussad -- @DecimalByte
# School Computer Science Project/ Projet NSI

from tkinter import *
from tkinter import messagebox

# ROT13
class rot13:
    def __init__(self):

        # Creation of Tkinter GUI
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("CryptIt")
        self.root.resizable(False, False)

        # Label
        self.label = Label(self.root, text="Input your message : ", font=('Arial', 16))
        self.label.pack(padx=20, pady=20)

        # Entry
        self.entry = Entry(self.root, width=50, font=('Arial', 16))
        self.entry.pack(pady=20, padx=20)

        # Manages buttons 'buttonManager'
        self.buttonManager = Frame(self.root)
        self.buttonManager.columnconfigure(0, weight=1)
        self.buttonManager.columnconfigure(1, weight=1)

        # Encrypt button
        self.button = Button(self.buttonManager, width=18, bg="green", fg="white", bd=0, font=('Arial', 14), text="Encrypt", command=self.rot13_encryption)
        self.button.grid(row=0, column=0)

        # Decrypt button
        self.button1 = Button(self.buttonManager, width=18, bg="red", fg="white", bd=0, font=('Arial', 14), text="Decrypt", command=self.rot13_decryption)
        self.button1.grid(row=0, column=1)

        self.buttonManager.pack(fill="x")
        
        self.root.mainloop()

    # ROT13 Encryption
    def rot13_encryption(self):
        
        # Message inputted by user
        message = self.entry.get()

        # Uppercase version of message
        upper_message = message.upper()

        # Encrypted text that will be outputted to the user
        encryp_text = ""

        # Key
        key = 13

        # Loops in the range of the message length
        for i in range(len(upper_message)):

            # Adds the key to the unicode of the characters for a 13 character rotation
            x = ord(upper_message[i]) + key
            
            # Encryption of the message
            if ord(upper_message[i]) == 32:
                encryp_text += " "
            elif x > 90:
                x -= 26
                encryp_text += chr(x)
            else:
                encryp_text += chr(x)

        # Takes as argument encrypted or decrypted text and
        # keeps the format of the original message
        def format_message(text):
            formated_text = ""
            for i in range(len(text)):
                if message[i].isupper():
                    formated_text += text[i].upper()
                elif message[i].islower():
                    formated_text += text[i].lower()
                else:
                    formated_text += message[i]
            return formated_text

        # Changes encryp_text to its original format
        encryp_text = format_message(encryp_text)

        # Ensures that the input isn't empty
        if encryp_text != "":

            # Encrypted message popup
            popup = Toplevel(self.root)
            popup.title("The Encrypted message")
            popup.geometry("400x200")
            popup.resizable(False, False)
            popup.configure(bg="green")

            text = Text(popup, font="Consolas 16")
            text.pack(padx=20, pady=20)

            text.insert("1.0", encryp_text)
        else:

            # Error if the input is empty
            messagebox.showerror(title="Error", message="Enter a message to encrypt!")


    # ROT13 Decryption
    def rot13_decryption(self):
        
       # Message inputted by user
        message = self.entry.get()

        # Uppercase version of message
        upper_message = message.upper()

        # Key
        key = 13
        decryp_text = ""

        # Loops in the range of the message length
        for i in range(len(upper_message)):
            
            # Subtracts unicode from key
            temp = ord(upper_message[i]) - key

            # Encryption algorithm
            if ord(upper_message[i]) == 32:
                decryp_text += " "
            elif temp < 65:
                temp += 26
                decryp_text += chr(temp)
            else:
                decryp_text += chr(temp)

        # Takes as argument encrypted or decrypted text and
        # keeps the format of the original message (ex. capital letters...)
        def format_message(text):
            formated_text = ""
            for i in range(len(text)):
                if message[i].isupper():
                    formated_text += text[i].upper()
                elif message[i].islower():
                    formated_text += text[i].lower()
                else:
                    formated_text += message[i]
            return formated_text

        # Changes decryp_text to its original format
        decryp_text = format_message(decryp_text)

        # Assures that the input isn't empty
        if decryp_text != "":

            # Decrypted message popup
            popup = Toplevel(self.root)
            popup.title("The Decrypted message")
            popup.geometry("400x200")
            popup.resizable(False, False)
            popup.configure(bg="red")

            text = Text(popup, font="Consolas 16")
            text.pack(padx=20, pady=20)

            text.insert("1.0", decryp_text)
        else:
            # Error if the input is empty
            messagebox.showerror(title="Erreur", message="Entrez un message pour le decrypter!")


# Cesar encoding
class cesar:
    def __init__(self):

        # Creation of Tkinter GUI
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Cryptography")
        self.root.resizable(False, False)

        # Label
        self.label = Label(self.root, text="Entrez votre message : ", font=('Arial', 16))
        self.label.pack(padx=20, pady=20)

        # Entry
        self.entry = Entry(self.root, width=50, font=('Arial', 16))
        self.entry.pack(pady=20, padx=20)

        self.label1 = Label(self.root, text="Entrez la clé : ", font=('Arial', 16))
        self.label1.pack(padx=20, pady=20)

        self.entry1 = Entry(self.root, width=50, font=('Arial', 16))
        self.entry1.pack(pady=20, padx=20)

        # Manages buttons 'buttonManager'
        self.buttonManager = Frame(self.root)
        self.buttonManager.columnconfigure(0, weight=1)
        self.buttonManager.columnconfigure(1, weight=1)

        # Encrypt button
        self.button = Button(self.buttonManager, width=18, bg="green", fg="white", bd=0, font=('Arial', 14), text="Crypter", command=self.cesar_encryption)
        self.button.grid(row=0, column=0)

        # Decrypt button
        self.button1 = Button(self.buttonManager, width=18, bg="red", fg="white", bd=0, font=('Arial', 14), text="Decrypter", command=self.cesar_decryption)
        self.button1.grid(row=0, column=1)

        self.buttonManager.pack(fill="x")

        self.root.mainloop()

    # Caesar encryption
    def cesar_encryption(self):

        # Message inputted by user
        message = self.entry.get()
        upper_message = message.upper()

        # Ensure that a key is entered
        if self.entry1.get() == "":
            # Error if no key is entered
            messagebox.showerror(title="Erreur", message="Entrez la clé!")


        # Key inputted by user
        k = self.entry1.get().upper()
        key = int(k)

        # Encrypted text that will be outputted to the user
        encryp_text = ""

        # Loops in the range of the message length
        for i in range(len(upper_message)):

            # Adds the key to the unicode of the characters for a chosen character rotation
            temp = ord(upper_message[i]) + key

            # Encryption of the message
            if ord(upper_message[i]) == 32:
                encryp_text += " "
            elif temp > 90:
                temp -= 26
                encryp_text += chr(temp)
            else:
                encryp_text += chr(temp)

        # Takes as argument encrypted or decrypted text and
        # keeps the format of the original message (ex. capital letters...)
        def format_message(text):
            formated_text = ""
            for i in range(len(text)):
                if message[i].isupper():
                    formated_text += text[i].upper()
                elif message[i].islower():
                    formated_text += text[i].lower()
                else:
                    formated_text += message[i]
            return formated_text

        # Changes encryp_text to its original format
        encryp_text = format_message(encryp_text)

        # Continue if input isn't empty
        if encryp_text != "":

            # Encrypted message popup
            popup = Toplevel(self.root)
            popup.title("Encryption")
            popup.geometry("400x200")
            popup.resizable(False, False)
  

            text = Text(popup, font="Consolas 16")
            text.pack(padx=20, pady=20)

            text.insert("1.0", encryp_text)
        else:
            # Error if the input is empty
            messagebox.showerror(title="Erreur", message="Entrez un message pour le crypter!")



    # Caesar decryption
    def cesar_decryption(self):

        # Message inputted by user
        message = self.entry.get()

        # Uppercase version of message
        upper_message = message.upper()
        
        # Ensure that a key is entered
        if self.entry1.get() == "":
            # Error if no key is entered
            messagebox.showerror(title="Erreur", message="Entrez la clé!")

        # Encrypted text that will be outputted to the user
        k = self.entry1.get().upper()
        key = int(k)

        decryp_text = ""

        # Boucle for qui balaye la longueur du message
        for i in range(len(upper_message)):
            temp = ord(upper_message[i]) - key
            if ord(upper_message[i]) == 32:
                decryp_text += " "
            elif temp < 65:
                temp += 26
                decryp_text += chr(temp)
            else:
                decryp_text += chr(temp)

        # Takes as argument encrypted or decrypted text and
        # keeps the format of the original message (ex. capital letters...)
        def format_message(text):
            formated_text = ""

            for i in range(len(text)):
                if message[i].isupper():
                    formated_text += text[i].upper()
                elif message[i].islower():
                    formated_text += text[i].lower()
                else:
                    formated_text += message[i]
            return formated_text

        decryp_text = format_message(decryp_text)

        # Assurer que l'entree du message n'est pas vide
        if decryp_text != "":

            popup = Toplevel(self.root)
            popup.title("Encryption")
            popup.geometry("400x200")
            popup.resizable(False, False)
         

            text = Text(popup, font="Consolas 16")
            text.pack(padx=20, pady=20)

            text.insert("1.0", decryp_text)
        else:
            # Si le message est vide, une erreur se produira chez l'utilisateur
            messagebox.showerror(title="Erreur", message="Entrez un message pour le decrypter!")
            

class Main:
    if __name__ == "__main__":

        # Mainscreen GUI
        main = Tk()
        main.geometry("500x500")
        main.title("CryptIt!")
        main.resizable(False, False)

        # Label
        label0 = Label(main, text=" \n >>\__  Crypt It !  __/<< ", fg="black", font=('Roboto', 18))
        label0.pack(padx=10, pady=10)
        
        label = Label(main, text=" \n  \nChoose the Encryption/Decryption Method", fg="black", font=('Arial', 14))
        label.pack(padx=20, pady=20)
        
        # Button manager
        buttonManager = Frame(main)
        buttonManager.columnconfigure(0, weight=1)
        buttonManager.columnconfigure(1, weight=1)
        buttonManager.columnconfigure(2, weight=1)

        button = Button(buttonManager, text="ROT13", width=18, bg="#00a7e1", fg="white", bd=0, font=('Arial', 14), command=rot13)
        button.grid(row=0, column=0)

        button1 = Button(buttonManager, width=18, text="Caeser Cipher", bg="#00a7e1", fg="white", bd=0, font=('Arial', 14), command=cesar)
        button1.grid(row=0, column=1)

        buttonManager.pack(fill="x")

        # Credits
        name = Label(main, text="Made by DILEM Boussad\n Version 1.0 ", font=('Consolas', 12))
        name.pack(padx=10, pady=120)

        main.mainloop()

