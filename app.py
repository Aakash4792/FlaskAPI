from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import base64

app = Flask(__name__)
CORS(app) 

@app.route('/flask', methods=['POST'])
def upload_files():
    print('req recv2');
    uploaded_files = request.files.getlist('photos')
    print(request.form);
    data = {'summary' : 'lorem1isadj asiod joajd oiasjd oas'}
    selected_flight = request.form.get('selectedFlight')
    selected_date = request.form.get('selectedDate')
    number_input1 = int(request.form.get('numberInput1'))
    print('data 1 : ',data);
    flight_number = request.form.get('flightNumber')
    print('data 2 : ',data);
    flight_info = {'selected_flight' : selected_flight,'selected_date' : selected_date,'number_input1' : number_input1,'flight_number' : flight_number}
    data['flight_info'] = flight_info
    print('data 3 : ',data);
    print(selected_flight,selected_date,number_input1,flight_number);


    uploaded_photos = []
    
    for file in uploaded_files:
        # Process each file as needed, e.g., save to a directory
        file_path = 'photos/' + file.filename
        file.save(file_path)
        # Encode the photo as a base64 string
        with open(file_path, 'rb') as photo_file:
            encoded_photo = base64.b64encode(photo_file.read()).decode('utf-8')
            uploaded_photos.append({'filename': file.filename, 'data': encoded_photo,'image_id' : len(uploaded_photos),'defects' : [{"defectName": "abcd","defectContent": "asdjks ajdnasjnd kasnjd ka","coords": [134, 197, 43, 99],},{"defectName": "poqii","defectContent": "opaksdop oasdk poaskd okaso;","coords": [154, 511, 40, 107],},]})
        
    data['uploaded_photos'] = uploaded_photos
    return jsonify(data), 200

if __name__ == '__main__':
    app.run()