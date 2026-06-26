"""Basic engagement metric helpers for content analytics."""


def engagement_rate(likes: int, comments: int, shares: int, views: int) -> float:
    if views <= 0:
        return 0.0
    return (likes + comments + shares) / views


def completion_proxy(avg_watch_seconds: float, video_seconds: float) -> float:
    if video_seconds <= 0:
        return 0.0
    return min(avg_watch_seconds / video_seconds, 1.0)
