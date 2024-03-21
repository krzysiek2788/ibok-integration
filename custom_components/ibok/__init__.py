DOMAIN = "ibok"


async def async_setup(hass, config):
    hass.states.async_set("ibok.world", "Paulus")

    # Return boolean to indicate that initialization was successful.
    return True
