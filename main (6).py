click=''
import tkinter
root = tkinter.Tk()
canvas=tkinter.Canvas(root,height=750,width=1000)
var= tkinter.StringVar()
label=tkinter.Label(root,textvariable=var)
var.set("select a piece")
Row = [1,2,3,4,5,6,7,8]
Column =['a','b','c','d','e','f','g','h']
PieceList=[]
Dict_x={'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[],'h':[]}
Dict_y={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
boardx1=150
boardy1=25
boardx2=850
boardy2=725
rectangle=canvas.create_rectangle(150,25,850,725)
board_length=boardx2-boardx1
square_length=board_length/8
(boardx1+square_length,boardy1+square_length)
Squarey1=boardy1
Squarey2=boardy1+square_length
#evey thing up here are variables that are being defined for later use in the program
for column in Column:
    for row in Row:
        Squarey1 = boardy1 + (Row.index(row) * square_length)
        Squarey2 = boardy1 + square_length + (Row.index(row) * square_length)
        Squarex1 = boardx1 + (Column.index(column) * square_length)
        Squarex2 = boardx1 + square_length + (Column.index(column) * square_length)
        Dict_x[column]=([Squarex1,Squarex2])
        Dict_y[row]=([Squarey1, Squarey2])
        if Row.index(row)%2==0 and Column.index(column)%2==0 :
            canvas.create_rectangle(Squarex1,Squarey1,Squarex2,Squarey2,fill='Orange')
        if Row.index(row)%2==1 and Column.index(column)%2==1:
            canvas.create_rectangle(Squarex1, Squarey1, Squarex2, Squarey2, fill='Orange')
        if Column.index(column)%2==0 and Row.index(row)%2==1:
            canvas.create_rectangle(Squarex1,Squarey1,Squarex2,Squarey2, fill='Black')
        if Column.index(column)%2==1 and Row.index(row)%2==0:
            canvas.create_rectangle(Squarex1, Squarey1, Squarex2, Squarey2, fill='Black')
# These lines are how we set up the board colors
print(Dict_x)
print(Dict_y)
class piece:
    def __init__(self,position,color,health):
        self.health = health
        self.position=position
        self.color=color
        PieceList.append(self)
# This is where the "class" piece was first defined and all of the pieces "Init" functions for "self" where also defined
class pawn(piece):
    def __init__(self,position,color,health):
        super().__init__(position,color,health)
        self.startingposition = position
        if color == 'white':
            self.pawn1 = tkinter.PhotoImage(file=r"C:\Users\sarah\PycharmProjects\chess\0cbcd810018309.560de1db2832c_(2).png")
        else:
            self.pawn1 = tkinter.PhotoImage(file=r"C:\Users\sarah\PycharmProjects\chess\0cbcd810018309.560de1db2832c_(8).png")
        self.x = boardx1 + float(Column.index(self.position[0]) * square_length + .5 * float(square_length))
        self.y = boardy1 + float(Row.index(self.position[1]) * square_length + .5 * float(square_length))
        self.image=canvas.create_image(self.x,self.y, image=self.pawn1)
    def check_move(self,column, row):
        self.position
        global Piece_check
        Piece_check = 0
        if self.position[0] == column and row - self.position[1] == 1 and self.color=='white':
            for x in PieceList:
                if x.position == [column, row]:
                    Piece_check+=1
            if Piece_check==1:
                return False
            else:
                return True
        if self.position[0] == column and row - self.position[1] == 2 and self.color=='white':
            if self.startingposition==self.position:
                for x in PieceList:
                    if x.position == [column, row]:
                        Piece_check += 1
                if Piece_check == 1:
                    return False
                else:
                    return True
            else:
                return False
        if row-self.position[1]==1 and (Column.index(column)-Column.index(self.position[0])==1 or Column.index(column)-Column.index(self.position[0])== -1) and self.color=='white':
            for x in PieceList:
                if x.position == [column, row]:
                    print('piecefound')
                    Piece_check+=1
            if Piece_check==1:
                return True
            else:
                return False
        elif self.position[0] == column and row - self.position[1] ==-1 and self.color=='black':
            for x in PieceList:
                if x.position == [column, row]:
                    Piece_check += 1
            if Piece_check == 1:
                return False
            else:
                return True
        if self.position[0] == column and row - self.position[1] == -2 and self.color == 'black':
            if self.startingposition == self.position:
                for x in PieceList:
                    if x.position == [column, row]:
                        Piece_check += 1
                if Piece_check == 1:
                    return False
                else:
                    return True
        if row - self.position[1] == -1 and (Column.index(column) - Column.index(self.position[0]) == 1 or Column.index(column) - Column.index(self.position[0]) == -1 and self.color == 'black'):
            for x in PieceList:
                if x.position == [column, row]:
                    Piece_check += 1
            if Piece_check == 1:
                return True
            else:
                return False
    def move (self,position):
        canvas.delete(self.image)
        self.position=position
        self.x = boardx1 + float(Column.index(self.position[0]) * square_length + .5 * float(square_length))
        self.y = boardy1 + float(Row.index(self.position[1]) * square_length + .5 * float(square_length))
        self.image = canvas.create_image(self.x, self.y, image=self.pawn1)
PawnA=pawn(['a',2],'white', 'alive')
PawnB=pawn(['b',2],'white','alive')
PawnC=pawn(['c',2],'white','alive')
PawnD=pawn(['d',2],'white','alive')
PawnE=pawn(['e',2],'white','alive')
PawnF=pawn(['f',2],'white','alive')
PawnG=pawn(['g',2],'white','alive')
PawnH=pawn(['h',2],'white','alive')
PawnA1=pawn(['a',7],'black','alive')
PawnB1=pawn(['b',7],'black','alive')
PawnC1=pawn(['c',7],'black','alive')
PawnD1=pawn(['d',7],'black','alive')
PawnE1=pawn(['e',7],'black','alive')
PawnF1=pawn(['f',7],'black','alive')
PawnG1=pawn(['g',7],'black','alive')
PawnH1=pawn(['h',7],'black','alive')
# ^^All of these lines of code are for the first subclass of "Piece". The pawn. In these lines of code,
# we are defining its moveset(Moving once or twice, or moving diagonal if another Piece is present in a spot where it
# can), and defining all of the pawns starting positions(ExplePawnA=pawn(['a',2],'white', 'alive')
class bishop(piece):
    def __init__(self, position, color, health):
        super().__init__(position, color, health)
        if color == 'white':
            self.bishop1 = tkinter.PhotoImage(file=r"C:\Users\sarah\PycharmProjects\chess\0cbcd810018309.560de1db2832c_(5).png")
        else:
            self.bishop1 = tkinter.PhotoImage(file=r"C:\Users\sarah\PycharmProjects\chess\0cbcd810018309.560de1db2832c_(11).png")
        self.x = boardx1 + float(Column.index(self.position[0]) * square_length + .5 * float(square_length))
        self.y = boardy1 + float(Row.index(self.position[1]) * square_length + .5 * float(square_length))
        self.image = canvas.create_image(self.x, self.y, image=self.bishop1)
    def check_move(self, column, row):
        self.position
        if row-self.position[1] == Column.index(column) - Column.index(self.position[0]) or self.position[1]-row == Column.index(column) - Column.index(self.position[0]):
            return True
        else:
            return False
    def move(self, position):
        canvas.delete(self.image)
        self.position = position
        self.x = boardx1 + float(Column.index(self.position[0]) * square_length + .5 * float(square_length))
        self.y = boardy1 + float(Row.index(self.position[1]) * square_length + .5 * float(square_length))
        self.image = canvas.create_image(self.x, self.y, image=self.bishop1)
BishopA=bishop(['c',1],'white','alive')
BishopB=bishop(['f',1],'white','alive')
BishopA1=bishop(['c',8],'black','alive')
BishopB1=bishop(['f',8],'black','alive')
# ^^ These lines of code are for the second subclass. The bishop. We defined how it can move(diagonal going to the
# left,right and backwards), and defined all the bishops starting positions.
class rook(piece):
        def __init__(self, position, color, health):
            super().__init__(position, color, health)
            if color == 'white':
                self.rook1 = tkinter.PhotoImage(file=r"C:\Users\sarah\PycharmProjects\chess\0cbcd810018309.560de1db2832c_(3).png")
            else:
                self.rook1 = tkinter.PhotoImage(file=r"C:\Users\sarah\PycharmProjects\chess\0cbcd810018309.560de1db2832c_(9).png")
            self.x = boardx1 + float(Column.index(self.position[0]) * square_length + .5 * float(square_length))
            self.y = boardy1 + float(Row.index(self.position[1]) * square_length + .5 * float(square_length))
            self.image = canvas.create_image(self.x, self.y, image=self.rook1)
        def check_move(self, column, row):
                self.position
                if self.position[0] == column or self.position[1] == row:
                    return True
                else:
                    return False
        def move(self, position):
            canvas.delete(self.image)
            self.position = position
            self.x = boardx1 + float(Column.index(self.position[0]) * square_length + .5 * float(square_length))
            self.y = boardy1 + float(Row.index(self.position[1]) * square_length + .5 * float(square_length))
            self.image = canvas.create_image(self.x, self.y, image=self.rook1)
RookA=rook(['a',1],'white','alive')
RookB=rook(['h',1],'white','alive')
RookA1=rook(['a',8],'black','alive')
RookB1=rook(['h',8],'black','alive')
# These Lines of code are for the third subclass. The Rook. We defined its moveset(moving Foward,left,right,back)
class knight(piece):
    def __init__(self, position, color, health):
        super().__init__(position, color, health)
        if color == 'white':
            self.knight1 = tkinter.PhotoImage(file=r"C:\Users\sarah\PycharmProjects\chess\0cbcd810018309.560de1db2832c_(4).png")
        else:
            self.knight1 = tkinter.PhotoImage(file=r"C:\Users\sarah\PycharmProjects\chess\0cbcd810018309.560de1db2832c_(10).png")
        self.x = boardx1 + float(Column.index(self.position[0]) * square_length + .5 * float(square_length))
        self.y = boardy1 + float(Row.index(self.position[1]) * square_length + .5 * float(square_length))
        self.image = canvas.create_image(self.x, self.y, image=self.knight1)
    def check_move(self, column, row):
        self.position
        if Column.index(column)-Column.index(self.position[0])==2 and Row.index(row)-Row.index(self.position[1])==1:
             return True
        elif Column.index(column)-Column.index(self.position[0])==2 and Row.index(row)-Row.index(self.position[1])==-1:
            return True
        elif Column.index(column)-Column.index(self.position[0])==-2 and Row.index(row)-Row.index(self.position[1])==-1:
            return True
        elif Column.index(column)-Column.index(self.position[0])==-2 and Row.index(row)-Row.index(self.position[1])==1:
            return True
        elif Column.index(column)-Column.index(self.position[0])==1 and Row.index(row)-Row.index(self.position[1])==2:
            return True
        elif Column.index(column)-Column.index(self.position[0])==-1 and Row.index(row)-Row.index(self.position[1])==2:
            return True
        elif Column.index(column)-Column.index(self.position[0])==1 and Row.index(row)-Row.index(self.position[1])==-2:
            return True
        elif Column.index(column)-Column.index(self.position[0])==-1 and Row.index(row)-Row.index(self.position[1])==-2:
            return True
        else:
            return False
    def move (self,position):
        canvas.delete(self.image)
        self.position=position
        self.x = boardx1 + float(Column.index(self.position[0]) * square_length + .5 * float(square_length))
        self.y = boardy1 + float(Row.index(self.position[1]) * square_length + .5 * float(square_length))
        self.image = canvas.create_image(self.x, self.y, image=self.knight1)
KnightA=knight(['b',1],'white','alive')
KnightB=knight(['g',1],'white','alive')
KnightA1=knight(['b',8],'black','alive')
KnightB1=knight(['g',8],'black','alive')
# These Lines of code are for the fourth subclass. The Knight. We defined its moveset(moving in an L shape any direction, no diaganal though )
class queen(piece):
    def __init__(self, position, color, health):
        super().__init__(position, color, health)
        if color == 'white':
            self.queen1 = tkinter.PhotoImage(file=r"C:\Users\sarah\PycharmProjects\chess\0cbcd810018309.560de1db2832c_(6).png")
        else:
            self.queen1 = tkinter.PhotoImage(file=r"C:\Users\sarah\PycharmProjects\chess\0cbcd810018309.560de1db2832c_(12).png")
        self.x = boardx1 + float(Column.index(self.position[0]) * square_length + .5 * float(square_length))
        self.y = boardy1 + float(Row.index(self.position[1]) * square_length + .5 * float(square_length))
        self.image = canvas.create_image(self.x, self.y, image=self.queen1)
    def check_move(self, column, row):
        self.position
        if self.position[0] == column or self.position[1] == row or row-self.position[1] == Column.index(column) - Column.index(self.position[0]) or self.position[1] - row == Column.index(column) - Column.index(self.position[0]):
            return True
        else:
            return False
    def move(self, position):
        canvas.delete(self.image)
        self.position = position
        self.x = boardx1 + float(Column.index(self.position[0]) * square_length + .5 * float(square_length))
        self.y = boardy1 + float(Row.index(self.position[1]) * square_length + .5 * float(square_length))
        self.image = canvas.create_image(self.x, self.y, image=self.queen1)
# These Lines of code are for the fifth subclass. The Queen. We defined its moveset(can move everywere any spaces)
QueenA=queen(['e',1],'white','alive')
QueenB=queen(['e',8],'black','alive')
class king(piece):
    def __init__(self, position, color, health):
        super().__init__(position, color, health)
        if color == 'white':
            self.king1 = tkinter.PhotoImage(file=r"C:\Users\sarah\PycharmProjects\chess\0cbcd810018309.560de1db2832c_(7).png")
        else:
            self.king1 = tkinter.PhotoImage(file=r"C:\Users\sarah\PycharmProjects\chess\0cbcd810018309.560de1db2832c_(13).png")
        self.x = boardx1 + float(Column.index(self.position[0]) * square_length + .5 * float(square_length))
        self.y = boardy1 + float(Row.index(self.position[1]) * square_length + .5 * float(square_length))
        self.image = canvas.create_image(self.x, self.y, image=self.king1)
    def check_move(self, column, row):
        self.position
        if -1<= Column.index(column)-Column.index(self.position[0]) and -1<= Row.index(row)-Row.index(self.position[1]) and 1 >=Column.index(column)-Column.index(self.position[0]) and 1>= Row.index(row)-Row.index(self.position[1]):
            return True
        else:
            return False
    def move (self,position):
        canvas.delete(self.image)
        self.position=position
        self.x = boardx1 + float(Column.index(self.position[0]) * square_length + .5 * float(square_length))
        self.y = boardy1 + float(Row.index(self.position[1]) * square_length + .5 * float(square_length))
        self.image = canvas.create_image(self.x, self.y, image=self.king1)
KingA=king(['d',1],'white','alive')
KingB=king(['d',8],'black','alive')
# These Lines of code are for the sixth subclass. The King. We defined its moveset(moving anywere only once )
CurrentRow=0
CurrentColumn=0
CurrentPiece=PawnA
click = 'piece'
print('Please select the piece you would like to move')
print('Once you have selected your piece, select a valid move on the board')
def move(event):
    global click
    global CurrentPiece
    global CurrentColumn
    global CurrentRow
    global Setpiece
    if click=='piece':
        CurrentPiece=0
        for Key,Value in Dict_x.items():
            if event.x>Value[0] and event.x<Value[1]:
                print(Key)
                CurrentColumn=Key
        for Key,Value in Dict_y.items():
            if event.y>Value[0] and event.y<Value[1]:
                print(Key)
                CurrentRow=Key
        for x in PieceList:
            if x.position==[CurrentColumn,CurrentRow]:
                CurrentPiece=x
        if CurrentPiece==0:
            var.set('Hey! Thats not a piece silly! Please select a piece on the board')
        else:
            click='move'
            var.set("click the space where you want to move")
    elif click=='move':
        for Key,Value in Dict_x.items():
            if event.x>Value[0] and event.x<Value[1]:
                print(Key)
                CurrentColumn=Key
        for Key,Value in Dict_y.items():
            if event.y>Value[0] and event.y<Value[1]:
                print(Key)
                CurrentRow=Key
        if CurrentPiece.check_move(CurrentColumn,CurrentRow):
            Setpiece = 0
            for x in PieceList:
                if x.position == [CurrentColumn, CurrentRow]:
                        #Setpiece = x
                    PieceList.remove(x)
                    canvas.delete(x.image)
                    x.health = 'dead'
                #if Setpiece != 0:
                    #print(Setpiece)
                    #PieceList.remove(Setpiece)
                    #canvas.delete(Setpiece.image)
                    #Setpiece.health = 'dead'
            CurrentPiece.move([CurrentColumn,CurrentRow])
            click = 'piece'
            var.set('click a piece to move')
        else:
            var.set('Invalid move. Please try again')
#These are the tested moves we have put in so far. Everything seems to be working great
root.bind('<Button>',move)
label.pack()
canvas.pack()
root.mainloop()
