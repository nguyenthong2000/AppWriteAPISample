from appwrite.client import Client
from appwrite.services.users import Users
from appwrite.exception import AppwriteException
import os
import json
from generator import image_generator
from server import app

# This Appwrite function will be executed every time your function is triggered
def main(context):
    # You can use the Appwrite SDK to interact with other services
    # For this example, we're using the Users service
    # client = (
    #     Client()
    #     .set_endpoint(os.environ["APPWRITE_FUNCTION_API_ENDPOINT"])
    #     .set_project(os.environ["APPWRITE_FUNCTION_PROJECT_ID"])
    #     .set_key(context.req.headers["x-appwrite-key"])
    # )
    # users = Users(client)

    context.log(context.req.body_raw)  # Raw request body, contains request data
    context.log(json.dumps(context.req.body))  # Object from parsed JSON request body, otherwise string
    context.log(json.dumps(context.req.headers))  # String key-value pairs of all request headers, keys are lowercase
    context.log(context.req.scheme)  # Value of the x-forwarded-proto header, usually http or https
    context.log(context.req.method)  # Request method, such as GET, POST, PUT, DELETE, PATCH, etc.
    context.log(context.req.url)  # Full URL, for example: http://awesome.appwrite.io:8000/v1/hooks?limit=12&offset=50
    context.log(context.req.host)  # Hostname from the host header, such as awesome.appwrite.io
    context.log(context.req.port)  # Port from the host header, for example 8000
    context.log(context.req.path)  # Path part of URL, for example /v1/hooks
    context.log(context.req.query_string)  # Raw query params string. For example "limit=12&offset=50"
    context.log(json.dumps(context.req.query))  # Parsed query params. For example, req.query.limit

    # The req object contains the request data
    if context.req.path == "/ping":
        # Use res object to respond with text(), json(), or binary()
        # Don't forget to return a response!
        return context.res.text("Pong")

    if context.req.path == "imagegenerate" and context.req.method == "POST":
        json_data = json.loads(context.req.body_raw)

        base_filename = json_data['base_filename']
        amount = json_data['amount']
        prompt = json_data['prompt']
        prompt_size = json_data['prompt_size']
        negative_prompt = json_data['negative_prompt']
        style = json_data['style']
        resolution = json_data['resolution']
        guidance_scale = json_data['guidance_scale']

        context.log("-"*10)
        context.log(base_filename)
        context.log(amount)
        context.log(prompt)
        context.log(prompt_size)
        context.log(negative_prompt)
        context.log(style)
        context.log(resolution)
        context.log(guidance_scale)

        generator = image_generator(
            base_filename=base_filename,
            amount=amount,
            prompt=prompt,
            prompt_size=prompt_size,
            negative_prompt=negative_prompt.replace(' ', ', '),
            style=style,
            resolution=resolution,
            guidance_scale=guidance_scale
        )

        context.log(generator)


    return context.res.json(
        {
            "motto": "Build like a team of hundreds_",
            "learn": "https://appwrite.io/docs",
            "connect": "https://appwrite.io/discord",
            "getInspired": "https://builtwith.appwrite.io",
        }
    )