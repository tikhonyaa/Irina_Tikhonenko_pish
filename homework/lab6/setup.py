from setuptools import setup, find_packages

setup(
    name="lab6",
    version="0.1",
    author="Тихоненко Ирина",
    author_email="your_email@example.com",
    description="Описание проекта",
    packages=find_packages(),
    install_requires=[
        "requests>=2.20.0",  # Пример зависимости
        "numpy>=1.18.0"
    ],
    entry_points={
        "console_scripts": [
            "lab6=lab6.main:main",  # Создание командной строки
        ],
    },
)