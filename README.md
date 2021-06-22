# DEFI Index

The repo contains the tools necessary to prepare the output file necessary for updating sDEFI/iDEFI indices. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The code needs miniconda, as all packages were installed and tested on conda v4.9.2. Installation of miniconda can be done by running the following:

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -p $HOME/miniconda3
```

### Installing Enviroment

Refer to [conda docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

The enviroment files are available under conda_env folder. Enviroment setup can be done with the one of the below actions:

#### With the enviroment file
```
conda env create --name defi --file=env\environment.yml
```

## Running the model
### Activating imported enviroment

```
conda activate defi
```


### Preparing the yaml file

The following command would run the model

```
python main.py
```

### Yaml file
In order to produce the output correctly when the defi composition changes, the yaml file `config\tickers.yaml` needs to be properly populated:
```
uni: 
    id:  'uniswap'
    concentration:  0.12
```

`uni`: just  an arbirtrary identifier, ticker could be used

`id`: is the id as per coingecko, please refer to [api](https://www.coingecko.com/en/api)

`concentration`: is usually prepared by the authors of the sccp


## Authors

**Kaleb**

