

from setuptools import find_packages, setup




setup(
    name="imghst",
    version="0.0.1",
    author="Mustafa Mohamed",
    author_email="ms7mohamed@gmail.com",
    description="A simple and fast image hoster for applications like ShareX.",
    long_description="A simple and fast image hoster for applications like ShareX.",
    long_description_content_type="text/markdown",
    url="https://github.com/ms7m/imghst",
    python_requires=">=3.6.0",
    packages=find_packages(
        exclude=["testing", "*.testing", "*.testing.*", "testing.*"]
    ),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "imghst = imghst.app.entry:entry"
        ]
    },
    include_package_data=True,
    install_requires=[
        "aiofiles==0.6.0",
        "click==7.1.2",
        "fastapi==0.61.1",
        "filetype==1.0.7",
        "h11==0.11.0",
        "loguru==0.5.3",
        "pydantic==1.7.1",
        "python-multipart==0.0.5",
        "six==1.15.0",
        "starlette==0.13.6",
        "typing-extensions==3.7.4.3",
        "uvicorn==0.12.2",  
    ])
