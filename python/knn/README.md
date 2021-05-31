Perform a classic k-nearest neighbour computation in a map/reduce style

## KNN Algorithm for Classification

Given
- `k`, a number of neighbours to consider
- `D`, a dataset of examples
- `x`, an unseen datum to classify
- `dist(a, b)`, a distance function (like Euclidian distance)

Then:

- for each example in `D`
  - calculate the distance `dist(x, example)`
  - sort the dataset by the calculated distances
  - return the majority class of the nearest `k` distances

## Run Mapper
```shell
cat python/knn/iris.data \
 | pipenv run python python/knn/mapper.py 4.7,3.2,1.3,0.2 \ # where we specify the new point to classify
 | sort
```

Output:
```
Iris-setosa     0.0
Iris-setosa     0.2000000000000004
Iris-setosa     0.2999999999999998
Iris-setosa     0.30000000000000004
Iris-setosa     0.3999999999999999
...
```

## Run Map/Reduce
```shell
cat python/knn/iris.data \
 | pipenv run python python/knn/mapper.py 4.7,3.2,1.3,0.2 \
 | sort \
 | pipenv run python python/knn/reducer.py
```

Output:
```python
Iris-setosa     [0.0, 0.2000000000000004, 0.2999999999999998, 0.30000000000000004, 0.3999999999999999]
Iris-versicolor [3.8, 4.0, 4.5, 4.6, 4.6000000000000005]
Iris-virginica  [5.6000000000000005, 6.6, 6.7, 6.800000000000001, 6.800000000000001]
```

## Run Map/Reduce/Map
```shell
cat python/knn/iris.data \
 | pipenv run python python/knn/mapper.py 4.7,3.2,1.3,0.2 \
 | sort \
 | pipenv run python python/knn/reducer.py \
 | pipenv run python python/knn/mapper_2.py
```
Output:
```
0.0     Iris-setosa
0.2000000000000004      Iris-setosa
0.2999999999999998      Iris-setosa
0.30000000000000004     Iris-setosa
0.3999999999999999      Iris-setosa
3.8     Iris-versicolor
4.0     Iris-versicolor
...
```

## Run Map/Reduce/Map/Reduce

Produces the final classification

```shell
cat python/knn/iris.data \
 | pipenv run python python/knn/mapper.py 4.7,3.2,1.3,0.2 \
 | sort \
 | pipenv run python python/knn/reducer.py \
 | pipenv run python python/knn/mapper_2.py \
 | sort \
 | pipenv run python python/knn/reducer_2.py
```

Output: 5/5 say setosa
```python
[('Iris-setosa', 5)]
```

## A Different Example to Classify

```shell
cat python/knn/iris.data \
 | pipenv run python python/knn/mapper.py 1,2,3,4 \
 | sort \
 | pipenv run python python/knn/reducer.py \
 | pipenv run python python/knn/mapper_2.py \
 | sort \
 | pipenv run python python/knn/reducer_2.py
```

Output: 3/5 say versicolor
```python
[('Iris-versicolor', 3)]
```

