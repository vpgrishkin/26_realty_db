from flask import Flask, render_template

from model import db, Ads

ADDS_PER_PAGE = 15

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)


@app.route('/', methods=['GET'])
def ads_list(page=1):
    query = Ads.query.filter(Ads.show== True).paginate(page, ADDS_PER_PAGE)
    return render_template('ads_list.html', ads=query)


if __name__ == "__main__":
    app.run()
