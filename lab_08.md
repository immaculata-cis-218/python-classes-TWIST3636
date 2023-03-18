# Week 8: Creating your class

## Lab Requirements

1. Practice Test Driven Development (TDD) by creating your tests as you create your code. Tests are a requirement of all submissions and test coverage is checked in your pull request submissions.

2. Determine the theme of your `class`.

   - This should ideally reflect a person, place, or thing and you will want to keep this as generic as possible since you will be extending this functionality to other classes. See the [example parent classes](./README.md#Examples) for ideas.

   - The theme of your class should not duplicate what your classmates are creating.

   - Add the class to the title of your post in Moodle under `Discussion 8B: Lab 8 - Share your work` and provide a link to your Github repository in the body of your discussion.

   - If you are having issues during completion of the lab, feel free to commit and push your branch to Github and share with your classmates what is not working correctly in the discussion.

3. Create your `class` in [main.py](./main.py)

4. Add a protected variable that is set when the class is initiated and is an input to the `__init__` method.

5. Add a function to your class which uses your protected variable and then uses that to compute a value.

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

| Points | Location        | Criteria                                    |
| ------ | --------------- | ------------------------------------------- |
| 10     | main.py         | Protected variable set when class initiated |
| 10     | main.py         | Function that uses protected variable       |
| 10     | pytest coverage | Tests cover all aspects of main.py          |
| 10     | pylint          | Pylint score >= 8.0.                        |
|        | instructor      | Code style, efficiency, and readability     |
