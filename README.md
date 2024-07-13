# LMS Platform

This Django web application allows learners to combine multiple functions in one platform 

## Features

* **Task Management:** CRUD operations with tasks 
* **Note Management:** CRUD operations with notes
* **Dictionary:** Get the description of english words
* **Wikipedia** Get Wikipedia Pages
* **You Tube** Get videos from you tube api
* **Books** Get books from google api
* **Responsive Design:** Built with Bootstrap for a user-friendly experience.
* **API Integration:** Utilizes you tube, google-api and dictionary api.

## Technologies

* Django: Web framework
* Bootstrap: CSS framework
* OpenWeatherMap API: Weather data provider
* Python: Programming language
* JS: Programming language
  

## Installation

**Prerequisites:**

* Git
* Python 3 and pip

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd LMS

2. **Install Dependencies:**
   ```bash
   pipenv install
   pipenv shell  # Activate virtual environment (optional)

3. **Set Up Environment Variables**
   Create a file named .env in the root directory. Add the following lines, replacing placeholders:
   ```bash
    DJANGO_SECRET_KEY==your_secret_key
    DEBUG = set_debug_mode
    API_KEY_BOOKS=your_api_key
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_databse_password
    DB_HOST=your_host
    DB_PORT = port_number

4. **Run Migrations**
    ```bash
   python manage.py migrate
     

5. **  Run the development server**
   ```bash
   python manage.py runserver

6. **Usage**
   Visit http://localhost:8000/ in your browser.
   To fully use the platform,
   first register and start using the app fully!
   
   #Note: This is a basic setup guide. Additional configuration and development steps might be required.

**For demo usage:**
```bash
    https://lms-cpnw.onrender.com/
