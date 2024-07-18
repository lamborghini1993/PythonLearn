# -*- utf-8 -*-
"""
@field_validator 用于验证单个字段，
@model_validator 则可以验证整个模型。
"""

from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    name: str
    age: int

    @field_validator("age")
    def age_must_be_positive(cls, value):
        if value < 0:
            raise ValueError("age must be positive")
        return value

    @model_validator(mode="after")
    def validate_user(cls, values):
        """
        model_validator 在 Pydantic V2 中用于验证整个模型的状态，而不仅仅是单个字段。
        这使得你可以在验证器中检查多个字段之间的关系或者执行更复杂的逻辑。model_validator 可以在模型实例化之前 (mode='before') 或之后 (mode='after') 执行。
        下面是一个使用 model_validator 的示例，该示例确保 User 模型中的 name 和 age 字段满足特定条件：
        """
        if values.age < 18 and values.name.startswith("Minor"):
            raise ValueError('Users under 18 with "Minor" prefix are not allowed')
        return values


for name, age in (("John Doe", -1), ("Minor John1", 17), ("Minor John2", 18)):
    print(name, age)
    try:
        user = User(name=name, age=age)
        print("创建成功:", user)
    except ValueError as e:
        print(e)
