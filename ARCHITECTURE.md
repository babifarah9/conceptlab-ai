# Architecture

```mermaid
graph LR
    U[Learner] --> UI[Web Interface]
    UI --> API[FastAPI]
    API --> L[Lesson Generator]
    API --> T[Teach Back Evaluator]
    L --> R[OpenAI Responses API / GPT-5.6]
    T --> R
    API --> C[Community Learning Cards]
    C --> UI
```

## Core objects

### Lesson
- topic and learner level
- explanation and analogy
- key ideas
- Mermaid diagram
- experiment and starter code
- quiz
- Teach Back prompt

### Teach Back evaluation
- mastery score
- verdict
- strengths
- gaps or misconceptions
- improved explanation
- next challenge

### Community Learning Card
- lesson
- learner's voluntary explanation
- evaluation
- future social metadata such as forks and likes
