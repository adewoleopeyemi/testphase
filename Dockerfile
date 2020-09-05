FROM continuumio/anaconda3
COPY . /usr/app
EXPOSE 5001
WORKDIR /usr/app/
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["flask_api.py"] 