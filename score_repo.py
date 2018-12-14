from pathlib import Path
#Repo for writing the HighScores into a text file, HighScores is a class
class HighScores():
    #Initalize
    def __init__(self):
        self.__highscores__ = []
        p = Path('.')
        self.__highscores_file__ = p.resolve() / 'highscore.txt'
        with open(self.__highscores_file__, 'r') as highscores:
            for highscore in highscores:
                self.__highscores__.append(highscore)
    
    #Add this instance of HighScore as a new_score, write it into the text file
    def add_score(self, new_score):
        try:
            self.__highscores__.append(new_score)

            with open(self.__highscores_file__, 'a') as highscores:
                highscores.write(new_score + '\n')
            return 1
        except:
            return 0
    #Read all the scores from file
    def get_scores(self):
        return self.__highscores__