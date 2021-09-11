
<h1 align="center">Welcome to Storeify 👋</h1>
<p>
</p>

> Storeify is an online ecommerce website built with Python/Django and Bootstrap. An ecommece with Registration, Login with Token Based Verification & Message Alerts. Reset Password with Secure Validation Links. Cart Checkout, automatically assign the Cart Items to Logged-in User.

## Status
In Development 🚧 

## Requirements
- Python 3+
- Pip

## Running this project localy

To get this project up and running clone this repository and you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env or python3 -m venv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```
Activate Virtual Enviroment Windows:

```
.\venv\scripts\activate
```

Then install the project dependencies with

```
pip install -r requirements.txt
```
Migrate the Database:
```
python manage.py migrate
```

Create SuperUser:
```
python manage.py createsuperuser
```

Now you can run the project with this command

```
python manage.py runserver
```


## Author

👤 **Ibrahim Ramadhan**

* Website: ibby360.me
* Github: [@ibby360](https://github.com/ibby360)

## Inspiration

This project is based on the goal of improving my skills as a Self-taught enthusiast and the best way to improve is by building projects. I wanted to gain a deeper understanding of Django and Object-oriented programming in Python. I have learnt different technologies for the project and I keep on learning new skills as I add new features to the project.

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/ibby360/edupty/issues). You can also take a look at the [contributing guide](https://github.com/ibby360/edupty/blob/master/CONTRIBUTING.md).

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_