from setuptools import setup, find_packages
setup(
    name="Task-Tracker", version="1.0.0", packages=find_packages (), install_requires=[],
    entry_points={
    "console_scripts": [
    "Task-Tracker=Task-Tracker.backend:main"
    ]
    },
    author="Cameron Thornton",
    author_email="camthornton.07@gmail.com",
    description="A simple task tracker app used to store and manage tasks.", long_description=open ("README.md") .read (),
    long_description_content_type="text/markdown", url= "https://github.com/Tazme12/Task-Tracker",
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
