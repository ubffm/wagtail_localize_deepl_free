# wagtail_localize_deepl_free

This is a simple plugin for [Wagtail Localize](https://www.wagtail-localize.org/) to allow the usage of the [DeepL](https://www.deepl.com) free API in your multilingual Wagtail CMS project. 

# Installation

Clone this repository and move the ```deepl_free``` to your Wagtail CMS project.
Enable the plugin by simply adding it to your ```INSTALLED_APPS``` list in your projects settings like so:

```python
INSTALLED_APPS = [
	...,
	'deepl_free',
	...
```

You also need to enable the machine translation for Wagtail Localize by adding the following lines to your projects configuration

```python
WAGTAILLOCALIZE_MACHINE_TRANSLATOR = {
    'CLASS': 'deepl_free.translators.deepl_free.DeepLFreeTranslator',
    'OPTIONS': {
        'AUTH_KEY': <your_DEEPL_API_KEY>,
    }
}
```

Needless to say, you need to have an account with DeepL and an API-Key for their free API.

# Usage

Once the machine translator is installed, a button should appear while translating multilingual Wagtail Pages. 
*Only newly translated pages can be auto-translated*
Click the button and correct the translation if necessary.

# Dependencies

Since this is a plugin for Wagtail Localize, Wagtail Localize is needed for this plugin to work.

# Environment

Tested with:
- Python 3.8, 3.9, 3.10
- Django 3.1, 3.2
- Wagtail 2.13, 2.14, 2.15