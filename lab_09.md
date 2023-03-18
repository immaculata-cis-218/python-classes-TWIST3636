# Week 9: Subclasses and Inheritance

## Lab Requirements

1. Practice Test Driven Development (TDD) by creating your tests as you create your code. Tests are a requirement of all submissions and test coverage is checked in your pull request submissions.

2. Share your work in Moodle under `Discussion 9B: Lab 9 - Share your work` and provide a link to your Github repository in the body of your discussion.

   If you are having issues during completion of the lab, feel free to commit and push your branch to Github and share with your classmates what is not working correctly in the discussion.

3. Add two classes which extend the `class` you previously created in [main.py](./main.py). See the [example extended classes](./README.md#Examples) for ideas.

4. For each of the classes that you have extended, add a new function to each that is specific to that class. See the [example extended class functions](./README.md#Examples) for ideas.

5. Each of the 2 new functions should set an attribute on the class (e.g `self.attribute = something`).

6. Open your terminal window and type the following to review your python file for linting issues:

   _Linux / macOS_

   ```
   pylint main.py
   ```

   _Windows_

   ```
   py -m pylint main.py
   ```

   For this lab, a pylint score of at least 8.0/10 is required. If your code rates lower than this, please make changes to your code to address the issues. [Documentation on the pylint error codes](https://pylint.pycqa.org/en/latest/user_guide/messages/messages_overview.html) will provide you with examples of how to resolve specific issues.

7. Your program should also be written efficiently, and code should be easy to read and review.

8. Commit your code and push. Then create a pull request and upload the URL of the pull request to the Moodle lab.

   Your Github pull request has also been configured to automatically run `pytest` and `pylint` against your code for your convenience.

   Please do not merge the pull request as this will be done when the professor reviews your code.

## Grading

| Points | Location        | Criteria                                |
| ------ | --------------- | --------------------------------------- |
| 5      | main.py         | 2 Classes extend the parent class       |
| 10     | main.py         | 2 Functions on the extended classes     |
| 5      | main.py         | Functions set a class attribute         |
| 10     | pytest coverage | Tests cover all aspects of main.py      |
| 10     | pylint          | Pylint score >= 8.0.                    |
|        | instructor      | Code style, efficiency, and readability |
