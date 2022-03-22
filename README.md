# Three Word Sequence Seeker

**Purpose**: Accept a file name(s), or content from stdin, and produce a list of the most common three-word sequence. 

## Usage
This assumes Python 3.x as Python 2.x is well past the end-of-life date.
```sh
# Ensure pep8 is available
$ pip -r requirements.txt
# Launch the demo script
$ python3 run_me.py moby-dick.txt
```
Example Output (top 5 lines):
> the sperm whale - 86 \
> of the whale - 78 \
> the white whale - 71 \
> one of the - 64 \
> of the sea - 57

## Tests
### Manual Testing
```sh
# Ensure pep8 is available
$ pip -r requirements.txt
# Launch the demo script
$ python3 -m unittest test
```
Example Output:
> \.\.\.\.\. \
> ---------------------------------------------------------------------- \
> Ran 5 tests in 0.919s \
> \
> OK

### Tests Covered
1. Verify that 100 results are returned using stdin
2. Verify the second result is exactly as expected using stdin
3. Verify that 100 results are returned using file reading
4. Verify the third result is exactly as expected using file reading
5. Verify pep8 compliance
