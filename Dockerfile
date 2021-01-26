FROM python:3.6
LABEL maintainer="Maya Teperman"
COPY app/ .
RUN pip install requests flask
EXPOSE 8787
ENTRYPOINT ["python"]
CMD ["app.py"]