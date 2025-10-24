from modules.recognition import recognize_face, recognize_all_faces, recognize_faces_in_real_time, \
    recognize_theft_faces_in_real_time
from modules.registration import register_face


def main():

    while True:
        print("\n--- MENU ---")
        print("1. Registrar rosto")
        print("2. Reconhecer rosto")
        print("3. Reconhecer rostos")
        print("4. Reconhecimento de rostos em tempo real")
        print("5. Reconhecimento de rostos intrusos")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Digite o nome: ")
           # age = input("Digite a idade: ")
            register_face(name, "age")
        elif choice == "2":
            recognize_face()
        elif choice == "3":
            recognize_all_faces()
        elif choice == "4":
            recognize_faces_in_real_time()
        elif choice == "5":
            recognize_theft_faces_in_real_time()
        elif choice == "6":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
