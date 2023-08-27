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
    data = {'summary' : 
                {
                    'total_images_uploaded' : len(uploaded_files),
                    'total_defects' : 10,
                    'identified_defect_tags' : ['Cracks','Dents','Missing Heads'],
                    '0' : {
                        'name' : 'Scratch',
                        'total' : 5,
                        'red' : 10,
                        'orange' : 0,
                        'blue' : 4,
                        'big' : 1,
                        'medium' : 2,
                        'small' : 3,
                        
                    },
                    '1' : {
                        'name' : 'Paint off',
                        'total' : 5,
                        'red' : 10,
                        'orange' : 0,
                        'blue' : 4,
                        'big' : 1,
                        'medium' : 2,
                        'small' : 3,
                        
                    },
                    '2' : {
                        'name' : 'Crack',
                        'total' : 5,
                        'red' : 10,
                        'orange' : 0,
                        'blue' : 4,
                        'big' : 1,
                        'medium' : 2,
                        'small' : 3,
                        
                    },
                    '3' : {
                        'name' : 'Missing Head',
                        'total' : 5,
                        'red' : 10,
                        'orange' : 0,
                        'blue' : 4,
                        'big' : 1,
                        'medium' : 2,
                        'small' : 3,
                        
                    },
                    '4' : {
                        'name' : 'Dent',
                        'total' : 5,
                        'red' : 10,
                        'orange' : 0,
                        'blue' : 4,
                        'big' : 1,
                        'medium' : 2,
                        'small' : 3,
                        
                    },
                }
        }
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
            uploaded_photos.append({
                'filename': file.filename, 
                'data': encoded_photo,
                'image_id' : len(uploaded_photos),
                'defects' : [{"type": 4,"severity": "Red","size" : "Big","coords": [134, 197, 43, 99]},{"type": 4,"severity": "Red","size" : "Big","coords": [134, 197, 43, 99]}],
                '0' : {
                    'name' : 'scratch',
                    'total' : 5,
                    'red' : 10,
                    'orange' : 0,
                    'blue' : 4,
                    'big' : 1,
                    'medium' : 2,
                    'small' : 3,
                    },
                '1' : {
                    'name' : 'Paint off',
                    'total' : 5,
                    'red' : 10,
                    'orange' : 0,
                    'blue' : 4,
                    'big' : 1,
                    'medium' : 2,
                    'small' : 3,                
                },
                '2' : {
                    'name' : 'Crack',
                    'total' : 5,
                    'red' : 10,
                    'orange' : 0,
                    'blue' : 4,
                    'big' : 1,
                    'medium' : 2,
                    'small' : 3,
                },
                '3' : {
                    'name' : 'Missing Head',
                    'total' : 5,
                    'red' : 10,
                    'orange' : 0,
                    'blue' : 4,
                    'big' : 1,
                    'medium' : 2,
                    'small' : 3,
                },
                '4' : {
                    'name' : 'Dent',
                    'total' : 5,
                    'red' : 10,
                    'orange' : 0,
                    'blue' : 4,
                    'big' : 1,
                    'medium' : 2,
                    'small' : 3,
                },})
        
    data['uploaded_photos'] = uploaded_photos
    return jsonify(data), 200

if __name__ == '__main__':
    app.run()