import os
import requests
from typing import Dict, List, Tuple


def get_problem_data(url: str) -> Tuple[int, str, List[str], List[Dict[str, str]]]:
    title_slug = url.split('/')[-2]

    json_query_info = {
        "query": "query consolePanelConfig($titleSlug: String!) { question(titleSlug: $titleSlug) { questionId questionFrontendId questionTitle enableDebugger enableRunCode enableSubmit enableTestMode exampleTestcaseList metaData } }",
        "variables": {"titleSlug": title_slug}}

    json_query_code_snippets = {
        "query": "query questionEditorData($titleSlug: String!) { question(titleSlug: $titleSlug) { questionId questionFrontendId codeSnippets { lang langSlug code } envInfo enableRunCode } }",
        "variables": {"titleSlug": title_slug}}

    api_url = "https://leetcode.com/graphql/"

    data_info = requests.get(api_url, json=json_query_info).json()
    data_info_question = data_info["data"]["question"]

    problem_id = data_info_question["questionId"]
    problem_title = data_info_question["questionTitle"]
    example_test_cases = data_info_question["exampleTestcaseList"]

    data_code_snippets = requests.get(api_url, json=json_query_code_snippets).json()
    code_snippets = data_code_snippets["data"]["question"]["codeSnippets"]

    return problem_id, problem_title, example_test_cases, code_snippets


def main() -> None:
    lang_map = {"c++": "cpp",
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
                "dart": "dart"}

    lang_file_extension = {"cpp": ".cpp",
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
                           "dart": ".dart"}

    problem_url = input("Enter problem url: ")
    lang = lang_map[input("Enter programming language (default is python3): ").lower() or "python3"]

    problem_id, problem_title, example_test_cases, code_snippets = get_problem_data(problem_url)

    file_name = f"{problem_id}. {problem_title}{lang_file_extension[lang]}"
    directory = f"./{lang}/"
    file_path = directory + file_name

    if os.path.exists(file_path):
        if input(f"A file already exists at '{file_path}', do you want to overwrite it? [Y/n]: ").lower() != "y":
            print("Exiting program!")
            return

    file_content = ""

    for code_snippet in code_snippets:
        if code_snippet["langSlug"] == lang:
            file_content = code_snippet["code"]
            break

    if lang == "python3":
        file_content = f'from typing import Dict, List, Tuple\n\n\n{file_content}\n\n\nif __name__ == "__main__":\n    '

        try:
            function_name = file_content.split('\n')[4].split()[1].split('(')[0]
        except IndexError:
            function_name = "replace_this_with_solution_method_name"

        test_cases = []

        for test_case in example_test_cases:
            args = ", ".join(test_case.split('\n'))
            test_cases.append(f"print(Solution().{function_name}({args}))")

        file_content += "\n    ".join(test_cases)

    os.makedirs(directory, exist_ok=True)

    with open(file_path, 'w') as f:
        f.write(file_content)

    print(f"File '{file_path}' created successfully!")


if __name__ == '__main__':
    main()
