def create_prompt(topic, level):

    if level == "Beginner":
        return f"""
Create beginner-friendly study notes on {topic}.

Include:
1. Definition
2. Key Concepts
3. Advantages
4. Disadvantages
5. Applications
6. Important Interview Questions

Use simple language and easy-to-understand examples.
"""

    elif level == "Intermediate":
        return f"""
Create intermediate-level study notes on {topic}.

Include:
1. Definition
2. Key Concepts
3. Advantages
4. Disadvantages
5. Applications
6. Important Interview Questions

Explain concepts in moderate technical detail.
Use technical terminology where appropriate.
Include practical examples where possible.
"""

    elif level == "Advanced":
        return f"""
Create advanced-level study notes on {topic}.

Include:
1. Definition
2. Key Concepts
3. Advantages
4. Disadvantages
5. Applications
6. Internal Working / Architecture
7. Performance Considerations
8. Real-world Industry Use Cases
9. Advantages, Disadvantages and Trade-offs
10. Common Interview Questions with Brief Answers

Assume the reader already understands the fundamentals.
Use professional technical terminology.
Explain concepts in depth with implementation details where applicable.
"""

    else:
        return f"""
Create beginner-friendly study notes on {topic}.

Include:
1. Definition
2. Key Concepts
3. Advantages
4. Disadvantages
5. Applications
6. Important Interview Questions

Use simple language and easy-to-understand examples.
"""