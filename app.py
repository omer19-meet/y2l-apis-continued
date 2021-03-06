from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    
    image_url = request.form['url-input']
    # At this point you have the image_url value from the front end
    # Your job now is to send this information to the Clarifai API
    # and read the result, make sure that you read and understand the
    # example we covered in the slides! 

    # YOUR CODE HERE!
    headers = {'Authorization': 'Key 7d2c88d5001448ae8691c3a3c0231c54'}
    api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
    data ={"inputs": [
      {
        "data": {
          "image": {
            "url": image_url
          }
        }
      }
    ]}

    response2 = requests.post(api_url, headers=headers, data=json.dumps(data))
    # response = response.content
    # response_dict = json.loads(response.content)
    # response_dict["outputs"][0]["data"]#["concepts"]#
    response2 = json.loads(response2.content)
    return render_template('home.html', results=response2["outputs"][0]["data"]["concepts"], image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)