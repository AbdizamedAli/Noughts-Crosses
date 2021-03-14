import utility as s1

class TicTacToe():
    # Constructor function
    def __init__(self):
        # Properties
        self.Board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.EmptyCells = [0,1,2,3,4,5,6,7,8]
        self.Turn = 'O'
        self.Winner = None
        self.StatesX = []
        self.StatesO = []

    def RandomTurn(self):
        player = self.Turn
        emptyCell = s1.GetRandomElement(s1.GetEmptyCells(self.Board))
        self.Board[emptyCell] = player 
    
    def BestTurn(self, StateValues):
        Values = []
        for Index in self.EmptyCells:
            Board = self.Board.copy()
            Board[Index] = self.Turn
            stringBoard = s1.ListToString(Board)
            corValue = StateValues.get(stringBoard,0)
            Values.append(corValue)
        Indices = s1.MaxIndices(Values)
        Index = s1.GetRandomElement(Indices)
        Position = self.EmptyCells[Index]
        self.Board[Position] = self.Turn

    def HumanVsComputer(self,Game, stateValues,PrintGame):
        if PrintGame :
            print(self)
            print(self.Turn + "'s turn:")
        if self.Turn == 'X':
            self.GetHumanTurn(Game)
        elif self.Turn == 'O':
            self.BestTurn(stateValues)
        self.Update()

        return

    def LearningTurn(self, stateValues):
        import random
        r = random.uniform(0,1)
        if r <= 0.3:
            self.RandomTurn
        else:
            self.BestTurn(stateValues)
        return

    def ComputerVsComputer( self , StateValuesX , StateValuesO,PrintGame ):
        while self.Winner == None:
            if PrintGame:
                print(self)
                print(self.Turn,"'s turn")
            # Player X
            if self.Turn == 'X':
                self.LearningTurn(StateValuesX)
            # Player O
            elif self.Turn == 'O':
                self.LearningTurn(StateValuesO)
            self.Update()
            if PrintGame:
                print(self)
                print(self.Winner," wins!")
        return

    def GetHumanTurn(self,Game):        
        self.Board[Game.Move] = self.Turn

           
    def Update(self):
        self.EmptyCells = s1.GetEmptyCells(self.Board)
        player = self.Turn
        if player == 'X':
            self.StatesX.append(s1.ListToString(self.Board))
            self.Turn = 'O'
        elif player == 'O':
            self.StatesO.append(s1.ListToString(self.Board))
            self.Turn = 'X'
        else:
            raise Exception("Invalid Turn")
        self.IsGameOver()
        return


    # Function which prints out the board
    # Call this function using 'print(self)'
    def __str__(self):
        Board = self.Board
        # Printing upper border
        print("╔═══╦═══╦═══╗")
        # Printing the first row
        print('║', Board[0], '║', Board[1], '║', Board[2], '║')
        print("╠═══╬═══╬═══╣")
        # Second row
        print('║', Board[3], '║', Board[4], '║', Board[5], '║')
        print("╠═══╬═══╬═══╣")
        # Third row
        print('║', Board[6], '║', Board[7], '║', Board[8], '║')
        # Lower border
        print("╚═══╩═══╩═══╝")
        return ''

    def IsGameOver(self):
        Board = self.Board
        # Check to see if we have any three in a row
        # The rows
        Row1 = Board[0] + Board[1] + Board[2]
        Row2 = Board[3] + Board[4] + Board[5]
        Row3 = Board[6] + Board[7] + Board[8]
        # The columns
        Col1 = Board[0] + Board[3] + Board[6]
        Col2 = Board[1] + Board[4] + Board[7]
        Col3 = Board[2] + Board[5] + Board[8]
        # The diagonals
        Diag1 = Board[0] + Board[4] + Board[8]
        Diag2 = Board[2] + Board[4] + Board[6]

        Threes = [Row1, Row2, Row3, Col1, Col2, Col3, Diag1, Diag2]


        if 'XXX' in Threes:
            self.Winner = 'X'
        elif 'OOO' in Threes:
            self.Winner = 'O'

        # Check to see if the board is full
        elif self.EmptyCells == []:
            self.Winner = 'Tie'


#######################
# TESTING
# - Uncomment one at a time (and recomment them when you move on to the next test)
#######################

# Game = TicTacToe()
# print(Game)

# # Task 1:
# Game.RandomTurn()
# print(Game)

# # Task 2:
# Game.HumanTurn()
# print(Game)

# Task 3:
# print("BEFORE")
# print("Board: ", Game.Board, "\nEmpty Cells: ", Game.EmptyCells, "\nTurn: ", Game.Turn, "\nWinner: ", Game.Winner, "\nStatesX: ", Game.StatesX, "\nStatesO: ", Game.StatesO)
# Game.RandomTurn()
# Game.Update()
# print("\nAFTER")
# print("Board: ", Game.Board, "\nEmpty Cells: ", Game.EmptyCells, "\nTurn: ", Game.Turn, "\nWinner: ", Game.Winner, "\nStatesX: ", Game.StatesX, "\nStatesO: ", Game.StatesO)

# # Task4:
# Game = TicTacToe()
# Game.HumanVsRandom()
