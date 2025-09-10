# Grader Analyser

Grader Analyser is a tool designed to automate and streamline the process of grading student assignments, exams, or projects. By analyzing submissions and providing detailed feedback, Grader Analyser helps educators save time and maintain consistency in their grading workflow.

## Features

- **Automated Grading:** Quickly assess student submissions based on customizable rules and rubrics.
- **Detailed Reports:** Generate comprehensive feedback for each student, highlighting strengths and areas for improvement.
- **Flexible Input:** Supports various file formats (CSV, Excel, PDF, etc.) and integrates with popular LMS platforms.
- **Customizable Rubrics:** Easily create or modify grading rubrics to fit different assignments or courses.
- **Analytics Dashboard:** Visualize grading trends, average scores, and common mistakes across the class.
- **Export Results:** Export grades and feedback in multiple formats for easy sharing and record-keeping.

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/grader-analyser.git
cd grader-analyser
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare your grading rubric:** Edit or create a rubric file according to your assignment's requirements.
2. **Collect student submissions:** Ensure all files are organized in a directory.
3. **Run the analyser:**

```bash
python grader_analyser.py --submissions ./submissions --rubric ./rubric.json
```

4. **View results:** Check the generated reports in the `output/` directory.

## Configuration

- Edit `config.yaml` to set up custom grading parameters.
- Rubrics can be defined in `rubric.json` (sample provided).

## Example

```bash
python grader_analyser.py --submissions ./midterm_submissions --rubric ./midterm_rubric.json
```

## Contributing

Contributions are welcome! Please open issues for bugs or feature requests, and feel free to submit pull requests.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes
4. Open a pull request

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact [lekhrajsinghsolanki@7773gamail.com].

---

