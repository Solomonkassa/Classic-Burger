## Classic-Burger Flask Web App
A Restaurant Web Application with **Table Booking, Online Food Ordering and Delivery Tracking.**<br/>
<p align="center">
 <a href="https://github.com/Solomonkassa/Jedan-Care"><img alt="Github" src="https://img.shields.io/static/v1?logo=github&color=blueviolet&label=Test&message=Passing"/></a> <a href="LICENSE"><img alt="License" src="https://img.shields.io/static/v1?logo=GPL&color=Blue&message=GPL-v3&label=License"/></a> <a href="https://pypi.org/project/smartbetsAPI"><img alt="PyPi" src="https://img.shields.io/static/v1?logo=pypi&label=Pypi&message=v1.1.4&color=green"/></a> <a href="#"><img alt="Accuracy" src="https://img.shields.io/static/v1?logo=accuracy&label=Accuracy&message=55%&color=critical"/></a> <a href="#"><img alt="Passing" src="https://img.shields.io/static/v1?logo=Docs&label=Docs&message=Passing&color=green"/></a> <a href="#"><img alt="coverage" src="https://img.shields.io/static/v1?logo=Coverage&label=Coverage&message=85%&color=yellowgreen"/></a>  <a href="#" alt="progress"><img alt="Progress" src="https://img.shields.io/static/v1?logo=Progress&label=Progress&message=35%&color=green"/></a>  <a href="https://pepy.tech/project/smartbetsapi"></a></p><br>
 
# Brief Description
Classic-Burger is a web-based application that is operated on a web server with its data being retained in a database. It is designed to enable the registered customer to reserve a table at the restaurant at a specified time in accordance with its availability, view and order the offered food item of their choice, and track the delivery of their order. <br/> 
Since the Internet provides a wider range of customers, the application will provide the restaurant with a chance to increase their profits while customers can avail the restaurant's services at the comforts of their homes.



🍔 A mouthwatering web application built with Flask for ordering and enjoying classic burgers online.

🚀 Features:
- Browse a delicious menu of classic burger options.
- Customize your burger with a variety of toppings and ingredients.
- Place orders securely and conveniently.
- Real-time order tracking for customers.
- Admin panel for managing orders, menu items, and user accounts.
- Responsive and user-friendly design for seamless ordering on any device.

🔧 Technologies:
Python, Flask, SQLAlchemy, HTML/CSS, JavaScript, Bootstrap, SQLite

📝 Instructions:
1. Clone this repository.
2. Install the required dependencies.
3. Run the Flask app.
4. Start enjoying classic burgers online


# How to install our project <br/>

First, clone this repository and create a virtual environment using:
```
python -m venv venv
```
Activate the virtual environment:
```
./venv/Scripts/activate
```
Install the required packages using: <br/>
```
pip install -r requirements.txt
```

Create an Authy Application and grab your API Key https://www.twilio.com/console/authy/applications <br/>
Edit `config.py` and update the API key with your application key. Create a secret key for managing sessions. <br/>

`cd` to the location of the cloned repository and run the command:
```
python run.py
```
Copy `http://127.0.0.1:5000/` and paste it in the address bar of a browser.

# Working of our Website 
The front-end portion of the web application has been developed using **HTML, CSS & JavaScript** while the backend portion has been developed using **Flask & SQLite**. The information regarding the users, food items, tables and orders are stored in a database created using **SQLite**. Through the use of **Flask**, the web app interacts with the database. To verify the user's phone number, we have used **Twilio Authy API** and the delivery tracking has been implemented using **Google Maps Javascript API** and **Google Directions API**

🤝 Contributions:
Contributions and bug reports are welcome! Feel free to fork and submit pull requests.

📄 License:
This project is licensed under the MIT License.

🌐 Live Demo:
[Link to Live Demo](https://classic-burger.onrender.com/)



### Home Page
![home-page](https://github.com/Solomonkassa/Classic-Burger/blob/main/resources/home.png)

### Registration Page
![register](https://github.com/Solomonkassa/Classic-Burger/blob/main/resources/sign_up.png)

### Phone Number Verification
![otp page]()

### Login Page
![login](https://github.com/Solomonkassa/Classic-Burger/blob/main/resources/log_in.png)


### Services Page
![services](https://github.com/Solomonkassa/Classic-Burger/blob/main/resources/services.png)


### Menu Page
![menu](https://github.com/Solomonkassa/Classic-Burger/blob/main/resources/menu.png)

### Cart Page
![cart](https://github.com/Solomonkassa/Classic-Burger/blob/main/resources/cart.png)

### Order Confirmation Page
![congrats](https://github.com/Solomonkassa/Classic-Burger/blob/main/resources/congrats.png)

### Delivery Tracking Page
![order-id-page](https://github.com/Solomonkassa/Classic-Burger/blob/main/resources/06.09.2023_15.40.12_REC.png)


### About Us Page
![about-us](https://github.com/Solomonkassa/Classic-Burger/blob/main/resources/about.png)



# Developed by: <br/>
- [Solomon Kassa](https://github.com/Solomonkassa/)


If you would like to make any suggestions to improve the web application, feel free to contact any of the developers.

📌 Explore the Code:
Check out the source code and get started with classic burger ordering today!
