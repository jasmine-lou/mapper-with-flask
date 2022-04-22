from flask import Flask, render_template, request

app = Flask(__name__)

data = {"0": {"id": 0,
              "polygon": [[40.8099, -73.961],
                          [40.80965, -73.9604],
                          [40.80929, -73.96064],
                          [40.80953, -73.96124],
                          [40.8099, -73.961]],
              "color": "red",
              "description": "CEPSR Building",
              'lat': 40.80959,
              'lon': -73.96082,
              },

        "1": {"id": 1,
              "polygon": [[40.80963, -73.96031],
                          [40.80928, -73.95947],
                          [40.80908, -73.95961],
                          [40.80943, -73.96045],
                          [40.80963, -73.96031]],
              "color": "blue",
              "description": "Mudd Building",
              'lat': 40.80935,
              'lon': -73.95993,
              }
        }


@app.route('/')
def root():
    global data
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(host="localhost", port=3001, debug=True)
