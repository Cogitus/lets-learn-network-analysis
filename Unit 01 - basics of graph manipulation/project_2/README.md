# About the data on this repo
All the data contained here was already transformed and filtered in the [Alvaro's repository](https://github.com/alvarofpp/dataset-flights-brazil). The scripts

    extract.py
    transform_to_airports_csv.py
    transform_to_anac_csv.py
    transform_to_graphml.py
    
are his productions and here are being used to extract from the ```.csv's``` the ```air_traffic.graphml``` file. Only the ```transform_to_graphml.py``` script is adpated to return more information than that of the original file.

# Installing the dependencies
If you have anaconda installed, you can create an isolated enviroment using:

    $ conda create --name data_flights python==3.10
    $ conda activate data_flights

For the installation of the necessary libraries to make this project run, it is achievable by executing the following command (on this repo root folder):

    $ pip install -r requirements.txt

# Data preparation
For the data preparation, the following commands are necessary (executed in the same order as it follows):

    # to download the proper .csv data
    python extract.py

    # data transformation and generation of the graphml file
    python transform_to_anac_csv.py
    python transform_to_airports_csv.py
    python transform_to_graphml_adapted.py

And its done! The jupyter notebook ```air_traffic_network_analysis``` its ready to be used.