# Pinging Ipaddress Example
Ping checks the server status, if there is a change, it was going to email to the user

**Set the sender email and recipients email in enums.py**

# Run Manually 
## Installation
* Miniconda: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

## Starting
```
python main.py
```

# Run With Docker 
## Installation

* Get Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
* Install docker for Ubuntu 18.04: [https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)
* Install docker compose for Linux: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

## Starting
```
cd pinging-ipaddress-example
```
```
docker-compose up --build -d
```

If your sender email have 2-Step Verification You need to Create and use App Passwords email: https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637846808076357632-2640835334&rd=1