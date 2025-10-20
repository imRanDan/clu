# CLU - Codified Testing Utility

> *"I'm CLU. I'm here to create the perfect system. "*

An AI-powered test generation agent that writes comprehensive unit tests for your code automatically. Inspired by TRON: Legacy.

![Language](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## What It Does

CLU analyzes your code and generates comprehensive, production-ready unit tests using Claude AI. Point it at any code file and watch it write tests with edge cases, error handling, and proper structure.

**No more:**
- Spending hours writing boilerplate tests
- Forgetting edge cases
- Copy-pasting test templates
- Context-switching between code and tests

**Just:**
```bash
python3 clu.py mycode.js
```

And CLU handles the rest.

## Features

- 🤖 **AI-Powered** - Uses Claude Sonnet 4.5 for intelligent test generation
- 🔍 **Auto-Detection** - Automatically detects language and testing framework from file extension
- 🎯 **Comprehensive** - Generates tests for main functionality, edge cases, and error handling
- ⚡ **Fast** - Generates full test suites in seconds
- 🌐 **Multi-Language** - Supports JavaScript, TypeScript, Python, Go, Rust, Java, C++, and more
- 💡 **Smart Naming** - Follows language-specific test file conventions

## Currently Supported
- ✅ **JavaScript/JSX** - Jest (tested and working)
- ✅ **TypeScript/TSX** - Jest (tested and working)

## Roadmap - Coming Soon
- Python (pytest)
- Go (testing)
- Rust (cargo test)
- Java (JUnit)
- And more...

CLU's architecture is language-agnostic, so adding new languages is straightforward. Contributions welcome!

## Installation

### Prerequisites
- Python 3.9+
- Claude API key ([get one here](https://console.anthropic.com))

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

3. **Set up your API key:**

Create a `.env` file in the project root:
```bash
ANTHROPIC_API_KEY=your-api-key-here
```

⚠️ **Important:** Never commit your `.env` file to version control!

## Usage

### Basic Usage
```bash
python3 clu.py <code_file>
```

CLU will automatically:
1. Detect the programming language
2. Choose the appropriate testing framework
3. Generate comprehensive tests
4. Save them with proper naming conventions

## Examples

### JavaScript (Tested ✅)
python3 clu.py app.js
# Creates: app.test.js with Jest tests

### Coming Soon
Python, Go, and other languages will work similarly once implemented.

### Manual Override

If you want to specify a different framework:
```bash
python3 clu.py mycode.js javascript mocha
```

### Running the Generated Tests

After CLU generates your tests, run them with the appropriate test runner:

**JavaScript/TypeScript:**
```bash
npm install --save-dev jest
npx jest
```

**Python:**
```bash
pip install pytest
pytest
```

**Go:**
```bash
go test
```

## Example Output

Given this simple JavaScript file:
```javascript
function add(a, b) {
    return a + b;
}

function divide(a, b) {
    if (b === 0) {
        throw new Error("Cannot divide by zero");
    }
    return a / b;
}
```

CLU generates:
```javascript
describe('Math Operations', () => {
  describe('add()', () => {
    test('should add two positive numbers correctly', () => {
      expect(add(2, 3)).toBe(5);
    });

    test('should handle zero correctly', () => {
      expect(add(0, 5)).toBe(5);
    });

    test('should handle decimal numbers', () => {
      expect(add(0.1, 0.2)).toBeCloseTo(0.3);
    });
    // ... more comprehensive tests
  });

  describe('divide()', () => {
    test('should divide two numbers correctly', () => {
      expect(divide(6, 2)).toBe(3);
    });

    test('should throw error when dividing by zero', () => {
      expect(() => divide(5, 0)).toThrow('Cannot divide by zero');
    });
    // ... edge cases and error handling
  });
});
```

## API Costs

CLU uses the Claude API, which has usage-based pricing. Typical costs:

- **Small file** (~100 lines): ~$0.01
- **Medium file** (~500 lines): ~$0.05
- **Large file** (~1000 lines): ~$0.10

Anthropic provides **$5 in free credits** when you sign up, which covers hundreds of test generations. (STILL FIGURING OUT COSTS FOR THIS PROJECT BUT THESE WERE SOME I'VE SEEN THROUGH RESEARCH)

## How It Works

1. **Detection:** CLU analyzes your file extension to determine language and framework
2. **Analysis:** Sends your code to Claude AI with instructions to write comprehensive tests
3. **Generation:** Claude analyzes your code structure, functions, and logic
4. **Output:** CLU saves the generated tests with proper naming conventions

## Roadmap

- [ ] Batch processing (test entire directories)
- [ ] Auto-run tests and iterate on failures
- [ ] Custom test templates
- [ ] IDE extensions (VSCode, JetBrains)
- [ ] Support for more testing frameworks
- [ ] Test coverage analysis
- [ ] Git hook integration

## Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## Inspiration

CLU is inspired by the character in *TRON:Legacy , where CLU is created by Kevin Flynn to help create the perfect system.

## License

MIT License - see [LICENSE](LICENSE) for details

## Acknowledgments

- Built with [Claude API](https://www.anthropic.com/claude) by Anthropic
- Inspired by TRON: Legacy
- Created because I hate writing tests

---

**"Am I still to create the perfect system?"** - CLU

**"yeAHH"** - Kevin Flynn
