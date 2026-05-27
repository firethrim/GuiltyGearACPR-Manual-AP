from typing import Optional, Any
from BaseClasses import MultiWorld

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item:  dict[str, Any]) -> Optional[bool]:

    return None

def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from ..Items import item_name_groups
    from ..Locations import location_name_groups

    if category_name in item_name_groups["Character"]:
        # This category is the name of a champion
        from ..Helpers import get_option_value
        enabled_characters = get_option_value(multiworld, player, "enabled_characters")
        return category_name in enabled_characters
    if category_name in location_name_groups["Condition"]:
        # This category is the name of a champion
        from ..Helpers import get_option_value
        enabled_characters = get_option_value(multiworld, player, "enabled_conditions")
        return category_name in enabled_characters
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location:  dict[str, Any]) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the event, False to disable it, or None to use the default behavior
def before_is_event_enabled(multiworld: MultiWorld, player: int, event:  dict[str, Any]) -> Optional[bool]:
    return None
