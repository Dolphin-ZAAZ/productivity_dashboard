from setuptools import setup, find_packages

setup (
    name= "Productivity Dashboard",
    version= "1.0",
    description= "A dashboard for custom productivity tools.",
    author="Me",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    pyhton_requires={">=3.7"},
    entry_point={
        "gui_scripts": [
            "dashboard = main:main",
        ],
    }
)