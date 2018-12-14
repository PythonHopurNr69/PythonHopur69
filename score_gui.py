from tkinter import *
from score_repo import HighScores
_highscores = HighScores()

def guiApplicaton(readOrWrite, getPoints):
    
    window = Tk()
    disp_scores = StringVar()
    window.title("HighScores")
    window.configure(background='white')
    Frame(width=500, height=500, background='white').pack()
    disp_scores = StringVar()
    
    if readOrWrite == 1:
            for score in _highscores.get_scores():
                    tmp = disp_scores.get()
                    tmp += '\n' + score
                    disp_scores.set(tmp)
                    the_scores = Label(textvariable=disp_scores, anchor='w', justify='left', wraplength=500, background='white')
                    the_scores.pack()
                    the_scores.place(y=0)
    
    elif readOrWrite == 0:
        entry = Entry()
        str_point = str(getPoints)
        entry.pack(fill=X) 
        
        def commitHighScore(str_point): 
            inputName = entry.get()
            newHighScore = 'name: ' + inputName + ' ' + 'Score: ' + str_point
            if newHighScore and _highscores.add_score(newHighScore):
                tmp = disp_scores.get()
                tmp += newHighScore      #tmp += '\n' + newHighScore
                disp_scores.set(tmp)
            else:
                tkinter.messagebox.showinfo('Error, could not add scores')
        
        Button(text='Submit name', command=commitHighScore(str_point), background='green').pack()
        
     
    window.mainloop()