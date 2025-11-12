from pydantic import BaseModel, Field, field_validator


class PageProfile(BaseModel):
    page_handle: str
    theme: str
    timezone: str
    never_post: list[str] = Field(default_factory=list)
    core_goal: str
    content_focus: str
    audience: list[str] = Field(default_factory=list)
    schema_version: str = "1.0"

    @field_validator("page_handle")
    @classmethod
    def ensure_at_handle(cls, v: str) -> str:
        v = v.strip()
        return v if v.startswith("@") else f"@{v}"
