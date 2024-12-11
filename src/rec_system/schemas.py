from pydantic import BaseModel
from typing import List


class CreatorRecommendRequest(BaseModel):
    channel_name: str
    channel_category: str
    subscribers: int


class ItemRecommendRequest(BaseModel):
    title: str
    item_category: str
    media_type: str
    score: int
    item_content: str

# 응답(Response) 모델


class RecommendCreator(BaseModel):
    creator_id: int
    channel_category: str
    channel_name: str
    subscribers: int


class RecommendItem(BaseModel):
    item_id: int
    title: str
    item_category: str
    media_type: str
    score: int
    item_content: str

# item -> creator 추천


class CreatorRecommendResponse(BaseModel):
    recommended_creators: List[RecommendCreator]


# creator -> item 추천
class ItemRecommendResponse(BaseModel):
    recommended_items: List[RecommendItem]
