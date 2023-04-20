from flask import Flask, request
from util import suggest_program


app = Flask(__name__)

@app.route('/')
def hello_world():
    args = request.args
    print(args.to_dict())
    query_dict = args.to_dict()

    # convert some str to int
    query_dict["grade_aggregate"] = int(query_dict.get("grade_aggregate"))
    query_dict["age"] = int(query_dict.get("age"))

    suggested_program = suggest_program(query_dict)
    return {"status": "success", "data": suggested_program}


if __name__ == "__main__":
    app.run(debug=True)