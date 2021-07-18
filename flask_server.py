from save import save_to_file
from flask import Flask, render_template, request, redirect, send_file
from main import get_jobs

app = Flask(__name__)

db = {}

@app.route("/")
def home():
    return render_template('potato.html')

@app.route("/report")
def report():
    keyword = request.args.get('keyword')
    pages = request.args.get('pages')
    pages = int(pages)
    if keyword:
        keyword = keyword.lower()
        myDB = db.get(keyword)
        if myDB:
            jobs = myDB
        else:
            jobs = get_jobs(keyword, pages)
            db[keyword] = jobs
    else:
        return redirect("/")
    return render_template('report.html', keyword= keyword, resultNumber = len(jobs), jobs=jobs)


@app.route("/export")
def export():
    try:
        keyword = request.args.get('keyword')
        if not keyword:
            raise Exception()
        keyword = keyword.lower()
        jobs = db.get(keyword)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")

app.run(host='127.0.0.1', port='4000')