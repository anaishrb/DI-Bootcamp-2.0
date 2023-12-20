import psycopg2
import requests
import random

conn = psycopg2.connect(
    dbname='Day4xpmandatory',
    user='postgres',
    password='pgjav',
    host='localhost',
    port='5432'
)

# Create a cursor object to execute SQL queries
cur = conn.cursor()

def fetch_random_countries():
    try:
        response = requests.get('https://restcountries.com/v3.1/all')
        if response.status_code == 200:
            countries_data = response.json()
            return random.sample(countries_data, 10)
        else:
            print("Failed to fetch data from the API.")
            return []
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return []

def insert_countries_to_db(countries):
    for country in countries:
        name = country.get('name', '')
        capital = country.get('capital', '')
        flag = country.get('flags', [''])[0]  # Taking the first flag URL
        subregion = country.get('subregion', '')
        population = country.get('population', 0)

        # Inserting data into the database using 'cur' (cursor object)
        cur.execute(
            "INSERT INTO countries (name, capital, flag, subregion, population) VALUES (%s, %s, %s, %s, %s)",
            (name, capital, flag, subregion, population)
        )

# Fetching 10 random countries
random_countries = fetch_random_countries()

# Inserting fetched countries into the database
insert_countries_to_db(random_countries)

# Commit changes to the database and close connections
conn.commit()
cur.close()
conn.close()


#this error is showing and i cant solve it /Library/Frameworks/Python.framework/Versions/3.12/Resources/Python.app/Contents/MacOS/Python: can't open file '/Users/anaisherbillon/Documents/Bootcamp/Week3/Day4/Dailychallengegit': [Errno 2] No such file or directory
#anaisherbillon@MacBook-Air-de-Anais Week3 % 