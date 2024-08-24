import random
import string
import os
from termcolor import colored

# دالة لتفريغ الشاشة عند بدء التشغيل فقط
def clear_screen():
    os.system('clear')

# دالة لعرض الشعار مرة واحدة
def display_logo():
    logo = """

   ▄████████  ▄█    █▄   ▄█   ▄█               ▄██████▄     ▄████████ ███▄▄▄▄   
  ███    ███ ███    ███ ███  ███              ███    ███   ███    ███ ███▀▀▀██▄ 
  ███    █▀  ███    ███ ███▌ ███              ███    █▀    ███    █▀  ███   ███ 
 ▄███▄▄▄     ███    ███ ███▌ ███             ▄███         ▄███▄▄▄     ███   ███ 
▀▀███▀▀▀     ███    ███ ███▌ ███            ▀▀███ ████▄  ▀▀███▀▀▀     ███   ███ 
  ███    █▄  ███    ███ ███  ███              ███    ███   ███    █▄  ███   ███ 
  ███    ███ ███    ███ ███  ███▌    ▄        ███    ███   ███    ███ ███   ███ 
  ██████████  ▀██████▀  █▀   █████▄▄██        ████████▀    ██████████  ▀█   █▀  
                             ▀                                                  
                  Version 1.0
                  Support : (Discord : ez.1k)
                 All Rights Reseved To Evil Devil Team
    
    """
    print(colored(logo, 'cyan', attrs=['bold', 'blink']))

# دالة لإنشاء كلمة مرور قوية
def generate_password(length, use_upper, use_digits, use_special):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# دالة لحفظ كلمات المرور في ملف
def save_password(password):
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")
    print(colored("Password saved to passwords.txt", 'green', attrs=['bold']))

# دالة لعرض القائمة الرئيسية
def start_menu():
    clear_screen()
    display_logo()
    print(colored("Welcome to the Advanced Password Generator!", 'yellow', attrs=['bold', 'underline']))
    print(colored("1. Start - ", 'green', attrs=['bold']))
    print(colored("2. Exit - ", 'red', attrs=['bold']))

    choice = input("\nSelect an option : ")
    if choice == '1':
        password_options()
    elif choice == '2':
        exit()
    else:
        print(colored("Invalid choice, please try again. ", 'red', attrs=['bold']))
        start_menu()

# دالة للحصول على خيارات كلمة المرور من المستخدم
def password_options():
    try:
        length = int(input(colored("Enter password length (e.g., 16) -  ", 'blue', attrs=['bold'])))
    except ValueError:
        print(colored("Invalid input, please enter a number.", 'red', attrs=['bold']))
        return password_options()

    use_upper = input(colored("Include uppercase letters? (y/n) : ", 'blue', attrs=['bold'])).lower() == 'y'
    use_digits = input(colored("Include digits? (y/n): ", 'blue', attrs=['bold'])).lower() == 'y'
    use_special = input(colored("Include special characters? (y/n): ", 'blue', attrs=['bold'])).lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_special)
    print(colored(f"\nGenerated Password: {password}", 'green', attrs=['bold', 'blink']))

    save_choice = input(colored("Save password to file? (y/n): ", 'yellow', attrs=['bold'])).lower()
    if save_choice == 'y':
        save_password(password)

    again = input(colored("Generate another password? (y/n): ", 'yellow', attrs=['bold'])).lower()
    if again == 'y':
        password_options()
    else:
        start_menu()

if __name__ == "__main__":
    clear_screen()  # تنظيف الشاشة مرة واحدة عند بدء التشغيل
    display_logo()  # عرض اللوجو مرة واحدة عند بدء التشغيل
    start_menu()    # بدء القائمة الرئيسية
