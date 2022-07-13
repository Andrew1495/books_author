from flask import Flask, render_template, redirect, Blueprint, request
from repositories import book_repo
from repositories import author_repo
from models.book import Book

book_blueprint = Blueprint("books", __name__)

@book_blueprint.route("/books")
def books():
    return render_template("books/index.html")