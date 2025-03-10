# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import List, Union
from botbuilder.schema import Activity
from botbuilder.schema.teams import (
    NotificationInfo,
    TeamsChannelData,
    TeamInfo,
    TeamsMeetingInfo,
    OnBehalfOf,
)


def teams_get_channel_data(activity: Activity) -> TeamsChannelData:
    if not activity:
        return None

    if activity.channel_data:
        return TeamsChannelData().deserialize(activity.channel_data)

    return None


def teams_get_channel_id(activity: Activity) -> str:
    if not activity:
        return None

    if activity.channel_data:
        channel_data = TeamsChannelData().deserialize(activity.channel_data)
        return channel_data.channel.id if channel_data.channel else None

    return None


def teams_get_selected_channel_id(activity: Activity) -> str:
    if not activity:
        return None

    if activity.channel_data:
        channel_data = TeamsChannelData().deserialize(activity.channel_data)
        return (
            channel_data.settings.selected_channel.id
            if channel_data
            and channel_data.settings
            and channel_data.settings.selected_channel
            else None
        )

    return None


def teams_get_team_info(activity: Activity) -> TeamInfo:
    if not activity:
        return None

    if activity.channel_data:
        channel_data = TeamsChannelData().deserialize(activity.channel_data)
        return channel_data.team

    return None


def teams_notify_user(
    activity: Activity, alert_in_meeting: Union[bool, None] = None, external_resource_url: Union[str, None] = None
):
    if not activity:
        return

    if not activity.channel_data:
        activity.channel_data = {}

    channel_data = TeamsChannelData().deserialize(activity.channel_data)
    channel_data.notification = NotificationInfo(alert=not alert_in_meeting)
    channel_data.notification.alert_in_meeting = alert_in_meeting
    channel_data.notification.external_resource_url = external_resource_url
    activity.channel_data = channel_data


def teams_get_meeting_info(activity: Activity) -> TeamsMeetingInfo:
    if not activity:
        return None

    if activity.channel_data:
        channel_data = TeamsChannelData().deserialize(activity.channel_data)
        return channel_data.meeting

    return None


def teams_get_team_on_behalf_of(activity: Activity) -> List[OnBehalfOf]:
    if not activity:
        return None

    if activity.channel_data:
        channel_data = TeamsChannelData().deserialize(activity.channel_data)
        return channel_data.on_behalf_of

    return None
