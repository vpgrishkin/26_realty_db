from datetime import datetime

from flask import Flask, render_template, request

from model import db, Ads

ADDS_PER_PAGE = 15
NEW_BUILDING_AGE = 2

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)


@app.route('/', methods=['GET'])
@app.route('/<int:page>', methods=['GET'])
def ads_list(page=1):
    query = Ads.query.filter(Ads.show== True).paginate(page, ADDS_PER_PAGE)
    return render_template('ads_list.html', ads=query)


@app.route('/search', methods=['GET'])
@app.route('/search/<int:page>', methods=['GET'])
def search(page=1):
    oblast_district = request.args.get('oblast_district', default=None, type=str)
    min_price = request.args.get('min_price', default=None, type=int)
    max_price = request.args.get('max_price', default=None, type=int)
    new_building = request.args.get('new_building', default=None, type=bool)

    ads_query = Ads.query.filter_by(show=True)
    if oblast_district:
        ads_query = ads_query.filter_by(oblast_district=oblast_district)
    if min_price:
        ads_query = ads_query.filter(Ads.price >= min_price)
    if max_price is not None:
        ads_query = ads_query.filter(Ads.price <= max_price)
    if new_building == True:
        ads_query = ads_query.filter(Ads.construction_year >= datetime.today().year - NEW_BUILDING_AGE)
    ads = ads_query.order_by(Ads.price).paginate(page, ADDS_PER_PAGE)
    return render_template('ads_list.html', 
                            ads=ads,
                            min_price=min_price,
                            max_price=max_price,
                            new_building=new_building,
                            oblast_district=oblast_district)


if __name__ == "__main__":
    app.run()
