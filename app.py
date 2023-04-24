from flask import Flask, request
from util import suggest_program
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, origins="*")

@app.route('/')
def hello_world():
    args = request.args

    query_dict = args.to_dict()

    if len(query_dict) != 9:
        return {"status": "error", "message": "length of arguments must be 9"}

    # convert some str to int
    query_dict["grade_aggregate"] = int(query_dict.get("grade_aggregate"))
    query_dict["age"] = int(query_dict.get("age"))

    suggested_program = suggest_program(query_dict)
    return {"status": "success", "data": suggested_program}


if __name__ == "__main__":
    app.run(debug=True)