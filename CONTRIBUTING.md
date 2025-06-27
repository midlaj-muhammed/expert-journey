# Contributing to Expert Journey

Thank you for your interest in contributing to Expert Journey! We welcome contributions from developers of all skill levels.

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- Basic knowledge of NLP concepts (helpful but not required)

### Development Setup

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/expert-journey.git
   cd expert-journey
   ```

2. **Set Up Development Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r resume_ranker_ai/requirements.txt
   python -m spacy download en_core_web_md
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🎯 Ways to Contribute

### 🐛 Bug Reports
- Use the GitHub issue tracker
- Include detailed steps to reproduce
- Provide system information (OS, Python version)
- Include error messages and stack traces

### 💡 Feature Requests
- Check existing issues first
- Clearly describe the feature and its benefits
- Provide use cases and examples

### 📝 Code Contributions
- Follow the coding standards below
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass

### 📚 Documentation
- Improve README files
- Add code comments and docstrings
- Create tutorials and examples
- Fix typos and grammar

## 📋 Coding Standards

### Python Style Guide
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Maximum line length: 88 characters (Black formatter)
- Use type hints where appropriate

### Code Structure
```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief description of the function.
    
    Args:
        param1: Description of parameter 1
        param2: Description of parameter 2
        
    Returns:
        Description of return value
    """
    # Implementation here
    return True
```

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb in present tense
- Keep the first line under 50 characters
- Add detailed description if needed

Example:
```
Add keyword extraction feature

- Implement TF-IDF based keyword extraction
- Add unit tests for new functionality
- Update documentation with usage examples
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
python -m pytest resume_ranker_ai/tests/

# Run with coverage
python -m pytest --cov=resume_ranker_ai resume_ranker_ai/tests/
```

### Writing Tests
- Add tests for all new features
- Use descriptive test names
- Include edge cases and error conditions
- Aim for high test coverage

## 📦 Pull Request Process

1. **Before Submitting**
   - Ensure all tests pass
   - Update documentation
   - Add changelog entry if applicable
   - Rebase your branch on the latest main

2. **Pull Request Template**
   - Describe what changes you made
   - Reference any related issues
   - Include screenshots for UI changes
   - List any breaking changes

3. **Review Process**
   - Maintainers will review your PR
   - Address any feedback promptly
   - Be open to suggestions and changes

## 🏷️ Issue Labels

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements to docs
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention needed
- `question`: Further information requested

## 🎨 UI/UX Contributions

### Streamlit Guidelines
- Keep the interface clean and intuitive
- Use consistent styling and colors
- Ensure mobile responsiveness
- Test with different screen sizes

### Design Principles
- Prioritize user experience
- Minimize cognitive load
- Provide clear feedback
- Use progressive disclosure

## 🔧 Development Tips

### Debugging
- Use Streamlit's built-in debugging features
- Add logging for complex operations
- Test with various file formats
- Validate edge cases

### Performance
- Profile code for bottlenecks
- Optimize NLP operations
- Cache expensive computations
- Monitor memory usage

## 📞 Getting Help

- **GitHub Discussions**: For general questions
- **GitHub Issues**: For bug reports and feature requests
- **Code Review**: Tag maintainers for review

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- GitHub contributor graphs

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Expert Journey! 🎉
