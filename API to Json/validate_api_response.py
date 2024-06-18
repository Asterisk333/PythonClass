def validate_api_response(response):
    if response.status_code == 200:
        return True