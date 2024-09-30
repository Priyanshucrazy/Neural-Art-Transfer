Neural Art Style Transfer
Neural Art Style is a web application that allows users to transform their images by applying the artistic style of one image onto another using neural style transfer. This project provides an interactive platform where users can upload a content image and a style image, then apply the style of the latter to the former in real-time.

Features
Neural Style Transfer: Combines the artistic features of one image (style image) with the structural features of another (content image).
Image Upload: Users can upload both content and style images directly through the web interface.
Live Preview: After uploading images, users can preview their selected content and style images.
Stylized Output: The resulting stylized image is displayed directly on the web page once the style transfer is complete.
Technologies Used
Frontend:
HTML5, CSS3 (custom styles + Bootstrap for layout)
JavaScript for image preview and interactivity
Backend:
Flask to manage routing and server-side processing
Neural Networks: Pre-trained neural network models for performing the style transfer.
Installation and Setup
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/artsy-style-transfer.git
Navigate to the project directory:
bash
Copy code
cd artsy-style-transfer
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Run the Flask server:
bash
Copy code
python app.py
Access the application in your browser at http://127.0.0.1:5000.
Project Structure
app.py: The Flask application for handling routes and rendering templates.
templates/layout.html: Base layout for the web application.
templates/index.html: Main page for users to upload images and apply style transfer.
static/: Contains static assets including custom CSS and JavaScript files.
