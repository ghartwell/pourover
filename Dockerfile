FROM python:3
ADD pourover.py /
RUN pip install Flask flask_restful
ENTRYPOINT ["python"]
# CMD ["pourover.py -r 20"]
CMD ["pourover.py"]