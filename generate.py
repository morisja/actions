#!/usr/bin/python3
import json

from actionitem import ActionItem

spec = [
    ActionItem(title="Play Pause", section="Control", path="playpause"),
    ActionItem(title="VolUp", section="Control", path="volup"),
    ActionItem(title="VolDown", section="Control", path="voldown"),
    ActionItem(title="Next", section="Control", path="next"),
    ActionItem(title="Prev", section="Control", path="prev"),
    ActionItem(
        title="Philly Soul",
        section="Playlists",
        path="select/a937aa9dd2e00385476b927d0de8c073",
    ),
    ActionItem(
        title="Dinner with friends",
        section="Playlists",
        path="select/076b41167e5d5d9a2fc40c6e41c4253e",
    ),
]
print(json.dumps([s.as_dict() for s in spec]))
