

from gi.repository import Gtk as gtk
import gi

gi.require_version('Gtk', '3.0')


class Main:
    def __init__(self):
        gladeFile = "mainWindow.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(gladeFile)
        self.builder.connect_signals(self)

        #button = self.builder.get_object("button")
        #button.connect("clicked", self.printText)

        window = self.builder.get_object("MainWindow")
        window .connect("delete-event", gtk.main_quit)
        window.show()

    def printText(self, widget):
        entradaInput = self.builder.get_object("entrada")
        texto       =entradaInput.get_text().strip()
        
        #print("Hola Mundo")
        print(texto)


if __name__ == "__main__":
    main = Main()
    gtk.main()
