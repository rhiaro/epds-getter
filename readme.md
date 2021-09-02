# Environmental Permits Data Service: data getter

## Dev notes

Currently just loads from local CSV files into postgres tables.

Different registers have different fields (see samples in `tmpdata`).

Build:

```
$ docker-compose build .
```

(rebuild if you add new dependencies)

Run:

```
$ docker-compose up -d
```

Then to just keep a terminal up:

```
$ docker-compose exec getter /bin/bash
```

Or run specific CLI commands:

```
$ docker-compose run getter epdsgetter get
$ docker-compose run getter epdsgetter count
```