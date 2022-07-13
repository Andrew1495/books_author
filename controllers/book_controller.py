from flask import Flask, render_template, redirect, Blueprint, request
from repositories import book_repo
from repositories import author_repo
from models.book import Book

book_blueprint = Blueprint("books", __name__)

@book_blueprint.route("/books")
def books():
    books = book_repo.select_all()
    return render_template("books/index.html", all_books=books)


@book_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete(id):
    breakpoint()
    book_repo.delete_id(id)
    return redirect("/books")
