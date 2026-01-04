from app.models.prompt import AIAgentPrompt
from app.models.upload import DocumentChunks


def build_insight_prompt(
        question: str,
        prompt_message: AIAgentPrompt,
        context_chunks: DocumentChunks
) -> str:
    """
    Construct the final prompt string for the InsightAgent.

    This function combines:
    - the system-level agent instructions,
    - the retrieved context chunks,
    - and the user question

    :param question: User question to be answered
    :param prompt_message: System and instruction prompts for the agent
    :param context_chunks: Retrieved document chunks used as context
    :return: Fully composed prompt string
    """
    context_block = "\n\n".join(
        f"- {chunk.page_content}" for chunk in context_chunks.chunks
    )

    return f"{prompt_message.system}\nContext: {context_block}\n\nThe question is: {question}"
