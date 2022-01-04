from tkinter import *

def callback(r,c):
	global player
	if stats[r][c]==0:
		if player=='X' and stop_game== False:
			B[r][c].configure(text='X')
			player='O'
			stats[r][c]= 'X'
		elif player=='O' and stop_game== False:
			B[r][c].configure(text='O')
			player='X'
			stats[r][c]= 'O'
	else:
		# need fixing, marche po actuellement. ça marche sur debug mais le rouge ne s'affiche pas en temps normal
		B[r][c].configure(bg='red')
		root.after(400)
		B[r][c].configure(bg='gold')
	check_for_victory()

def check_for_victory():
	global stop_game
	for i in range(3):
		if stats[i][0]==stats[i][1]==stats[i][2]!=0:
			B[i][0].configure(bg='red')
			B[i][1].configure(bg='red')
			B[i][2].configure(bg='red')
			stop_game = True
	for i in range(3):
		if stats[0][i]==stats[1][i]==stats[2][i]!=0:
			B[0][i].configure(bg='red')
			B[1][i].configure(bg='red')
			B[2][i].configure(bg='red')
			stop_game = True
		if stats[0][0]==stats[1][1]==stats[2][2]!=0:
			B[0][0].configure(bg='red')
			B[1][1].configure(bg='red')
			B[2][2].configure(bg='red')
			stop_game = True
		if stats[2][0]==stats[1][1]==stats[0][2]!=0:
			B[2][0].configure(bg='red')
			B[1][1].configure(bg='red')
			B[0][2].configure(bg='red')
			stop_game = True

root = Tk()

stats= [[0,0,0],
   		[0,0,0],
   		[0,0,0]]
B=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(3):
	for j in range(3):
		B[i][j]= Button(font=('Verdana', 58),width='3', bg='gold', command= lambda r=i,c=j: callback(r,c))
		B[i][j].grid(row=i,column=j)
player='X'
stop_game= False
		
mainloop()