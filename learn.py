import oxo as ox

def Learn(n):
    stateX = {}
    stateO = {}
    for i in range(n):
        game = ox.TicTacToe()
        game.ComputerVsComputer(stateX,stateO,False)
        if game.Winner == 'X':
            statex = UpdateSVs(stateX,game.StatesX,1)
            stateO = UpdateSVs(stateO,game.StatesO,-1)
        elif game.Winner == "O":
            statex = UpdateSVs(stateX,game.StatesX,-1)
            stateO = UpdateSVs(stateO,game.StatesO,1)
        else:
            statex = UpdateSVs(stateX,game.StatesX,0)
            stateO = UpdateSVs(stateO,game.StatesO,0)
    return stateO



def UpdateSVs(StateValues, States, Score):
    # Our learning parameter
    Alpha = 0.2
    # Iterate through the states backwards updating the states
    VSt1 = Score
    for State in reversed(States):
        VSt = StateValues.get(State, 0)
        Value = VSt + (Alpha * (VSt1 - VSt))
        StateValues[State] = Value
        VSt1 = Value
    return StateValues


def Play(TrainingN, TestingN):
    SVs = Learn(TrainingN)
    for i in range(TestingN):
        Game = ox.TicTacToe()
        Game.HumanVsComputer(SVs,PrintGame=True)
