FROM python:3-onbuild

EXPOSE 5000

CMD ["python3", "./test_simple.py"]
