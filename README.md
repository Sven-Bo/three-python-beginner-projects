# 3 Python Beginner Projects

Python is an in-demand language for beginning programmers. It's easy to learn, with many modules and libraries available. This article is part of the following [YouTube Video (will follow soon)](https://youtube.com/c/codingisfun). In the YouTube video, I will introduce three beginner Python projects with source code. These projects are perfect for learning the basics of this powerful language.
Therefore it is recommended that you first watch the video and then come back to this article.  

## 1. Create a GUI application using `PySimpleGUI`

Creating a GUI application is a great way to learn the basics of Python programming. You can use many different libraries to create GUI applications, such as Tkinter, Qt, and wxPython. Each library has its own strengths and weaknesses. My all-time favourite library for building GUI's is `PySimpleGUI`.
I suggest creating a program you found helpful and fun to use. This could be a YouTube downloader, PDF merger app, database entry form, or anything you could think of.
To get started, you can also check out some videos on my YouTube channel, where I am coding out an entire GUI and explaining every line of code.

- Word Data Entry Form: https://youtu.be/fziZXbeaegc
- Excel Data Entry Form: https://youtu.be/svcv8uub0D0
- Excel 2 CSV Convert: https://youtu.be/LzCfNanQ_9c

### Do you need more inspiration? 💡

`PySimpleGUI` comes with tons of demo applications.
To view all demos:

- Run `pip install psgdemos` in your terminal
- Afterwards, run `psgdemos.`

There are also many interactive online demos available. You can find them [HERE](https://pysimplegui.trinket.io/demo-programs#/demo-programs/intro-to-this-page)

## 2. Build & deploy a WebApp

When you want to build a web app, you might think you need to learn HTML, CSS & Javascript. Yet, you can also create an entire web application in pure Python using streamlit. Streamlit is primarily designed to turn your data scripts into shareable web apps. However, you are not limited to only building a front end for your machine or deep learning model. You could also use streamlit to create a digital resume or personal website or turn your Excel sheet into an interactive Dashboard. You can find the individual tutorials here.

- Digital Resume: https://youtu.be/BXAeMICmUSQ
- Personal website: https://youtu.be/VqgUkExPvLY
- Sales Dashboard: https://youtu.be/Sb0A9i6d320

### Are you up for some real nerdy stuff? 🤓
Perhaps you do not know it, but you can request a copy of your personal Tinder data. The data includes all your messages, your swiping behaviour and much more. How about using that data to build a dashboard with all the insights you gathered from the data?
To get started, here are a couple of useful links:  

- Request a copy of your Tinder data: [CLICK HERE](https://www.help.tinder.com/hc/en-us/articles/115005626726-How-do-I-request-a-copy-of-my-personal-data-)
- A basic tutorial on analyzing your Tinder data: [CLICK HERE](https://medium.com/analytics-vidhya/tinder-data-54ba494e0a59)
- Get some inspiration on what you could visualize: https://tinderinsights.com/

## 3. Build your personal newsletter

When I started learning Python, this was one of the most fun projects: Building a personal newsletter! The idea is simple: Schedule a Python script that sends you all the information that interests you every morning per email. That could be as simple as retrieving and sending you every morning the current weather, your to-do's for today and a useless fact. You could scrape the information from various websites before sending it in a compact email to yourself. Or you could leverage the services from multiple APIs to build your unique email.
To get you started, I have built a very simple newsletter for you. You can find the script here:

- [EMAIL NEWSLETTER CODE](/personal_newsletter/EMAIL_VERSION/main.py)

Yet, I would encourage you to build your very own email newsletter. Once you have created your email, you want to schedule it on a server. An easy & free way to schedule your Python scripts is to use deta. On my channel, I already have a tutorial on scheduling email scripts. You can find the video here:

- [YOUTUBE TUTORIAL SCHEDULING EMAILS ONLINE](https://youtu.be/OLrC4J2-pvk)

### Do you want to take it to the next level? 🚀

Instead of an email, you could also send our morning message directly to your Smartphone using the free messenger app `LINE`. You might have never heard about `LINE` before. `LINE` is the No. 1 messenger app in Japan. The functionalities are similar to WhatsApp, yet `LINE` offerers a free developer API. That means you can programmatically send images, text, videos, and emojis. In addition, `LINE` has an SDK for Python that makes it easy to develop bots using their API. With the SDK, you can create a sample bot within minutes.
You can find the `LINE` Messaging API SDK for Python here:

- [EMAIL NEWSLETTER CODE](https://github.com/Sven-Bo/three-python-beginner-projects/blob/master/personal_newsletter/EMAIL_Version/main.py)

To get you started, I have also created a sample project for you here:

- [LINE NEWSLETTER CODE](https://github.com/Sven-Bo/three-python-beginner-projects/blob/master/personal_newsletter/LINE_Version/main.py)