
from flask import Flask, request, redirect, url_for

app = Flask(__name__)
assets = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("asset_name", "").strip()
        if name:
            assets.append(name)
        return redirect(url_for("home"))

    asset_list = "".join(
        f"<li>{name}</li>" for name in assets
    )

    return f"""
    <!DOCTYPE html>
    <html>
    <head><title>Asset System v1</title></head>
    <body>
        <h1>Asset System - Version 1</h1>
        <h2>Add Asset</h2>
        <form method="POST">
            <input name="asset_name"
                   placeholder="Enter asset name" required>
            <button type="submit">Add Asset</button>
        </form>
        <h3>Added assets</h3>
        <ul>{asset_list}</ul>
    </body>
    </html>
    """

if __name__ == "__main__":
    print("Starting Asset System v1...")
    app.run(host="0.0.0.0", port=5000, debug=False)
