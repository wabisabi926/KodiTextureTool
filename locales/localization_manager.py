import json
import os
import sys

class LocalizationManager:
    def __init__(self, default_lang='en'):
        self.default_lang = default_lang
        self.current_lang = self._detect_system_language()
        self.translations = {}
        self._load_translations()

    def _detect_system_language(self):
        try:
            if sys.platform == 'win32':
                import ctypes
                windll = ctypes.windll.kernel32
                language_code = windll.GetUserDefaultUILanguage()
                lang_id = hex(language_code)
                if lang_id.startswith('0x8'):
                    return 'zh_CN'
            return 'en'
        except Exception:
            return 'en'

    def _load_translations(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        
        for lang in ['en', 'zh_CN']:
            lang_path = os.path.join(base_path, lang, 'strings.json')
            try:
                with open(lang_path, 'r', encoding='utf-8') as f:
                    self.translations[lang] = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                self.translations[lang] = {}

    def t(self, key, **kwargs):
        lang = self.current_lang
        if lang not in self.translations:
            lang = self.default_lang

        text = self.translations.get(lang, {}).get(key, key)
        
        if kwargs:
            try:
                text = text.format(**kwargs)
            except (KeyError, ValueError):
                pass
        
        return text

    def set_language(self, lang):
        if lang in self.translations:
            self.current_lang = lang
            return True
        return False

    def get_available_languages(self):
        return list(self.translations.keys())

_localization_manager = None

def get_localization():
    global _localization_manager
    if _localization_manager is None:
        _localization_manager = LocalizationManager()
    return _localization_manager

def t(key, **kwargs):
    return get_localization().t(key, **kwargs)