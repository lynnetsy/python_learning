import utils
import repositories


def main():
    owner_repo = repositories.OwnerRepository()
    pet_repo = repositories.PetRepository()
    user = None

    option = utils.menu_init()

    if option == 1:
        owner_data = utils.user_register()
        owner_repo.save(owner_data['name'],owner_data['email'])
        user = owner_repo.find_by_email(owner_data['email'])
    elif option == 2:
        owner_data = utils.user_login()
        user = owner_repo.find_by_email(owner_data['email'])
    else:
        print("Goodbye, thanks for your time")
        return

    print("Hi!  %s" % user.name)

    opt = 0
    while opt != 3:
        opt = utils.menu_opt_pets()

        if opt == 1:
            pet_data = utils.pet_register()
            pet_repo.save(pet_data['name'], pet_data['specie'], pet_data['age'], user)
        elif opt == 2:
            # Obtener todas las mascotas del usuario
            pets = pet_repo.get_by_owner(user)
            # Imprimir menu de mascotas
            opt = utils.menu('My current pets', pets)
            # Obtener a la mascota elegida por el usuario
            choose_pet = pets[opt - 1]
            print(choose_pet)
        else:
            print('BYE BYE BYEEEE ToT')




if __name__=='__main__':
    main()
