# Learning-Log
Learning Log is a web application that allows users to log topics they are interested in and make journal entries as they learn. Users can:

    Register and log in to their accounts
    Create new topics
    Add journal entries under each topic
    View and edit existing entries

Tech Stack

    Backend: Django (Python)
    Frontend: HTML, CSS, JavaScript
    Database: PostgreSQL (or SQLite for development)
    Authentication: Django’s built-in authentication system
Installation and Setup
1. Clone the Repository

git clone https://github.com/shaker-maker/learning-log.git
cd learning-log

2. Create a Virtual Environment (Optional but Recommended)

python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

3. Install Dependencies

pip install -r requirements.txt

4. Apply Migrations

python manage.py migrate

5. Run the Development Server

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.
Usage

    Sign Up / Log In – Create an account or log in.
    Create Topics – Add topics you want to track.
    Add Entries – Write journal entries for each topic.
    View & Edit – Review and edit your past entries.
