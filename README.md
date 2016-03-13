# Integer Server

A web application which serves integers sequences. The following API endpoints are available:

- `/sequences/{sequence_name}/{n}` should return the `n`th term of `sequence_name`;

**/sequences/fibonacci/6**

```json
{"nth_term": 8}
```
- `/sequences/{sequence_name}/first/{n}` should return the first `n` terms, in order, of `sequence_name`.

**/sequences/fibonacci/first/6/**
```json
{"first_terms": [0, 1, 1, 2, 3, 5]}
```

The app supports the following sequences:

- [The fibonacci sequence](https://oeis.org/A000045)
- [Happy numbers](https://oeis.org/A007770)
- [Abundant numbers](https://oeis.org/A005101)
- [Sphenic numbers](https://oeis.org/A007304)
- [The Baum-Sweet sequence](https://oeis.org/A086747) 


To install just run:

pip install -r requirements.txt
