# Bright network: tech challenge
## Jonathan Pearson

## Requirements
- have `python3` & `make` installed system-wide

This enables a python venv to be created and the code executed.

## Installation & execution
- To setup, execute
```bash 
make setup
```
This will start a new python `venv` and install all dependencies.

- To run the unit test suite, execute
```bash
make test
```
- To clean up and delete the venv, execute
```bash
make clean
```


- To run the code, execute
```bash
make run
```
The code will execute and print out a list of possible job suggestions per member, ranked by a suggestion-score. The job with the top score is marked with an asterisk.
An example output includes the  following
```
Member: Marta
Bio: I'm looking for an internship in London
Suggestions: 
*  (2) Legal Internship in London
  (2) Sales Internship in London
  (1) Software Developer in London
  (1) Marketing Internship in York
  (1) Data Scientist in London
  (1) UX Designer in London
```
```
Member: Grace
Bio: I'm looking for a job in marketing outside of London
Suggestions: 
*  (1) Marketing Internship in York
```

## Design
This code submission has been optimised to showcase good coding practices, architecture, & design, rather than a rock-solid suggestion algorithm, whilst faithfully remaining inside the ~3hour development window constraint.

I have chosen a data-structure/algorithm split: python `dataclass`s are used to hold data, and functions have been written to modify or calculate on that data. This approach optmises for testing and dependency-injection, which is vital for high quality maintainable code.

I have chosen to use type-hints in functions and class-definitions. This helps readability and maintainability (since the python IDE uses these to help the coder).

### Dataloader
Each "data source" has been abstracted so that "any" source can be swapped in as needed, so long as it fulfils the contract of having a `load`-method. As an example, 
```python
class JobsDataLoader(ABC):
    @abstractmethod
    def load(self) -> Jobs:
        pass
```
and the function `new_data_jobs_loader()` in `bright.loaders.jobs` will build and return the appropriate jobs-loader-instance:
```python
def new_data_jobs_loader(source: str):
    if source == FILE_SOURCE:
        return JobsDataFromFile()
    elif source == HTTP_SOURCE:
        return JobsDataFromHTTP()
    raise Exception("unkown source: " + source)
```

 I have implemented 2 data loaders for each data: one from `http` and one from a local `json`-file.

In addition to `ABC` I have also showcased defining a `Protocol` in the `bright.matcher.report` file:
```python
class Writer(Protocol):
    def write(self, message): ...
```
Here we declare that a class can be used "as a" writer if it implements the `write` method. A function expecting a `Writer` would have its signature written as
```python
def report_matches_for_member(writer: Writer, suggestions: JobSuggestionsForMember)
```
An example of a class that can be used as a `Writer` is `sys.stdout`.

 ### Jobs matcher
 I have implemented a "first-pass" of a jobs -> member matcher in `bright.matcher.matcher`. 
 
 I noticed a few challenges in the data.  By changing all bios and job-roles to lower-case strings we can get around the issue of capitalisation; for example, the member with bio
```
I'm looking for an internship in London
```
can be easily matched up with the job role `Sales Internship`.
 
As a trickier example, the member with bio
 ```
 I'm looking for a job in marketing outside of London
 ```
 is looking for a job in a city that is NOT London. This can be detected by analysing the bio and looking for keywords like `outside`.

A significantly trickier example is the member with bio
```
I'm a software developer currently in Edinburgh but looking to relocate to London
```
Here two cities are mentioned (Edinburgh and London), but the member expresses a desire to ignore Edinburgh and focus on London. This has been detected in my code by analysing the bio and looking for key-phrases like `relocate to`.



### Job suggestion scores
Each `JobSuggestion` for a `Member` has the following properties: the `Job` and a `score` for that job. This score is supposed to be a stand-in for how "good" a match the suggestion is (I have implemented a very simple scoring system - how many words in the `Member`'s bio and in the `Job` `location` and `title` overlap). This score is only calculated on jobs that pass simple tests already

## Unit testing
I have written basic unit tests - mainly around the bio-analysis piece.

## Further work

The code and algorithm in this submission has a good number of areas for improvement:
- **test coverage**: adding more unit tests, creating service and integration tests, and if needed load-testing.
- **matching algorithm development**: is is clear that the algorithm I have constructed isnt quite able to cope with the fuzziness of actual written language. Propose to include some fuzzy-matching or NLP principles in order to capture the semantic meaning in written sentances.
- **configuration**: at the moment, the "data source" is hard-coded inside the `config.py` file. This is ok in development, but should be abstracted out to e.g., an environment variable.
- **logging**: error handling and visibility is incredibly important in a prod-ready application. A mechanism for logging choices would be pertininent to include (as well as somewhere to capture errors). Examples of centralised targets for such logs include grafana or sentry.
- **code architecture**: this could be improved to reduce coupling of dependencies. 