from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
import requests
import os
import subprocess

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
