#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template

DEVELOPMENT_ENV  = True

app = Flask(__name__)

app_data = {
    "name":         "Dissertation Planner",
    "description":  "A basic Flask app for students to plan their dissertations",
    "author":       "Peter Simeth",
    "html_title":   "Dissertation Planner",
    "project_name": "Dissertation Planner",
    "keywords":     "flask, webapp, dissertation, planning, python"
}


@app.route('/')
def index():
    return render_template('index.html', app_data=app_data)


@app.route('/calendar')
def about():
    return render_template('calendar.html', app_data=app_data)


@app.route('/workload')
def service():
    return render_template('workload.html', app_data=app_data)
    

if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)