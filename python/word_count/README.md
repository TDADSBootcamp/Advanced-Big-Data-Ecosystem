Example based on https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

## Run Mapper
```shell
echo 'kitten puppy kitten puppy kitten kitten kitten' \
 | pipenv run python python/word_count/mapper.py \
 | sort
```

Output:
```
kitten  1
kitten  1
kitten  1
kitten  1
kitten  1
puppy   1
puppy   1
```

## Run Map/Reduce
```shell
echo 'kitten puppy kitten puppy kitten kitten kitten' \
 | pipenv run python python/word_count/mapper.py \
 | sort \
 | pipenv run python python/word_count/reducer.py
```

Output:
```
kitten  5
puppy   2
```

# War of the Worlds

Words in ["War of the Worlds" by H. G. Wells](http://www.gutenberg.org/ebooks/36), ordered by most frequent last

```shell
cat python/word_count/war_of_the_worlds.txt \
 | pipenv run python python/word_count/mapper.py \
 | sort \
 | pipenv run python python/word_count/reducer.py \
 | sort -k2 -n
```