# coding=utf8
import os
from flask import render_template, redirect
from flask import send_from_directory, request, Response
from jinja2 import Environment, FileSystemLoader, environment
from app import app

@app.route('/')
def index():
    return render_template('index.html')


