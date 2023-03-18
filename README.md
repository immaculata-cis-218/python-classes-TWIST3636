# CIS-218 Python Classes Lab

This is a 3 week lab. You get to design your lab (within the confines of the assignment requirements).

You will have separate submissions in Moodle for each week. Each week will have a specific focus of using Python Classes:

| Week | Focus                                     |
| ---- | ----------------------------------------- |
| 8    | [Creating your class](./lab_08.md)        |
| 9    | [Subclasses and Inheritance](./lab_09.md) |
| 10   | [Dunder/Magic Methods](./lab_10.md)       |

Your code repository's visibility has been set by Github Classroom to `public` by default for these labs. This will allow all students in the class to see the work that you are completing along with feedback from the instructor. Please feel free to share your code with your classmates in the weekly discussions.

## Examples:

These are for example purposes only. You may define your own classes and functions within the requirements of the lab

| Parent Class | Example Parent Class Functions                               |
| ------------ | ------------------------------------------------------------ |
| Athlete      | `hourly_pay` using salary and number of hours in a week      |
| Student      | `gpa` using number of courses and credits earned             |
| Person       | `working_years` using age minus retirement age               |
| Car          | `depreciation` using cost and age                            |
| Company      | `revenue_per_employee` using revenue and number of employees |
| Employee     | `hourly_pay` using salary and number of hours in a week      |
| Book         | `reading_time` given pages and reading speed                 |
| Shape        | `perimeter` of a shape adding up its sides                   |

| Parent Class | Extended Classes    | Example Extended Class Functions                        |
| ------------ | ------------------- | ------------------------------------------------------- |
| Athlete      | `Runner`            | `speed` using distance, time                            |
|              | `BaseballPlayer`    | `rbi` using hits and at-bats                            |
| Student      | `HighSchoolStudent` | `walk_time` using distance to school and walking speed  |
|              | `CollegeStudent`    | `credits_needed` using earned credits and amount needed |
| Person       | `Teacher`           | `salary` using years of tenure and base rate            |
|              | `Doctor`            | `paycheck` given hours and rate of pay                  |
| Car          | `Tesla`             | `mpg` given eMPG calculation and distance               |
|              | `Ford`              | `mpg` given fuel and distance                           |
| Company      | `TechCompany`       | `server_cost` given cost per user and usage             |
|              | `RetailCompany`     | `profit_margin` given revenue and cost                  |
| Employee     | `Manager`           | `bonus` given salary and bonus percent                  |
|              | `Sales Associate`   | `commission` given sales and commission amount          |
| Book         | `FictionBook`       | `word_count` given pages and words per page             |
|              | `NonFictionBook`    | `reading_time` given pages and readingSpeed             |
| Shape        | `Triangle`          | `area` using base and height                            |
|              | `Rectangle`         | `area` using length and width                           |
