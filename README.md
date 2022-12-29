# pizzaDeliveryApp
A simple backend for fetching pizza delivery details. Made for learning FASTAPI and PostgreSQL.
# How to run the Project
* Install Postgreql. (I used elephantsql which provides free instance of postgres database)
* Install Python
* Git clone the project with  git clone https://github.com/Sumit70421/pizzaDeliveryApp.git
* Create your virtualenv with Pipenv or virtualenv and activate it.
* Install the requirements with pip install -r requirements.txt
* Set Up your PostgreSQL database and set its URI in your database.py
`engine=create_engine('postgresql://postgres:<username>:<password>@localhost/<db_name>',
    echo=True
)`
* Create your database by running python init_db.py
* Finally run the API ``` uvicorn main:app ``
