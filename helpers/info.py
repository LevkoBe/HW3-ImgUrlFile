# helpers/info.py

info = {
    "endpoints": [
        {
            "path": "/",
            "method": "GET",
            "description": "Get info about the endpoints, as well as about the website."
        },
        {
            "path": "/info",
            "method": "GET",
            "description": "Get information provided by the server."
        },
        {
            "path": "/image/{image_name}",
            "method": "GET",
            "description": "Get a specific image by providing the image name in the path."
        },
        {
            "path": "/urlParse?url={url_string}",
            "method": "GET",
            "description": "Parse and get information about the provided URL."
        },
        {
            "path": "/fileParse",
            "method": "POST",
            "description": "Parse the content of a file and provide metadata based on user input."
        }
    ]
}
