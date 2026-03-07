import os
import json
import datetime
import requests
import hashlib
import hmac
import base64

workspace_id = os.environ.get("LOG_ANALYTICS_WORKSPACE_ID")
shared_key = os.environ.get("LOG_ANALYTICS_SHARED_KEY")

log_type = "CustomAppLogs"

def build_signature(date, content_length, method, content_type, resource):

    x_headers = "x-ms-date:" + date
    string_to_hash = method + "\n" + str(content_length) + "\n" + content_type + "\n" + x_headers + "\n" + resource

    bytes_to_hash = bytes(string_to_hash, encoding="utf8")
    decoded_key = base64.b64decode(shared_key)

    encoded_hash = base64.b64encode(
        hmac.new(decoded_key, bytes_to_hash, digestmod=hashlib.sha256).digest()
    ).decode()

    return "SharedKey {}:{}".format(workspace_id, encoded_hash)


def send_log(message):

    body = json.dumps([
        {
            "TimeGenerated": datetime.datetime.utcnow().isoformat(),
            "Message": message
        }
    ])

    method = "POST"
    content_type = "application/json"
    resource = "/api/logs"
    rfc1123date = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

    content_length = len(body)

    signature = build_signature(
        rfc1123date,
        content_length,
        method,
        content_type,
        resource
    )

    uri = "https://" + workspace_id + ".ods.opinsights.azure.com" + resource + "?api-version=2016-04-01"

    headers = {
        "Content-Type": content_type,
        "Authorization": signature,
        "Log-Type": log_type,
        "x-ms-date": rfc1123date
    }

    requests.post(uri, data=body, headers=headers)