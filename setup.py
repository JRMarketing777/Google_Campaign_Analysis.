from setuptools import setup, find_packages

setup(
    name="campaign_analyzer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "tkinter",
    ],
    entry_points={
        "console_scripts": [
            "campaign_analyzer=campaign_analyzer.app:main",
        ],
    },
)

