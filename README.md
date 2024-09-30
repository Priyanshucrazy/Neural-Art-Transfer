

Neural Art Style Transfer

**Neural Art Style Transfer** is a web application that allows users to transform their images by applying the artistic style of one image onto another. The project uses neural style transfer techniques to combine the content of one image with the artistic style of another in real-time.

## 🖼️ Features
- **Neural Style Transfer**: Apply the style of one image to the content of another using pre-trained neural networks.
- **Image Upload**: Upload both content and style images directly through the web interface.
- **Live Preview**: Preview both the content and style images before the style transfer.
- **Stylized Output**: The resulting stylized image is displayed directly on the web page once the style transfer is complete.

## 🚀 Technologies Used
- **Frontend**: 
  - HTML5, CSS3 (custom styles + Bootstrap for layout)
  - JavaScript for image preview and interactivity
- **Backend**: 
  - Flask to handle server-side routing and processing
- **Machine Learning**: Pre-trained neural networks to perform the style transfer

## 📦 Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/neural-art-style-transfer.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd neural-art-style-transfer
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask server**:
   ```bash
   python app.py
   ```

5. **Access the app** in your web browser:
   - Open `http://127.0.0.1:5000`

## 📂 Project Structure
```bash
neural-art-style-transfer/
│
├── app.py                   # Flask application and routing
├── requirements.txt          # List of dependencies
├── templates/
│   ├── layout.html           # Base layout for the web app
│   └── index.html            # Main page for image upload and style transfer
├── static/
│   ├── css/
│   │   └── custom.css        # Custom styles
│   └── js/
│       └── image_upload.js   # JavaScript for handling image preview and submission
└── README.md                 # Project documentation
```
## 🛠️ Requirements
- Python 3.x
- Flask
- Other dependencies listed in `requirements.txt`

SCREENSHOT
![Screenshot 2024-07-29 194418](https://github.com/user-attachments/assets/ee2a5402-023e-40da-8bc8-2f48fc044420)


