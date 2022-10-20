from os.path import exists
from pathlib import Path


languageReference = {
    "default": "System language",
    "ca"    : "Catalan - Català",
    "zh"    : "Chinese - 中文",
    "en"    : "English - English",
    "fr"    : "French - Français",
    "hi"    : "Hindi - हिंदी",
    "pt_BR" : "Portuguese (Brazil)",
    "pt_PT" : "Portuguese (Portugal)",
    "tr"    : "Turkish - Türkçe"
}


languageRemap = {
    "pt-PT":      "pt_PT",
    "pt-BR":      "pt_BR",
    "uk":         "ua",
    "zh-Hant-TW": "zh_TW",
    "zh-Hans-CN": "zh_CN",
}


# ISO 3166-1
languageFlagsRemap = {
    "ar": "sa",
    "bs": "ba",
    "ca": "ad",
    "cs": "cz",
    "da": "dk",
    "en": "gb",
    "el": "gr",
    "et": "ee",
    "fa": "ir",
    "he": "il",
    "ja": "jp",
    "hi": "in",
    "ko": "kr",
    "nb": "no",
    "nn": "no",
    "pt_BR": "br",
    "pt_PT": "pt",
    "si": "lk",
    "zh": "cn",
    #"zh_CN": "cn",
    "zh_TW": "tw",
    "vi": "vn",
    "sr": "rs",
    "sv": "se",
}


def getMarkdownSupportLangs():
    from translated_percentage import untranslatedPercentage

    readmeLangs = [
        "| Language | Translated | |",
        "| :-- | :-- | --- |",
    ]

    dir = str(Path(__file__).parent)
    for lang, langName in languageReference.items():
        if (not exists(f"{dir}/lang_{lang}.json")): continue
        perc = untranslatedPercentage[lang] if (lang in untranslatedPercentage) else "100%"
        if (perc == "0%"): continue
        langName = languageReference[lang] if (lang in languageReference) else lang
        flag = languageFlagsRemap[lang] if (lang in languageFlagsRemap) else lang
        readmeLangs.append(f"| {langName} | {perc} | <img src='https://flagcdn.com/{flag}.svg' width=20> |")
    readmeLangs.append("")

    return "\n".join(readmeLangs)
