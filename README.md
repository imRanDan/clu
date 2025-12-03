# 🔵 CLU - Codified Testing Utility

> *"I'm CLU. I'm here to create the perfect system."*

**AI-powered test generation CLI that writes comprehensive, production-ready unit tests for your code in 14+ languages.**

CLU analyzes your code and automatically generates test suites with edge cases, error handling, and proper structure using Claude AI. Point it at any code file and watch it create production-ready tests in seconds.

---

## 🚀 Features

- 🤖 **AI-Powered** - Uses Claude Sonnet 4.5 for intelligent test generation
- 🔍 **Auto-Detection** - Automatically detects language and testing framework from file extension
- 🎯 **Comprehensive** - Generates tests for main functionality, edge cases, and error handling
- ⚡ **Fast** - Generates full test suites in seconds
- 🌐 **Multi-Language** - Supports JavaScript, TypeScript, Python, Go, Rust, Java, C++, and more
- 💡 **Smart Naming** - Follows language-specific test file conventions

## Supported Languages

| Language   | Framework    | Extension        |
|------------|--------------|------------------|
| JavaScript | Jest         | `.js`, `.jsx`    |
| TypeScript | Jest         | `.ts`, `.tsx`    |
| Python     | pytest       | `.py`            |
| Go         | testing      | `.go`            |
| Rust       | cargo test   | `.rs`            |
| Java       | JUnit        | `.java`          |
| C++        | Google Test  | `.cpp`           |
| Ruby       | RSpec        | `.rb`            |
| PHP        | PHPUnit      | `.php`           |
| Swift      | XCTest       | `.swift`         |
| Kotlin     | JUnit        | `.kt`            |

---

## 📦 Installation

### Prerequisites

- **Python 3.9+** ([Download here](https://www.python.org/downloads/))
- **Claude API Key** ([Get one here](https://console.anthropic.com))

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/clu.git
cd clu
```

2. **Install dependencies:**
```bash
pip3 install anthropic python-dotenv
```

Or using a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install anthropic python-dotenv
```

3. **Configure your API key:**
   
   Create a `.env` file in the project root:
```bash
ANTHROPIC_API_KEY=your-api-key-here
```

⚠️ **Important:** Never commit your `.env` file to version control! Add it to `.gitignore`.

---

## 💻 Usage

### Basic Usage

```bash
python3 clu.py <code_file>
```

CLU will automatically:
1. Detect the programming language from the file extension
2. Select the appropriate testing framework
3. Analyze your code structure
4. Generate comprehensive tests
5. Save them with proper naming conventions

## Examples

**JavaScript:**
```bash
python3 clu.py app.js
# Creates: app.test.js with Jest tests
```

**Python:**
```bash
python3 clu.py calculator.py
# Creates: test_calculator.py with pytest tests
```

**Go:**
```bash
python3 clu.py main.go
# Creates: main_test.go with Go testing tests
```

### Manual Override

If you need to specify a different framework manually:
```bash
python3 clu.py mycode.js javascript mocha
```

### Running Generated Tests

After CLU generates your tests, run them with the appropriate test runner:

**JavaScript/TypeScript:**
```bash
npm install --save-dev jest
npx jest
```

**Rust:**
```bash
cargo test
```

---

## 📖 Example Output

### Input Code (`example.js`)

```javascript
function add(a, b) {
    return a + b;
}

function multiply(a, b) {
    return a * b;
}

function divide(a, b) {
    if (b === 0) {
        throw new Error("Cannot divide by zero");
    }
    return a / b;
}

module.exports = { add, multiply, divide };
```

### Generated Test File (`example.test.js`)

```javascript
const { add, multiply, divide } = require('./example');

describe('Math Operations', () => {
  describe('add()', () => {
    test('should add two positive numbers correctly', () => {
      expect(add(2, 3)).toBe(5);
    });

    test('should handle zero correctly', () => {
      expect(add(0, 5)).toBe(5);
      expect(add(5, 0)).toBe(5);
    });

    test('should handle negative numbers', () => {
      expect(add(-2, 3)).toBe(1);
      expect(add(-5, -3)).toBe(-8);
    });

    test('should handle decimal numbers', () => {
      expect(add(0.1, 0.2)).toBeCloseTo(0.3);
    });
  });

  describe('multiply()', () => {
    test('should multiply two positive numbers correctly', () => {
      expect(multiply(3, 4)).toBe(12);
    });

    test('should handle zero', () => {
      expect(multiply(5, 0)).toBe(0);
      expect(multiply(0, 5)).toBe(0);
    });

    test('should handle negative numbers', () => {
      expect(multiply(-2, 3)).toBe(-6);
      expect(multiply(-2, -3)).toBe(6);
    });
  });

  describe('divide()', () => {
    test('should divide two numbers correctly', () => {
      expect(divide(6, 2)).toBe(3);
      expect(divide(10, 5)).toBe(2);
    });

    test('should handle decimal results', () => {
      expect(divide(5, 2)).toBe(2.5);
    });

    test('should throw error when dividing by zero', () => {
      expect(() => divide(5, 0)).toThrow('Cannot divide by zero');
      expect(() => divide(-10, 0)).toThrow('Cannot divide by zero');
    });

    test('should handle negative numbers', () => {
      expect(divide(-6, 2)).toBe(-3);
      expect(divide(6, -2)).toBe(-3);
      expect(divide(-6, -2)).toBe(3);
    });
  });
});
```

---

## 🔧 How It Works

1. **File Analysis** – CLU reads your code file and extracts the file extension
2. **Language Detection** – Maps the extension to the appropriate language and testing framework
3. **Code Processing** – Reads and prepares your code for analysis
4. **AI Generation** – Sends structured prompt to Claude API with code context and testing requirements
5. **Test Creation** – Claude generates comprehensive test suite following framework best practices
6. **File Output** – Saves generated tests with language-appropriate naming conventions

### Zero-Shot Prompting

CLU uses zero-shot prompting, meaning it generates tests without requiring:
- Example test files
- Training data
- Pre-configured templates
- Manual test structure definitions

The AI understands your code context and generates appropriate tests on the first attempt.

---

## 💰 API Costs

CLU uses the Anthropic Claude API with usage-based pricing. Typical costs per generation:

- **Small file** (~100 lines): ~$0.01
- **Medium file** (~500 lines): ~$0.05
- **Large file** (~1000 lines): ~$0.10

Anthropic provides **$5 in free credits** when you sign up, which covers hundreds of test generations.

---

## 🗺️ Roadmap

- [ ] Batch processing (test entire directories at once)
- [ ] Auto-run tests and iterate on failures
- [ ] Custom test templates and configurations
- [ ] IDE extensions (VSCode, JetBrains)
- [ ] Support for additional testing frameworks
- [ ] Test coverage analysis and reporting
- [ ] Git hook integration for pre-commit testing
- [ ] Interactive mode for test refinement

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests
- 📖 Improve documentation

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details

---

## 🙏 Acknowledgments

- Built with [Claude API](https://www.anthropic.com/claude) by Anthropic
- Inspired by *TRON: Legacy* (CLU character)
- Created to eliminate the tedious task of writing boilerplate tests

---

**"Am I still to create the perfect system?"** - CLU

**"yeAHH"** - Kevin Flynn
