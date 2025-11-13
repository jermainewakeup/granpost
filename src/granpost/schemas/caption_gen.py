from typing import Optional

from pydantic import BaseModel, Field


class Quote(BaseModel):
    text: str = Field(..., description="The full quote text, ready to paste as a Facebook caption.")

    hashtags: list[str] = Field(
        default_factory=list, description="0–5 relevant hashtags, without the leading # character."
    )

    alt_text: Optional[str] = Field(
        default=None,
        description="Optional alt-text describing a suggested image that matches the quote.",
    )
