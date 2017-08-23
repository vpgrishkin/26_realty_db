import os
import argparse
import json
import sys

from flask import Flask

from model import db, Ads


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)


def load_file(filepath):
    if os.path.exists(filepath):
        return open(filepath, 'r', encoding='utf-8')


def load_data(json_file):
    return json.load(json_file)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--json_file', help='Input a json file path')
    parser.add_argument('-c', '--create', help='To create new db input: --create db')
    args = parser.parse_args()
    return args


def create_db():
    with app.app_context():
        db.drop_all()
        db.create_all()


def update_db_session(ads):
    for ad in ads:
        ads_to_db = Ads(ad['id'], 
                        ad['settlement'], 
                        ad['under_construction'], 
                        ad['description'], 
                        ad['price'],
                        ad['oblast_district'],
                        ad['living_area'],
                        ad['has_balcony'],
                        ad['address'],
                        ad['construction_year'],
                        ad['rooms_number'],
                        ad['premise_area'],
                        is_actual=True)
        db.session.add(ads_to_db)


def set_is_actual_false_for_all_ads_in_session():
    for ad in Ads.query.all():
        ad.is_actual = False
        db.session.add(ad)


if __name__ == '__main__':
    args = get_args()
    if args.create == 'db':
        print('Try to create the db')
        create_db()
    elif args.json_file:
        print('Try update db from {}'.format(args.json_file))
        json_file_path = args.json_file
        json_file = load_file(json_file_path)
        if json_file is None:
            print('No file: {}'.format(json_file_path))
            sys.exit(1)
        json_data = load_data(json_file)
        with app.app_context():
            set_is_actual_false_for_all_ads_in_session()
            update_db_session(json_data)
            db.session.commit()
    else:
        print('No arguments. Try -h')

