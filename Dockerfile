FROM openjdk:11

WORKDIR /hadoop

RUN wget -q -O hadoop.tar.gz https://apache.mirrors.nublue.co.uk/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz \
  && tar xzf hadoop.tar.gz \
  && rm hadoop.tar.gz

RUN ln -s hadoop-3.3.0 hadoop-dist

RUN apt-get update \
  && apt-get install -y python3.7 \
  && ln -s python3.7 /usr/bin/python3

ENTRYPOINT ["hadoop-dist/bin/mapred", "streaming"]