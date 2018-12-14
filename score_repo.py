from pathlib import Path

class HighScores():
    def __init__(self):
        self.__highscores__ = []
        p = Path('.')
        self.__highscores_file__ = p.resolve() / 'highscore.txt'
        with open(self.__highscores_file__, 'r') as highscores:
            for highscore in highscores:
                self.__highscores__.append(highscore)
    
    def add_score(self, new_score):
        try:
            self.__highscores__.append(new_score)

            with open(self.__highscores_file__, 'a') as highscores:
                highscores.write(new_score + '\n')
            return 1
        except:
            return 0
    
    def get_scores(self):
        return self.__highscores__