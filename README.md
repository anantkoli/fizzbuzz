## Getting Started with FizzBuzz

FizzBuzzApp is a robust and production-ready application running, built on a Django server. 

It follows the classic Fizz-Buzz logic. You can use the functionality using the REST API.

## To run the application server locally follow the below steps:
1. Install git on a system to checkout the project locally.
    > If you don't have Git installed already, follow the relevant link below 
    - Check the link: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

2.	Checkout project
    - use a command to clone
    ``` 
        git clone https://github.com/anantkoli/fizzbuzz.git 
    ```
    - Check the link to clone project: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

3.	Install Docker to run the application server
    > If you don't have Docker installed already, follow the relevant link below to get
    - Windows > https://docs.docker.com/desktop/install/windows-install/
    - MacOS > https://docs.docker.com/desktop/install/mac-install/
    - Linux > https://docs.docker.com/desktop/install/linux-install/

4.	Now go to checkout project folder using cmd
    ``` 
    cd <checked_path>/fizzbuzz
    ```

5.	Run docker command on the terminal. Make sure you are inside the project folder. Wait till it build and running.
    ```
    docker-compose up -d --build fizzbuzz
    ```

6.	You can now check the container running using cmd
    - windows, macOS > ``` docker ps -a ```
    - Linux > ``` sudo docker ps -a ```

7.	Now your app is running **successfully**

## Check API documentation for more
https://docs.google.com/document/d/1Bj06jliuYRqfcmeV0r4YFrGHuFSLFi0SAA6ue8FX2hI/edit?usp=sharing

## Check the below API for reference to play:
    http://localhost:8000/fizzBuzz/get_fizz_buzz/?num1=3&num2=5&limit=40&str1=fizz&str2=buzz
    http://localhost:8000/fizzBuzz/get_stats/

## Third-party libraries use
1.	Docker: 
    - Use to set up the server/application in an isolated container so it will not affect the current environment while running the application. It will maintain the needed environment for applications running on any system. 
    - Use the link to learn more > https://docs.docker.com/guides/get-started/
2.	Gunicorn: [link](https://docs.gunicorn.org/en/stable/)
    - It is a python WSGI HTTP server. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.
    - It provides a perfect balance of performance, flexibility, and configuration simplicity.
    - Communicating with multiple web servers.
    - Reacting to lots of web requests at once and distributing the load.
    - Keeping multiple processes of the web application running
3.	Django: [link](https://docs.djangoproject.com/en/5.0/)
    - Is a back-end server-side web framework.
    - Django is free, open source and written in Python.
    - Django makes it easier to build web pages using Python.
4.	Pytest: [link](https://docs.pytest.org/en/7.4.x/)
    - Pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

