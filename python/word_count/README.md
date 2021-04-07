Example based on https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

## Run Mapper
```shell
echo 'hello testing one two two three three three hello' \
 | pipenv run python python/word_count/mapper.py \
 | sort
```

Output:
```
hello   1
testing 1
one     1
two     1
two     1
three   1
three   1
three   1
hello   1
```

## Run Map/Reduce
```shell
echo 'hello testing one two two three three three hello' \
 | pipenv run python python/word_count/mapper.py \
 | sort \
 | pipenv run python python/word_count/reducer.py
```

Output:
```
hello   2
one     1
testing 1
three   3
two     2
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