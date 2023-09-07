import urllib.parse
import requests
import csv
from faker import Faker
from time import sleep

fake = Faker()

with open("raw_yelp_review_data.csv", mode="r") as file:
    csvFile = csv.reader(file)
    for _ in range(1, 4340):
        next(csvFile, None)
    for line in csvFile:
        URL = "http://127.0.0.1:5000/api/add?name=" + urllib.parse.quote(fake.name()) + "&review=" + urllib.parse.quote(
            line[1])
        requests.get(URL)
        sleep(0.1)
