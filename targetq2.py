def main():
    user_input = input("Informe uma string: ")
    count = user_input.lower().count('a')

    if count:
        print(f"A letra 'a' aparece {count} vez(es) na string.")
    else:
        print("A letra 'a' não está presente na string.")


if __name__ == "__main__":
    main()