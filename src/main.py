from flask import Flask, jsonify
from shippingtracker.v1_0_0.Container.controllers.TracksController import TracksController
from shippingtracker.v1_0_0.Container.models.request.TrackRequest import TrackRequest

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def root():
    return "It's working on this port!"
    
@app.route("/tracking/<slug>/<tracking_number>")
def call_tracking_action(slug, tracking_number):
    reqBody = TrackRequest(slug=slug, tracking_number=tracking_number)
    tracksController = TracksController()
    res = tracksController.tracking(reqBody)
    return res.todict(), 200