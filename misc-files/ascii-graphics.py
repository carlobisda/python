#ASCII GENERATOR
import termcolor
import pyfiglet
from termcolor import cprint, colored
from pyfiglet import figlet_format, Figlet

#ASCII PLUS FORMATTING
cprint(figlet_format('ASCII ART', font='slant'),'green', attrs=['bold'])
cprint('best type of art.....', 'green', attrs=['bold'])

#TO RENDER ASCII TEXT EXAMPLE
#f = Figlet(font='slant')
#print(f.renderText('ASCII ART'))

#TO RENDER FONT FORMATTING ONLY EXAMPLE
#cprint('GLITCH', 'green', attrs=['bold'])

