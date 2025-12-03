import anthropic 
import os
import sys
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")

LANGUAGE_MAP = {
    '.js': ('javascript', 'jest'),
    '.jsx': ('javascript', 'jest'),
    '.ts': ('typescript', 'jest'),
    '.tsx': ('typescript', 'jest'),
    '.py': ('python', 'pytest'),
    '.java': ('java', 'junit'),
    '.cpp': ('c++', 'googletest'),
    '.c': ('c', 'unity'),
    '.go': ('go', 'testing'),
    '.rs': ('rust', 'rust test'),  # Fixed: "cargo test" is a command, not framework name
    '.rb': ('ruby', 'rspec'),
    '.php': ('php', 'phpunit'),
    '.swift': ('swift', 'xctest'),
    '.kt': ('kotlin', 'junit'),
}

def detect_language(filepath):
    """Auto-detect language and framework from file extension"""
    _, ext = os.path.splitext(filepath)

    if ext in LANGUAGE_MAP:
        return LANGUAGE_MAP[ext]
    else:
        print(f"⚠️  Unknown file type: {ext}")
        print("Supported: .js, .jsx, .ts, .tsx, .py, .java, .cpp, .c, .go, .rs, .rb, .php, .swift, .kt")
        sys.exit(1)

def read_code_file(filepath):
    """Read the code file you want to generate tests for"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        sys.exit(1)

def generate_tests(code, language, framework, filepath):
    """Use Claude to generate tests"""
    if not API_KEY:
        print("❌ Error: ANTHROPIC_API_KEY not found in environment variables")
        print("💡 Create a .env file with: ANTHROPIC_API_KEY=your-key-here")
        sys.exit(1)
    
    try:
        client = anthropic.Anthropic(api_key=API_KEY)

        prompt = f"""You are CLU - a test-writing optimization program. Designed to help create perfect systems. I need you to write comprehensive unit tests for the following {language} code.
    
    Use the {framework} testing framework.

    Write tests that:
    - Cover all major functions/methods
    - Test edge cases
    - Test error handling
    - Are well-organized and readable
    - Includes helpful comments
    - Follow best software engineering practices for {framework}

    Here's the code from {filepath}:
    ```{language}
    {code}
    ```

    Generate ONLY the test file code. No explanations. Just the complete, runnable test file."""

        print(f"🔵 CLU analyzing {language} code...")
        print(f"⚡ Generating {framework} tests...")

        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4096,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return message.content[0].text
    except anthropic.APIError as e:
        print(f"❌ API Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error generating tests: {e}")
        sys.exit(1)

def get_test_filename(original_file, language):
    """Generate appropriate test filename based on language conventions"""
    base, ext = os.path.splitext(original_file)
    base_name = os.path.basename(base)
    base_dir = os.path.dirname(base) if os.path.dirname(base) else ''

    # Different languages have different test file conventions
    if language in ['javascript', 'typescript']:
        return f"{base}.test{ext}"
    elif language == "python":
        return os.path.join(base_dir, f"test_{base_name}.py") if base_dir else f"test_{base_name}.py"
    elif language == 'go':
        return f"{base}_test.go"
    elif language == 'rust':
        # Rust tests usually go in the same file or tests/ directory
        # For now, we'll create a separate test file
        return f"{base}_test.rs"
    elif language == 'java':
        # Java: UserService.java -> UserServiceTest.java
        return os.path.join(base_dir, f"{base_name}Test.java") if base_dir else f"{base_name}Test.java"
    elif language == 'ruby':
        # Ruby/RSpec: calculator.rb -> calculator_spec.rb
        return os.path.join(base_dir, f"{base_name}_spec.rb") if base_dir else f"{base_name}_spec.rb"
    elif language == 'php':
        # PHP/PHPUnit: Calculator.php -> CalculatorTest.php
        return os.path.join(base_dir, f"{base_name}Test.php") if base_dir else f"{base_name}Test.php"
    elif language == 'swift':
        # Swift/XCTest: Calculator.swift -> CalculatorTests.swift
        return os.path.join(base_dir, f"{base_name}Tests.swift") if base_dir else f"{base_name}Tests.swift"
    elif language == 'kotlin':
        # Kotlin/JUnit: Calculator.kt -> CalculatorTest.kt
        return os.path.join(base_dir, f"{base_name}Test.kt") if base_dir else f"{base_name}Test.kt"
    elif language == 'c++':
        # C++/Google Test: calculator.cpp -> calculator_test.cpp
        return f"{base}_test{ext}"
    elif language == 'c':
        # C/Unity: calculator.c -> calculator_test.c
        return f"{base}_test{ext}"
    else:
        # Default fallback
        return f"{base}.test{ext}"


def save_tests(test_code, output_path):
    """Save the generated tests to a file"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(test_code)
        print(f"✅ Tests saved to: {output_path}")
    except Exception as e:
        print(f"❌ Error saving test file: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("🔵 CLU - Codified Testing Utility")
        print("\nusage: python3 clu.py <code_file> [language] [framework]")
        print("\nExamples:")
        print("  python3 clu.py mycode.js                    # Auto-detects JS + Jest")
        print("  python3 clu.py app.py                       # Auto-detects Python + pytest")
        print("  python3 clu.py main.go                      # Auto-detects Go + testing")
        print("  python3 clu.py mycode.js javascript mocha   # Manual override")
        print("\nSupported extensions: .js, .jsx, .ts, .tsx, .py, .java, .cpp, .c, .go, .rs, .rb, .php, .swift, .kt")
        sys.exit(1)

    code_file = sys.argv[1]

    #Check if language and framework were manually specified
    if len(sys.argv) >= 4:
        language = sys.argv[2]
        framework = sys.argv[3]
        print(f"🔧 Manual mode: {language} + {framework}")
    else:
        #Auto-detect
        language, framework = detect_language(code_file)
        print(f"🔍 Detected: {language} + {framework}")
    
    #Read the code
    print(f"📖 Reading {code_file}...")
    code = read_code_file(code_file)

    #Generate ze tests
    test_code = generate_tests(code, language, framework, code_file)

    #save tests with appropriate naming convention
    output_file = get_test_filename(code_file, language)
    save_tests(test_code, output_file)

    print("\n⚡ CLU has optimized your testing grid.")
    print(f"💡 To run tests: ", end="")

    # Give helpful command for running tests
    if language in ['javascript', 'typescript']:
        print("npx jest")
    elif language == 'python':
        print("pytest")
    elif language == 'go':
        print("go test")
    elif language == 'rust':
        print("cargo test")
    elif language == 'ruby':
        print("rspec")
    elif language == 'php':
        print("phpunit")
    elif language == 'swift':
        print("swift test")
    elif language == 'java' or language == 'kotlin':
        print("mvn test  # or gradle test")
    elif language == 'c++' or language == 'c':
        print(f"# Compile and run {framework} tests")
    else:
        print(f"{framework}")

if __name__ == "__main__":
    main()