from guizero import App, Text, TextBox, Box, PushButton, Window

from random import choice, shuffle


#Creates Password At Random
def generate_pass():

    #Only works for passwords 20 characters or less
    if int(password_length.value) > 20:
        app.error("Password Length", "Enter a password less than 21 characters")
        return


    #Checks for values less than or equal to zero
    try:
        count = [int(lowercase_count.value), int(uppercase_count.value), int(special_char_count.value), int(number_count.value)]
        for num in count:
            if num <= 0:
                raise ValueError()
    except:
        app.error("Error", "Make sure all values are greater than zero")
        return


    #Makes sure numbers are not greater than password length
    if sum(count) > int(password_length.value) or int(password_length.value) < 7:

        err_text = "Enter A more secure password" if int(password_length.value) < 7 else "Characters are greater than password length"
        app.error("", err_text)
        return

    # Shuffles List
    def shuffle_pass(p):
        lst = list(p)
        shuffle(lst)
        pass_text.value = ''.join(lst)

    #Possible Values
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = '!$-_?'
    numbers = '123456789'
    password = ''


    characters = [lower, upper, symbols, numbers]

    #Additional Characters
    random_chars = int(password_length.value) - (int(lowercase_count.value) + int(uppercase_count.value) + int(special_char_count.value))


    for i, c in enumerate(characters):
        for n in range(count[i]):
            password += choice(c)

    if random_chars > 0:
        for f in range(random_chars - 1):
            seq = choice(characters)
            password += choice(seq=seq)

    #Shuffles Password
    p_list = list(password)
    shuffle(p_list)

    pass_window = Window(app, height=100, width=300, title="Password")
    pass_text = TextBox(pass_window, text=''.join(p_list), align='top', width="fill")
    shuffle_button = PushButton(pass_window, text="Shuffle", command=shuffle_pass, args=[pass_text.value])


"""
    Creates the GUI Below
    Generates a Password at random using the restrictions
"""

app = App(title="Password Generator", height=200, width=275)

title_box = Box(app, width="fill", align="top", border=True)
title_box.bg = "gray"

message = Text(title_box, text="Create A Password Below")

password_box = Box(app, width="fill", height =175, border=True, layout="grid")
password_box.bg = "lightgray"

password_label = Text(password_box, text="Password Length: ", grid=[0,0], align="left")
password_length = TextBox(password_box, grid=[1,0], text="8")

lowercase_label = Text(password_box, text="Lowercase Letters: ", grid=[0,1], align="left")
lowercase_count = TextBox(password_box, grid=[1,1], text="3")

uppercase_label = Text(password_box, text="Uppercase Letters: ", grid=[0,2], align="left")
uppercase_count = TextBox(password_box, text="3", grid=[1,2])

special_char_label = Text(password_box, text="Special Characters: ", grid=[0,3], align="left")
special_char_count = TextBox(password_box, text="1", grid=[1,3])

number_label = Text(password_box, text="Numbers: ", grid=[0,4], align="left")
number_count = TextBox(password_box, text='1', grid=[1,4])

submit_label = Text(password_box, text="Generate Password: ", grid=[0,5], align="left")
submit = PushButton(password_box, command=generate_pass, grid=[1,5], text="Submit", padx=5, pady=5)

app.display()

