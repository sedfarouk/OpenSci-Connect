<img src="https://i.imgur.com/cEGtEzn.png" alt="MLH-banner" width="100%" height="200px">

# CollabSpace: Nasa International Space Apps Challenge

## 🚀 About the Team

Welcome to the **ScriptSages**!

At our core, we are more than just software developers. We are a passionate group of open-source advocates, forward-thinking innovators, and problem-solvers. Our deep understanding of the challenges in the open science community has led us to create a revolutionary solution. Our platform, CollabSpace, is not just a networking tool—it's a catalyst for transformative scientific collaborations.

**Our Vision:** A thriving marketplace for open science projects, where project creators can seamlessly find the skilled talent they need, and contributors can find meaningful projects to support.

## 🌌 About the Challenge

The open science community is flooded with projects and potential contributors. However, a major bottleneck exists: the difficulty in efficiently connecting project creators with apt contributors. Our solution, developed for the Nasa International Space Apps Challenge, aims to bridge this gap, creating a platform where open-source innovation flourishes.

## 💻 Installation and Running Instructions

1. **Setting up the environment:**
   ```bash
   pip install django
   pip install scikit-learn
   ```

If working with an IP or API(NASA API) (e.g., for making requests):

```bash
pip install django
```

## Instructions

1. Run the server:
   ```bash
   python manage.py runserver
   ```
2. Setting up a User Account:
   To create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

   After creation, visit the path /admin to access the admin panel.

3. Git Commands for Collaboration:
   Pushing changes to a branch:
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin your_branch_name
   ```
   Post-push, switch back to the main branch:

```bash
 git checkout main
```

Pulling changes from a branch:

```bash
 git pull origin branch_name
```

## 🌠 Project Highlights

- Web-based Solution: Developed using the Django template, our platform is user-friendly, allowing easy account setups, skill-project matching, and integrated messaging.
- NASA Integration: We've incorporated NASA's APIs such as APOD, EPIC, and Mars rover images to motivate users and enhance the platform's appeal.
- AI-Powered Recommendations: Our platform uses scikit-learn, a Python machine learning library, to offer users personalized project recommendations based on their profiles and preferences.
- Rapid Development: Our choice of Django for both frontend and backend ensured we could build a robust solution within the limited timeframe of the hackathon.

## 🎥 Video Presentation

link =

## 🔗 Links & Resources

- Tech With Tim Django For Beginners - Full Tutorial: https://www.youtube.com/watch?v=sm1mokevMWk
- Programming with Mosh Python Django Tutorial for Beginners: https://www.youtube.com/watch?v=rHux0gMZ3Eg
- Python Programming Tutorials Python Programming tutorials from beginner to advanced on a massive variety of topics. All video and text tutorials are free.: https://pythonprogramming.net/jinja-templates-django-python-tutorial/
- Tutorials A complete list of free Django tutorials covering best practices, APIs, deployment, authentication, testing, search, and more: https://learndjango.com/tutorials/
- Problem Solving Point How to display Data from any API in Django template | using Requests: https://www.youtube.com/watch?v=sgEhb50YSTE
- api.nasa.gov: https://api.nasa.gov/

## 📜 Conclusion

CollabSpace is more than just a platform—it's the future of open science collaboration. By creating an ecosystem where innovators and contributors can effortlessly come together, we believe that the boundaries of innovation will be pushed even further. Join us in this revolutionary journey and be part of the open science transformation.

# OpenSci-Connect

A web app built during the NASA Space Apps Challenge to help connect users' projects with collaborators with the necessary skills
