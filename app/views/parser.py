import json
from helper import helper

def parse(input_json):
    city = input_json["city"]
    shop = input_json["shop"]
    voucher_id = helper.generate_voucher_id()