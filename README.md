# Airbnb Clone Console Project
This project is the first step in building a full-fledged Airbnb clone web application using Python. It lays the foundation with a console application that acts as the initial "front-end" for managing data. The console implements CRUD (Create, Read, Update, Delete) operations for users and properties, utilizing object-oriented programming (OOP) principles for a well-structured codebase. Serialization/deserialization allows seamless data movement between Python objects and JSON for storage and retrieval. Unit tests ensure the code's reliability before progressing to a user-friendly web interface and a more robust database. This project exemplifies the Software Development Life Cycle (SDLC) by establishing a solid foundation for future functionalities.

**Project Goals:**

- Establish a solid foundation for data management and manipulation.
- Implement core functionalities essential for an Airbnb clone, such as user management, property listings, and bookings (to be addressed in future projects).
- Provide a platform for iterative development and testing through a user-friendly console interface.

**Project Structure:**

```
AirBnB-clone/
├── __init__.py           # (Optional) Empty file to mark the directory as a package
├── models/
│   ├── __init__.py       # Optional file for model-related initialization
│   ├── base_model.py     # Base class for all models
│   └── engine/
│       └── file_storage.py  # File-based storage engine
├── console.py            # Console application logic
├── README.md             # Project documentation
├── tests/                # Directory for unit tests
│   └── ...               # Unit test files (e.g., test_base_model.py, test_user.py)
└── AUTHOR                # File containing author information
```

| File Name                                            | Description                                                                                                                                                                                                        |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `__init__.py` (in root directory & models directory) | Optional empty file to mark the directory as a Python package (can be omitted).                                                                                                                                    |
| `models/`<br>(directory)                             | Defines the base class for all models in the project, containing common attributes and methods like initialization, serialization, and deserialization, and all the other classes that inherit from the base class |
| `file_storage.py`                                    | Implements the file-based storage engine, responsible for saving and loading data from JSON files.                                                                                                                 |
| `console.py`                                         | Contains the logic for the interactive console application, handling user input, executing commands, and interacting with models.                                                                                  |
| `README.md`                                          | Project documentation, explaining its purpose, functionalities, usage instructions, and future development plans.                                                                                                  |
| `tests/` (directory)                                 | Contains unit test files for various parts of the code (e.g., `test_base_model.py`)                                                                                                                                |
| `AUTHOR`                                             | Text file containing information about the project's author(s) (name, email, website).                                                                                                                             |

**How to use it:**

1. **Prerequisites:** Ensure you have Python (version 3 recommended) and a code editor or IDE installed on your system.
2. **Clone the Repository:** If you haven't already, clone this project's repository from your version control system.
3. **Run the Console:** Navigate to the project directory and execute `python3 console.py` to launch the interactive console.
	- Type `help` at the prompt to display a list of available commands.
	- Each command has specific arguments that you can use to interact with the data.
	- For detailed information on a particular command, type `help <command_name>`.

**Example Usage:**

```
sai@sai:~/AirBnB_clone$ ./console.py 
(HBNB) create BaseModel
3d867a87-977d-405d-81e9-b09a719702ef
(HBNB) create User
e484c630-5b51-4e61-8ddc-77445aa0754d
(HBNB) all
["[BaseModel] (3d867a87-977d-405d-81e9-b09a719702ef) {'id': '3d867a87-977d-405d-81e9-b09a719702ef', 'created_at': '2024-03-10T21:48:15.475100', 'updated_at': '2024-03-10T21:48:15.475131', '__class__': 'BaseModel'}", "[User] (e484c630-5b51-4e61-8ddc-77445aa0754d) {'id': 'e484c630-5b51-4e61-8ddc-77445aa0754d', 'created_at': '2024-03-10T21:48:19.572443', 'updated_at': '2024-03-10T21:48:19.572465', '__class__': 'User'}"]
(HBNB) show BaseModel 3d867a87-977d-405d-81e9-b09a719702ef
[BaseModel] (3d867a87-977d-405d-81e9-b09a719702ef) {'id': '3d867a87-977d-405d-81e9-b09a719702ef', 'created_at': '2024-03-10T21:48:15.475100', 'updated_at': '2024-03-10T21:48:15.475131', '__class__': 'BaseModel'}
(HBNB) destroy BaseModel 3d867a87-977d-405d-81e9-b09a719702ef
(HBNB) show BaseModel 3d867a87-977d-405d-81e9-b09a719702ef
** no instance found **
(HBNB) all
["[User] (e484c630-5b51-4e61-8ddc-77445aa0754d) {'id': 'e484c630-5b51-4e61-8ddc-77445aa0754d', 'created_at': '2024-03-10T21:48:19.572443', 'updated_at': '2024-03-10T21:48:19.572465', '__class__': 'User'}"]
(hbnb)
(hbnb) quit
```
