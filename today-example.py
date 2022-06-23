class Student():
    def __init__(self, name, favorite_color=None):
        # When this method is called, Python builds an instance of the class
        self.name = name # an attribute that can hold different values for different instances
        self.favorite_color = favorite_color
        self.languages = []

    def __str__(self):
        return f"<Student name = {self.name}, and their favorite color is {self.favorite_color}>"
    
    def show_languages(self):
        return f"{self.name} knows these languages: {self.languages}"
    
    def get_languages(self):
        language = None
        while language != "Done":
            language = input("What's a language you know? (Input Done when done)")
            self.languages.append(language)



connor = Student("Connor")
#the above line is calling the __init__() method and saving what that returns in the variable "connor"
connor.favorite_color = "purple"
connor.name = "Ace"
connor.get_languages()
print(connor.show_languages())

rachel = Student("Rachel")
rachel.favorite_color = "blue"
rachel.get_languages()
print(rachel.show_languages())
