# sappo_core/main.py

from sappo_core.values import greet_user

def main():
    user = input("Siapa namamu? ")
    greet_user(user)

if __name__ == "__main__":
    main()
