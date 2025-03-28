import sys
import qdarkstyle
import xml.etree.ElementTree as ET
import xml.dom.minidom
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QFileDialog, QMessageBox
from PySide6.QtCore import QSettings
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_Dialog as about_ui
import uuid

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
        self.action_about_qt.triggered.connect(lambda: QApplication.aboutQt())
        self.action_about.triggered.connect(lambda: AboutWindow(dark_mode=self.action_dark_mode.isChecked()).exec())

        # buttons
        self.button_add.clicked.connect(self.add_employee)
        self.button_update.clicked.connect(self.update_employee)
        self.button_delete.clicked.connect(self.delete_employee)

    def new_file(self): # Create a new XML file for storing employee data
        self.clear_fields()
        self.filename = QFileDialog.getSaveFileName(self, 'Create a new file', '', 'Data File (*.xml)',)

        if not self.filename[0]:
            return  # Do nothing if no file is selected
        
        self.initialize_table()
        
        self.setWindowTitle(self.filename[0].split('/')[-1])
        try:
            root = ET.Element("employees")
            tree = ET.ElementTree(root)
            tree.write(self.filename[0], encoding="utf-8", xml_declaration=True)

        except FileNotFoundError:
            pass

    def open_file(self): # Open an existing XML file for updating, deleting and appending
        self.clear_fields()
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', '', 'Data File (*.xml)')

        if not self.filename[0]:
            return  # Do nothing if no file is selected
        
        self.initialize_table()

        self.setWindowTitle(self.filename[0].split('/')[-1])

        try:
            tree = ET.parse(self.filename[0])
            root = tree.getroot()

            self.employees = []  # Initialize the list to store existing employees
            
            for employee in root.findall("employee"):
                id = employee.get("id")  # Extract the employee ID from the XML
                name = employee.find("name")
                if name is not None:
                    firstname = name.find("firstname").text if name.find("firstname") is not None else ""
                    middlename = name.find("middlename").text if name.find("middlename") is not None else ""
                    lastname = name.find("lastname").text if name.find("lastname") is not None else ""
                age = employee.find("age").text
                title = employee.find("title").text
                department = employee.find("department").text
                address = employee.find("address")
                if address is not None:
                    address1 = address.find("address1").text if address.find("address1") is not None else ""
                    address2 = address.find("address2").text if address.find("address2") is not None else ""
                    country = address.find("country").text if address.find("country") is not None else ""
                misc = employee.find("misc").text

                row = self.table.rowCount()

                self.populate_table(row, id, firstname, middlename, lastname, age, title, department, address1, address2, country, misc)

            print(f"File '{self.filename[0]}' opened successfully.")
        except ET.ParseError:
            print("Failed to parse the XML file.")
            return
        except FileNotFoundError:
            pass

    def add_employee(self):
        try: # try these, if the xml file isn't loaded a message will pop up
            xml_file = self.filename[0]
            
            id = str(uuid.uuid4()) # Generate a unique ID
            firstname = self.line_firstname.text()
            middlename = self.line_middlename.text()
            lastname = self.line_lastname.text()
            age = self.line_age.text()
            title = self.line_title.text()
            department = self.line_department.text()
            address1 = self.line_address1.text()
            address2 = self.line_address2.text()
            country = self.line_country.text()
            misc = self.line_misc.text()

            row = self.table.rowCount()

            self.populate_table(row, id, firstname, middlename, lastname, age, title, department, address1, address2, country, misc)

            tree = ET.parse(xml_file)
            root = tree.getroot()

            # Create a new book entry
            employee = ET.SubElement(root, "employee", id=id)

            name = ET.SubElement(employee, "name")
            firstname_element = ET.SubElement(name, "firstname")
            firstname_element.text = firstname
            middlename_element = ET.SubElement(name, "middlename")
            middlename_element.text = middlename
            lastname_element = ET.SubElement(name, "lastname")
            lastname_element.text = lastname
            
            age_element = ET.SubElement(employee, "age")
            age_element.text = age
            
            title_element = ET.SubElement(employee, "title")
            title_element.text = title
            
            department_element = ET.SubElement(employee, "department")
            department_element.text = department
            
            address = ET.SubElement(employee, "address")
            address1_element = ET.SubElement(address, "address1")
            address1_element.text = address1
            address2_element = ET.SubElement(address, "address2")
            address2_element.text = address2
            country_element = ET.SubElement(address, "country")
            country_element.text = country

            misc_element = ET.SubElement(employee, "misc")
            misc_element.text = misc

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

        except AttributeError:
            QMessageBox.warning(self, "NO FILE TO SUBMIT", "Please select a file or create one")

        self.clear_fields()

    def update_employee(self):
        try:
            xml_file = self.filename[0]

            # Open and parse the existing XML file
            tree = ET.parse(xml_file)
            root = tree.getroot()

            # Iterate through all rows in the table to capture the updated data
            for row in range(self.table.rowCount()):
                id = self.table.item(row, 0).text()  # Get the employee ID from the table
                firstname = self.table.item(row, 1).text()
                middlename = self.table.item(row, 2).text()
                lastname = self.table.item(row, 3).text()
                age = self.table.item(row, 4).text()
                title = self.table.item(row, 5).text()
                department = self.table.item(row, 6).text()
                address1 = self.table.item(row, 7).text()
                address2 = self.table.item(row, 8).text()
                country = self.table.item(row, 9).text()
                misc = self.table.item(row, 10).text()

                # Find the corresponding employee in the XML by ID
                for employee in root.findall("employee"):
                    if employee.get("id") == id:

                        name = employee.find("name")
                        if name is not None:
                            name.find("firstname").text = firstname
                            name.find("middlename").text = middlename
                            name.find("lastname").text = lastname
                        employee.find("age").text = age
                        employee.find("title").text = title
                        employee.find("department").text = department
                        address = employee.find("address")
                        if address is not None:
                            address.find("address1").text = address1
                            address.find("address2").text = address2
                            address.find("country").text = country
                        employee.find("misc").text = misc
                        break  # no need to check further

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

        self.table.resizeColumnsToContents()

    def delete_employee(self):
        try:
            # Get the currently selected row index
            selected_row = self.table.currentRow()

            if selected_row == -1:
                QMessageBox.warning(self, "No Selection", "Please select a row to delete.")
                return

            # Get the employee ID from the selected row (column 0)
            id = self.table.item(selected_row, 0).text()

            # Ask for confirmation before deleting
            confirm = QMessageBox.question(self, "Confirm Deletion",
                                        f"Are you sure you want to delete the book with ID {id}?",
                                        QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.No:
                return

            # Remove the selected row from the table
            self.table.removeRow(selected_row)

            # Now, update the XML to delete the corresponding book entry
            xml_file = self.filename[0]
            tree = ET.parse(xml_file)
            root = tree.getroot()

            # Find and remove the employee element with the matching ID
            for employee in root.findall("employee"):
                if employee.get("id") == id:
                    root.remove(employee)
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

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to delete book: {str(e)}")

    def initialize_table(self):
        self.table.setRowCount(0) # clears the table
        self.table.setColumnCount(11)
        self.table.setHorizontalHeaderLabels(['ID', 'First Name', 'Middle Name', 'Last Name', 'Age', 'Title', 'Department', 'Address 1', 'Address 2', 'Country', 'Misc'])

    def populate_table(self, row, id, firstname, middlename, lastname, age, title, department, address1, address2, country, misc):
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(str(id)))
        self.table.setItem(row, 1, QTableWidgetItem(firstname))
        self.table.setItem(row, 2, QTableWidgetItem(middlename))
        self.table.setItem(row, 3, QTableWidgetItem(lastname))
        self.table.setItem(row, 4, QTableWidgetItem(age))
        self.table.setItem(row, 5, QTableWidgetItem(title))
        self.table.setItem(row, 6, QTableWidgetItem(department))
        self.table.setItem(row, 7, QTableWidgetItem(address1))
        self.table.setItem(row, 8, QTableWidgetItem(address2))
        self.table.setItem(row, 9, QTableWidgetItem(country))
        self.table.setItem(row, 10, QTableWidgetItem(misc))
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def clear_fields(self):
        self.line_firstname.clear()
        self.line_middlename.clear()
        self.line_lastname.clear()
        self.line_age.clear()
        self.line_title.clear()
        self.line_department.clear()
        self.line_address1.clear()
        self.line_address2.clear()
        self.line_country.clear()
        self.line_misc.clear()

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

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

class AboutWindow(QDialog, about_ui): # this is the About Window
    def __init__(self, dark_mode=False):
        super().__init__()
        self.setupUi(self)
        if dark_mode:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        self.button_ok.clicked.connect(self.accept)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # needs to run first
    main_window = MainWindow()  # Instance of MainWindow
    main_window.show()
    sys.exit(app.exec())