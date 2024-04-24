import random 
import string
def generate_password(length):
    characters=string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choice(characters) for x in range(length))
    return password
def main():
    print(" Welcome to Password Generator !")
    length=int(input("enter the desired length of the password: "))

    if length<=0:
        print("Invalid length. Please enter a positive integer.")
        return 

    password=generate_password(length)
    print("Generated password:\n",password)

if __name__=="__main__":
    main()
