#!/usr/bin/env python
# coding: utf-8

import cred

import requests as rq
import sqlite3

dbc = sqlite3.connect("udemy_classes.db")
dbr = dbc.cursor()
dbr.execute(
    """create table if not exists udemy_classes(
    key integer,
    title text,
    price test)
    """)
dbc.commit()

all_classes = list()
page: int = 0
# change this up to 10000 to get more

page_end: int = 10
udemy_url_endpoint: str = "https://www.udemy.com/api-2.0"
udemy_url_classes: str = f"courses/?page={page}"
headers: dict = {
  "Accept": "application/json, text/plain, */*",
  "Authorization": cred.authorisation,
  "Content-Type": "application/json"
}

while page < 10:
    classes_response = rq.get(
        f"{udemy_url_endpoint}/{udemy_url_classes}",
        headers=headers)
    classes_json = classes_response.json()
    if "results" in classes_json:
        all_classes.extend(classes_json["results"])
    page += 1
    udemy_url_classes = f"courses/?page={page}"
    print(f"page: {page}")

print(f"len all_classes: {len(all_classes)}")

for i, all_class in enumerate(all_classes):
    dbr.execute(
        "insert into udemy_classes values (?, ?, ?)",
        (i, all_class["title"], all_class["price"])
    )

    print(
        f"{i} class\n"
        f"TITLE: {all_class['title']}\n"
        f"PRICE: {all_class['price']}\n"
        "####\n"
    )

dbc.commit()

nonfree = dbr.execute("select * from udemy_classes where price != 'Free'")
nonfree_courses = nonfree.fetchall()
for nonfree_course in nonfree_courses:
    print(f"nonfreecourse: {nonfree_course}")
