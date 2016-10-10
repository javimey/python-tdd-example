FROM python:3-onbuild
RUN \
	apt-get update \
	&& apt-get --yes install

RUN pip install coverage

EXPOSE 5000

CMD ["python3", "./test_name_formatter.py"]
