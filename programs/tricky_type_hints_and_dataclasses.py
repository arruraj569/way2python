from dataclasses import dataclass
@dataclass(frozen=True)
class Config:
    tags: list[str]

config = Config(["smoke"])
config.tags.append("api")
print(config.tags)
print(Config(["x"]) == Config(["x"]))
