---
name: "performance-analyzer"
description: "Checks code time and space complexity, and analyzes performance. Invoke when user asks about complexity, performance, or optimization."
---

# Performance Analyzer

This skill helps analyze code for time and space complexity, identify performance bottlenecks, and suggest optimizations.

## Capabilities

- **Complexity Analysis**: Determine Big O notation for time and space complexity.
- **Performance Review**: Identify potential performance issues (e.g., unnecessary loops, expensive operations).
- **Optimization Suggestions**: Provide recommendations to improve code efficiency.

## When to Use

Invoke this skill when the user:
- Asks "What is the complexity of this code?"
- Asks "How can I make this faster?"
- Asks to check for performance issues.
- Asks for a code review specifically focused on performance.
- Asks to analyze the complexity of an algorithm.

## Instructions for the Assistant

1. **Identify the Scope**: Determine if the user wants complexity analysis, performance review, or optimization.
2. **Review Code**: 
   - Analyze specific algorithms or functions provided.
   - Look for nested loops, recursion, heavy memory usage, etc.
3. **Report**:
   - **Time Complexity**: Provide Big O notation (e.g., O(n), O(log n)) with a clear explanation.
   - **Space Complexity**: Provide Big O notation (e.g., O(n), O(1)) with a clear explanation.
   - **Bottlenecks**: Point out specific lines or blocks causing issues.
   - **Suggestions**: Provide concrete steps to improve performance.

## Example

User: "Check the complexity of this function."

Assistant:
- **Time Complexity**: O(n^2) due to the nested loop iterating over the array.
- **Space Complexity**: O(n) for storing the intermediate results in a new array.
- **Suggestion**: Consider using a hash map to reduce time complexity to O(n).
