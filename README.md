# ⚙️ pd-socket-based-middleware

## Install requirements
`pip install -r requirements.txt`

## Run
First, run the DNS server.

`python .\dns.py`

Next, run the Colori server.

`python .\server_colori.py`

Also run the Ducks server.

`python .\server_ducks.py`

Finally, run the main application passing the name of the service to be used as an argument. In this case, DNS only knows the 'colori' and 'ducks' services.

`python main.py colori`
`python main.py ducks`

Instructions for using the service will be printed on the screen.

## About the authors and the project
This project was developed for the Distributed Programming class, taught by professor Frederico Lopes at the Federal University of Rio Grande do Norte. 2024.1. 
### Authors
- [Antony Lemos](https://github.com/antonylemos)
- [Rita Cruz](https://github.com/rcchcz/)
