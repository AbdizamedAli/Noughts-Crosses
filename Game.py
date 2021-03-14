import pygame
from move import TicTacToe
from utility import GetKey
import os

class GameClass():
    def __init__(self):
        self.Width = 100
        self.Height = 100
        self.Font_Size = None
        self.Scale = 10
        self.LocationDict = self.NumFromCenter()
        self.Move = None
        self.GameSpeed = 25

        # Colours
        self.BackgroundColour = (0,0,0)
        self.TextColour = (0,255,255)
        self.LineColour = 0xffff00
        #Initialise pygame
        pygame.init()
        self.Icon = pygame.image.load_extended('assets/oxo.png')
        self.Display = pygame.display.set_mode( (self.Width * self.Scale, self.Height * self.Scale) )
        self.Clock = pygame.time.Clock()
        pygame.display.set_caption('Noughts and Crosses')
        pygame.display.set_icon(self.Icon)

    def Play(self,SVs):
        GameOver = False
        GameStarted = False
        T = TicTacToe()
        while not GameOver:
            self.DisplayFrame(T,T.Turn + "'s turn:")
            self.Clock.tick(self.GameSpeed)
            if T.Winner != None:
                self.DisplayFrame(T,T.Turn + "'s turn:")
                GamePaused = True
                while GamePaused:
                    self.DisplayFrame(T,f"GAME OVER: Winner is {T.Winner}")
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            GamePaused = False
                            GameOver = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            GameClass().Play(SVs)
                            return    
            if T.Turn == 'O':
                self.DisplayFrame(T,T.Turn + "'s turn:")
                T.HumanVsComputer(self,SVs,False)
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0]:
                    if self.GetRect(pygame.mouse.get_pos(),T):
                        T.HumanVsComputer(self,SVs,False)

    
    def DisplayFrame(self,Tic,text):
        self.Display.fill(self.BackgroundColour)
        self.DrawLines()
        for idx,i in enumerate(Tic.Board):
            if i == 'X':
                self.DrawLetter(GetKey(self.LocationDict,idx),'X')
            elif i == 'O':
                self.DrawLetter(GetKey(self.LocationDict,idx),'O')
        self.DisplayText(text)
        pygame.display.update()
    
    def DrawLetter(self,Center,player):
        Font = pygame.font.SysFont('dejavusansmono', self.Font_Size - ((self.Width + self.Height)))
        player_choice = Font.render(player, False, self.TextColour)
        choice_rect = player_choice.get_rect(center=Center)
        self.Display.blit(player_choice, choice_rect)

    def DisplayText(self,Message):
        # Scale up from our grid system to pixels
        Point = [ x*self.Scale for x in [0,0] ]
        # Set the font and size
        Font = pygame.font.SysFont('dejavusansmono',self.Scale)
        TextSurface = Font.render(Message, True, self.TextColour)
        self.Display.blit(TextSurface, Point)
    
    def GetRect(self,MouseLocation, Tic): 
        Rows = [int((self.Width * self.Scale / 3) / 2), int((self.Width * self.Scale / 3) / 2) * 3, int((self.Width * self.Scale / 3) / 2) * 5]
        Cols = [int((self.Height * self.Scale / 3) / 2), int((self.Height * self.Scale / 3) / 2) * 3, int((self.Height * self.Scale / 3) / 2) * 5]
        X,Y = MouseLocation
        CenterX = min(Rows,key=lambda x:abs(x-X))
        CenterY = min(Cols,key=lambda x:abs(x-Y))
        Center = (CenterX,CenterY)
        if self.LocationDict.get(Center) not in  Tic.EmptyCells:
            self.DisplayFrame(Tic,f"This Cell is already Filled")
            return False
        else:
            self.Move = self.LocationDict.get(Center)
            return True
    
    def DrawLines(self):
        vertical_line_1 = int(self.Width * self.Scale / 3) 
        pygame.draw.line(self.Display, self.LineColour, (vertical_line_1, 0), (vertical_line_1, self.Width * self.Scale), self.Scale )
        vertical_line_2 = vertical_line_1 * 2
        pygame.draw.line(self.Display, self.LineColour, (vertical_line_2, 0), (vertical_line_2, self.Width * self.Scale),self.Scale)
        # Draw horizontal lines 
        horizontal_line_1 = int(self.Height * self.Scale/ 3)
        pygame.draw.line(self.Display, self.LineColour, (0, horizontal_line_1), (self.Width * self.Scale, horizontal_line_1),self.Scale )
        horizontal_line_2 = horizontal_line_1 * 2
        pygame.draw.line(self.Display, self.LineColour, (0, horizontal_line_2), (self.Width * self.Scale, horizontal_line_2), self.Scale)
        self.Font_Size = int((int(self.Width * self.Scale / 3) /2) * 4) -  ((self.Width + self.Height)) + self.Scale
        return

    def NumFromCenter(self):
        Rows = [int((self.Width * self.Scale / 3) / 2), int((self.Width * self.Scale / 3) / 2) * 3, int((self.Width * self.Scale / 3) / 2) * 5]
        Cols = [int((self.Height * self.Scale / 3) / 2), int((self.Height * self.Scale / 3) / 2) * 3, int((self.Height * self.Scale / 3) / 2) * 5]
        return { 
                    (Rows[0],Cols[0]) : 0,
                    (Rows[1],Cols[0]) : 1,
                    (Rows[2],Cols[0]) : 2,
                    (Rows[0],Cols[1]) : 3,
                    (Rows[1],Cols[1]) : 4,
                    (Rows[2],Cols[1]) : 5,
                    (Rows[0],Cols[2]) : 6,
                    (Rows[1],Cols[2]) : 7,
                    (Rows[2],Cols[2]) : 8}


