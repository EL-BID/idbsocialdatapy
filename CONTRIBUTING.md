### To effectively contribute to this package code base, below are some guidelines to help you set up your development enviroment:

The first step will be to clone this repository, and after that, follow the steps below in order.


1. Create a new virtual environment with `venv`
```bash
python -m venv env
```

2. Then, activate it.

**On Linux:**
```bash
source ./env/bin/activate
```
**On Windows Powershell:**
```powershell
.\env\Scripts\Activate.ps1
```
3. Make sure you have the latest pip version on your virtual environment to avoid errors on the next steps.
```bash
python -m pip install --upgrade pip
```
4. Install the required packages.
```bash
pip install -e ."[dev,test]"
```
5. This library uses several tools to ensure a consistent code format throughout the project, to automatically run all these tests we make use of `pre-commit`,
which you can install running the following command
```bash
pre-commit install
```

### Commiting Guidelines

To maintain a proper documentation of how the project is evolving and to help the automatic versioning of this package,
commit messages must have the following structure:
```
<type>(optional scope): short summary in present tense

(optional body: explains motivation for the change)

(optional footer: note BREAKING CHANGES here, and issues to be closed)
```
`<type>` refers to the kind of change made and is usually one of:

* `feat`: A new feature.
* `fix`: A bug fix.
* `docs`: Documentation changes.
* `style`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc).
* `refactor`: A code change that neither fixes a bug nor adds a feature.
* `perf`: A code change that improves performance.
* `test`: Changes to the test framework.
* `build`: Changes to the build process or tools.

`scope` is an optional keyword that provides context for where the change was made. It can be anything relevant to your package or development workflow
(e.g., it could be the module or function name affected by the change).
