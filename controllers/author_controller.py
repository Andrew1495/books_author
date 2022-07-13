from flask import Flask, render_template, redirect, Blueprint, request
from repositories import book_repo
from repositories import author_repo
from models.book import Book

author_blueprint = Blueprint("author", __name__)

@author_blueprint.route("/authors")
def author():
    authors = author_repo.select_all()
    return render_template("authors/index.html", all_authors=authors)