import os
import re
from pathlib import Path

import requests

PROGRAMMING_LANGUAGES = {
    "c++": "cpp",
    "cpp": "cpp",
    "java": "java",
    "python": "python",
    "py": "python",
    "python3": "python3",
    "py3": "python3",
    "c": "c",
    "c#": "csharp",
    "cs": "csharp",
    "csharp": "csharp",
    "javascript": "javascript",
    "js": "javascript",
    "ruby": "ruby",
    "rb": "ruby",
    "swift": "swift",
    "go": "golang",
    "golang": "golang",
    "scala": "scala",
    "kotlin": "kotlin",
    "kt": "kotlin",
    "rust": "rust",
    "rs": "rust",
    "php": "php",
    "typescript": "typescript",
    "ts": "typescript",
    "racket": "racket",
    "rkt": "racket",
    "dart": "dart"
}
LANGUAGE_FILE_EXTENSIONS = {
    "cpp": ".cpp",
    "java": ".java",
    "python": ".py",
    "python3": ".py",
    "c": ".c",
    "csharp": ".cs",
    "javascript": ".js",
    "ruby": ".rb",
    "swift": ".swift",
    "golang": ".go",
    "scala": ".scala",
    "kotlin": ".kt",
    "rust": ".rs",
    "php": ".php",
    "typescript": ".ts",
    "racket": ".rkt",
    "dart": ".dart"
}

URL = "https://leetcode.com/graphql/"
GQL_QUERY = """
            query consolePanelConfig($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionTitle
                    questionFrontendId
                    exampleTestcaseList
                    codeSnippets {
                        lang langSlug code
                    }
                }
            }
            """


def get_problem_data(url: str) -> dict[str]:
    return requests.get(
        URL,
        json={
            "query": GQL_QUERY,
            "variables": {"titleSlug": re.search(r"(?<=problems/)[^\s/]+", url).group()}
        }
    ).json()["data"]["question"]


def generate_python3_file_content(code_snippet: str, test_cases: list[str]) -> str:
    function_name = re.search(r"(?<=class Solution:\n {4}def )[^(]+", code_snippet).group()

    file_content = f"{code_snippet}raise NotImplementedError\n\n\nif __name__ == \"__main__\":\n"

    for test_case in test_cases:
        args = test_case.split('\n')
        file_content += f"    print(Solution().{function_name}({', '.join(args)}))\n"

    return file_content


def generate_rust_file_content(code_snippet: str, test_cases: list[str]) -> str:
    function_name = re.search(r"(?<=impl Solution {\n {4}pub fn )[^(]+", code_snippet).group()

    file_content = f"struct Solution;\n\n{code_snippet}\n\nfn main() {{\n"

    for test_case in test_cases:
        args = test_case.split('\n')
        file_content += f"    println!(\"{{:?}}\", Solution::{function_name}({', '.join(args)}));\n"

    file_content += "}"

    return file_content


def create_file(file_path: Path, content: str) -> None:
    os.makedirs(file_path.parent, exist_ok=True)

    with open(file_path, 'w') as f:
        f.write(content)


def main() -> None:
    problem_url = input("Enter problem url: ")

    problem_data = get_problem_data(problem_url)
    problem_id = problem_data["questionFrontendId"]
    problem_title = problem_data["questionTitle"]
    test_cases = problem_data["exampleTestcaseList"]

    language = input("Enter programming language (default is python3): ").lower() or "python3"
    language_slug = PROGRAMMING_LANGUAGES[language]

    code_snippet = next(
        (snippet["code"] for snippet in problem_data["codeSnippets"] if snippet["langSlug"] == language_slug),
        ""
    )

    directory = Path(language_slug).resolve()

    file_name = f"{problem_id}. {problem_title}{LANGUAGE_FILE_EXTENSIONS[language_slug]}"
    file_path = directory / file_name

    if os.path.exists(file_path):
        if input(f"A file already exists at '{file_path}', do you want to overwrite it? [Y/n]: ").lower() != "y":
            print("Exiting program!")
            return

    match language_slug:
        case "python3":
            file_content = generate_python3_file_content(code_snippet, test_cases)
        case "rust":
            file_content = generate_rust_file_content(code_snippet, test_cases)
        case _:
            file_content = code_snippet

    create_file(file_path, file_content)

    print(f"File '{file_path}' created successfully!")


if __name__ == '__main__':
    main()
