import random
import string

lettere = input("La tua password deve contenere delle lettere? (Sì/No)\n").capitalize()

numeri = input("La tua password deve contenere dei numeri? (Sì/No)\n").capitalize( )

caratteri_speciali = input("La tua password deve contenere dei caratteri speciali? (Sì/No)\n").capitalize()

lunghezza = int(input("Inserisci il numero di caratteri che deve contenere la tua password o pin:\n"))

def genera_password(lunghezza, lettere, numeri, caratteri_speciali):
    caratteri = ''
    
    if lettere == 'Si':
        caratteri += string.ascii_letters
    
    if numeri == 'Si':
        caratteri += string.digits
    
    if caratteri_speciali == 'Si':
        caratteri += string.punctuation
            
    password = ''.join(random.choice(caratteri) for _ in range(lunghezza))   
    return password

print('-'*50)
while True:
    if lunghezza < 4:
        print('La password non è sicura!')
        break
    
    elif lunghezza >= 4 and lunghezza < 8:
            risposta = input('La password può essere non molto sicura vuoi procedere comunque? (Si/No)\n').capitalize()
            print('-'*50)
            while True:
                if risposta == "Si":
                    password_generata = genera_password(lunghezza,lettere,numeri,caratteri_speciali)
                else: 
                    print("Uscita dal programma in corso")
                    break
                
                break
            print(f"Questo è la tua password: {password_generata}")
    
    elif lunghezza >= 8:
        password_generata = genera_password(lunghezza,lettere,numeri,caratteri_speciali)
        print(f"Questo è la tua password: {password_generata}")
    
    break

input("Premi Invio per chiudere...")
