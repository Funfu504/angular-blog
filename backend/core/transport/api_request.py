import logging
import json

logger = logging.getLogger(__name__)

#Logs useful debugging information associated to a request.
def logRequest(event):
    identity = get_identity(event)
    logger.info(
        json.dumps(
            {
                "route": event["requestContext"]["routeKey"],
                "user": identity.get("sub"),
                "request_id": event["requestContext"]["requestId"]
            }
        )
    )

#This fetches the claims entity from the request which has, among other things, the canonical userid
#maintained in Cognito.
def get_identity(event):
    return (
        event
        .get("requestContext", {})
        .get("authorizer", {})
        .get("jwt", {})
        .get("claims", {})
    )

#This handler can be called either thru the test harness in AWS or the Gateway...code for both.
def get_payload(event):
    body = event.get("body")  #attempt to pull the body out of the event.
    if body:                  #if successful, convert that into json.
        return json.loads(body)

    return event              #otherwise, it's already in json.  just return.

#unpacks the json from the body and adds it to the desired model.
def parse_event_model(event, model):
    identity = get_identity(event)
    payload = get_payload(event)
    payload["userId"] = identity.get("sub")
    return model.model_validate(payload)

