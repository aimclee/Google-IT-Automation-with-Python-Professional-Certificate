#!/usr/bin/env python3

import json
import locale
import sys
from reports import generate as report
from emails import generate as email_generate
from emails import send as email_send

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  sales = {"total_sales":0}
  most_popular_car_years = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$")) # float
    item_revenue = item["total_sales"] * item_price
    

    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if item["total_sales"] > sales["total_sales"]:
      sales = item
    # TODO: also handle most popular car_year
    if not item['car']['car_year'] in most_popular_car_years.keys():
      most_popular_car_years[item['car']['car_year']] = item["total_sales"]
    else:
      most_popular_car_years[item['car']['car_year']] += item["total_sales"]
  

  # value값이 최대인 key값 찾기
  # dict.get == dict.get(key) : 해당 key에 대한 value를 가져오라는 뜻 
  most_popular_year = max(most_popular_car_years, key=most_popular_car_years.get)
  
  all_sales = most_popular_car_years.values()
  max_total_sale = max(all_sales)



  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}"
    .format(format_car(sales["car"]), sales["total_sales"]),
    "The most popular year was {} with {} sales."
    .format(most_popular_year,max_total_sale )
  ]

  return summary

def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("/home/student-03-5ca45b691a2a/car_sales.json")
  summary = process_data(data)
  new_summary = ''.join(summary)
  print(summary)
  # TODO: turn this into a PDF report
  report('/tmp/cars.pdf', "Cars report", new_summary, cars_dict_to_table(data))
  # TODO: send the PDF report as an email attachment
  msg = email_generate("automation@example.com", "student-03-5ca45b691a2a@example.com",
                         "Sales summary for last month", new_summary, "/tmp/cars.pdf")
  email_send(msg)

if __name__ == "__main__":
  main(sys.argv)
