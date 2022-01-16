def menu(title, items):
    menu_text = "%s: \n" % title

    for index in range(len(items)):
        menu_text = "%s \n %s. %s" % (menu_text, index + 1, items[index])

    opt = int(input("%s \n" % menu_text))

    if (opt < 1 or opt > len(items)):
        opt = menu(title, items)

    return opt


def menu_init():
    title = 'My foo bar pets'
    opts = ('Register', 'Log in', 'Exit',)

    return menu(title, opts)


def menu_opt_pets():
    title = 'What do you want to do with the pets?'
    opts = ('Adopt a pet', 'Play with your pets', 'Exit',)

    return menu(title, opts)

def menu_pet_activities():
    title = 'Pets Activities'
    opts = ('Play', 'Feed', 'Give water', 'My stats', 'Exit',)

    return menu(title, opts)


def user_register():
    name = input("Give me your first name\n")
    email = input("Give me your email\n")

    return {"name": name, "email": email,}


def user_login():
    email = input("Give me your email for log in\n")
    return {"email": email,}


def pet_register():
    name = input("Give me the name of your pet:\n")
    specie = input("Now the specie of your pet:\n")
    age = input("The age of your pet:\n")
    #id_owner = pass


    return {"name": name, "specie": specie, "age": age,}