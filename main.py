from flask import Flask, request, render_template, Blueprint
import logging
import os

import functions

data_file = os.path.join("data", "posts.json")
log_file = os.path.join("log.log")
upload_pic = "uploads/images/"

app = Flask(__name__)

main_blueprint = Blueprint("main_blueprint", __name__)

logging.basicConfig(filename=log_file, level=logging.DEBUG)


@main_blueprint.route("/")
def main_page():
    logging.info("Loading the main page")
    return render_template("index.html")


@main_blueprint.route("/search")
def search_posts():
    s = request.args.get("s")
    logging.info("A search is being performed")
    return render_template("post_list.html", posts=functions.search_post(s, data_file), s=s)


@main_blueprint.route("/posts", methods=["GET"])
def create_new_post():
    logging.info("page add post")
    return render_template("post_form.html")


@main_blueprint.route("/posts", methods=["POST"])
def created_new_post():
    logging.info("page add post")
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("No data uploaded")
        return "Отсуствует часть данных!"
    posts = functions.load_json_fliles(data_file)
    picture_path = f"{upload_pic}{picture.filename}"
    picture.save(picture_path)
    new_post = {"pic": picture_path, "content": content}
    posts.append(new_post)
    functions.overwrite_json_files(posts, data_file)
    return render_template("post_uploaded.html", new_post=new_post)


app.register_blueprint(main_blueprint)


app.run(port=800)
