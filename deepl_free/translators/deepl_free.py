from wagtail_localize.machine_translators.base import BaseMachineTranslator

import requests

from wagtail_localize.strings import StringValue


def language_code(code, is_target=False):
    # DeepL supports targeting Brazillian Portuguese but doesn't have this for other languages
    if is_target and code in ['pt-pt', 'pt-br']:
        return code

    return code.split("-")[0].upper()


class DeepLFreeTranslator(BaseMachineTranslator):
    display_name = "DeepLFree"

    def translate(self, source_locale, target_locale, strings):
        response = requests.post('https://api-free.deepl.com/v2/translate', {
            'auth_key': self.options['AUTH_KEY'],
            'text': [string.data for string in strings],
            'tag_handling': 'xml',
            'source_lang': language_code(source_locale.language_code),
            'target_lang': language_code(target_locale.language_code, is_target=True),
        })

        return {
            string: StringValue(translation['text'])
            for string, translation in zip(strings, response.json()['translations'])
        }

    def can_translate(self, source_locale, target_locale):
        return language_code(source_locale.language_code) != language_code(target_locale.language_code, is_target=True)
