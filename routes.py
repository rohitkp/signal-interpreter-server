#!/usr/bin/env python3

from flask import Flask, request

signal_interpreter_app = Flask(__name__)

"""
    Function to serve GET request
"""
@signal_interpreter_app.route("/",methods=["GET"])
def hello():
    return "Hello world!"

"""
    Function to serve POST request
""" 
@signal_interpreter_app.route("/", methods=["POST"])
def mirror_data():
    data = request.get_json()
    return data
