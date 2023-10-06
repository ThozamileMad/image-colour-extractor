from flask import Flask, render_template, redirect, url_for, request
from data_processor import generate_array, get_random_code

app = Flask(__name__)
app.config["SECRET_KEY"] = "SBAALAV327IUMWSLMD;LMDJIOHOHND"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/<file>/<int:range_num>", methods=["GET", "POST"])
def display(file, range_num):
    array = generate_array(f"static/images/{file}")
    if range_num < 30:
        codes = get_random_code(array, range_num)
        return render_template("display.html", codes=codes, file=file)
    else:
        codes = get_random_code(array, 30)
        return render_template("display.html", codes=codes, file=file)


@app.route("/upload/<error>", methods=["GET", "POST"])
def upload(error):
    if request.method == "POST":
        filename = str(request.files["file"]).split()[1][1:-1]
        try:
            range_num = int(request.form["range_num"])
        except ValueError:
            return redirect(url_for("upload", error="true"))

        if filename == "":
            return redirect(url_for("upload", error="true"))
        elif range_num > 30:
            return redirect(url_for("upload", error="true"))
        else:
            if "file" in request.files:
                file = request.files["file"]
                file.save(rf"static\images\{filename}")
                return redirect(url_for("display", file=filename, range_num=range_num))
            
    return render_template("upload_image.html", error=error)


if __name__ == "__main__":
    app.run(debug=True)

