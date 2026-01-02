from app.models.prompt import AIAgentPrompt
from app.models.upload import DocumentChunks


def build_insight_prompt(
        question: str,
        prompt_message: AIAgentPrompt,
        context_chunks: DocumentChunks
) -> str:
    context_block = "\n\n".join(
        f"- {chunk.page_content}" for chunk in context_chunks.chunks
    )

    return f"{prompt_message.system}\nContext: {context_block}\n\nThe question is: {question}"
