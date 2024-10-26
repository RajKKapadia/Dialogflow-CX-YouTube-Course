import json
from typing import Any, Dict, List

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def handle_get_home():
    return "OK", 200


def format_response_for_dialogflow(messages: List[str]) -> Dict[str, Any]:
    response_data = {
        "fulfillmentResponse": {
            "messages": [],
            "mergeBehavior": "MERGE_BEHAVIOR_UNSPECIFIED"
        }
    }
    for message in messages:
        response_data["fulfillmentResponse"]["messages"].append({
            "responseType": "RESPONSE_TYPE_UNSPECIFIED",
            "text": {
                "text": [message],
                "allowPlaybackInterruption": False
            }
        })
    return response_data


@app.post("/")
def handle_post_home():
    body = request.get_json()
    print(json.dumps(body))
    return jsonify(format_response_for_dialogflow([
        "First message",
        "Second message"
    ])), 200


if __name__ == "__main__":
    app.run(
        debug=True
    )
