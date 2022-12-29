# pizzaDeliveryApp
A simple backend for fetching pizza delivery details. Made for learning FASTAPI and PostgreSQL.
# Installation

1. Clone the Pizza Delivery App repository from GitHub using the following command:
`git clone https://github.com/Sumit70421/pizzaDeliveryApp.git`

2. Create a virtual environment using Pipenv or virtualenv and activate it.

3. Install the necessary requirements for the app using the following command:
`pip install -r requirements.txt`

# Configuration

1. Set up your PostgreSQL database and obtain the URI needed to connect to it. You can use a service such as ElephantSQL to set up a free instance of a PostgreSQL database.

2. In the file "database.py," update the engine variable with the PostgreSQL URI in the following format:
`engine=create_engine('postgresql://postgres:<username>:<password>@localhost/<db_name>', echo=True )`

3. Initialize the database by running the following command:
`python init_db.py`

4. Run the API by using the following command:
`uvicorn main:app`
