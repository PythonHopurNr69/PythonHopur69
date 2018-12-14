from tkinter import *
from tkinter import messagebox
from score_repo import HighScores
_highscores = HighScores()
str_points = ''

#Main function to call the tkinter gui window, accepts 1 or 0 to see if it's suppose to read from HighScore or add
def guiApplicaton(readOrWrite, getPoints):
    
    window = Tk()
    disp_scores = StringVar()
    window.title("HighScores")
    window.configure(background='white')
    Frame(width=500, height=500, background='white').pack()
    disp_scores = StringVar()

    #If it's 1 go ahead and read the highscore
    if readOrWrite == 1:
            for score in _highscores.get_scores():
                    tmp = disp_scores.get()
                    tmp += '\n' + score
                    disp_scores.set(tmp)
                    the_scores = Label(textvariable=disp_scores, anchor='w', justify='left', wraplength=500, background='white')
                    the_scores.pack()
                    the_scores.place(y=0)
            Button(text='Close', command=window.destroy, background='red').pack()       
    #If it's 0 go ahead and add to the highscore
    elif readOrWrite == 0:
        global str_points
        entry = Entry()
        str_point = str(getPoints)
        entry.pack(fill=X) 
        
        def commitHighScore(): 
            inputName = entry.get()
            newHighScore = 'name: ' + inputName + ' ' + 'Score: ' + str_point
            if newHighScore and _highscores.add_score(newHighScore):
                tmp = disp_scores.get()
                tmp += newHighScore    
                disp_scores.set(tmp)
                messagebox.showinfo("Updated", "Your score has been submitted")
                return quit()
            else:
                messagebox.showerror('Error, could not add scores')
        
        Button(text='Submit name', command=commitHighScore, background='red').pack()
        #Close the GUI window
        def quit():
           window.destroy()
	
    window.mainloop()
   