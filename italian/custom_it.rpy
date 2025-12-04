init python:

    def replace_text(t):
        import re
        if _preferences.language == "italian":
            t = t.replace("Relationship:" , "Relazione:")
            t = t.replace("Jump to page:" , "Vai a Pagina:")
            t = t.replace("Pregnant:" , "Incinta:")
            t=re.sub(r"\bYes\b","Sì",t)
        
        return t            
    config.replace_text = replace_text


translate italian strings:

    old "Italian"
    new "italiano"

    old "Previous Entry"
    new "Precedente"

    old "Next Entry"
    new "Successivo"

    old "Previous Page"
    new "Pagina Precedente"

    old "Next Page"
    new "Pagina Successiva"

    old "Close Entry"
    new "Chiudi"

    old "v[config.version] • Taboo Edition"
    new "v[config.version] • Edizione Taboo"

    old "v[config.version] • Standard Edition"
    new "v[config.version] • Edizione Standard"

    old "v[config.version] • Taboo Edition, Extra Scenes"
    new "v[config.version] • Edizione Taboo Edition, Scene Extra"

    old "Support me on Patreon:\nwww.patreon.com/perverteer"
    new "Sostienimi su Patreon:\nwww.patreon.com/perverteer"

    old "v[config.version] • Standard Edition, Extra Scenes"
    new "v[config.version] • Edizione Standard, Scene Extra"

    old "{=location_subheading}THANK YOU{/=location_subheading}"
    new "{=location_subheading}GRAZIE!{/=location_subheading}"

    old "{b}A big thank you to my top tier backers, you rock!{/b}"
    new "{b}Un grande ringraziamento ai miei finanziatori top, siete fantastici!{/b}"

    old "Italiano (Tacito)"
    new "Italiano (Tacito)"

    old "Italian (Tacito)"
    new "Italiano (Tacito)"
