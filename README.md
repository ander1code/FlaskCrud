# FlaskCrud 🐍💻

**FlaskCrud** is a system for registering individuals developed in **Python** 🐍, using the microframework **Flask** 🔥, the ORM **SQLAlchemy** 🗄️, and the **SQLite** database 💾.  
The project was structured to demonstrate good organizational practices, such as the use of the *Application Factory* 🏗️ pattern, Blueprints 🧩, DTOs 📑, and forms with robust validations ✅.  

Below, you’ll find a description of the main parts of the system, organized by the folders that make up its architecture 📂✨.

---

## configs ⚙️🛠️

This folder contains the files responsible for configuring and initializing the application 🚀.  
`main.py` uses the *application factory* 🏗️ pattern through the `create_app` function, configuring the Flask application via the `Config` class. This is where the database is initialized with `db.init_app` 🗄️, blueprints are registered (including `app`, `login`, `legal_person`, and `natural_person`) 🧩, and tables are created within the application context using `db.create_all()`. Additionally, the server runs in debug mode 🐞 on port 80 🌐, with manual definition of template 🎨 and static 📁 folders.  

`config.py` centralizes the application’s settings 🗂️. It defines `BASE_DIR` using functions from the `os` module, creates the `Config` class, and sets parameters such as `SECRET_KEY` 🔑, the use of SQLite via `SQLALCHEMY_DATABASE_URI` 💾, and disabling `SQLALCHEMY_TRACK_MODIFICATIONS`.  

`database.py` is responsible for importing `SQLAlchemy` 📦 and instantiating the `db` object, which is used throughout the application to manipulate the database 🗄️.

---

## dtos 📑🔄

DTOs (Data Transfer Objects) are used to transport data between application layers 🚚.  
The file `natural_person_dto.py` defines the `NaturalPersonDTO` class, which initializes its attributes from form data 📝, such as name, email 📧, status, description, CPF 🆔, gender ⚧️, salary 💰, birthday 🎂, and photo 📷. It also includes the `get_salary_decimal` method, which converts the salary into a `Decimal` type, cleaning 🧹 and normalizing the string before conversion. The code handles empty values 🚫 or invalid formats ❌, ensuring greater data consistency.

---

## factories 🏭⚡

Factories are responsible for creating object instances from DTOs 🧩.  
In `natural_person_factory.py`, the Singleton 🔄 pattern is implemented to ensure only one instance is used. This class uses `secure_filename` 📂 to handle file names and works directly with the `Person` 👤 and `NaturalPerson` 👥 models. The `create_person` method instantiates a `Person` object with the received attributes, while `create_natural_person` handles the creation of an individual, including image processing 🖼️, upload directory creation 📁, saving files in `app/static/pictures`, CPF normalization 🆔, and instantiation of `NaturalPerson`.

---

## forms 📝📋

Forms are built with **WTForms** 🧾 and ensure input data validation ✅.  
`login_form.py` defines the `LoginForm` class, with user 👤 and password 🔒 fields, both configured with `render_kw` for visual customization 🎨 and validated by the `Validators` class.  

`natural_person_form.py` is more complex, with fields such as name, email 📧, status, description, CPF 🆔, gender ⚧️, salary 💰, birthday 🎂, and photo 📷. It uses an internal tuple for gender options and organizes validations specifically for each field.  

`natural_person_search_form.py` is simple, with only one search field 🔍 configured for querying individuals.  

`person_form.py` defines the `PersonForm` class, which has basic fields such as name 👤, email 📧, status ✅, and description 📝. All are configured with `render_kw` and validated by the `Validators` class, including specific methods for validating each attribute.

---

## models 🗄️📊

Models represent database tables 🏛️ and are defined with **SQLAlchemy** 📦.  
`natural_person.py` describes the `naturalpersons` table, with columns such as CPF 🆔, gender ⚧️, salary 💰, birthday 🎂, and photo 📷, along with the relationship to the `persons` table. It applies validations with `@validates` ✅ and defines constraints such as `UniqueConstraint` for CPF and `CheckConstraint` for gender and salary range.  

`person.py` defines the `persons` table, with columns for name 👤, email 📧, status ✅, description 📝, and creation 📅 and update 🔄 dates. It also applies validations and constraints, such as uniqueness for email and consistency between `created_at` and `updated_at`.  

