# GUI-CRUD-Tkinter

![](https://github.com/mtraczu/GUI-CRUD-Tkinter/blob/main/CRUD.png?raw=true)
<br/><br/>
<h2 style="font-size: 32px;">Application Documentation</h2>
This documentation provides an overview and explanation of the code for the CRUD application using Tkinter and MySQL. The application allows the user to perform CRUD operations (Create, Read, Update, Delete) on a database table.
<br/><br/>
<h2 style="font-size: 32px;">Table of Contents</h2>
Introduction<br/><br/>
Dependencies<br/><br/>
Database Configuration<br/><br/>
GUI Components<br/><br/>
Button Functions<br/><br/>
Data Refresh Function<br/><br/>
Main Application Loop<br/><br/>
<h2 style="font-size: 32px;">1. Introductions</h2>
The CRUD application is built using the Tkinter library for the graphical user interface (GUI) and MySQL Connector for the database connection. It provides a simple interface for managing records in a database table.


<h2 style="font-size: 32px;">2. Dependencies</h2>
The application requires the following dependencies:

Python 3.x
Tkinter library
MySQL Connector library
Make sure these dependencies are installed before running the application.

<h2 style="font-size: 32px;">3. Database Configuration</h2>
To connect the application to your MySQL database, you need to provide the following details:
<br/><br/>
<strong>DATABASE:</strong> The name of the database.<br/><br/>
<strong>DATABASE_PASSWORD:</strong> The password for the database user.<br/><br/>
<strong>TABLE:</strong> The name of the table in the database.<br/><br/>
<strong>HOST:</strong> The host address of the database server.<br/><br/>
<strong>USER:</strong> The username for the database user.<br/><br/>
Make sure to replace the placeholder values (<PASSWORD>) with the actual password for the database user.<br/><br/>

<h2 style="font-size: 32px;">4. GUI Components</h2>
The application GUI consists of three main components:<br/><br/>
Table Treeview: Displays the database records in a table format.<br/><br/>
Buttons: Create, Update, Delete, and Refresh buttons for performing CRUD operations.<br/><br/>
Data Entry Fields: Text entry fields for entering record details.<br/><br/>

<h2 style="font-size: 32px;">5. Button Functions</h2>
The application defines the following button functions:<br/><br/>

<strong>create_record():</strong> Inserts a new record into the database table based on the values entered in the data entry fields.<br/><br/>
<strong>update_record():</strong> Updates the selected record in the database table with the values entered in the data entry fields.<br/><br/>
<strong>delete():</strong> Deletes the selected record from the database table.<br/><br/>
<strong>refresh():</strong> Refreshes the table view with the latest data from the database.<br/><br/>

<h2 style="font-size: 32px;">6. Data Refresh Function</h2>
The refresh() function retrieves the latest data from the database and updates the table view. It performs the following steps:

Clears the existing table view.
Executes a SELECT query to fetch all records from the database table.
Formats the retrieved data into a list of tuples.
Updates the column headings and widths.
Inserts the data into the table view.

<h2 style="font-size: 32px;">7. Main Application Loop</h2>
The application window is created and configured in the main loop. It sets the window title, size, and position. The GUI components (table view, buttons, and data entry fields) are placed within separate frames. The main loop also binds the item_selected() function to the treeview widget, which updates the data entry fields when a record is selected.<br/><br/>

To run the application, execute the Python script. The GUI window will appear, and you can interact with the CRUD functionality using the provided buttons and data entry fields.<br/><br/>

Please note that this documentation provides an overview of the code. For more detailed explanations, refer to the code comments and consult the Tkinter and MySQL Connector documentation for further information on specific functions and methods used in the application.
