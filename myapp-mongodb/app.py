from flask import Flask, request
import pymongo

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    body = """<!DOCTYPE html>
<html><body><h2>HTML Forms</h2>
<form action="/dest" method="get">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="Harish"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="KR"><br><br>
  <input type="submit" value="Click to Submit">
</form>
<p>If you click the "Click to Submit" button, the form-data will be sent to a page called "/dest". with GET as method</p>
</body></html>
"""
    return body


def write_to_db(data):
    myclient = pymongo.MongoClient("mongodb://admin:password@harimongodb/")
    mydb = myclient["haridb"]
    mycollection = mydb["haritable"]
    x = mycollection.insert_one(data)
    print(x.inserted_id)


@app.route("/dest", methods=["GET"])
def destination():
    vars_in_get = ""
    data = dict()
    for key, val in request.args.items():
        # insert into mongo
        # append to body for display
        data[key] = val
        vars_in_get = "<p> inserted record :" + vars_in_get + key + ":" + val + "</p>"

    # Display body
    write_to_db(data)
    body = """<!DOCTYPE html>
<html><body><h2>HTML Forms</h2>
{}
</body></html>
""".format(
        vars_in_get
    )

    return body


app.run(host="0.0.0.0")