Finally, `user.py` defines the `users` table, with username 👤 and password 🔒 fields, applying uniqueness to the username and specific validations for both.

---

## routes 🌐🛣️

Routes organize the application’s navigation logic 🧭.  
`app_routes.py` creates the main blueprint 🧩, with routes for the home page 🏠, person selection 👥, and modal cleanup 🧹.  

`legal_person_routes.py` defines routes for legal entities 🏢, displaying informational messages via modal 💬 and redirecting to person selection.  

`login_routes.py` handles authentication 🔐, with routes for login and logout. It uses `LoginForm` and `LoginService`, validates credentials, displays feedback messages with `flash` ⚡, and protects routes with the `login_required` decorator.  

`natural_person_routes.py` manages CRUD 🛠️ operations for individuals 👤. It allows listing 📋 and searching 🔍 records with pagination 📑, creating new people from DTOs 🧩, viewing details with salary 💰 and birthday 🎂 formatting, editing ✏️ or deleting 🗑️ records, always handling errors with `abort(404)` 🚫 and displaying success 🎉 or failure ❌ messages.

---

## services 🔧⚙️

Services encapsulate the application’s business logic 🧠.  
`login_service.py` implements authentication 🔐 and route protection 🛡️. It imports `wraps` from the `functools` module, as well as Flask functions like `flash` ⚡, `redirect` ↩️, `session` 📦, and `url_for` 🔗. It also uses `and_` from SQLAlchemy, the `User` 👤 model, the `Format` 🎨 class, and the `db` 🗄️ object. The `LoginService` class follows the Singleton 🔄 pattern and provides methods such as `login`, which authenticates users with SHA-512 hash 🔑 and sets `session['logged']`, and `logout`, which removes the session key. The `login_required` decorator protects routes, checking for an active session and redirecting otherwise.  

`natural_person_service.py` is responsible for handling individuals 👥. It manages transactions with `db.session.add`, `commit`, `flush`, and `rollback` 🔄, handling exceptions with simple logs 📝 and ensuring data consistency. During edits ✏️, it processes image uploads 📷 with `secure_filename` and applies fallback to old values when new ones are not provided.

---

## utils 🛠️✨

Utilities provide support for formatting 🎨, validations ✅, and modal messages 💬.  
`formats.py` defines the `Format` class, also as a Singleton 🔄. It includes methods to format salaries 💰 in Brazilian currency style 🇧🇷, convert birthdays 🎂 to strings, transform decimal values into monetary strings 💵 and vice versa, and generate SHA-512 hashes 🔑.  

`modal.py` implements the `Modal` class, with simple methods to display 💡 and clear 🧹 modal messages directly in the Flask session.  

`validators.py` centralizes all form validations ✅. It provides methods to validate name 👤, email 📧, description 📝, CPF 🆔, salary 💰, birthday 🎂, gender ⚧️, image 📷, username 👤, and password 🔒.  
Validations include presence checks 🔍, length 📏, format 🧩, database uniqueness 🗄️, and data consistency 🔄. Regular expressions are used to validate email 📧 and username 👤, while exceptions are handled in date 📅 and decimal number 🔢 parsing.  
The code also ensures monetary values are correctly converted 💵, CPFs are unique and consistent 🆔, and birthdays respect the minimum age of 18 🎂➡️🔞. This way, the system maintains integrity and security in all data inputs 🛡️.

---

## Technologies Used 🚀💡

The project was built with:
- **Python 3** 🐍  
- **Flask** 🔥  
- **Flask-SQLAlchemy** 🗄️  
- **SQLite** 💾  
- **WTForms** 🧾  

Together, these tools form a solid foundation 🧱 for modern 🌐, secure 🔐, and scalable 📈 web applications.

---

## Purpose 📌✨

**FlaskCrud** was developed as a complete example of CRUD 🛠️ for individuals 👤, with authentication 🔐, robust validations ✅, and modular organization 📂.  
It serves as a foundation for larger systems 🏗️, demonstrating how to structure a Flask application in a clear 🌟, secure 🛡️, and extensible 🔄 way.

---

## Installation and Execution 🖥️⚡

To run the project locally, follow the steps below:

```bash
# Clone the repository
git clone https://github.com/your-username/FlaskCrud.git

# Access the project folder
cd FlaskCrud

# Create and activate a virtual environment (optional, but recommended)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install the dependencies
pip install -r requirements.txt

# Run the application
flask run
