from pprint import pprint
from textwrap import wrap
from flask import Flask, jsonify, request
import pyshorteners

app = Flask(__name__)
methods = ["GET", "POST", "PATCH", "DELETE"]

@app.route("/<echo>/<name>", methods = methods)
def hello(echo, name):
    return echo + name

@app.route("/short", methods = methods)
def get_tiny_url():

    j = request.get_json()
    print(j)
    
    short = pyshorteners.Shortener()

    new_url = short.tinyurl.short(j["url"])

    return jsonify(
        {
            "data:": new_url,
        }
    )

if __name__ == "__main__":
    app.run()


# @app.route("/watch", methods=methods, defaults={"path": ""})
# @app.route("/watch/<path:path>", methods=methods)
# def hello_world(path):
#     divider = "================================================================"
#     j = request.get_json()

#     print(divider)
#     print(f"*** Received data at: {path}")

#     print("\n** data:")
#     print("\n".join(wrap(request.data.decode())))

#     print("\n** form:")
#     pprint(request.form)

#     print("\n** json:")
#     pprint(j)

#     print(f"{divider}\n\n")

#     return jsonify(
#         {
#             "endpoint": path,
#             "data": request.data.decode("utf-8"),
#             "form": request.form,
#             "json": request.get_json(),
#         }
#     )

