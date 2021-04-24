class BaseGame:

    # Lenght which the message is centered
    message_lenght = 60
    
    description = ""    
        
    def __init__(self, points_to_win, n_lives=3):
        """Base game class

        Args:
            points_to_win (int): the points the game will need to be finished 
            n_lives (int): The number of lives the student have. Defaults to 3.
        """
        self.points_to_win = points_to_win

        self.points = 0
        
        self.lives = n_lives

    def get_numeric_input(self, message=""):

        while True:
            # Get the user input
            user_input = input(message) 
            
            # If the input is numeric, return it
            # If it isn't, print a message and repeat
            if user_input.isnumeric():
                return int(user_input)
            else:
                print("The input must be a number")
                continue     
             
    def print_welcome_message(self):
        print("PYTHON MULTIPLICATION GAME".center(self.message_lenght))

    def print_lose_message(self):
        print("SORRY YOU LOST ALL OF YOUR LIVES".center(self.message_lenght))

    def print_win_message(self):
        print(f"CONGRATULATION YOU REACHED {self.points}".center(self.message_lenght))
        
    def print_current_lives(self):
        print(f"Currently you have {self.lives} lives\n")

    def print_current_score(self):
        print(f"\nYour score is {self.points}")

    def print_description(self):
        print("\n\n" + self.description.center(self.message_lenght) + "\n")

    # Basic run method
    def run(self):
        self.print_welcome_message()
        
        self.print_description()

game = BaseGame(5)

# Accessing game message lenght class attr from class
print(game.message_lenght) # 60

# Accessing the message_lenght class attr from class
print(BaseGame.message_lenght)  # 60

# Accessing the points instance attr from instance
print(game.points) # 0

# Accesing the points instance attribute from class
print(BaseGame.points) # Attribute error
