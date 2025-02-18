import sys
import qdarkstyle
import xml.etree.ElementTree as ET
import xml.dom.minidom
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QFileDialog, QMessageBox
from PySide6.QtCore import QSettings
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_Form as about_ui

class MainWindow(QMainWindow, main_ui): # used to display the main user interface
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # loads main_ui
        self.settings_manager = SettingsManager(self)  # Initializes SettingsManager
        self.settings_manager.load_settings()  # Load settings when the app starts

        # menubar
        self.action_new.triggered.connect(self.new_file)
        self.action_open.triggered.connect(self.open_file)
        self.action_dark_mode.toggled.connect(self.dark_mode)
        self.action_about.triggered.connect(self.show_about)
        self.action_about_qt.triggered.connect(self.about_qt)

        # buttons
        self.button_add.clicked.connect(self.add_book)
        self.button_update.clicked.connect(self.update_book)
        self.button_delete.clicked.connect(self.delete_book)

    def new_file(self):
        self.initialize_table()
        self.filename = QFileDialog.getSaveFileName(self, 'Create a new file', '', 'Data File (*.xml)',)

        if not self.filename[0]:
            return  # Do nothing if no file is selected
        
        self.setWindowTitle(self.filename[0].split('/')[-1])
        try:
            root = ET.Element("library")
            tree = ET.ElementTree(root)
            tree.write(self.filename[0], encoding="utf-8", xml_declaration=True)

        except FileNotFoundError:
            pass

    def open_file(self):
        self.initialize_table()
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Data File (*.xml)')
        self.setWindowTitle(self.filename[0].split('/')[-1])

        try:
            tree = ET.parse(self.filename[0])
            root = tree.getroot()

            self.book_ids = []  # Initialize the list to store existing book IDs
            
            for book in root.findall("book"):
                book_id = book.get("id")  # Extract the book ID from the XML
                title = book.find("title").text
                author = book.find("author").text
                pages = book.find("pages").text
                year = book.find("year").text

                row = self.table.rowCount()

                self.populate_table(row, book_id, title, author, pages, year)

                self.book_ids.append(int(book_id))

            print(f"File '{self.filename[0]}' opened successfully.")
        except ET.ParseError:
            print("Failed to parse the XML file.")
            return
        except FileNotFoundError:
            pass

    def add_book(self):
        try: # try these, if the xml file isn't loaded a message will pop up
            xml_file = self.filename[0]
        
            title = self.line_title.text()
            author = self.line_author.text()
            pages = self.line_pages.text()
            year = self.line_year.text()

            row = self.table.rowCount()

            book_id = str(self.get_next_book_id())

            self.populate_table(row, book_id, title, author, pages, year)

            # Check if the XML file exists, if not, create it
            if os.path.exists(xml_file):
                tree = ET.parse(xml_file)
                root = tree.getroot()

            # Create a new book entry
            book = ET.SubElement(root, "book", id=book_id)
            title_element = ET.SubElement(book, "title")
            title_element.text = title
            author_element = ET.SubElement(book, "author")
            author_element.text = author
            pages_element = ET.SubElement(book, "pages")
            pages_element.text = pages
            year_element = ET.SubElement(book, "year")
            year_element.text = year

            # Write the updated XML to the file (does not prettify at this point)
            tree.write(xml_file, encoding="utf-8", xml_declaration=True)

            # Now, let's format the XML nicely using minidom
            with open(xml_file, "r", encoding="utf-8") as f:
                xml_str = f.read()

            # Use minidom to parse and pretty-print the XML string
            xml_str = xml.dom.minidom.parseString(xml_str).toprettyxml(indent="  ")

            # Clean up any extra blank lines added by minidom
            xml_str = "\n".join([line for line in xml_str.split("\n") if line.strip()])

            # Write the nicely formatted string back into the XML file
            with open(xml_file, "w", encoding="utf-8") as f:
                # Remove the extra line added at the beginning by minidom
                f.write(xml_str)

            # Print confirmation
            print(f"Book '{title}' by {author} added to XML.")

        except AttributeError:
            QMessageBox.warning(self, "NO FILE TO SUBMIT", "Please select a file or create one")

        self.clear_fields()

    def get_next_book_id(self):
        # This function retrieves the next available book ID from the existing XML data
        xml_file = self.filename[0]
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            # Get all book IDs
            book_ids = [int(book.get("id")) for book in root.findall("book")]
            next_id = max(book_ids) + 1 if book_ids else 1
            return next_id
        except (FileNotFoundError, IndexError):
            # If no books exist or the file is empty, return the first ID (1)
            return 1

    def update_book(self):
        try:
            xml_file = self.filename[0]

            # Open and parse the existing XML file
            tree = ET.parse(xml_file)
            root = tree.getroot()

            # Iterate through all rows in the table to capture the updated data
            for row in range(self.table.rowCount()):
                book_id = self.table.item(row, 0).text()  # Get the book ID from the table
                title = self.table.item(row, 1).text()  # Get the updated title
                author = self.table.item(row, 2).text()  # Get the updated author
                pages = self.table.item(row, 3).text()  # Get the updated pages
                year = self.table.item(row, 4).text()  # Get the updated year

                # Find the corresponding book in the XML by ID
                for book in root.findall("book"):
                    if book.get("id") == book_id:
                        book.find("title").text = title
                        book.find("author").text = author
                        book.find("pages").text = pages
                        book.find("year").text = year
                        break  # Once we've found the book, no need to check further

            # Write the updated XML back to the file
            tree.write(xml_file, encoding="utf-8", xml_declaration=True)

            # Format the XML for better readability
            with open(xml_file, "r", encoding="utf-8") as f:
                xml_str = f.read()
            xml_str = xml.dom.minidom.parseString(xml_str).toprettyxml(indent="  ")
            xml_str = "\n".join([line for line in xml_str.split("\n") if line.strip()])

            with open(xml_file, "w", encoding="utf-8") as f:
                f.write(xml_str)

            print(f"XML file '{xml_file}' updated successfully.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to update book information: {str(e)}")

    def delete_book(self):
        try:
            # Get the currently selected row index
            selected_row = self.table.currentRow()

            if selected_row == -1:
                QMessageBox.warning(self, "No Selection", "Please select a row to delete.")
                return

            # Get the book ID from the selected row (column 0)
            book_id = self.table.item(selected_row, 0).text()

            # Ask for confirmation before deleting
            confirm = QMessageBox.question(self, "Confirm Deletion",
                                        f"Are you sure you want to delete the book with ID {book_id}?",
                                        QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.No:
                return

            # Remove the selected row from the table
            self.table.removeRow(selected_row)

            # Now, update the XML to delete the corresponding book entry
            xml_file = self.filename[0]
            tree = ET.parse(xml_file)
            root = tree.getroot()

            # Find and remove the book element with the matching ID
            for book in root.findall("book"):
                if book.get("id") == book_id:
                    root.remove(book)
                    break  # Exit once the matching book is found and removed

            # Save the updated XML file
            tree.write(xml_file, encoding="utf-8", xml_declaration=True)

            # Format the XML for readability
            with open(xml_file, "r", encoding="utf-8") as f:
                xml_str = f.read()
            xml_str = xml.dom.minidom.parseString(xml_str).toprettyxml(indent="  ")
            xml_str = "\n".join([line for line in xml_str.split("\n") if line.strip()])

            with open(xml_file, "w", encoding="utf-8") as f:
                f.write(xml_str)

            print(f"Book with ID {book_id} has been deleted.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to delete book: {str(e)}")

    def initialize_table(self):
        self.table.setRowCount(0) # clears the table
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['ID', 'Title', 'Author', 'Pages', 'Year'])

    def populate_table(self, row, book_id, title, author, pages, year):
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(str(book_id)))
        self.table.setItem(row, 1, QTableWidgetItem(title))
        self.table.setItem(row, 2, QTableWidgetItem(author))
        self.table.setItem(row, 3, QTableWidgetItem(pages))
        self.table.setItem(row, 4, QTableWidgetItem(year))
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def clear_fields(self):
        self.line_title.clear()
        self.line_author.clear()
        self.line_pages.clear()
        self.line_year.clear()

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

    def show_about(self):  # loads the About window
        self.about_window = AboutWindow(dark_mode=self.action_dark_mode.isChecked())
        self.about_window.show()

    def about_qt(self):  # loads the About Qt window
        QApplication.aboutQt()

    def closeEvent(self, event):  # Save settings when closing the app
        self.settings_manager.save_settings()  # Save settings using the manager
        event.accept()

class SettingsManager: # used to load and save settings when opening and closing the app
    def __init__(self, main_window):
        self.main_window = main_window
        self.settings = QSettings('settings.ini', QSettings.IniFormat)

    def load_settings(self):
        size = self.settings.value('window_size', None)
        pos = self.settings.value('window_pos', None)
        dark = self.settings.value('dark_mode')
        
        if size is not None:
            self.main_window.resize(size)
        if pos is not None:
            self.main_window.move(pos)
        if dark == 'true':
            self.main_window.action_dark_mode.setChecked(True)
            self.main_window.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    def save_settings(self):
        self.settings.setValue('window_size', self.main_window.size())
        self.settings.setValue('window_pos', self.main_window.pos())
        self.settings.setValue('dark_mode', self.main_window.action_dark_mode.isChecked())

class AboutWindow(QWidget, about_ui): # Configures the About window
    def __init__(self, dark_mode=False):
        super().__init__()
        self.setupUi(self)

        if dark_mode:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

if __name__ == "__main__":
    app = QApplication(sys.argv)  # needs to run first
    main_window = MainWindow()  # Instance of MainWindow
    main_window.show()
    sys.exit(app.exec())
