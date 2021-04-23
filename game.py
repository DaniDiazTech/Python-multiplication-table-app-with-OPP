import random
class BaseGame:
    
    def __init__(self, points_to_win, n_lives=3):
        """Base game class

        Args:
            points_to_win (int): the points the game will need to be finished 
            n_lives (int): The number of lives the student have. Defaults to 3.
        """
        self.points_to_win = points_to_win

        self.points = 0
        
        self.lives = n_lives

        # Lenght which the message is centered
        self.message_lenght = 60
        
    def print_welcome_message(self):
        print("PYTHON MULTIPLICATION GAME".center(self.message_lenght))

    def print_lose_message(self):
        print("SORRY YOU LOSE ALL OF YOUR LIVES".center(self.message_lenght))

    def print_current_lives(self):
        print(f"Currently you have {self.lives} lives")

    def print_current_score(self):
        print(f"Your score is {self.points}")

        

class RandomMultiplication(BaseGame):

    def __init__(self, *args, **kwargs):
        
    
        