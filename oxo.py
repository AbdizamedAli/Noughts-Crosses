import utility as util

class TicTacToe():
    # Constructor function
    def __init__(self):
        # Properties
        self.Board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.EmptyCells = [0,1,2,3,4,5,6,7,8]
        self.Turn = 'X'
        self.Winner = None
        self.StatesX = []
        self.StatesO = []

    def RandomTurn(self):
        player = self.Turn
        emptyCell = util.GetRandomElement(util.GetEmptyCells(self.Board))
        self.Board[emptyCell] = player 
    
    def BestTurn(self, StateValues):
        Values = []
        for Index in self.EmptyCells:
            Board = self.Board.copy()
            Board[Index] = self.Turn
            stringBoard = util.ListToString(Board)
            corValue = StateValues.get(stringBoard,0)
            Values.append(corValue)
        Indices = util.MaxIndices(Values)
        Index = util.GetRandomElement(Indices)
        Position = self.EmptyCells[Index]
        self.Board[Position] = self.Turn
    
    def HumanVsComputer(self, stateValues,PrintGame):
        while self.Winner == None:
            if PrintGame :
                print(self)
                print(self.Turn + "'s turn:")
            if self.Turn == 'X':
                self.HumanTurn()
            elif self.Turn == 'O':
                self.BestTurn(stateValues)
            self.Update()
        if PrintGame:
            print(self)
            print(self.Winner + " wins!")
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

    def HumanTurn(self):
        # Ask the user (you) to input a number/position
        print("Please input a number from 0-8 corresponding to the position in which you wish to play:")
        Input = input()
        # If the input is not a number between 0 and 8 ask again
        if (len(Input) != 1) or (ord(Input) < 48) or (ord(Input) > 56):
            print("Incorrect input. Please try again.")
            self.HumanTurn()
            return
        # Turn the input from a string into an integer
        Position = int(Input)
        if  Position not in self.EmptyCells:
            print("Cell is already filled")
            self.HumanTurn()
        self.Board[Position] = self.Turn
  
    def Update(self):
        self.EmptyCells = util.GetEmptyCells(self.Board)
        player = self.Turn
        if player == 'X':
            self.StatesX.append(util.ListToString(self.Board))
            self.Turn = 'O'
        elif player == 'O':
            self.StatesO.append(util.ListToString(self.Board))
            self.Turn = 'X'
        else:
            raise Exception("Invalid Turn")
        self.IsGameOver()
        return

    def HumanVsRandom(self):
        while self.Winner == None:
            print(self)
            print(self.Turn + "'s turn:")
            if self.Turn == 'X':
                self.HumanTurn()
            elif self.Turn == 'O':
                self.RandomTurn()
            self.Update()
        print(self)
        print(self.Winner + " wins!")
        return

    # Function which prints out the board
    # Call this function using 'print(self)'
    def __str__(self):
        Board = self.Board
        # Printing upper border
        print("╔═══╦═══╦═══╗")
        # Printing the first row
        print('║', Board[0], '║', Board[1], '║', Board[2], '║')
        print("╠═══╬═══╬═══╣5")
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