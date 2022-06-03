# ResumeParser
A simple Resume Parser used for extracting information from Resumes/CVs


# Installation

```bash
pip install pyresparser
```

# GUI

- Django used
- Easy extraction and interpretation using GUI
- For running GUI execute:

```bash
python resume_parser/manage.py makemigrations
python resume_parser/manage.py migrate
python resume_parser/manage.py runserver
```

- Visit `127.0.0.1` to view the GUI

# Working:

![Working](results/resume_parser_result.png)

# Running app in Docker

- Install docker-compose
- Execute the following commands from the root of the project
    - Build our images

        `docker-compose build`

    - Starting our containers and services

        `docker-compose up -d`

- Visit `localhost:8080` in your browser to run the app

# Result

The module would return a list of dictionary objects with result as follows:

```
[
    {
        'education': [('B Tech', '2022')],
        'email': 'nirala161@gmail.com',
        'mobile_number': '9708387178',
        'name': 'Raushan Kumar',
        'skills': [
            'NLP',
            'Django',
            'Mysql',
            'C',
            'Machine learning',
            'C++',
            'DSA',
            'Algorithms',
            'Github',
            'Php',
            'Python',
            'Robotics'
        ]
    }
]
```

# To DO

- [x] Extracting Experience
- [ ] Extracting Projects
- [ ] Extracting hobbies
- [ ] Extracting universities
- [ ] Extracting month of passing
- [ ] Extracting Awards/ Achievements/ Recognition

# References that helped me get here


- [https://www.analyticsvidhya.com/blog/2017/04/natural-language-processing-made-easy-using-spacy-%E2%80%8Bin-python/](https://www.analyticsvidhya.com/blog/2017/04/natural-language-processing-made-easy-using-spacy-%E2%80%8Bin-python/)

- [https://medium.com/@divalicious.priya/information-extraction-from-cv-acec216c3f48](https://medium.com/@divalicious.priya/information-extraction-from-cv-acec216c3f48)
