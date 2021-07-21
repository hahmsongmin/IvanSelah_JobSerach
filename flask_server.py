from jobs_save.save import save_to_file
from flask import Flask, render_template, request, redirect, send_file
from jobs_combine_hub.combine import get_jobs

app = Flask(__name__, static_url_path="/static")

db = {}

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/report")
def report():
    keyword = request.args.get('keyword')
    location = request.args.get('select')
    
    pages = 0 # default
    if keyword:
        keyword = keyword.lower()
        myDB = db.get(keyword)
        if myDB:
            jobs = myDB
        else:
            jobs = get_jobs(keyword, pages)
            db[keyword] = jobs

        if location != '전국':
            location_list_temp = list()
            for job in jobs:
                if job["지역"][:2] == location:
                    location_list_temp.append(job)
            return render_template('index_result.html', keyword= keyword, resultNumber = len(location_list_temp), jobs=jobs, location=location)
        else:
            return render_template('index_result.html', keyword= keyword, resultNumber = len(jobs), jobs=jobs, location=location)
    else:
        return redirect("/")


@app.route("/export")
def export():
    try:
        keyword = request.args.get('keyword')
        location = request.args.get('select')
        if not keyword:
            raise Exception()
        keyword = keyword.lower()
        jobs = db.get(keyword)
        if not jobs:
            raise Exception()
        save_to_file(jobs, location)
        return send_file("jobs.csv")
    except:
        return redirect("/")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080')