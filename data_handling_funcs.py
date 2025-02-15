def determine_content_type(file_name):
    if file_name.endswith(".html"):
        return "text/html; charset=utf-8"
    elif file_name.endswith(".css"):
        return "text/css"
    elif file_name.endswith(".js"):
        return "application/javascript"
    elif file_name.endswith(".jpg"):
        return "image/jpeg"
    elif file_name.endswith(".jpeg"):
        return "image/jpeg"
    elif file_name.endswith(".png"):
        return "image/png"
    elif file_name.endswith(".gif"):
        return "image/gif"
    elif file_name.endswith(".ico"):
        return "image/x-icon"
    elif file_name.endswith(".json"):
        return "application/json"
    elif file_name.endswith(".pdf"):
        return "application/pdf"
    elif file_name.endswith(".zip"):
        return "application/zip"
    elif file_name.endswith(".txt"):
        return "text/plain"
    else:
        return "application/octet-stream"

def get_content_type_header(file_name):
    return {"Content-Type": determine_content_type(file_name)}