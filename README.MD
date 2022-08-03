Screenplay Parser is a rule-based parser to parse the data from screenplays for your NLP project. 
How to use it:

```python
script=Screenplay.read_txt('file.txt')
```

Accessing the dictionary. 

#### Pages of a Script.
Start with `1`.
```python
script[1]
```

#### Dialog in the Scene. 
Characters and their lines.
```python
script[1]['dialog']
script[1]['dialog']['JOHN']
```

The number of the characters in the scene woun't necessarily match
because of the same chacter can be written more times e.g.: `John` or `John (OS)`
```python
len(script[1]['dialog'])
```

#### Interior, Exterior or Both.
```python
script[1]['int_ext']
```

#### Time of Day.
```python
script[1]['tod']
```
#### Transitions.
If there aren't any transition, returns empty list.
```python
script[1]['transitions']
```

#### Location.
```python
script[1]['location']
```
#### Action Description of a Scene.
```python
script[1]['action']
```