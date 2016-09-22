# This module creates the base Movie class which would be used to create the objects

class Movie():
    def __init__(self, m_title, m_desc, m_logo, m_trailer): #  Initializing the constructor here with 4 attributes
        self.title = m_title
        self.desc = m_desc
        self.logo_url = m_logo
        self.trailer_url = m_trailer

    def show_trailer(self):
    	webbrowser.open(self.movie_trailer_url) #  Defining the show trailer function
