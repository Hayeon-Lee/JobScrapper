from flask import Flask, render_template, request
from extractors.remoteok import extract_remoteok_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html")


db = {}


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword in db:
        jobs = db[keyword]
    else:
        remoteok = extract_remoteok_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = remoteok + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=db[keyword])


app.run("0.0.0.0")
