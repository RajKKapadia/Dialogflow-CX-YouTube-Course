import json
from typing import Any, Dict, List

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def handle_get_home():
    return "OK", 200


def format_response_for_dialogflow(
        messages: List[str],
        session_info: Dict[str, Any] = None,
        page_info: Dict[str, Any] = None) -> Dict[str, Any]:
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
    if session_info != None:
        response_data["sessionInfo"] = session_info
    if page_info != None:
        response_data["pageInfo"] = page_info
    return response_data


def handle_default_welcome_intent():
    return format_response_for_dialogflow(
        messages=["Hi, how can I help you today?"]
    )


def handle_first_page(body: Dict[str, Any]) -> Dict[str, Any]:
    """PERFORM A TASK
    [1] Validate the parameters
    [2] Save in the database
    [3] Return a response
    [4] Call Openai, chat completion, generate response, send the response back
    """
    return format_response_for_dialogflow(
        messages=["We have received the parameters."]
    )


@app.post("/")
def handle_post_home():
    body = request.get_json()
    tag = body["fulfillmentInfo"]["tag"]
    response_data = {}
    if tag == "defaultWelcomeIntent":
        response_data = handle_default_welcome_intent()
    elif tag == "firstPage":
        response_data = handle_first_page(body)
    else:
        response_data = format_response_for_dialogflow([
            f"No handler for the tag: {tag}"
        ])
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(
        debug=True
    )
