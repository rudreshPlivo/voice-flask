from flask import Flask, render_template, Response, request
import plivo
from lxml import etree
import xmlresponse


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sms")
def sms():
    return render_template("sms.html")


@app.route("/call", methods=['POST'])
def call():
    if request.method == 'POST':
        # handle making the call

        call_data = request.get_json()
        print('call data is {}'.format(call_data))
        to_number = call_data['toNumber']
        from_number = call_data['fromNumber']
        answer_url_xml = 'https://plvo-voice.herokuapp.com/callgetdigitxml'

        # create plivo call client

        try:
            client = plivo.RestClient(
                auth_id='YOUR_AUTH_ID', auth_token='YOUR_AUTH_TOKEN')
            response = client.calls.create(
                from_=from_number,
                to_=to_number,
                answer_url=answer_url_xml,
                answer_method='POST'
            )
            print(response)
            return Response('success', mimetype='text/plain')

        except expression as PlivoError:
            print('the error is {}'.format(PlivoError))
            return Response('could not make call', mimetype='text/plain')


@app.route("/callgetdigitxml", methods=['POST'])
def callgetdigitxml():
    print('here in get xml')
    if request.method == 'POST':
        # send back xml with speak and get digit values
        # create response xml
        responsexml = xmlresponse.generatexml()

        resp = app.make_response(responsexml)
        resp.mimetype = 'text/xml'
        return resp


if __name__ == "__main__":
    app.run(debug=True)
