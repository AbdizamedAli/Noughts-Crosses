from Game import GameClass
from learn import Learn

def main():
    Game = GameClass()
    Svs = Learn(100000)
    Game.Play(Svs)


if __name__ == "__main__":
    main()