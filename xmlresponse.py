from plivo import plivoxml


def generatexml():
    response = plivoxml.ResponseElement()
    response.add(plivoxml.GetDigitsElement(
        action='https://webhook.site/dd354ce2-29b3-427a-be8e-93bdf5029e68', method='POST',))

    return response.to_string()
