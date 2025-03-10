# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import Union

from botbuilder.core import ConversationState
from botbuilder.core.skills import (
    BotFrameworkClient,
    BotFrameworkSkill,
    ConversationIdFactoryBase,
)


class SkillDialogOptions:
    def __init__(
        self,
        bot_id: Union[str, None] = None,
        skill_client: BotFrameworkClient = None,
        skill_host_endpoint: Union[str, None] = None,
        skill: BotFrameworkSkill = None,
        conversation_id_factory: ConversationIdFactoryBase = None,
        conversation_state: ConversationState = None,
        connection_name: Union[str, None] = None,
    ):
        self.bot_id = bot_id
        self.skill_client = skill_client
        self.skill_host_endpoint = skill_host_endpoint
        self.skill = skill
        self.conversation_id_factory = conversation_id_factory
        self.conversation_state = conversation_state
        self.connection_name = connection_name
