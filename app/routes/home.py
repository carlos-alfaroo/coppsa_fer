from flask import Blueprint, render_template, url_for

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
  return render_template('home.html')

@home_bp.route('/pozos')
def pozos():
  return render_template('pozos.html')

@home_bp.route('/fosas')
def fosas():
  return render_template('fosas.html')

@home_bp.route('/banos')
def banos():
  return render_template('banos.html')