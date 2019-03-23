# Backend

This README outlines the details of collaborating and running this code.

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](https://git-scm.com/)
* [PostgreSQL](https://www.postgresql.org/) (username:postgres, password:postgres)
  * If you want a different password, change line 9 to: url = "postgres://postgres:YOUR_PASSWORD_HERE@localhost:5432/CarPark"
* [Python 3](https://www.python.org)
* [Google Chrome](https://google.com/chrome/)

## Installation

* `git clone <repository-url>` this repository
* copy the directory to somewhere memorable 
* `pip install -r requirements.txt`
* Create a Server in PostgreSQL and name it whatever you want
* Next create a Database in the server and name it CarPark

## Running / Development

* `python main.py`
* Visit your app at [http://localhost:5000](http://localhost:5000).

### Deploying

See Master Branch for more details on how to run the full app

## Further Reading / Useful Links

* [Pony ORM](https://ponyorm.org/)
* [Flask](http://flask.pocoo.org/)
