# This module creates the base Movie class

# Create a Class and methods
#Put classes in a separate file and the actual operation like creating 
#objects in separate file

class Movie():
    def __init__(self, m_title, m_desc, m_logo, m_trailer):
        self.title = m_title
        self.desc = m_desc
        self.logo_url = m_logo
        self.trailer_url = m_trailer

    def show_trailer(self):
    	webbrowser.open(self.movie_trailer_url)