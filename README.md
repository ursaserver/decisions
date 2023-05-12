## Name

A decision file name matches the regular expression

```
MATCHER = re.compile('\d{4}[A-Z]-[a-z]+\.md')
```

written in `Python  3.10.10`. A minimal driver program to provide file name checker is available [here](./code/filename_matcher.py).

Any file that matches this format is a decision files.

## Requirements / Format

Decision files obey the followings:

1. Every decision file has a conclusion at the bottom with the summary of that decision.
