import pandas as pd
import csv


def add_kills(gamename, num_add):
    with open('Killcounter.csv') as archivo:
        reader_arch = csv.reader(archivo)
        for lineas in reader_arch:
            if (lineas[0]==gamename):
                Kills = int(lineas[1])
                Kills = int(Kills+num_add)
    df = pd.read_csv('Killcounter.csv')
    df.loc[df["GAME"]==gamename, "KILLS"] = Kills
    df.to_csv("Killcounter.csv", index=False)
    return
        
        
def show_game_kills(gamename):
    df = pd.read_csv('Killcounter.csv')
    Kills = df[(df['GAME'] == gamename)]
    try:
        print(Kills.head())    
    except KeyError:
        pass
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
        ADDKILLS = int(input("Cuantas kills para añadir: "))
        add_kills(Game, ADDKILLS)
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