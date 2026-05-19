import json

#This handler can be called either thru the test harness in AWS or the Gateway...code for both.
def get_payload(event):
    body = event.get("body")  #attempt to pull the body out of the event.
    if body:                  #if successful, convert that into json.
        return json.loads(body)

    return event              #otherwise, it's already in json.  just return.

#unpacks the json from the body and adds it to the desired model.
def parse_event_model(event, model):
    payload = get_payload(event)
    return model.model_validate(payload)