import pandas as pd


def add_kills(gamename, num_add):
    df = pd.read_csv('Killcounter.csv')
    Kills = df[(df['GAME'] == gamename)]
    print(Kills.head())
    return 

def show_game_kills(gamename):
    df = pd.read_csv('Killcounter.csv')
    Kills = df[(df['GAME'] == gamename)]
    print(Kills.head())    
    return 




def main():
    print("Que desea hacer?")
    print("1).- Añadir kills")
    print("2).- Ver estadisticas")
    print("3).- Cerrar")
    Quedesea = int(input("Seleccione: "))
    while (Quedesea<1 or Quedesea>3):
        print("ERROR intente de nuevo. Ingrese un numero entre 1-3")
        Quedesea = int(input("Seleccione: "))
    if (Quedesea==1):
        Game = str(input("Ingrese juego: "))
        Game = Game.upper()
        main()
    if (Quedesea==2):
        Game = str(input("Ingrese juego: "))
        Game = Game.upper()
        show_game_kills(Game)
        main()
    if (Quedesea==3):
        return 




if __name__ == "__main__":
    main()