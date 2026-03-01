def calculate_learning_efficiency(time_spent, concept_links, knowledge_gaps, research_questions):
    if knowledge_gaps == 0 or research_questions == 0:
        return 0

    return (time_spent * concept_links) / (knowledge_gaps * research_questions)