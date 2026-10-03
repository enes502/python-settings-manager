def add_setting(settings,settings_items):
    key = settings_items[0].lower()
    value = settings_items[1].lower()
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
def update_setting(settings,settings_items):
    key = settings_items[0].lower()
    value = settings_items[1].lower()
    if key in settings:
        settings.update({key: value})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(settings,key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
def view_settings(settings):
    if not settings:
        return "No settings available."
    else:
        writing = ""
        for key,value in settings.items():
            writing+=f'{key.capitalize()}: {value}\n'

        return f"Current User Settings:\n{writing}"
test_settings= dict({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}) 
